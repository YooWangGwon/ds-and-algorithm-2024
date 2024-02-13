# file : ds05_orderedList.py
# date : 20240213
# desc : 파이썬 자료구조와 알고리즘 p.109 Code03-5.py

def printPoly(p_x):
    term = len(p_x) - 1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + ""
        term -= 1

    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

## 전역 변수 선언부분

px = [7, -4, 0, 5]   # 7x^3 - 4x^2 + 0x^1 + 5x^0

## 메인 코드 부분

if __name__ == '__main__':
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input('X 값 --> '))

    pxValue = calcPoly(xValue,px)
    print(pxValue)