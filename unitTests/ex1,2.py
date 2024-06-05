import sys

# задание 2
def is_palindrome(data):
    return data == data[::-1]

input_string = sys.stdin.readline().strip()

if is_palindrome(input_string):
    print("YES")
else:
    print("NO")

# задание 1
def test_is_palindrome():
    test_cases = ["radar", "hello", "", "а роза упала на лапу Азора", "12321", "Python", " "]
    results = [True, False, True, False, True, False, True]
    
    for i, test_case in enumerate(test_cases):
        if is_palindrome(test_case) != results[i]:
            print("NO")
            return
    print("YES")

test_is_palindrome()