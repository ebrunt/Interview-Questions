#returns true if all chars in string are unique, false otherwise
def unique_string(string):
	chars = sorted(string)
	for i in range(len(chars) - 1):
		if chars[i] == chars[i+1]:
			return "False"
	return "True"


def main():
	test_string = ""
	print(test_string + " Result: " + unique_string(test_string))
	test_string = "a"
	print(test_string + " Result: " + unique_string(test_string))
	test_string = "abcdef"
	print(test_string + " Result: " + unique_string(test_string))
	test_string = "aa"
	print(test_string + " Result: " + unique_string(test_string))
	test_string = "aba"
	print(test_string + " Result: " + unique_string(test_string))
	
if __name__ == '__main__':
	main()