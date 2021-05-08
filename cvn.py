#!/bin/python3

import sys

def compare_length(s1, s2, l):
	for i in range(l):
		if s1[i] != s2[i]:
			return False
	return True

def string_is_bin(s):
	return compare_length(s, "0b", 2)
def string_is_oct(s):
	return compare_length(s, "0o", 2)
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

if __name__ == "__main__":
	argv = sys.argv
	inum = None
	otype = None

	if len(argv) == 1:
		exit(0)
	else: inum = argv[1]

	if len(argv) == 3:
		otype = argv[2]
	else: otype = "dec"

	if string_is_bin(inum):
		print_base(int(inum, 2), otype)
	elif string_is_oct(inum):
		print_base(int(inum, 8), otype)
	elif string_is_hex(inum):
		print_base(int(inum, 16), otype)
	else:
		print_base(int(inum, 10), otype)
