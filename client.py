#!python
# -*- coning utf-8 -*-
# vim: set fileencoding=utg8 :

import urllib2
import bs4

class Client(object):

    def get_web(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def run(self):
        # download the web page
        html = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        # parse it
        soup = bs4.BeautifulSoup(html, "lxml")
        # print results
if __name__ == '__main__':
    client = Client()
    client.run()