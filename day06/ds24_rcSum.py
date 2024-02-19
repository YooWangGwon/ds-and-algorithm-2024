# file : ds24_rcSum.py 
# date : 20240219
# desc : 재귀호출 합산함수

def  addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1) # 5 + addNumber(4)[4+addNumber(3)[3+addNumber(2)[2+addNumber(1)]]]

sum= addNumber(5) # 15
print(sum)