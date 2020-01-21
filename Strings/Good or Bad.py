
#https://practice.geeksforgeeks.org/problems/good-or-bad-string/0



def isVowel(c):
    if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        return True
    return False
    
for _ in range(int(input())):
    s=input()
    bad=False
    maxvowel=0
    maxcon=0
    for i in s:
        if isVowel(i):
            maxvowel+=1
            maxcon=0
            if maxvowel>5:
                bad=True
                break
        elif i=='?':
            maxvowel+=1
            maxcon+=1
            if maxvowel>5 or maxcon>3:
                bad=True
                break
        else:
            #works for consonents
            maxvowel=0
            maxcon+=1
            if maxcon>3:
                bad=True
                break
    if bad:
        print("0")
    else:
        print("1")
            
        
