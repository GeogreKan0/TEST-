from tkinter import *
from random import  randint

root = Tk()
background  = Canvas (root, width = 800, height = 600, bg ='#e6e6fa')
background.pack()


class Drop:
    def __init__ (self, a, x, y, speed, l):
        self.x = x                                       #задаем всем каплям случайное местоположение по ширине
        self.y = y                                       #чтобы неровно падали задать случайное местоположение за пределами экрана
        self.speed = speed                               #скорость падения
        self.l = l                                       #длина полос дождя
        self.a = a
        self.color = "#8a2be2"
        self.w=900                                       #длина
        self.h=600                                       #высота
        self.line = a.create_line(self.x, self.y, self.x, self.y+l, fill=self.color)

    def move(self):
        self.y += self.speed
        self.a.move(self.line, 0, self.speed)#падает сверху


        if self.y > self.h: #бесконечный дождь
            self.a.move(self.line, 0, -(self.h+self.l))
            self.y -= self.h + self.l


def move_drops():
    for drop in drops:
        drop.move()

    root.after(10, move_drops)

drops = [Drop(background, x=randint(0, 900), y=randint(0, 700),
                  speed=randint(5, 15), l=randint(5, 25)) for i in range(400)]#массив где 400 элементов

move_drops()
root.mainloop()