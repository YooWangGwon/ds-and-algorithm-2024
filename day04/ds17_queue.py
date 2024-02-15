# file : ds17_queue.py
# date : 20240215
# desc : 큐 일반구현

# Queue 풀 함수
def isQueueFull():
    global SIZE, rear
    if rear == (SIZE - 1):
        return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    else:
        return False
    
# Queue 엠티 확인함수
def isQueueEmpty():
    global front, rear
    if front == rear:
        return  True
    else:
        return False

# Queue 데이터 삽입 함수
def enQueue(data):
    global queue, rear
    if isQueueFull() == True: # 큐가 꽉 차서 데이터를 넣을 수 없다면
        print('큐가 꽉찼습니다.')
        return # 함수탈출
    else:
        rear += 1
        queue[rear] = data

# Queue 테이터 추출 함수
def deQueue():
    global front, queue
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data
    
# 추출 데이터 확인 함수
def peek():
    global queue, front
    if isQueueEmpty() == True:
        print('큐가 비었습니다')
        return None
    else:
        return queue[front+1]

# 전역변수
SIZE = int(input('큐 크기 입력(정수) > ')) # 대문자는 상수(constant)
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == '__main__':
    while True:
        select = input('삽입(e), 추출(d), 확인(p), 종료(x) > ')

        if select.lower() == 'e':
            data = input('입력할 데이터 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')

        elif select.lower() == 'd':
            data = deQueue()
            print(f'추출 데이터 > {data}')
            print(f'큐 상태:{queue}')

        elif select.lower() == 'p':
            data = peek()
            print(f'확인데이터 > {data}')
            print(f'큐 상태:{queue}')

        elif select.lower() == 'x':
            break
        
        else:
            continue