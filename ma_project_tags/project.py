from openerp import models, fields


class Project(models.Model):
    """"""

    _name = 'project.project'
    _inherits = {}
    _inherit = ['project.project']


    project_tag_ids = fields.Many2many('project_tags.project_tag', 'project_tags___project_tag_ids_rel', 'project_id', 'project_tag_id', string='Tags')


    _defaults = {
    }

    _constraints = [
    ]


Project()

 
