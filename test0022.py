#제어문 Control Statement

# ◈ 제어문
# - 프로그램의 순차적인 흐름을 바꾸어주는 문장
#  ⊙ 조건문 : 조건에 따라 다른 문장(각각의 조건에 해당되는)을 실행하는 문장
#     if / else
#
# ⊙ 반복문 : 동일한 코드를 여러번 실행시키는 문장
#     for / while
#
# ⊙ 분기문 : 멈추거나 빠져나가거나 계속 진행하거나 되돌아가거나
#     break / continue / return
# n=0
#
# if n!=1:
#     print('A')
# print('B')

# [문제]
#
# 점수를 입력받아 합격 여부를 출력한다.
# 점수가 60점 이상이면 “합격”,
# 그렇지 않으면 “불합격”인 프로그램을 만드시오.
#
# 점수 입력 : 78
#
# score=int(input('점수 입력:'))
# if score>=60:
#     print('합격')
# else:
#     print('불합격')
# [문제]
# 정수 n을 입력받아 짝수인지 홀수인지를 검사하여 출력하는 프로그램을 만드시오.
#
# 정수 입력 : 4
# 짝수
#2로 나누었을 때 나머지가 0이면 짝수, 그렇지 않으면 홀수
# n=int(input('정수 입력:'))
# if n%2==0:
#     print('짝수')
# else:
#     print('홀수')

# [문제]
# 수학점수가 70점 이상이고
# 코딩테스트를 응시했으면 ‘합격’,
# 아니면 ‘불합격’인 프로그램을 만드시오.
# (단, 코딩테스트 응시했을 때는 1, 아니면 0을 입력한다.)
# [입력]
# 수학 점수 : 77
# 코딩 테스트 응시 : 1
# [출력]
# 합격

math_test=int(input('수학 점수 : '))
coding_test=int(input('코딩 테스트 응시 : '))
if math_test>=70 and coding_test==1:
    print('합격')
else:
    print('불합격')
