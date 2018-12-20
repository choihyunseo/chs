#한양대학교
#산업융합학부
#2017053418
#최현서

from bisect import insort

def chs(n, a, b):
    ret = 1983      #문제에 나와있 듯이 처리
    while n:
        yield ret
        n -= 1
        ret = (ret * a + b) % 20090711      #문제에 나와있 듯이 처리


for case in range(int(input())):
    n, a, b = map(int, input().split())
    ans = 0
    seq = []
    for i in chs(n, a, b):
        insort(seq, i)      #시퀀스 번호에 i를 삽입      ※ 정렬하는 과정
        ans += seq[(len(seq)-1)//2]     #중앙에 있는 값 찾기
    print(ans % 20090711)       #문제에 나와있 듯이 찾은 중앙값을 20090711을 나눈 나머지 값 출력