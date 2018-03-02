#!/Applications/djangostack-1.11.10-0/python/bin/python
# -*- coding utf-8 -*-
# vim: set fileencoding=utg8 :

import urllib
import urllib2
import bs4


class Client(object):


    def print_book(self, title, description, points):

        print 'Title: ' + title.strip()
        print 'Description: ' + description.strip()
        for point in points.strip().split('\n'):
            print '\t* ' +  point

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

        # search the title
        book_title_html = soup.find("div", "dotd-title")
        title = book_title_html.text

        # search the book cover
        book_image_html = soup.find("img","bookimage imagecache imagecache-dotd_main_image")

        # download the cover if there is one
        if book_image_html:
            urllib.urlretrieve('https:' + book_image_html['src'], "book_cover.jpg")

        # search for the description of the book
        # which is in the same parent of the title in the 7th div
        # it has no identifier or class so we can only get it knowing the exact div where it is
        # as well for the points of the book

        for i,sibling in enumerate(book_title_html.parent):
            if i == 7: # description of the book
                description = sibling.text
            if i == 9: # points of the book
                points =  sibling.text

        # print results
        self.print_book(title,description, points)



if __name__ == '__main__':
    client = Client()
    client.run()
