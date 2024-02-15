# file : ds20_binarySearchTree.py
# date : 20240215
# desc : 이진검색트리 구현

# 트리노드 클래스 선언
class Treenode():
    left = right = data = None

    def __init__(self) -> None:
        self.left = self.right = self.data = None

# 중위 순회

def inorder(node):
    if node == None: return

    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)

# 전역변수
root = None
groupList = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

# 메인 코드
node = Treenode()
node.data = groupList[0] # 블랙핑크
root = node


for name in groupList[1:]: # 레드 벨벳부터 끝까지
    node = Treenode()
    node.data = name

    curr = root # 블랙핑크부터 시작
    while True:
        if name < curr.data: # 왼쪽트리로 이동
            if curr.left == None: # 왼쪽에 트리가 구성되어있지않으면
                curr.left = node
                break # while문 탈출
            else:
                curr = curr.left
        else: # 오른쪽 트리로
            if curr.right == None:
                curr.right = node
                break
            else:
                curr = curr.right

print('이진 탐색트리 구성 완료!')

print('탐색 시작!')
findName = '마마무'
level = 0
curr = root
while True: 
    if findName == curr.data: # 찾으면
        print(f'{curr.data}를 Level {level}에서 찾음')
        break
    elif findName < curr.data: # 찾는 이름이 현재의 이름보다 작을 경우 왼쪽 트리로
        if curr.left == None:
            print(f'{findName}이 트리에 없음')
        else:
            curr = curr.left
            level += 1
    else: # 찾는 이름이 현재의 이름보다 클 경우 오른쪽 트리로
        if curr.right == None:
            print(f'{findName}이 트리에 없음')
            break
        else:
            curr = curr.right
            level += 1

curr = root
print(' 중위 순회 : ', end='')
inorder(curr)
print('끝')

deleteName = '마마무'
curr = root
parent = None

while True:
    if deleteName == curr.data: # 삭제할 데이터를 찾은 경우
        if curr.left == None and curr.right == None: # 리프 노드(맨 끝단에 있는 노드)라 삭제가 용이함
            if parent.left == curr: # 내가 부모의 왼쪽에 붙어있으면
                parent.left = None
            else: # 내가 부모의 오른쪽에 붙어있으면
                parent.right = None
            
            del(curr) # 연결이 끊어진 자신의 노드를 완전히 삭제

        elif curr.left != None and curr.right == None: # 내 노드 왼쪽에 자식 노드가 있을 경우
            if parent.left == curr: # 부모 노드의 왼쪽에 내가 있으면 
                parent.left = curr.left # 부모노드의 왼쪽에 내 왼쪽에 있는 자식 노드를 연결
            else: # 부모노드의 오른쪽에 내가 있으면
                parent.right = curr.left # 부모노드의 오른쪽에 내 왼쪽에 있는 자식 노드를 연결

            del(curr) # 자신의 노드를 완전히 삭제

        elif curr.left == None and curr.right != None: # 내 노드 오른쪽에 자식 노드가 있을 경우
            if parent.left == curr: # 부모 노드의 왼쪽에 내가 있으면
                parent.left = curr.right # 부모노드의 왼쪽에 내 오른쪽에 있는 자식 노드를 연결
            else: # 부모노드의 오른쪽에 내가 있으면
                parent.right == curr.right # 부모노드의 오른쪽에 내 오른쪽에 있는 자식 노드를 연결

            del(curr) # 자신의 노드를 완전히 삭제

        print(f'{deleteName}이 삭제됨')
        break

    elif deleteName < curr.data: # 삭제할 이름이 현재 이름보다 작으면 왼쪽으로
        if curr.left == None: # 좌측에 값이 없을 경우
            print(f'{deleteName}이 현재 트리에 없음')
        else:
            parent = curr
            curr = curr.left
    else: # 삭제할 이름이 현재 이름보다 작으면 오른쪽으로
        if curr.right == None: # 우측에 값이 없을 경우
            print(f'{deleteName}이 현재 트리에 없음')
        else:
            parent = curr
            curr = curr.right
            
curr = root
print(' 중위 순회 : ', end='')
inorder(curr)
print('끝')