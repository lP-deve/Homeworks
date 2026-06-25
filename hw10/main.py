list1 = [1, 2, 3]
list2 = [ "a", "b", "c"]

list3 = list(zip(list1, list2))
print(list3)





from functools import reduce

def multiply(num):
    try:
        if not isinstance(num, list):
            raise TypeError("not a list")
        if not all(isinstance(x, (int, float)) for x in num):
            raise TypeError("you can type only numbers")
         
        return reduce(lambda x, y: x* y, num)
    except TypeError as e:
        return {e}
    
params = [1, 2, 3, 4, 5]
print(multiply(params))






list1 = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = (lambda x: [i for i in x if i % 2 != 0])(list1)
print(odd_numbers)



def filter_words(words,ending):
    try: 
        if not isinstance(words, list):
            raise TypeError("parametre must be list")
        if not isinstance(ending, str):
            raise TypeError("second paraametr must be string")
        if not all(isinstance(word, str) for word  in words):
            raise TypeError("All list elements must be strings")
        
        return list(filter(lambda word : word.endswith(ending), words))
    except TypeError as e:
        return  {e}
    
params = ['hello', 'world', 'coding', 'nod', "singing"]
print(filter_words(params, 'ing'))