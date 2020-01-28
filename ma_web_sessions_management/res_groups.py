 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

from openerp import fields
from openerp import models


class ResGroups(models.Model):
    _inherit = 'res.groups'


    login_calendar_id = fields.Many2one('resource.calendar'
                                             'Allow Login Calendar', company_dependent=True,
                                             help='The user will be only allowed to login in the calendar defined here.'),
    no_multiple_sessions = fields.Boolean('No Multiple Sessions', company_dependent=True,
                                               help='Select this to prevent user to start a session more than once'),
    interval_number = fields.Integer('Session Timeout', company_dependent=True, help='Timeout since last activity for auto logout')
    interval_type = fields.Selection([('minutes', 'Minutes')
                                           ('hours', 'Hours'), ('work_days', 'Work Days'),
                                           ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')],
                                          'Interval Unit', company_dependent=True),
