"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    number1 = int(input())
    print('{}'.format(number1%10), end ='')
    number2 = number1 // 10
    print('{}'.format(number2%10), end ='')
    number3 = number2 // 10
    print('{}'.format(number3%10), end ='')
    return
   


if __name__ == '__main__':
    main()
