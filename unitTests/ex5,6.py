import re
import sys

def strip_punctuation_ru(data):
    punctuation_pattern = r"[!\"#$%&'()*+,-./:;<=>?@\[\\\]^_`{|}~«»]"
    
    stripped_text = re.sub(punctuation_pattern, lambda match: " " if match.group() != "." else "", data)
    
    return " ".join(stripped_text.split())

input_string = sys.stdin.readline().strip()

print(strip_punctuation_ru(input_string))

def test_strip_punctuation_ru():
    test_data = [
        'Привет, как дела?',
        'Сегодня - отличная погода!',
        'Тест: 1, 2, 3... Проверка.',
        'Это предложение без знаков препинания'
    ]
    expected_results = [
        'Привет как дела',
        'Сегодня отличная погода',
        'Тест 1 2 3 Проверка',
        'Это предложение без знаков препинания'
    ]
    
    for data, expected in zip(test_data, expected_results):
        if strip_punctuation_ru(data) != expected:
            print("NO")
            return
    print("YES")

test_strip_punctuation_ru()