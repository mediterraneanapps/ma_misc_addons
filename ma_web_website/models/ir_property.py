 
 
 
import logging
from odoo import models, fields, api
from odoo.addons.base.models.ir_property import TYPE2FIELD


_logger = logging.getLogger(__name__)

GET_CONTEXT = dict(
    _get_domain_website_dependent=True,
    _search_order_website_dependent=True,
    _search_make_website_priority=True,
)


class IrProperty(models.Model):

    _inherit = 'ir.property'

    website_id = fields.Many2one('website', 'Website')

    @api.multi
    def _update_values(self, values):
        """Support for html fields.

        Can be removed in first odoo release with this patch: https://github.com/odoo/odoo/pull/26556
        """
        if values.get('type') == 'html':
            values['type'] = 'text'
        return super(IrProperty, self)._update_values(values)

    @api.model
    def _is_website_dependent(self, name, model):
        return getattr(self.env[model]._fields[name], 'website_dependent', None)

    @api.model
    def _check_website_dependent(self, name, model, **kwargs):
        if self._is_website_dependent(name, model):
            return self.with_context(website_dependent=True, **kwargs)
        else:
            none_values = dict((key, None) for key in kwargs.keys())
            return self.with_context(**none_values)

    @api.model
    def _get_website_id(self):
        website_id = self._context.get('website_id') or self.env.user.backend_website_id.id
        return website_id

    def _get_domain(self, prop_name, model):
        domain = super(IrProperty, self)._get_domain(prop_name, model)
        if self.env.context.get('_get_domain_website_dependent'):
            website_id = self._get_website_id()
            domain += [('website_id', 'in', [website_id, False])]
        return domain

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if self.env.context.get('_search_order_website_dependent'):
            new_order = [order] if order else []
            new_order.insert(0, 'website_id')
            order = ','.join(new_order)
        if self.env.context.get('_search_domain_website_dependent'):
            website_id = self._get_website_id()
            args.append(('website_id', '=', website_id))
        ids = super(IrProperty, self)._search(
            args,
            offset=offset,
            limit=limit,
            order=order,
            count=count,
            access_rights_uid=access_rights_uid
        )
        if self.env.context.get('_search_make_website_priority'):
             
             
             
            res = self.browse(ids)
            for prop in res:
                if prop.website_id and not prop.res_id:
                     
                     
                    res = res.filtered(lambda r: r.website_id)
                    break
            return res.ids

        return ids

    @api.model
    def create(self, vals):
        if self.env.context.get('create_website_dependent'):
            website_id = self._get_website_id()
            vals['website_id'] = website_id
        return super(IrProperty, self).create(vals)

    @api.model
    def get(self, name, model, res_id=False):
        return super(IrProperty, self._check_website_dependent(
            name, model,
            **GET_CONTEXT
        )).get(name, model, res_id=res_id)

    @api.model
    def get_multi(self, name, model, ids):
         
         
         
        if not ids:
            return {}
         
        website_id = self._get_website_id() or None
        field = self.env[model]._fields[name]
        field_id = self.env['ir.model.fields']._get(model, name).id
        company_id = self._context.get('force_company') or self.env['res.company']._company_default_get(model, field_id).id or None

         
        if field.type == 'html':
            TYPE2FIELD['html'] = 'value_text'

        if field.type == 'many2one':
            comodel = self.env[field.comodel_name]
            model_pos = len(model) + 2
            value_pos = len(comodel._name) + 2
            query = """
                SELECT substr(p.res_id, %s)::integer, r.id, p.company_id, p.website_id
                FROM ir_property p
                LEFT JOIN {} r ON substr(p.value_reference, %s)::integer=r.id
                WHERE p.fields_id=%s
                    AND (p.company_id=%s OR p.company_id IS NULL)
                    AND (p.website_id=%s OR p.website_id IS NULL)
                    AND (p.res_id IN %s OR p.res_id IS NULL)
                ORDER BY p.website_id NULLS FIRST, p.company_id NULLS FIRST
            """.format(comodel._table)
            params = [model_pos, value_pos, field_id, company_id, website_id]
        elif field.type in TYPE2FIELD:
            model_pos = len(model) + 2
            query = """
                SELECT substr(p.res_id, %s)::integer, p.{0}, p.company_id, p.website_id
                FROM ir_property p
                WHERE p.fields_id=%s
                    AND (p.company_id=%s OR p.company_id IS NULL)
                    AND (p.website_id=%s OR p.website_id IS NULL)
                    AND (p.res_id IN %s OR p.res_id IS NULL)
                ORDER BY p.website_id NULLS FIRST, p.company_id NULLS FIRST
            """.format(TYPE2FIELD[field.type])
            params = [model_pos, field_id, company_id, website_id]
        else:
            return dict.fromkeys(ids, False)

         
        cr = self.env.cr
        result = {}
        refs = {"%s,%s" % (model, id) for id in ids}
        for sub_refs in cr.split_for_in_conditions(refs):
            cr.execute(query, params + [sub_refs])
            fetched_result = cr.fetchall()
            _logger.debug('Properties for website=%s, company=%s, resource=%s:\n%s', website_id, company_id, sub_refs, fetched_result)
             
             

             
             

             
             

             
             

             

            res = {
                i[0]: i for i in fetched_result
            }
            result.update(res)

         
         

         
         
         
        default_value = result.pop(None, None)
        default_company_id = default_value and default_value[2]
        default_website_id = default_value and default_value[3]
        for ID in ids:
            if ID not in result:
                 
                result[ID] = default_value
            else:
                result_website_id = result[ID][3]
                if result_website_id:
                     
                    continue
                if default_website_id:
                     
                    result[ID] = default_value
                 
                result_company_id = result[ID][2]
                if result_company_id:
                     
                    continue
                 
                if default_company_id:
                     
                    result[ID] = default_value

        if field.type == 'many2one':
            def clean(data):
                return data and self.env[field.comodel_name].browse(data[1])
        else:
            def clean(data):
                return data and data[1]

        for key, value in result.items():
             
            result[key] = clean(value)
         
        return result

    @api.model
    def search_multi(self, name, model, operator, value):
        return super(IrProperty, self._check_website_dependent(
            name, model,
            **GET_CONTEXT
        )).search_multi(name, model, operator, value)

    @api.model
    def set_multi(self, name, model, values, default_value=None):
        return super(IrProperty, self._check_website_dependent(
            name, model,
            _search_domain_website_dependent=True,
            create_website_dependent=True,
        )).set_multi(name, model, values, default_value=default_value)

    @api.multi
    def _update_db_value_website_dependent(self, field):
        """Update db value if it's a default value"""
        for r in self:
            if r.fields_id != field:
                 
                continue
            if r.company_id:
                 
                continue
             
             
            if not r.res_id:
                 
                continue
             
            model, res_id = r.res_id.split(',')
            value = r.get_by_record()
            model = field.model_id.model
            record = self.env[model].browse(int(res_id))
            record._update_db_value(field, value)
