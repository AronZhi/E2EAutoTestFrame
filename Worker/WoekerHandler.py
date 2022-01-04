from BaseHandler import BaseHandler
from WorkerMgr import worker_mgr

class WorkerHandler(BaseHandler):    
    def post(self):
        body = self.ParseRequest()
        action = body.get('action', '').lower()
        if action == 'create':
            worker = worker_mgr.CreateWorker()
            id = worker.GetIdentity()
            self.write(id)
        elif action == 'stop':
            id = body.get('id', '')
            worker_mgr.StopWorker(id)
            self.write('success')
        else:
            self.write('action type error')
