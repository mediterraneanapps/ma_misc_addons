 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

from openerp import fields
from openerp import models
from datetime import datetime
from openerp import SUPERUSER_ID
from openerp.http import request
from openerp.addons.base.models.ir_cron import _intervalTypes
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ResUsers(models.Model):
    _inherit = 'res.users'


    login_calendar_id = fields.Many2one('resource.calendar'
                                             'Allowed Login Calendar', company_dependent=True,
                                             help='The user will be only allowed to login in the calendar defined here.'),
    no_multiple_sessions = fields.Boolean('No Multiple Sessions', company_dependent=True,
                                               help='Select this to prevent user to start a session more than once'),
    interval_number = fields.Integer('Session Timeout', company_dependent=True, help='Timeout since last activity for auto logout')
    interval_type = fields.Selection([('minutes', 'Minutes')
                                           ('hours', 'Hours'), ('work_days', 'Work Days'),
                                           ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')],
                                          'Interval Unit', company_dependent=True),
    session_ids = fields.One2many('ir.sessions', 'user_id', 'User Sessions')


     
    def get_expiring_date(self, cr, uid, id, context):
        now = datetime.now()
        user_obj = request.registry.get('res.users')
        user_id = user_obj.browse(cr, SUPERUSER_ID, id, context=context)
        g_exp_date = now + _intervalTypes['weeks'](1)
        if id != SUPERUSER_ID:
            if user_id.interval_type:
                u_exp_date = now + _intervalTypes[user_id.interval_type](user_id.interval_number)
            else:
                u_exp_date = g_exp_date
            g_no_multiple_sessions = False
             
            for group in user_id.groups_id:
                if group.no_multiple_sessions:
                    g_no_multiple_sessions = True
                if group.interval_type:
                    t_exp_date = now + _intervalTypes[group.interval_type](group.interval_number)
                    if t_exp_date < g_exp_date:
                        g_exp_date = t_exp_date
            if g_no_multiple_sessions:
                 
                pass
            if g_exp_date < u_exp_date:
                u_exp_date = g_exp_date
        else:
            u_exp_date = g_exp_date
        seconds = u_exp_date - now
        return datetime.strftime(u_exp_date, DEFAULT_SERVER_DATETIME_FORMAT), seconds.seconds
