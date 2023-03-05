from html.parser import HTMLParser

def show(attrs):
    for attr in attrs:
            print("-> {0} > {1}".format(attr[0], attr[1]))
            
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        show(attrs)
            
    def handle_endtag(self, tag):
        print("End   : " + tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        show(attrs)
        
parser = MyHTMLParser()
parser.feed(''.join([input() for _ in range(int(input()))]))
