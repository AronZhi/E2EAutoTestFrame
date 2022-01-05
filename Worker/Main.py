import sys
import os
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))

from Server import Server
from ReqHandler import ReqHandler
from MasterHandler import MasterHandler
from WoekerHandler import WorkerHandler
from Loger import g_main_log

if __name__ == '__main__':
    try:
        webServer = Server()
        webServer.Run(9001, [(r'/req', ReqHandler), (r'/master', MasterHandler), (r'/worker', WorkerHandler)])
    except Exception as e:
        g_main_log.error(str(e))
    