from BaseHandler import BaseHandler

class ReqHandler(BaseHandler):
    def post(self):
        data = self.ParseRequest()
