# file : ds18_circularQueue.py
# date : 20240215
# desc : 원형 큐 일반구현 : 원형큐에서는 rear|front % SIZE 개념이 핵심

# Queue 풀 함수
def isQueueFull(): 
    global SIZE, queue, front, rear
    if(rear+1)%SIZE == front:
        return True
    else:
        return False
    
    
# Queue 엠티 확인함수
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return  True
    else:
        return False

# Queue 데이터 삽입 함수
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() == True: # 큐가 꽉 차서 데이터를 넣을 수 없다면
        print('큐가 꽉찼습니다.')
        return # 함수탈출
    else:
        rear = (rear+1) % SIZE # 원형큐에서 데이터를 나눌 때 입력 공간확보
        queue[rear] = data

# Queue 테이터 추출 함수
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return None
    else:
        front = (front+1) % SIZE
        data = queue[front]
        queue[front] = None
        return data
    
# 추출 데이터 확인 함수
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty() == True:
        print('큐가 비었습니다')
        return None
    else:
        return queue[(front+1)%SIZE] # (front+1) % SIZE != front+1 % SIZE

# 전역변수
SIZE = int(input('큐 크기 입력(정수) > ')) # 대문자는 상수(constant)
queue = [None for _ in range(SIZE)]
front = rear = 0 # 원형 큐 에서는 초기값이 -1이 아닌 0이다.

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