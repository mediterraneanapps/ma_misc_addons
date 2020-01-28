 
 
import logging

from odoo.tests import common, tagged

_logger = logging.getLogger(__name__)


@tagged('at_install', 'post_install')
class TestFields(common.TransactionCase):

    def setUp(self):
        super(TestFields, self).setUp()
        self.MODEL_WEBSITE_DEPENDENT = 'test.website_dependent'
        self.field = self.env['ir.model.fields'].search([
            ('model', '=', self.MODEL_WEBSITE_DEPENDENT),
            ('name', '=', 'foo')])

    def test_website_dependent(self):
        """ test website-dependent fields. """
        MODEL = 'test.website_dependent'

         
        website0 = self.env.ref('website.default_website')
        website1 = self.env.ref('website.website2')
        website2 = self.env['website'].create({'name': 'Extra Website'})
        context0 = dict(website_id=website0.id)
        context1 = dict(website_id=website1.id)
        context2 = dict(website_id=website2.id)
         
        field = self.env['ir.model.fields'].search([('model', '=', MODEL),
                                                    ('name', '=', 'foo')])
        self.env['ir.property'].create({'name': 'foo', 'fields_id': field.id,
                                        'value': 'default', 'type': 'char'})

         
        record = self.env[MODEL].with_context(context0).create({'foo': 'main'})
        record.invalidate_cache()
        self.assertEqual(record.with_context(context0).foo, 'main')
        self.assertEqual(record.with_context(context1).foo, 'default')
        self.assertEqual(record.with_context(context2).foo, 'default')

        record.with_context(context1).foo = 'alpha'
        record.invalidate_cache()
        self.assertEqual(record.with_context(context0).foo, 'main')
        self.assertEqual(record.with_context(context1).foo, 'alpha')
        self.assertEqual(record.with_context(context2).foo, 'default')

         
        _logger.info('Default, company-specific and website-specific values, record {}'.format(record))
        record = self.env[MODEL].create({'foo': 'nowebsite'})
        record.invalidate_cache()
        self.assertEqual(record.foo, 'nowebsite')
        self.assertEqual(record.with_context(context1).foo, 'nowebsite')
        self.assertEqual(record.with_context(context2).foo, 'nowebsite')

        record.with_context(context1).foo = 'alpha'
        record.invalidate_cache()
        self.assertEqual(record.foo, 'nowebsite')
        self.assertEqual(record.with_context(context1).foo, 'alpha')
        self.assertEqual(record.with_context(context2).foo, 'nowebsite')

         
        res = self.env[MODEL].search([('foo', '=', False)])
        self.assertFalse(res)

         
        record = self.env[MODEL].create({
            'name': 'Name',
            'user_id': self.env.user,
        })
        record.invalidate_cache()
        self.assertEqual(record.user_id, self.env.user)

    def _create_property(self, vals, record=None):
        base_vals = {
            'name': 'foo',
            'fields_id': self.field.id,
            'type': 'char',
        }
        if record:
            base_vals['res_id'] = '%s,%s' % (record._name, record.id)

        base_vals.update(vals)
        _logger.info('create property with vals {}'.format(base_vals))
        return self.env['ir.property'].create(base_vals)

    def test_website_dependent_priority_all_websites(self):
        """ test section "How it works" in index.rst (All-website case) """
        MODEL = 'test.website_dependent'

        company = self.env.user.company_id
        website = self.env.ref('website.default_website')
        record = self.env[MODEL].create({'foo': 'new_record'})

         
        props = self.env['ir.property'].search([
            ('fields_id', '=', self.field.id),
        ])
        props.unlink()
         
        self._create_property({
            'value': 'only_field',
        })
        record.invalidate_cache()
        self.assertEqual(record.foo, 'only_field')

         
        self._create_property({
            'company_id': company.id,
            'value': 'only_company',
        })
        record.invalidate_cache()
        self.assertEqual(record.foo, 'only_company')

         
        self._create_property({
            'company_id': company.id,
            'value': 'company_and_resource',
        }, record)
        record.invalidate_cache()
        self.assertEqual(record.foo, 'company_and_resource')

         
        self._create_property({
            'website_id': website.id,
            'value': 'only_website',
        })
        record.invalidate_cache()
        self.assertEqual(record.foo, 'company_and_resource')

        self._create_property({
            'website_id': website.id,
            'value': 'website_and_resource',
        }, record)
        record.invalidate_cache()
        self.assertEqual(record.foo, 'company_and_resource')

    def test_website_dependent_priority(self):
        """ test section "How it works" in index.rst """
        MODEL = 'test.website_dependent'

        company = self.env.user.company_id
        wrong_company = self.env['res.company'].create({'name': 'A'})
        website = self.env.ref('website.default_website')
        website.company_id = company
        record = self.env[MODEL].create({'foo': 'new_record'})
        record = record.with_context(website_id=website.id)

         
        props = self.env['ir.property'].search([
            ('fields_id', '=', self.field.id),
        ])
        props.unlink()

         
        self._create_property({
            'value': 'only_field',
        })
        record.invalidate_cache()
        self.assertEqual(record.foo, 'only_field')

         
        self._create_property({
            'company_id': company.id,
            'value': 'only_company',
        })
        record.invalidate_cache()
        self.assertEqual(record.foo, 'only_company')

         
        self._create_property({
            'company_id': company.id,
            'value': 'company_and_resource',
        }, record)
        record.invalidate_cache()
        self.assertEqual(record.foo, 'company_and_resource')

         
        prop = self._create_property({
            'website_id': website.id,
            'value': 'only_website',
        })
        record.invalidate_cache()
        self.assertEqual(record.foo, 'only_website')

         
         
        prop.unlink()
        self._create_property({
            'website_id': website.id,
            'company_id': wrong_company.id,
            'value': 'website_and_company',
        })
        record.invalidate_cache()
        self.assertEqual(record.foo, 'company_and_resource')

         
        prop = self._create_property({
            'website_id': website.id,
            'value': 'website_and_resource',
        }, record)
        record.invalidate_cache()
        self.assertEqual(record.foo, 'website_and_resource')

         
         
        prop.unlink()
        prop = self._create_property({
            'website_id': website.id,
            'company_id': wrong_company.id,
            'value': 'website_company_resource',
        }, record)
        record.invalidate_cache()
        self.assertEqual(record.foo, 'company_and_resource')

    def test_company_dependent(self):
        """ test company-dependent fields. It's the same test as in odoo core"""
        MODEL = 'test.company_dependent'
         
        company0 = self.env.ref('base.main_company')
        company1 = self.env['res.company'].create({'name': 'A', 'parent_id': company0.id})
        company2 = self.env['res.company'].create({'name': 'B', 'parent_id': company1.id})
         
        self.env.user.company_id = company0
         
        user0 = self.env['res.users'].create({'name': 'Foo', 'login': 'foo',
                                              'company_id': company0.id, 'company_ids': []})
        user1 = self.env['res.users'].create({'name': 'Bar', 'login': 'bar',
                                              'company_id': company1.id, 'company_ids': []})
        user2 = self.env['res.users'].create({'name': 'Baz', 'login': 'baz',
                                              'company_id': company2.id, 'company_ids': []})
         
        field = self.env['ir.model.fields'].search([('model', '=', MODEL),
                                                    ('name', '=', 'foo')])
        self.env['ir.property'].create({'name': 'foo', 'fields_id': field.id,
                                        'value': 'default', 'type': 'char'})

         
        record = self.env[MODEL].create({'foo': 'main'})
        record.invalidate_cache()
        self.assertEqual(record.sudo(user0).foo, 'main')
        self.assertEqual(record.sudo(user1).foo, 'default')
        self.assertEqual(record.sudo(user2).foo, 'default')

        record.sudo(user1).foo = 'alpha'
        record.invalidate_cache()
        self.assertEqual(record.sudo(user0).foo, 'main')
        self.assertEqual(record.sudo(user1).foo, 'alpha')
        self.assertEqual(record.sudo(user2).foo, 'default')
