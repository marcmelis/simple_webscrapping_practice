#!/usr/bin/python3
# -*- coding utf-8 -*-
# vim: set fileencoding=utg8 :

from urllib.request import urlretrieve
from urllib.request import urlopen
import bs4


class Client(object):


    def print_book(self, title, description, points, web_url, output = "book_info.txt"):
        print (title.strip(), file=open(output,"w"))
        print (description.strip(), file=open(output,"a"))
        points = points.strip()
        if points:
            for point in points.split('\n'):
                print ('\t* ' +  point , file=open(output,"a"))
        print (web_url, file=open(output,"a"))

    def get_web(self, url):
        f = urlopen(url)
        html = f.read()
        f.close()
        return html

    def run(self):

        web_url = "https://www.packtpub.com/packt/offers/free-learning/"
        # download the web page
        html = self.get_web(web_url)

        # parse it
        soup = bs4.BeautifulSoup(html, "lxml")

        # search the title
        book_title_html = soup.find("div", "dotd-title")
        title = book_title_html.text

        # search the book cover
        book_image_html = soup.find("img","bookimage imagecache imagecache-dotd_main_image")

        # download the cover if there is one

        if book_image_html:
            urlretrieve('http:' + book_image_html['src'].replace(" ", "%20"), "book_cover.jpg")

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
        self.print_book(title,description, points, web_url)


if __name__ == '__main__':
    client = Client()
    client.run()
