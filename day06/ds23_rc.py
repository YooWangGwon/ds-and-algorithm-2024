# file : ds23_rc.py
# date : 20240219
# desc : 재귀 호출(recursive call)

# 재귀호출 : 두번째 호출이 첫번째 호출이 불렀다는 정보를 지속해서 보유하고 있다. 
# 이후에도 이전에 호출한 모든 정보들을 계속 보유하기 때문에 호출 속도가 점점 느려지고 while문 처럼 무한루프 할 수 없다.

import time

def open_box():
    global count
    print(f'{count} 번째 상자를 엽니다')
    count -= 1
    if count == 0:
        print('반지를 넣고 반환합니다.')
        return # 이걸 빼면 또 무한반복 됨

    time.sleep(0.1) # 0.5초동안 딜레이
    open_box()
    print('상자를 닫습니다.')

# 전역변수
count = 10
if __name__  == '__main__':
    open_box()