# file : ds04_orderedList.py
# date : 20240213
# desc : 선형리스트 프로그램

# 데이터 추가 함수
def add_data(friend):
    kakaotalk.append(None)
    size = len(kakaotalk)
    kakaotalk[size-1] = friend 

# 데이터 삽입 함수
def insert_data(pos, friend):
    if pos < 0 or pos >= len(kakaotalk):
        print('데이터 삽입범위 초과')
        return 
    
    kakaotalk.append(None) 
    size = len(kakaotalk) 

    for i in range(size-1, pos, -1): 
        kakaotalk[i] = kakaotalk[i-1]
        kakaotalk[i-1] = None

    kakaotalk[pos] = friend

# 데이터 삭제함수
def delete_data(pos):
    if pos < 0 or pos >= len(kakaotalk): 
        print('데이터 삭제 범위 초과')
        return
    
    size = len(kakaotalk)
    kakaotalk[pos] = None
    
    for i in range(pos + 1, size):
        kakaotalk[i-1] = kakaotalk[i]
        kakaotalk[i] = None

    del(kakaotalk[size - 1])


# 전역변수 선언
kakaotalk = [] # 빈 배열 생성
select = -1 # 1/추가 2/삽입 3/삭제 4/종료

if __name__ == '__main__':
    while (select != 4):
        select = int(input('선택(1:추가, 2:삽입, 3:삭제, 4:종료)'))

        if select == 1:
            data = input('추가 데이터 -->')
            add_data(data)
            print(kakaotalk)

        elif select == 2:
            pos = int(input('삽입 위치 --> '))
            data = input('삽입 데이터 --> ')
            insert_data(pos, data)
            print(kakaotalk)
        
        elif select == 3:
            pos = int(input('삭제 위치 --> '))
            delete_data(pos)
            print(kakaotalk)
        elif select == 4:
            exit(0) # 프로그램 자체를 종료 함수
        else:
            print('1 ~ 4 중 하나를 입력하세요.')
            continue