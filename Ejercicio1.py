i=0


while i < 101:
    if i % 3 == 0 and i % 5 == 0:
        print ("Fizzbuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)
    i = i + 1



def fizzbuzz():

    for number in range(1, 101):

        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


#fizzbuzz()