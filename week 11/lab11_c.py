from abc import ABC, abstractmethod, abstractproperty
from typing import List, Dict

class Node(ABC):
    def __init__(self, content:str ='', attributes:Dict ={}):
        self.__children = []
        self.__attributes = attributes
        self.__content = content

    @property
    def content(self):
        return self.__content

    @property
    def children(self):
        return self.__children

    @property
    def attribites(self):
        return self.__attributes

    @abstractmethod
    def html(self):
        pass

    def appendChild(self, child):
        self.__children.append(child)


class StandardNodeFactory():
    def makeNode(self, type, content:str ='', attributes:Dict ={}):
        if type == "div":
            node = Div(content, attributes)

        elif type == "b":
            node = B(content, attributes)

        elif type == 'body':
            node = Body(content, attributes)

        elif type == 'title':
            node = Title(content, attributes)

        elif type == "head":
            node = Head(content, attributes)

        elif type == "html":
            node = Html(content, attributes)
        return node
    
class DebugNodeFactory():
    def debugNode(self, type):
        if type == 'div':
            str = "Div node is created."
        elif type == "b":
            str = "B node is created."

        elif type == 'body':
            str = "Body node is created."

        elif type == 'title':
            str = "Title node is created."

        elif type == "head":
            str = "Head node is created."

        elif type == "html":
            str = "Html node is created."

        return str
        
class Div(Node):
    def html(self):
        str = '<div'
        for k, v in self.attribites.items():
            str += ' ' + k + '="' + v + '"'
        str += '>'

        # children
        for child in self.children:
            str += child.html()


        str += self.content


        str += '</div>'
        return str

class B(Node):
    def html(self):
        str = '<b'
        for k, v in self.attribites.items():
            str += ' ' + k + ' ="' + v + '"'

        str += '>'

        #children

        for child in self.children:
            str += child.html()

        str += self.content

        str +='</b>'
        return str

class Body(Node):
    def html(self):
        str = '<body'
        for k, v in self.attribites.items():
            str += ' ' + k + ' ="' + v + '"'

        str += '>'

        #children

        for child in self.children:
            str += child.html()

        str += self.content

        str +='</body>'
        return str

class Title(Node):
    def html(self):
        str = '<title'
        for k, v in self.attribites.items():
            str += ' ' + k + ' ="' + v + '"'

        str += '>'

        #children

        for child in self.children:
            str += child.html()

        str += self.content

        str +='</title>'
        return str

class Head(Node):
    def html(self):
        str = '<head'
        for k, v in self.attribites.items():
            str += ' ' + k + ' ="' + v + '"'

        str += '>'

        #children

        for child in self.children:
            str += child.html()

        str += self.content

        str +='</head>'
        return str

class Html(Node):
    def html(self):
        str = '<!DOCTYPE html><html '
        for k, v in self.attribites.items():
            str += ' ' + k + ' ="' + v + '"'

        str += '>'

        #children

        for child in self.children:
            str += child.html()

        str += self.content

        str +='</html>'
        return str

def main():

    factory = StandardNodeFactory()
    factory1 = DebugNodeFactory()
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = factory.makeNode('div','This is a test A', divAtts)
    divA1 = factory1.debugNode('div')
    print(divA1)

    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = factory.makeNode('div','This is a test B', divAtts)
    divB1 = factory1.debugNode('div')
    print(divB1)

    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = factory.makeNode('div','This is a test C', divAtts)
    divC1 = factory1.debugNode('div')
    print(divC1)

    b = factory.makeNode('b','This is a simple HTML file')
    divC.appendChild(b)
    b1 = factory1.debugNode('b')
    print(b1)

    body = factory.makeNode('body')
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    body1 = factory1.debugNode('body')
    print(body1)

    title = factory.makeNode('title','Example')
    head = factory.makeNode('head')
    head.appendChild(title)
    title1 = factory1.debugNode('title')
    print(title1)
    head1 = factory1.debugNode('head')
    print(head1)

    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = factory.makeNode('html','', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    html1 = factory1.debugNode('html')
    print(html1)
    
    print(html.html())


if __name__=="__main__":
    main()