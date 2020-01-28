 
 
 
 
import mimetypes
import base64
import hashlib
import re
import os

from odoo import models
from odoo.exceptions import AccessError
from odoo.tools.mimetypes import guess_mimetype
from odoo.http import request, STATIC_CACHE
from odoo.modules.module import get_resource_path, get_module_path
from odoo.tools import pycompat, consteq


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _find_field_attachment(cls, env, m, f, res_id):
        domain = [
            ('res_model', '=', m),
            ('res_field', '=', f),
            ('res_id', '=', res_id),
            ('type', '=', 'url'),
        ]
        return env['ir.attachment'].sudo().search(domain)

    @classmethod
    def find_field_attachment(cls, env, model, field, obj):
        is_attachment = env[model]._fields[field].attachment
        is_product = model == 'product.product' and field.startswith('image')
        if not (is_attachment or is_product):
            return None

        att = cls._find_field_attachment(env, model, field, obj.id)

        if not att and model == 'product.product':
             
             
             
             
            att = cls._find_field_attachment(env, 'product.template', field, obj.product_tmpl_id.id)
        return att

    @classmethod
    def binary_content(cls, xmlid=None, model='ir.attachment', id=None, field='datas',   
                       unique=False, filename=None, filename_field='datas_fname', download=False,
                       mimetype=None, default_mimetype='application/octet-stream',
                       access_token=None, related_id=None, access_mode=None, env=None):
        """ Get file, attachment or downloadable content
        If the ``xmlid`` and ``id`` parameter is omitted, fetches the default value for the
        binary field (via ``default_get``), otherwise fetches the field for
        that precise record.
        :param str xmlid: xmlid of the record
        :param str model: name of the model to fetch the binary from
        :param int id: id of the record from which to fetch the binary
        :param str field: binary field
        :param bool unique: add a max-age for the cache control
        :param str filename: choose a filename
        :param str filename_field: if not create an filename with model-id-field
        :param bool download: apply headers to download the file
        :param str mimetype: mintype of the field (for headers)
        :param related_id: the id of another record used for custom_check
        :param  access_mode: if truthy, will call custom_check to fetch the object that contains the binary.
        :param str default_mimetype: default mintype if no mintype found
        :param str access_token: optional token for unauthenticated access
                                 only available  for ir.attachment
        :param Environment env: by default use request.env
        :returns: (status, headers, content)
        """
        env = env or request.env
         
        obj = None
        if xmlid:
            obj = cls._xmlid_to_obj(env, xmlid)
        elif id and model in env.registry:
            obj = env[model].browse(int(id))
         
        if not obj or not obj.exists() or field not in obj:
            return (404, [], None)

         
        if model == 'ir.attachment' and access_token:
            obj = obj.sudo()
            if access_mode:
                if not cls._check_access_mode(env, id, access_mode, model, access_token=access_token, related_id=related_id):
                    return (403, [], None)
            elif not consteq(obj.access_token or u'', access_token):
                return (403, [], None)

         
        try:
            obj['__last_update']
        except AccessError:
            return (403, [], None)

        status, headers, content = None, [], None

         
        module_resource_path = None
        if model == 'ir.attachment' and obj.type == 'url' and obj.url:
            url_match = re.match(r"^/(\w+)/(.+)$", obj.url)
            if url_match:
                module = url_match.group(1)
                module_path = get_module_path(module)
                module_resource_path = get_resource_path(module, url_match.group(2))
                if module_path and module_resource_path:
                    module_path = os.path.join(os.path.normpath(module_path), '')   
                    module_resource_path = os.path.normpath(module_resource_path)
                    if module_resource_path.startswith(module_path):
                        with open(module_resource_path, 'rb') as f:
                            content = base64.b64encode(f.read())
                         

            if not module_resource_path:
                module_resource_path = obj.url

            if not content:
                status = 301
                content = module_resource_path
        else:
             
            att = env['ir.http'].find_field_attachment(env, model, field, obj)
            if att:
                content = att.url
                status = 301
                 
                 
                 
                 
                 
                mimetype = att.mimetype

            if not content:
                content = obj[field] or ''
             

         
        if not filename:
            if filename_field in obj:
                filename = obj[filename_field]
            elif module_resource_path:
                filename = os.path.basename(module_resource_path)
            else:
                filename = "%s-%s-%s" % (obj._name, obj.id, field)

         
         
        if not mimetype:
            mimetype = 'mimetype' in obj and obj.mimetype or False
        if not mimetype:
            if filename:
                mimetype = mimetypes.guess_type(filename)[0]
            if not mimetype and getattr(env[model]._fields[field], 'attachment', False):
                 
                attach_mimetype = env['ir.attachment'].search_read(domain=[('res_model', '=', model), ('res_id', '=', id), ('res_field', '=', field)], fields=['mimetype'], limit=1)
                mimetype = attach_mimetype and attach_mimetype[0]['mimetype']
            if not mimetype:
                mimetype = guess_mimetype(base64.b64decode(content), default=default_mimetype)

        headers += [('Content-Type', mimetype), ('X-Content-Type-Options', 'nosniff')]

         
        etag = bool(request) and request.httprequest.headers.get('If-None-Match')
        retag = '"%s"' % hashlib.md5(pycompat.to_text(content).encode('utf-8')).hexdigest()
        status = status or (304 if etag == retag else 200)
        headers.append(('ETag', retag))
        headers.append(('Cache-Control', 'max-age=%s' % (STATIC_CACHE if unique else 0)))

         
        if download:
            headers.append(('Content-Disposition', cls.content_disposition(filename)))
        return (status, headers, content)
