from BaseHandler import BaseHandler
import tornado.ioloop
from Loger import g_main_log

class MasterHandler(BaseHandler):
    def StopServer(self):
        tornado.ioloop.IOLoop.instance().stop()
    
    def get(self):
        try:
            data = self.ParseRequest()
            command = data.get('command', '')
            if command == 'stop':
                self.write('success')
                tornado.ioloop.IOLoop.instance().stop()
                g_main_log.info('stop consumer')
            else:
                self.write("unrecognized")
        except Exception as e:
            self.HandleError('master Error occur: % s' % e)
