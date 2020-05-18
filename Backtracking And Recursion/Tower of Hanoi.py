

def hanoi(n,from_rod, to_rod, aux_rod):
    if n==1:
        print ("move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    else:
        hanoi(n-1, from_rod, aux_rod, to_rod)
        print ("move disk ", n ,"from rod",from_rod,"to rod",to_rod)
        hanoi(n-1,aux_rod, to_rod,from_rod)
    

for i in range(int(input())):
    n=int(input())
    hanoi(n,1,3,2)
    print((2**n) -1)
