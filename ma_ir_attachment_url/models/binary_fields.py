 
 
 
 
from odoo import fields
import mimetypes
import requests

from odoo.tools.mimetypes import guess_mimetype
from . import image


def get_mimetype_and_optional_content_by_url(url):
    mimetype = mimetypes.guess_type(url)[0]
    content = None

     
    if not mimetype:
        with requests.head(url, timeout=5) as r:
            mimetype = getattr(r, 'headers', {}).get('Content-Type')

    index_content = mimetype and mimetype.split('/')[0]
    if not mimetype or index_content == 'text':
        with requests.get(url, timeout=5) as r:
            content = getattr(r, 'content')
            if not mimetype and content:
                mimetype = guess_mimetype(content)

    return mimetype, content


class Binary(fields.Binary):

     
    def create(self, record_values):
        assert self.attachment
        if not record_values:
            return
         
        env = record_values[0][0].env

         
        url_record_values = []
        other_record_values = []
        for pair in record_values:
            value = pair[1]
            if image.is_url(value):
                url_record_values.append(pair)
            else:
                other_record_values.append(pair)

        with env.norecompute():
            env['ir.attachment'].sudo().with_context(
                binary_field_real_user=env.user,
            ).create([{
                'name': self.name,
                'res_model': self.model_name,
                'res_field': self.name,
                'res_id': record.id,
                'type': 'url',   
                'url': value,   
            }
                for record, value in url_record_values
                if value
            ])
         
        super(Binary, self).create(other_record_values)
         

    def write(self, records, value):
        domain = [
            ('res_model', '=', self.model_name),
            ('res_field', '=', self.name),
            ('res_id', 'in', records.ids),
        ]
        atts = records.env['ir.attachment'].sudo().search(domain)
        if value and atts.url and atts.type == 'url' and not image.is_url(value):
            atts.write({
                'url': None,
                'type': 'binary',
            })
        if value and image.is_url(value):
             
            with records.env.norecompute():
                 
                 
                 
                 
                 
                 
                if value:
                    mimetype, content = get_mimetype_and_optional_content_by_url(value)
                    index_content = records.env['ir.attachment']._index(content, None, mimetype)

                     
                    atts.write({
                        'url': value,
                        'mimetype': mimetype,
                        'datas': None,
                        'type': 'url',
                        'index_content': index_content,
                    })

                     
                    for record in (records - records.browse(atts.mapped('res_id'))):
                        atts.create({
                            'name': self.name,
                            'res_model': record._name,
                            'res_field': self.name,
                            'res_id': record.id,
                            'type': 'url',
                            'url': value,
                            'mimetype': mimetype,
                            'index_content': index_content,
                        })
                else:
                    atts.unlink()
        else:
            super(Binary, self).write(records, value)


fields.Binary = Binary
