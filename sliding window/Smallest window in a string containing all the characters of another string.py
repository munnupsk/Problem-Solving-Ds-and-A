
#https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string/0

no_of_chars = 256
def findSubString(string, pat): 

	len1 = len(string) 
	len2 = len(pat) 

	# check if string's length is less than pattern's 
	# length. If yes then no such window can exist 
	if len1 < len2: 
	
		return -1 

	hash_pat = [0] * no_of_chars 
	hash_str = [0] * no_of_chars 

	# store occurrence ofs characters of pattern 
	for i in range(0, len2): 
		hash_pat[ord(pat[i])] += 1

	start, start_index, min_len = 0, -1, float('inf') 

	# start traversing the string 
	count = 0 # count of characters 
	for j in range(0, len1): 
	
		# count occurrence of characters of string 
		hash_str[ord(string[j])] += 1

		# If string's char matches with 
		# pattern's char then increment count 
		if (hash_pat[ord(string[j])] != 0 and hash_str[ord(string[j])] <=hash_pat[ord(string[j])]): 
			count += 1

		# if all the characters are matched 
		if count == len2: 
		
			
			while (hash_str[ord(string[start])] > hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0): 
			
				if (hash_str[ord(string[start])] > hash_pat[ord(string[start])]): 
        
			    hash_str[ord(string[start])] -= 1
				  start += 1
			
			
			len_window = j - start + 1
			if min_len > len_window: 
			
				min_len = len_window 
				start_index = start 

	# If no window found 
	if start_index == -1: 
		return -1
	
	
	return string[start_index : start_index + min_len] 

for _ in range(int(input())):
    string=input()
    pattern=input()
    print(findSubString(string, pattern))
    
