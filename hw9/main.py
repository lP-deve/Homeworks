# 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც  მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

int_list = [10,20,30,40]
def my_function(num):
    int_list.append(num)
    return int_list

print(my_function(50))


# 2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

my_list =[100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def list_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
print(list_sum(my_list))


# 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს  (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას.

gl_str = "Global"

def fun1():
    gl_str = "local"
    return gl_str

print(fun1())


# 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს  ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).
def sum_digits(number):
    if number == 0:
        return 0

    return number % 10 + sum_digits(number // 10)

print(sum_digits(12345))  


# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH)

    
def reverse_string(text):
    if text == "":
        return ""

    return text[-1] + reverse_string(text[:-1])

print(reverse_string("Hello"))  