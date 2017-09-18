import tornado.ioloop
import tornado.web

# Install tornado by doing: sudo pip install tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        parameter_a = self.get_argument("a", None)
        parameter_b = self.get_argument("b", None)
        if parameter_a is None or parameter_a.isnumeric() is False:
            # Handle me
            self.set_status(400)
            return self.finish("Invalid parameter a")
        elif parameter_b is None or parameter_b.isnumeric() is False:
            # Handle me
            self.set_status(400)
            return self.finish("Invalid parameter b")
        else:
            self.write({'res': float(parameter_a) + float(parameter_b)})


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
