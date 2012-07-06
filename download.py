import constants
import urllib2
import sys


def downloadFile():
    for url in constants.pics:
        data = urllib2.urlopen(url)

        fileName = "a" + str(hash(url))
        file = open("static/res/" + fileName, "wb")
        file.write(data.read())
        file.close()
