from .Worker import Worker

class WorkerMgr:
    def __init__(self):
        self.map = {}
    
    def __del__(self):
        for worker in self.map:
            worker.Stop()
    
    def CreateWorker(self, identiy):
        worker = self.map.get(identiy, None)
        if worker is None:
            worker = Worker()
            identity = worker.GetIdentity()
            self.map[identity] = worker
        return worker
    
    def GetWorker(self, identiy):
        return self.map.get(identiy, None)
    
    def StopWorker(self, indentiy):
        worker = self.map.get(indentiy, None)
        if worker is None:
            return
        worker.Stop()
        del self.map[indentiy]

worker_mgr = WorkerMgr()