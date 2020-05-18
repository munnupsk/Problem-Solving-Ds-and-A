


from itertools import combinations
 
for _ in range(int(input())):
    n = int(input())
    arr = sorted(input().split())
 
    comb = set()
 
    arr_set = list()
 
    for i in range(n+1):
        comb.add(combinations(arr, i))
 
    for c in comb:
        set_c = set(c)
        for item in set_c:
            arr_set.append(' '.join(item))
    print("(", ')('.join(sorted(arr_set)), ")", sep="")
