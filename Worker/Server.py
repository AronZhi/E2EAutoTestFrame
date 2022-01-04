import tornado.web
import tornado.httpserver
import tornado.ioloop

class Server(object):
    def Run(self, port: int, protocol: list):
        """
        windows环境python3.7及以上版本tornado使用asyncio抛出NotImplementedError异常，
        试用前需要以下处理
        if psutil.WINDOWS and sys.version_info >= (3,7):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        """
        app = tornado.web.Application(protocol)
        httpServer = tornado.httpserver.HTTPServer(app)
        httpServer.listen(port)
        tornado.ioloop.IOLoop.instance().start()