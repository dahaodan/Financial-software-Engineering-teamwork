import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from handler.login import LoginHandler
from handler.register import RegisterHandler
from handler.dashboard import DashboardHandler
from handler.research import ResearchHandler
from handler.userinfo import UserinfoHandler
from handler.stocknews import StocknewsHandler
from handler.transaction import TransactionHandler
from handler.simulation import SimulationHandler
from handler.forgetpassword import ForgetpasswordHandler

class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
      (r'/login', LoginHandler),
      (r'/register', RegisterHandler),
      (r'/dashboard',DashboardHandler),
      (r'/research',ResearchHandler),
      (r'/userinfo',UserinfoHandler),
      (r'/stocknews',StocknewsHandler),
      (r'/transaction',TransactionHandler),
      (r'/simulation',SimulationHandler),
      (r'/forgetpassword',ForgetpasswordHandler)
    ]

    settings = {
      'template_path': 'src/components',
      'static_path': 'static',
      "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
      "login_url": "/login",
      "register_url": "/register",
      "dashboard_url": "/dashboard",
      "research_url":"/research",
      "userinfo_url":"/userinfo",
      "stocknews_url":"/stocknews",
      "transaction_url":"/transaction",
      "simulation_url":"/simulation",
      "forgetpassword_url":"/forgetpassword"
    }

    tornado.web.Application.__init__(self, handlers, **settings)
    

if __name__ == '__main__':
  tornado.options.parse_command_line()
  app = tornado.httpserver.HTTPServer(Application())
  app.listen(8080)
  print("Tornado server is ready for service: http://localhost:8080/\r")
  tornado.ioloop.IOLoop.instance().start()
