# 자료구조와 알고리즘 2024
부경대학교 2024 IoT 개발자 과정 파이썬 자료구조와 알고리즘 학습 리포지토리

## 1일차
- 자료구조, 알고리즘 개요
- 파이썬 기초 복습, 함수까지

## 2일차
- 파이썬 기초 복습(완료)
- 파이썬 자료구조

    ![자료구조](https://t1.daumcdn.net/cfile/tistory/23202B4C53FDC5600C)

    - 선형리스트
    - 단순 연결 리스트 = 파이썬의 리스트와 동일

    ![연결리스트](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png)

## 3일차
- 파이썬 자료구조
    - 단순 연결 리스트 복습
    - 원형 연결 리스트(패스) : 마지막 노드가 제일 첫 노드와 연결
    - 스택(stack):Last In First Out(LIFO), First In Last Out(FILO)
        - pop : 데이터를 꺼내는 작업 - list.pop()
        - push : 데이터를 넣는 작업 - list.append()
        - top : 스택의 가장 윗부분

    ![stack](https://cs.lmu.edu/~ray/images/stack.gif)

    - 큐(queue) : First In First Out(FIFO)
        - enQueue : 큐에 데이터를 삽입
        - deQueue : 큐에 데이터를 추출
        - front(머리) : 데이터 중 첫 번째 데이터
        - rear(꼬리) : 데이터 중 마지막 데이터
        - front와 rear가 같이 있다면 데이터가 없는 것

    ![queue](https://raw.githubusercontent.com/YooWangGwon/ds-and-algorithm-2024/main/images/queue.png)


## 4일차
- 파이썬 자료구조
    - 큐 일반구현, 원형 큐
    - 트리(Tree) : 한 노드에서 시작해서 다른 정점들을 순회하여 자기 자신에게 돌아오는 순환이 없는 연결 그래프
        - 용어
            - Node : 트리를 구성하는 기본 원소
            - 뿌리 노드(Root Node) : 부모 노드가 없는 노드
            - 리프 노드 (leaf node) : 자식 노드가 없는 맨 마지막 끝의 노드
            - Edge : 노드를 연결하는 선
            - 차수(Degree) : 각 노드가 지닌 자식 노드의 수

    ![Tree](https://kahee.github.io//assets/post_img/tree3.png)

## 5일차
- 파이썬 자료구조/알고리즘
    - 그래프
        - 용어
            - 정점(Vertex) : 실세계에서의 어떤 대상을 표현하는 객체
            - 간선(Edge) : Vertex 간의 관계
        - 종료
            - 무방향 그래프 : 간선에 방향이 없는 그래프
            - 방향 그래프 : 화살표로 간선 방향을 표기하고, 그래프의 정점집합이 무방향 그래프와 같음
            - 가중치 그래프 : 무방향 그래프와 방향 그래프의 간선마다 가중치를 다르게 부여한 그래프
        - 그래프 순회(Graph Traversal) : 그래프의 모든 정점을 한 번씩 방문하는 것
            - 깊이 우선 탐색(DFS:Depth First Search) : Stack 활용
            - 너비 우선 탐색(BFS:Breadth First Search) : Queue 활용

    ![graph](https://raw.githubusercontent.com/YooWangGwon/ds-and-algorithm-2024/main/images/graph.png)

    - 재귀호출
    - 정렬
    - 검색

## 6일차


## 7일차