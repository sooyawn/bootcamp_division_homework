"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    a=int(input())
    s = 0
    while(a<=0):
        print('X')
        a=int(input())
    for i in range(1,a+1):
        s = s + i
    print(s)


    return


if __name__ == '__main__':
    main()
