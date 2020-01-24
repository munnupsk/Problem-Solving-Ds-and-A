
#https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0/?track=md-string&batchId=144

for _ in range(int(input())):
    s=input()
    a_pointer=0
    b_pointer=0
    l=[]
    maxi=0
    while b_pointer<len(s):
        if s[b_pointer] not in l:
            l.append(s[b_pointer])
            b_pointer+=1
            maxi=max(len(l),maxi)
        else:
            if len(l)>0:
                l.pop(0)
            a_pointer+=1
    print(maxi)
    
            
    
