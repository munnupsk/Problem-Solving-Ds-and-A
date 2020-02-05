#https://practice.geeksforgeeks.org/problems/sort-the-string-in-descending-order/0

for _ in range(int(input())):
    s=input()
    c=[0]*26
    for i in s:
        c[ord(i)-ord('a')]+=1
    for i in range(25,-1,-1):
        while c[i]!=0:
            print(chr(i+ord('a')),end='')
            c[i]-=1
    print()
