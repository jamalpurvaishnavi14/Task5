from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag, *('-> {0} > {1}'.format(*attr) for attr in attrs), sep='\n')

MyHTMLParser().feed(''.join([input() for _ in range(int(input()))]))
