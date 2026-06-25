
def fibonachi(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)

        next_num = a + b
        a = b
        b = next_num

fibonachi(10)


def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    return sorted(word1) == sorted(word2)


print(is_anagram("race", "care"))




def factorial(n):
    result = 1

    for i in range(1, n + 1):
        # print(i)
        result = result * i
        # print(result)

    return result


print(factorial(5))


def finder(text, symbol):
    count = 0
    for i in text:
        if symbol == i:
            count += 1
    return count
print(finder("I## ## like# writin#g homeworks#", "#"))

