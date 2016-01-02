#!/usr/bin/env python3

import tornado.ioloop
import tornado.web

class UserHandler(tornado.web.RequestHandler):
    def post(self):
        self.write('post')

    def get(self):
        self.write('get')

def make_app():
    return tornado.web.Application([
        (r'/user', UserHandler),
        (r'/(.*)', tornadotornado..web.StaticFileHandler, {'path': './web/dist',
                                           'default_filename': 'index.html'}),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

