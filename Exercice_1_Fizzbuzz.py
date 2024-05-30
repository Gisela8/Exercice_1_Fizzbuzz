def exercice(Fizzbuzz): 
 list_of_nums = list(range(1, Fizzbuzz))
 for num in list_of_nums: 
        if num % 3 == 0 and num % 5 == 0: 
            print('Fizzbuzz') 
        elif num % 3 == 0: 
            print('Fizz') 
        elif num % 5 == 0: 
            print('Buzz') 
        else: print(num)

exercice(100)