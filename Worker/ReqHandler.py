from BaseHandler import BaseHandler
from WorkerMgr import worker_mgr

class ReqHandler(BaseHandler):
    def post(self):
        body = self.ParseRequest()
        id = body.get('id', None)
        worker = worker_mgr.GetWorker(id)
        if worker is None:
            self.write('no container find, please find container first')
        else:
            data = body.get('data', '')
            res = worker.Handle(data)
            self.write(str(res))

