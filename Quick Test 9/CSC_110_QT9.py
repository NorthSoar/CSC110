from graphics import *

def main():
    window = GraphWin('Smiley',800,800)
    ears = Oval(Point(170,250),Point(630,500))
    head = Circle(Point(400,400),200)
    leftEye = Circle(Point(470,300),25)
    rightEye = Circle(Point(330,300),25)
    nose = Polygon(Point(400,320),Point(400,420),Point(370,420))
    mouth = Oval(Point(300,500),Point(500,400))
    toplip = Rectangle(Point(300,450),Point(500,400))
    teeth = Rectangle(Point(315,420),Point(485,468))
    beard = Polygon(Point(300,520),Point(320,600),Point(340,550),Point(360,650),Point(380,600),Point(400,700),Point(420,600),Point(440,650),Point(460,550),Point(480,600),Point(500,520))
    ears.draw(window).setFill('#ff940b')
    head.draw(window).setFill('#ffc021')
    leftEye.draw(window).setFill('#654400')
    rightEye.draw(window).setFill('#654400')
    mouth.draw(window).setFill('#ff940b')
    teeth.draw(window).setFill('white')
    toplip.setFill('#ffc021')
    toplip.draw(window).setWidth(width=0)
    nose.draw(window).setFill('#654400')
    beard.draw(window).setFill('#654400')
    
main()

