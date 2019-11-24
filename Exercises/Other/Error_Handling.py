
# while True:
#   try:
#     age = int(input('what is your age? '))
#     print(10/age)
#   except ValueError:                  # this block only runs once
#     print('Please enter a number!')
#   except ZeroDivisionError:
#     print('Zero division error')
#   except:                             # When i dont add this, it only handles the given type errors below
#     print('Something is wrong here')  # But, the error is vague so it is recommended to catch specific errors by type
#   else:
#     print('thank you')
#     break

# def sum(num1, num2):
#   try:
#     return num1 + num2
#   except TypeError as err:
#     print(f'please enter numbers Error: {err}')
#     # print('please enter numbers Error: ' + err) # this throws another error because err is an object not a string

# print(sum(1,'2'))

# def div(num1, num2):
#   try:
#     return num1 / num2
#   except (TypeError, ZeroDivisionError) as err:
#     print(err)

# print(div(1,'0'))
# print(div(1, 0))

while True:
    try:
        age = int(input('what is your age? '))
        print(10/age)
        # raise ValueError('hey cut it out')  # throws an error intentionally
        # raise Exception('hey cut it out')
    except ValueError:                  # only runs once, if it catches the first exception doesnt care about the rest
        print('Please enter a number!')
        # continue
    except ZeroDivisionError:
        print('Zero division error')
        # break
    else:
        print('thank you')
    finally:  # this runs after everything has been executed
        print('done')
    print('can you hear me?')
    break
