import asyncio
import json
import tornado.web
import tornado.ioloop
from Loger import g_main_log

class BaseHandler(tornado.web.RequestHandler):
    def ParseRequest(self):
        data = dict()        
        if self.request.headers.get('Content-Type') == 'application/json':
            data = json.loads(self.request.body.decode())
        else:
            for key in self.request.arguments:
                data[key] = self.get_argument(key)
        return data
    
    def HandleError(self, err_msg):
        self.write(err_msg)
        g_main_log.error(err_msg)
