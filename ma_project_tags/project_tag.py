from openerp import models, fields


class ProjectTag(models.Model):
    """"""

    _name = 'project_tags.project_tag'
    _description = 'project_tag'


    name = fields.Char(string='Name', required=True, size=64)
    project_id = fields.Many2many('project.project', 'project_tags___project_tag_ids_rel', 'project_tag_id', 'project_id', string='&lt;no label&gt;')


    _defaults = {
    }

    _constraints = [
    ]


ProjectTag()

 
