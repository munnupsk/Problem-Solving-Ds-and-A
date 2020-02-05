#https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not/0


def kmp(s1,s2):
    if len(s1)!=len(s2):
        return 0
    temp=s1+s1
    if s2 in temp:
        return 1
    return 0
for _ in range(int(input())):
    s1=input()
    s2=input()
    res=kmp(s1,s2)
    print(res)
