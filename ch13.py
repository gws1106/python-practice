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
##    cnt = lis.count(chr(ch))         #lis.count(x) - lis라는 리스트 안에 원소x의 수를 반환해준다
##
##    if cnt > 0:
##        print(f"{chr(ch)} : {cnt}")
##
    
##lis = input().split()
##
##for i in range(ord('A'), ord('Z') + 1):
##    if lis.count(chr(i)) > 0:
##        print(f"{chr(i)} : {lis.count(chr(i))}")


###자가진단3
##li = list(map(int, input().split()))
##cnt = [0 for _ in range(10)]
##
##for num in li:
##    cnt[num // 10] += 1
##
##for i in range(10):
##    if cnt[i] > 0:
##        print(f"{i} : {cnt[i]}")    


###자가진단4
##n = int(input())
##lis = [0 for _ in range(100)]
##
##lis[0] = 100
##lis[1] = n
##
##for i in range(2, 100):
##    lis[i] = lis[i - 2] - lis[i - 1]
##
##for i in range(100):
##    print(lis[i], end = ' ')
##    if lis[i] < 0:
##        break


###자가진단5
##arr = [[5, 8, 10, 6, 4], [11, 20, 1, 13, 2], [7, 9, 14, 22, 3]]
##
##for i in range(3):
##    for j in range(5):
##        print(f"   {arr[i][j]:2d}", end = ' ')
##    print()


###자가진단6
##arr1 = []
##arr2 = [0 for _ in range(2)]
##
##print("first array")
##for i in range(2):      #이중 리스트 입력받기
##    arr1.append(list(map(int, input().split())))
##
##print("second array")
##for i in range(2):      #또 다른 방법
##    arr2[i] = list(map(int, input().split()))
##
##for i in range(2):
##    for j in range(4):
##        print(arr1[i][j] * arr2[i][j], end = ' ')
##    print()


###자가진단7
##arr = []
##cnt_succ = 0
##
##for _ in range(5):   #이중 리스트 생성
##    arr.append(list(map(int, input().split())))
##
##for i in range(5):
##    sum_ = 0
##    for j in range(4):
##        sum_ += arr[i][j]
##    if sum_ / 4 >= 80:
##        print("pass")
##        cnt_succ += 1
##    else:
##        print("fail")
##
##print(f"Successful : {cnt_succ}")


###자가진단8
##arr = [[0 for _ in range(6)] for _ in range(6)]
##arr[0][1] = 1
##
##for i in range(1, 6):
##    for j in range(1, 6):
##        arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
##        print(arr[i][j], end = ' ')
##    print()


###형성평가
###1.
##lis = [f"No.{i}" for i in range(1, 6)]
##print(lis)


###2.
##size, n = map(int, input().split())
##lis = [0 for i in range(size)]
##
##for i in range(size):
##    if i % n == 0:
##        lis[i] = True
##    else:
##        lis[i] = False
##        
##print(lis)


###3.
##lis = list(map(int, input().split()))
##cnt = [0 for _ in range(6)]
##
##for i in range(6):
##    cnt[i] = lis.count(i + 1)
##    print(f"{i + 1} : {cnt[i]}")

###3. 다른답안
##lst = list(map(int, input().split()))
##
##for i in range(1, 7):
##    print(f"{i} : {lst.count(i)}")


###4.
##scores = list(map(int, input().split()))
##
##for i in range(len(scores)):
##    scores[i] = scores[i] // 10
##
##for i in range(10, -1, -1):
##    if scores.count(i) > 0:
##        print(f"{i * 10} : {scores.count(i)} person")

##scores = list(map(int, input().split()))
##lis = [0 for _ in range(11)]
##
##for score in scores:
##    lis[score // 10] += 1
##
##for i in range(len(lis) - 1, -1, -1):
##    if lis[i] > 0:
##        print(f"{i * 10} : {lis[i]} person")


#5.
