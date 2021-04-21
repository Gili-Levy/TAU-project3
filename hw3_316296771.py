# Skeleton file for HW3 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = ["316296771"]

# Q2 - A


def hex_to_float(s):
	if s == "0"*16:  # zero
		return 0
	
	trans = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
			 "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
	s1 = s[1:4]  # exp
	s2 = s[4:]  # freq

	#sign
	num = (-1)**int(s[0])

	#exp
	exp = 0
	for i in range (3):
		exp += trans[s1[i]]*(16**(2-i))
	
	num *= 16**(exp-2047)

	#freg
	fraction = 0
	for i in range (12):
		fraction += trans[s2[i]]*(16**(11-i))

	num *= fraction * (16**(-11))
	
	return num



# Q2 - B
def float_to_hex(num):
	pass  # replace this with your code


# Q3 - A
def search_combined(lst, key):
	res_even = modified_binary_search(lst, key, True)
	if res_even is not None:
		return res_even
	res_odd = modified_binary_search(lst, key, False)
	return res_odd


def modified_binary_search(lst, key, search_even):
	pass  # replace this with your code


# Q3 - B
def sort_combined(lst):
	pass  # replace this with your code


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
