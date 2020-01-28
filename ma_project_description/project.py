from openerp import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

         
    description = fields.Text('description', groups="ma_project_description.group_access_to_project_description")



class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    def name_get(self, cr, uid, ids, context=None):
        res = []
        if not ids:
            return res
        if isinstance(ids, int):
            ids = [ids]
        for id in ids:
            elmt = self.browse(cr, uid, id, context=context)
            res.append((id, elmt.name))
        return res
 
