#basic uppercase password cracker for passwords of up to length 6

import itertools

userPassword = input("Enter uppercase password : ")

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

done = False
count = 0

for i in range(0,27):
	count = count + 1
	perm_tuples = list(itertools.permutations(upper,count))
	perm_list = [''.join(item) for item in perm_tuples]
	for password in perm_list:
		print(password)
		if userPassword == password:
			print("Your password has been cracked " + userPassword)
			done = True
			break


	if done:
		break
