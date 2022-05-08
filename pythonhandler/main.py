import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from handler.login import LoginHandler
from handler.register import RegisterHandler

class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
      (r'/login', LoginHandler),
      (r'/register', RegisterHandler),
    ]

    settings = {
      'template_path': 'src/components',
      'static_path': 'static',
      "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
      "login_url": "/login",
      "register_url": "/register"
    }

    tornado.web.Application.__init__(self, handlers, **settings)
    

if __name__ == '__main__':
  tornado.options.parse_command_line()
  app = tornado.httpserver.HTTPServer(Application())
  app.listen(8080)
  print("Tornado server is ready for service: http://localhost:8080/\r")
  tornado.ioloop.IOLoop.instance().start()
