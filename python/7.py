"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    year = int(input())
    day = int(input())
    if day==4 or day==6 or day==9 or day==11:
        print('30')
    elif (year%4==0) and (day==2):
        print('29')
    elif (year%4!=0) and (day==2):
        print('28')
    else:
        print('31')

    return


if __name__ == '__main__':
    main()
