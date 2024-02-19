# file : ds27-1_fractalTriangle.py
# date : 20240219
# desc : 시에르핀스키 삼각형 그리기(파이썬 자료구조와 알고리즘 p.390)

from tkinter import *
import random

## 함수 선언
def drawTriangle(x, y, size):
    if size >= 30:
        drawTriangle(x,y,size/2)
        drawTriangle(x+size/2,y,size/2)
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4),size/2)
    else:
        canvas.create_polygon(x,y,x+size,y,x+size/2,y-size*(3**0.5)/2,fill=random.choice(colors),outline="black")

## 전역 변수 선언
wSize = 1000
radius = 400
colors = ['red','green','blue','black','orange','indigo','violet','crimson','gray']

## 메인코드
window = Tk()
window.title("프랙탈 삼각형 그리기")
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawTriangle(wSize/5,wSize/5*4,wSize*2/3)

canvas.pack()
window.mainloop()