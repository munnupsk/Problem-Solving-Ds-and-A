
#https://practice.geeksforgeeks.org/problems/remove-duplicates/0

def ls(s):
    li=[]
    for i in s:
        li.append(i)
    return li        
for _ in range(int(input())):
    s=input()
    mutable_string=ls(s)#since the string is immutable
    
    bin_hash=[0]*256
    temp=''
    i_ind=0
    j_ind=0
    while i_ind!=len(mutable_string):
        temp=mutable_string[i_ind]
        if bin_hash[ord(temp)]==0:
            bin_hash[ord(temp)]=1
            mutable_string[j_ind]=temp
            j_ind+=1
        i_ind+=1
    
    print(''.join(mutable_string[0:j_ind]))
   
