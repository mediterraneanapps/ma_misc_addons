 
 
 
 
 
import logging
import werkzeug

from odoo.http import request, route
from odoo.addons.web.controllers.main import Binary
from odoo.addons.ma_ir_attachment_url.models.image import SIZES_MAP

_logger = logging.getLogger(__name__)


def redirect(url):
    return werkzeug.utils.redirect(url, code=301)


class BinaryExtended(Binary):

    @route()
    def content_image(self, xmlid=None, model='ir.attachment', id=None, field='datas', filename_field='datas_fname', unique=None, filename=None, mimetype=None, download=None, width=0, height=0):   
        """
        Overrided content_image creates resized images (if required) and returns public s3 link of them

        When it works?
        - if given object is product image (see is_product_product_image var)
        - if base content_image method returns 301 (redirect) response and width or height given

        How resizing works?
        - Tries to get resized image from s3 storage. If it does not exists - it is created, stored in cache and returned
        - If given object is product image, new sizes are base on SIZES_MAP and given field value
        - If not, it resizes using given width and height
        """

        res = super(BinaryExtended, self).content_image(xmlid, model, id, field, filename_field, unique, filename, mimetype, download, width, height)

        if request.env['ir.config_parameter'].sudo().get_param('ma_ir_attachment_url.storage') != 's3':
            return res

        is_product_product_image = model == 'product.product' and field in ('image', 'image_small', 'image_medium')
        if not (res.status_code == 301 and (width or height)) and not is_product_product_image:
            return res

         
         
         

         
        env = request.env
         
        obj = None
        if xmlid:
            obj = env.ref(xmlid, False)
        elif id and model in env.registry:
            obj = env[model].browse(int(id))

         
        attachment = None
        if model == 'ir.attachment':
             
            attachment = obj
        elif is_product_product_image:
             
             
            attachment = env['ir.http']._find_field_attachment(env, model, field, obj.id)
            if not attachment:
                image_variant_attachment = env['ir.http']._find_field_attachment(env, model, 'image_variant', obj.id)
                if image_variant_attachment:
                    w, h = SIZES_MAP[field]
                    resized_attachment = image_variant_attachment._get_or_create_resized_in_cache(w, h, field=field)
                    attachment = resized_attachment.resized_attachment_id

        if not attachment and model != 'ir.attachment':
            attachment = env['ir.http'].find_field_attachment(env, model, field, obj)

        if not attachment:
             
            _logger.error('Attachment is not found')
            return res

         
        if not width and not height:
            return redirect(attachment.url)

         
        height = int(height or 0)
        width = int(width or 0)
         
        if width > 500:
            width = 500
        if height > 500:
            height = 500

        resized_attachment = attachment._get_or_create_resized_in_cache(width, height)
        url = resized_attachment.resized_attachment_id.url
        return redirect(url)
