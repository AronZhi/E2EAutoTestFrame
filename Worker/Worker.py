import multiprocessing
import json
from uuid import uuid1
from multiprocessing import Queue
from Container.Container import Container
from Container.ResponseProxy import ResponseProxy
from Loger import g_main_log

def Work(msg_queue: Queue, res_queue: Queue):
    container = Container()
    resProxy = ResponseProxy()
    while True:
        json_msg = msg_queue.get()
        if json_msg.lower() == 'stop':
            break
        data = json.loads(json_msg)
        res = container.CallFunc(data)
        error_msg = container.GetLastError()
        res_str = resProxy.ConstrutBody(res, error_msg)
        res_queue.put(res_str)
    return True

class Worker:
    def __init__(self) -> None:
        self.msg_queue = Queue()
        self.res_queue = Queue()
        self.id = uuid1()
        g_main_log.info(f'start {self.id} worker')
        self.process = multiprocessing.Process(target=Work, args=(self.msg_queue, self.res_queue))
        self.process.start()
    
    def GetIdentity(self):
        return self.id
    
    def Handle(self, msg: str):
        if msg is None or msg == '':
            return False
        self.msg_queue.put(msg)
        res = self.res_queue.get()
        return res
    
    def Stop(self):
        self.msg_queue.put('stop')
        self.process.join()
        g_main_log.info(f'stop {self.id} worker')
