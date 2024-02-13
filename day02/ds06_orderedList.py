# file : ds05_orderedList.py
# date : 20240213
# desc : 파이썬 자료구조와 알고리즘 p.111 Code03-6.py

def printPoly(t_x, p_x):
    polyStr = "P(x) = "

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + ""
        term -= 1

    return polyStr

def calcPoly(xVal, t_x, p_x):
    retValue = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

## 전역 변수 선언부분

tx = [300, 20, 0]
px = [7, -4, 5]   # 7x^3 - 4x^2 + 0x^1 + 5x^0

## 메인 코드 부분

if __name__ == '__main__':
    pStr = printPoly(tx, px)
    print(pStr)

    xValue = int(input('X 값 --> '))

    pxValue = calcPoly(xValue,tx,px)
    print(pxValue)