
import random
#def num_system():
#    denary_num = input("Please enter a number of your choice")
#    octo_num1 = denary_num // 8 
#    octo_num2 = octo_num1 // 8
#
#    octo_value = print(octo_num2)


def den_convert(den_num):
    result = ''
    while den_num > 0:
        rem_num = den_num % 8
        print('rem', rem_num)
        den_num = den_num // 8
        print('den', den_num)
        result = str(rem_num) + result
    print('The octal number is ', result)


#denary_num = input("Please enter a number of your choice: ")

#den_convert(int(denary_num))


#print(57 // 8)
#print(57 % 8)

numbers = [None] * 100
current_idx = 0
#check_stack = True

def push_test(dataValue, topStack):
 if topStack != 100:
    print("topStack index: ", topStack)
    numbers[topStack] = dataValue
    print("dataValue is:", dataValue)
    return True
 else:
    return False
 

#while check_stack: # While result from push() is True
#   ran_num = random.randint(0, 99)
#   check_stack = push_test(ran_num, current_idx) # Setting check_stack to True/False that is returned from push()
#   topStack = topStack + 1
#
#print(numbers)

# ----------------------------------
print('\nExecuting push_py() function from while loop\n-------------------------------------------\n\r')

numbers = [None] * 100
current_idx = 0
check_stack = True

def push_py(dataValue, topStack):
 print('Index: ', topStack)
 if topStack != 100:
    print('Inserting:', dataValue)
    numbers[topStack] = dataValue
    topStack = topStack + 1
    return True
 else:
    return False
 
while check_stack: # While result from push() is True
   ran_num = random.randint(0, 99)
   check_stack = push_test(ran_num, current_idx) # Setting check_stack to True/False that is returned from push()
   current_idx = current_idx + 1

print(numbers)


# ----------------------------------
print('\nExecuting push() function with value of 15\n-------------------------------------------\n\r')

numbers = [0] * 100
topStack = 0

def push(dataValue):
    global topStack   # ← THIS IS THE KEY LINE
    print('Index:', topStack)

    if topStack != 100:
        numbers[topStack] = dataValue
        topStack = topStack + 1
        return True
    else:
        return False

if push(15):
    print("Added")
else:
    print("Not Added")
