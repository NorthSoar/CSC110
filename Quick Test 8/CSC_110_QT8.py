from graphics import *

def main():
    window = GraphWin('Huy Le',250,250)
    bigCircle = Circle(Point(125,125),60)
    greenCircleOne = Circle(Point(113,113),12)
    greenCircleTwo = Circle(Point(137,113),12)
    redLine = Line(Point(100,150),Point(150,150))
    bigCircle.draw(window)
    greenCircleOne.draw(window).setFill('green')
    greenCircleTwo.draw(window).setFill('green')
    redLine.draw(window).setFill('red')
    
main()

# A clear neutral face emoji with green eyes and red lips