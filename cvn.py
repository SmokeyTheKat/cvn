#!/bin/python3

import sys

def compare_length(s1, s2, l):
	if len(s1) < l or len(s2) < l: return False
	for i in range(l):
		if s1[i] != s2[i]:
			return False
	return True

def string_is_bin(s):
	return compare_length(s, "0b", 2)
def string_is_oct(s):
	return compare_length(s, "0o", 2)
def string_is_dec(s):
	return (len(s) <= 2 or s[1].isnumeric())
def string_is_hex(s):
	return compare_length(s, "0x", 2)

def print_base(n, b):
	if b == "bin":
		print(bin(n))
	if b == "oct":
		print(oct(n))
	if b == "dec":
		print(n)
	if b == "hex":
		print(hex(n))

def is_type(n):
	if n == "bin":
		return True
	if n == "oct":
		return True
	if n == "dec":
		return True
	if n == "hex":
		return True
	return False
	

if __name__ == "__main__":
	argv = sys.argv
	inum = None
	otype = None
	findtype = False

	if len(argv) == 1:
		exit(0)

	if len(argv) > 2 and is_type(argv[1]):
		otype = argv[1]
		argv = argv[2:]
	else:
		argv = argv[1:]
		findtype = True


	for inum in argv:
		if findtype:
			if string_is_dec(inum):
				otype = "hex"
			else: otype = "dec"

		if string_is_bin(inum):
			print_base(int(inum, 2), otype)
		elif string_is_oct(inum):
			print_base(int(inum, 8), otype)
		elif string_is_hex(inum):
			print_base(int(inum, 16), otype)
		else:
			print_base(int(inum, 10), otype)
