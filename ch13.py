### 리스트3


###연습문제1
##print("원소가 모두 0:", [0 for _ in range(10)])
##print("또 다른 방법:", [0]*10)
##print("원소가 모두 'Hi':", ['Hi' for _ in range(10)])
##print("1부터 10까지:", [i for i in range(1, 11)])
##print("또 다른 방법:", list(range(1, 11)))
##print("5부터 15까지의 홀수:", [i for i in range(5, 16, 2)])
##print("60부터 40까지의 3의 배수:", [i for i in range(60, 39, -3)])
##print("A부터 F까지의 알파벳:", [chr(i) for i in range(ord('A'), ord('F')+1)])
##
                        
### 자가진단1
##n = int(input())
##lis = []
##
##for i in range(1, n + 1):
##    lis.append(i * i)
##
##print(lis)

###자가진단2
##lis = input().split()
##cnt = 0
##
##for ch in range(ord('A'), ord('Z') + 1):
##    cnt = lis.count(chr(ch))
##
##    if cnt > 0:
##        print(f"{chr(ch)} : {cnt}")
##
    
##lis = input().split()
##
##for i in range(ord('A'), ord('Z') + 1):
##    if lis.count(chr(i)) > 0:
##        print(f"{chr(i)} : {lis.count(chr(i))}")
