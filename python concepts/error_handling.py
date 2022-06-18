# Common errors
# syntax error, name error, index error, key error, value error, type error

while True:
    try:
        age = int(input("What is your age?"))
        print(10/age)
        # raise ValueError("Hey cut it out")  # when you want to terminate the programm for an error
    except ValueError:
        print("Please enter a number!")
        continue    # continue will start again from the while loop
    except ZeroDivisionError:
        print("Enter a nonzero number!")
    else:
        print("Thank you!")
        break   # break emediately break out the while loop
    finally:    # no matter what, this will run every single time the loop is started
        print("ok, I am finally done")
    print('can you hear me?')





# def summ(num1 = 0, num2 = 0):
#     try:
#         print(num1 + num2)
#         print(num1 / num2)
#     # except TypeError as sohan:
#     #     print(f"Please Enter numbers. Error: {sohan}")
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)

# summ(8, 0)