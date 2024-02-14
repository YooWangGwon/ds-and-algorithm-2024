# file : ds14_stack.py
# date : 20240214
# desc : 스택 전체  구현
import webbrowser
import time

# 스택 풀 확인함수
def isStackFull():
    global SIZE, stack, top
    if top == (SIZE - 1):
        return True # 스택이 꽉 찼음
    else:
        return False

# 스택 데이터 삽입함수
def push(data):
    global SIZE, stack, top
    if isStackFull() == True:
        print('스택이 꽉찼습니다.')
        return
    else:
        top += 1
        stack[top] = data

# 스택 앰티 확인함수
def isStackEmpty():
    global SIZE, stack, top
    if top <= -1:
        return True # 스택이 비었음
    else:
        return False
    

# 스택 데이터 추출함수
def pop():
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택이 비어있습니다')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
# 스택 최종 데이터 확인함수
def peek():
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택이 비어있습니다.')
        return None
    else:
        return stack[top]
    
# 전역변수 선언
SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

# 메인코드
if __name__ == '__main__':
    urls = ['naver.com','daum.net','nate.com','bing.com','github.com']

    for url in urls:
        push(url)
        webbrowser.open(f'https://www.{url}')
        print(url, end=' --> ')
        time.sleep(1) # 1초간 잠시 멈췄다가 다시 작업 재개

    print('방문종료')
    print(stack)
    time.sleep(5) # 5초동안 아무것도 하지않고 대기함


    while True:
        url = pop()
        if url == None:break

        webbrowser.open(f'https://www.{url}')
        print(url, end = ' --> ')
        time.sleep(1)
    
    print('방문종료')