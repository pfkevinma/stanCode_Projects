"""
File: largest_digit.py
Name: Pei-Feng (Kevin) Ma
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	print the largest digit in the input integer.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, a number that we want to get the largest digit of.
	:return: int, the largest digit in n.
	"""
	# convert negative integer to positive.
	if n < 0:
		n = n*-1

	# base case
	# return will n is a single digit number.
	if n < 10:
		return n

	# recursive case
	else:
		k = n % 10  # k mod 10 can get the last digit.
		n = (n-k)//10  # n minus last digit and floor divided by 10 will get rid of the last digit.
		if k > find_largest_digit(n):  # send new n to next layer. Comparing each layers k and return the bigger one.
			return k
		else:
			return find_largest_digit(n)


if __name__ == '__main__':
	main()
