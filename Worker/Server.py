import tornado.web
import tornado.httpserver
import tornado.ioloop
import psutil

class Server(object):
    def Run(self, port: int, protocol: list):
        if psutil.WINDOWS:
            import sys
            ver = sys.version_info
            if ver.major >= 3 and ver.micro >= 7:
                pass
            else:
                import asyncio
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        app = tornado.web.Application(protocol)
        httpServer = tornado.httpserver.HTTPServer(app)
        httpServer.listen(port)
        tornado.ioloop.IOLoop.instance().start()