from graphics import *

def main():
    window = GraphWin('CS110',600,600)
    pt1 = Point(40,340)
    pt2 = Point(260,80)
    pt3 = Point(560,200)
    line1 = Line(pt1, pt2)
    line2 = Line(pt2, pt3)
    line3 = Line(pt3, pt1)
    st1 = Point(20,80)
    st2 = Point(560,480)
    st21 = Point(540,200)
    st22 = Point(190,390)    
    point = Point(250,360)
    circle = Circle(point, 60)
    circle.setFill('Blue')
    square1 = Rectangle(st1,st2)
    square1.setFill('Yellow')
    square2 = Rectangle(st21, st22)
    square2.setFill('Red')
    square1.draw(window)
    square2.draw(window)
    line1.draw(window)
    line2.draw(window)
    line3.draw(window)
    circle.draw(window)
    point.draw(window)

main()
input()