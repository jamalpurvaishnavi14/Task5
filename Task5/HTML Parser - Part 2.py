from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        data = str(data).split('\n')
        if len(data)>1:
            print('>>> Multi-line Comment', *data, sep='\n')
        else:
            print('>>> Single-line Comment', data[0], sep='\n')            
    def handle_data(self, data):
        data = str(data).replace('\n', '')
        if len(data)>0:
            print('>>> Data', data, sep='\n')

html = ""       
for _ in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
