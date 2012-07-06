#!/usr/bin/python
import sys
import tornado.ioloop
import tornado.web
import download
import constants
import os
from os.path import join, isfile
from json import JSONEncoder


class MainHandler(tornado.web.RequestHandler):
    #isDownloaded = False
    def get(self):
        #if not self.isDownloaded:
        #    download.downloadFile()
        #    self.isDownloaded = True
        path = "static/res"
        files = ["http://127.0.0.1:8888/" + join(path, f) for f in os.listdir(path) if isfile(join(path, f))]
        json = {"pics": files}
        self.write(JSONEncoder().encode(json))

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
