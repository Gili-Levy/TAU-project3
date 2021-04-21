# Skeleton file for HW3 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
import math
SUBMISSION_IDS = ["316296771"]

# Q2 - A

def hex_to_float(s):
	if s == "0"*16:  # zero
		return 0

	sgn = (-1)**int(s[0])
	print (sgn)

	exp = int(s[1:4], 16)
	print (exp)

	fraction = int(s[4:17], 16)
	print (fraction)
	
	return (-1)**(sgn) * 16**(exp-2047) * fraction * 16**(-11)



"""
def left_fill_zeros(bin_str, output_len): # Pad with zeros on the left side
	return '0' * (output_len - len(bin_str)) + bin_str


# Q2 - B
def float_to_hex(num):
	print ("num: ", num)
	if num == 0: # zero
		return "0"*16
	#num= num/(16**-11)
	sgn = "0"
	if num < 0: # negative
		sgn = "1"
		num = abs(num)
	print (sgn)
	
	# Compute shift
	shift = math.floor(math.log(num,16.0))
	bexp = hex(shift + 2047)[2:]
	bexp = left_fill_zeros(bexp, 3)

	num = num * (16**-shift)  # Shift the number
	print (num)
	num -= 1  # num has form 1.xxx, we want the xxx part ???????? not bin

	# Compute mantissa
	num = int(num * (16**12))
	bfraction = hex(num)[2:]
	bfraction = left_fill_zeros(bfraction, 12)

	return sgn + bexp + bfraction


print(float_to_hex(10 * 16**2 + 7 * 16 + 11/16 + 3/16**2))

"""


# Q3 - A
def search_combined(lst, key):
	res_even = modified_binary_search(lst, key, True)
	if res_even is not None:
		return res_even
	res_odd = modified_binary_search(lst, key, False)
	return res_odd


def modified_binary_search(lst, key, search_even):
	n = len(lst)

	odd = 0
	if search_even == False:
		odd = 1
	left = 0 + odd
	right = n-2 + odd
	
	while left <= right: # binary search
		
		if ((left+right)//2 % 2 == 0) == search_even:  # middle rounded down
			mid = (left+right)//2
		else:
			mid = (left+right)//2 + 1
			
		if key == lst[mid]:	  # item found
			return mid
		elif key < lst[mid]:	 # item cannot be in top half
			right = mid-2
		else:					# item cannot be in bottom half
			left = mid+2
		
	return None



# Q3 - B
def sort_combined(lst):
	ev_lst = []
	od_lst= []
	for i in range (len(lst)): # complexity = O(n)
		if i%2 == 0:
			ev_lst.append(lst[i])
		else:
			od_lst.append(lst[i])
	od_lst.reverse() # complexity O(n/2) -> O(n)
	
	n = len(ev_lst)
	m = len(od_lst)
	res = [0 for i in range(n+m)]  # complexity = O(n)

	a=0 ; b=0 ; c=0
	while  a < n  and  b < m: # A & B have elements
		if ev_lst[a] < od_lst[b]:
			res[c] = ev_lst[a]
			a += 1
		else:
			res[c] = od_lst[b]
			b += 1
		c += 1

	if a == n: #A was completed
		while b < m:
			res[c] = od_lst[b]
			b += 1
			c += 1
	else: #B was completed
		while a < n:
			res[c] = ev_lst[a]
			a += 1
			c += 1
		
	return res


# Q3 - C
def find_duplicate(lst):
	pass  # replace this with your code


# Q4 - A, a
def find(lst, s):
	pass  # replace this with your code


# Q4 - A, b
def sort_from_almost(lst):
	pass  # replace this with your code


# Q4 - B
def find_local_min(lst):
	pass  # replace this with your code


# Q5 - a
def string_to_int(s):
	pass  # replace this with your code


# Q5 - b
def int_to_string(k, n):
	pass  # replace this with your code


# Q5 - c
def sort_strings1(lst, k):
	pass  # replace this with your code


# Q5 - e
def sort_strings2(lst, k):
	pass  # replace this with your code


# Q6 - A
def code(string):
	pass  # replace this with your code


# Q6 - B
def decode(bin_str):
	pass  # replace this with your code


########
# Tester
########
def test():
	import random

	# Q2 - A
	if hex_to_float('17ff200000000000') != -2.0 or \
			hex_to_float('07ff610000000000') != 6.0625:
		print("error in hex_to_float")

	# Q2 - B
	if float_to_hex(10 * 16 ** 2 + 7 * 16 + 11 / 16 + 3 / 16 ** 2) != '0801a70b30000000' or \
			float_to_hex(- (11 / 16 ** 2 + 3 / 16 ** 3 + 12 / 16 ** 5)) != '17fdb30c00000000':
		print("error in float_to_hex")

	# Q3 - A
	combined_lst1 = [1, 30, 10, 4, 15, 0, 100, -1]
	if search_combined(combined_lst1, 10) != 2 or \
			search_combined(combined_lst1, 0) != 5 or \
			search_combined(combined_lst1, 200) is not None:
		print("error in search_combined")

	# Q3 - B
	if sort_combined([1, 30, 10, 4, 15, 0, 100, -1]) != [-1, 0, 1, 4, 10, 15, 30, 100] or \
			sort_combined([-100, 100, -80, 80]) != [-100, -80, 80, 100]:
		print("error in sort_combined")

	# Q3 - C
	if find_duplicate([100, 100]) != 0 or \
			find_duplicate([80, 120, 100, 100]) != 2 or \
			find_duplicate([100, 250, 200, 210, 210, -300, 400, -400, 500, -500]) is not None:
		print("error in find_duplicate")

	# Q4 - A
	almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]

	if find(almost_sorted_lst, 5) != 3:
		print("error in find")

	if find(almost_sorted_lst, 50) != None:
		print("error in find")

	# Q4 - B
	if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
		print("error in sort_from_almost")

	# Q4 - C
	lst = [5, 6, 7, 5, 1, 1, 99, 100]
	pos = find_local_min(lst)
	if pos not in (0, 4, 5):
		print("error in find_local_min")

	# Q5
	lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
	for i in lst_num:
		s = int_to_string(4, i)
		if s is None or len(s) != 4:
			print("error in int_to_string")
		if string_to_int(s) != i:
			print("error in int_to_string and/or in string_to_int")

	lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc',
			'aacc', 'edea', 'becb', 'daea', 'ccea']
	if sort_strings1(lst1, 4) \
			!= ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
		print("error in sort_strings1")

	if sort_strings2(lst1, 4) \
			!= ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
		print("error in sort_strings2")

	# Q6 - A
	if code('7b') != '00111100001' or \
			code('cs1001') != '10001011001000001000000000000001':
		print("error in code")

	# Q6 - B
	if decode('00111100001') != '7b' or \
			decode('100000100010100000100001') != 'acab':
		print("error in code")

	# Creates a string of 50 random chars from our alphabet of digits and letters.
	s = ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=50))
	if decode(code(s)) != s:
		print("error in code and/or decode")
