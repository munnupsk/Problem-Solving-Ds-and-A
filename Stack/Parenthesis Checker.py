
#https://practice.geeksforgeeks.org/problems/parenthesis-checker/0


def check(s):
    st=[]
    for i in s:
        if i=='(' or i=='[' or i=='{':
            st.append(i)
        if len(st)==0:
            return False
        if i==')':
            x=st.pop()
            if x=='[' or x=='{':
                return False
        if i==']':
            x=st.pop()
            if x=='(' or x=='{':
                return False
        if i=='}':
            x=st.pop()
            if x=='(' or x=='[':
                return False
    if len(st)==0:
        return True
    return False
            

for _ in range(int(input())):
    s=input()
    res=check(s)
    if res:
        print("balanced")
    else:
        print("not balanced")
