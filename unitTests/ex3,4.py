import re
import sys

# задание 4

def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(8|\+7)[\-\s]?(?:\(\d{3}\)|\d{3})[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}$'
    return re.match(pattern, number) is not None

input_string = sys.stdin.readline().strip()

if is_correct_mobile_phone_number_ru(input_string):
    print("YES")
else:
    print("NO")

# задание 3
def test_is_correct_mobile_phone_number_ru():
    test_numbers = [
        '8(999)123-45-67',
        '+7 999 123-45-67',
        '89991234567',
        '+7(999)1234567',
        '7(999)123-45-67',
        '+7 123 456-78-90'
    ]
    expected_results = [True, True, True, True, False, True]
    
    for number, expected in zip(test_numbers, expected_results):
        if is_correct_mobile_phone_number_ru(number) != expected:
            print("NO")
            return
    print("YES")

test_is_correct_mobile_phone_number_ru()