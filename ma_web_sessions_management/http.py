 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

import logging
import openerp
import werkzeug.contrib.sessions
import werkzeug.datastructures
import werkzeug.exceptions
import werkzeug.local
import werkzeug.routing
import werkzeug.wrappers
import werkzeug.wsgi
from openerp.http import request
from openerp.tools.func import lazy_property
 
_logger = logging.getLogger(__name__)


class OpenERPSession(openerp.http.OpenERPSession):

    def logout(self, keep_db=False, logout_type=None, env=None):
        try:
            env = env or request.env
        except:
            pass

        if env and hasattr(env, 'registry') and env.registry.get('ir.sessions'):
            session = env['ir.sessions'].sudo().search([('session_id', '=', self.sid)])
            if session:
                session._on_session_logout(logout_type)
        return super(OpenERPSession, self).logout(keep_db=keep_db)


class RootTkobr(openerp.http.Root):

    @lazy_property
    def session_store(self):
         
        path = openerp.tools.config.session_dir
        _logger.debug('HTTP sessions stored in: %s', path)
        return werkzeug.contrib.sessions.FilesystemSessionStore(path, session_class=OpenERPSession)


root = RootTkobr()
openerp.http.root.session_store = root.session_store
