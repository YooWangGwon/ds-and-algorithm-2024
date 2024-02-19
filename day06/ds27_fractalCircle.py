# file : ds27_fractalCircle.py
# date : 20240219
# desc : 프랙탈 원 그리기

from tkinter import *
import random

def drawCircle(x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r, width = 2, outline=random.choice(colors)) # x-r,y-r은 왼쪽 상단 / x+r,y+r은 우측 하단

    if r >= 5:
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)

# 전역변수
radius = 400
wSize = 1000
colors = ['red','green','blue','black','orange','indigo','violet','crimson','gray']

# 메인코드
window = Tk()
window.title('프랙탈 원그리기')
canvas = Canvas(window, height=wSize, width=wSize, background='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()