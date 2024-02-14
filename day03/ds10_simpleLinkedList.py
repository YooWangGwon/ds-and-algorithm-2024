# file : ds10_simpleLinkedList.py
# date : 20240214
# desc : 단순 연결리스트 전체 구현

# 노드 클래스 선언
class Node():
    data = None # 실제 데이터 변수
    link = None # 다음 노드를 지정하는 변수

    def __init__(self) -> None:
        self.data = None # 클래스 자신이 self이므로 클래스의 변수에 접근하려면 반드시 self를 사용해야함
        self.link = None 

# start부터 시작해서 끝까지 node.data 출력하는 함수
def printNode(start): 
    curr = start # start == head
    if curr == None: return # 더이상 데이터가 없을 경우 종료, break와 continue는 반복문이 있어야함
    while True: # 무한 루프
        if curr.link == None: # 더이상 연결할 Node가 없을 경우
            print(curr.data) # 자기 데이터만 출력
            break # 반목문 탈출
        else: # 연결할 노드가 있을 경우
            print(curr.data, end = ' -> ') # 연결표기( -> )를 함
            curr = curr.link # 자기 뒤의 데이터를 curr로 바꿔줌

# 노드 삽입 함수
def insertNode(find, data):
    global head, prev, curr # 전역변수를 insertNode()에서 사용하겠다고 선언

    if head.data == find: # 맨 첫번째 노드
        node = Node()
        node.data = data
        node.link = head 
        head = node 
        return # 함수 탈출
    
    curr = head
    while curr.link != None: # 중간에 노드 삽입
        prev = curr
        curr = curr.link
        if curr.data == find: # 데이터를 찾았으면
            node = Node()
            node.data = data
            node.link = curr # 찾은 node 앞에 새로운 node를 연결
            prev.link = node # 이전 node 뒤에 새로운 node 연결
            return # 함수탈출
        
    node = Node() # 맨 마지막에 노드 삽입
    node.data = data
    curr.link = node
    return

# 노드 삭제 함수
def deleteNode(data):
    global head, prev, curr

    if head.data == data: # 첫번째 노드 삭제면
        curr = head
        head = head.link
        del(curr)
        return

    curr = head
    while curr.link != None: # 첫번째 외 노드 삭제
        prev = curr
        curr = curr.link

        if curr.data == data:
            prev.link = curr.link
            del(curr)
            return # 함수 탈출
        
# 노드 검색 함수
def findNode(find):
    global head, curr

    curr = head
    if curr.data == find: # curr의 데이터가 find값이라면
        return curr # 현재 노드를 리턴해주고 함수 탈출
    while curr.link != None:
        curr = curr.link # 다음 노드로 넘어감
        if curr.data == find: 
            return curr
    return Node() # 위에서 만족하는 것이 없으면 빈 노드 리턴 후 함수 탈출

# 전역변수
head, prev, curr = None, None, None 
originData = ['다현','정연','쯔위','사나','지효']

# 메인코드 영역
if __name__ == '__main__':
    
    node = Node() # 클래스 노드 생성
    node.data = originData[0] # '다현'이라는 데이터를 할당
    head = node # head는 node를 가리킴

    for data in originData[1:]: # 1번 인덱스부터 리스트의 끝까지 반복
        prev = node
        node = Node()
        node.data = data
        prev.link = node

    
    # 연결리스트 구성 완료
    print('최초 구성된 연결리스트')
    printNode(head) # 구성된 연결리스트가 맞는지 출력해서 확인
    # 다현 -> 정연 -> 쯔위 -> 사나 -> 지효

    # 노드 삽입
    print('맨앞에 노드 삽입')
    insertNode('다현','정국')
    printNode(head)
    # 정국 -> 다현 -> 정연 -> 쯔위 -> 사나 -> 지효

    print('중간에 노드 삽입')
    insertNode('사나','미미')
    printNode(head)
    # 정국 -> 다현 -> 정연 -> 쯔위 -> 미미 -> 사나 -> 지효

    print('마지막 노드 삽입')
    insertNode('재남','알엠') # 재남이라는 노드가 없어 마지막에 삽입
    printNode(head)
    # 정국 -> 다현 -> 정연 -> 쯔위 -> 미미 -> 사나 -> 지효 -> 알엠

    # 노드 삭제
    print('맨앞 노드 삭제')
    deleteNode('정국')
    printNode(head)

    print('중간 노드 삭제')
    deleteNode('쯔위')
    printNode(head)
    # 다현 -> 정연 -> 미미 -> 사나 -> 지효 -> 알엠

    # 노드 검색
    print('노드 검색')
    printNode(head)
    fNode = findNode('다현')
    print(f'찾는 노드 : {fNode.data}')

    fNode = findNode('재남')
    print(f'찾는 노드 : {fNode.data}')

