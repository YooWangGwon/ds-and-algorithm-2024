# file : ds15_stackBracelet.py
# date : 20240214
# desc : 스택 수식정합여부 판단

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
# 수식괄호 판단함수
def checkBracket(expr): # '(a+b)'
    for ch in expr: # '(' 'a' '+' 'b' ')'
        if ch in '({[<': # 여는 괄호가 있으면
            push(ch)
        elif ch in ')}]>': # 닫는 괄호가 있으면
            out = pop()
            if ch == ')' and out == '(':
                pass # continue
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            continue

    if isStackEmpty() == True:
        return True
    else:
        return False

# 전역변수 선언
SIZE = 50
stack = [None for _ in range(SIZE)]
top = -1

# 메인코드
if __name__ == '__main__':
    arr = ['(a+b)',')a*b(','((a+b)-c','(a+b]','(<a+{b+c}/[c*d]>)']
    print(arr.insert(1,3))

    # for expr in arr:
    #     top = -1
    #     print(f'{expr} ==> {checkBracket(expr)}')