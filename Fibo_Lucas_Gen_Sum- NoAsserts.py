"""test function selection based on boolean"""
import click


def fibonacci(n0, init1, init2):
    print('Fibonacci \n')
    list_of_fibs = [0] * n0  #
#    init1, init2 = 1, 1  # first two numbers of Fibonacci are 1 and 1

    list_of_fibs[0] = init1  # build list of Fibonacci numbers
    list_of_fibs[1] = init2  # starting with 1 and 1

    for i in range(2, n0):  # do the recursions
        list_of_fibs[i] = list_of_fibs[i - 1] + list_of_fibs[i - 2]

    sum_value = list_of_fibs[n0 - 1]
    return sum_value


def lucas(n0, init1, init2):
    print('Lucas \n')
    list_of_lucas = [0] * n0  # the 1st two Lucas numbers are 1 and 3
#    init1, init2 = 1, 3

    list_of_lucas[0] = init1  # build the list of Lucas numbers
    list_of_lucas[1] = init2  # starting with 1 and 1

    for i in range(2, n0):
        list_of_lucas[i] = list_of_lucas[i - 1] + list_of_lucas[i - 2]

    sum_value = list_of_lucas[n0 - 1]
    return sum_value



def gen_sum(n0, init1, init2):
    print('General Sum')
    list_of_gensum = [0] * n0  # the 1st two general sum numbers are n1 and n2
#    init1, init2 = n1, n2

    list_of_gensum[0] = init1  # build the list of GenSum numbers
    list_of_gensum[1] = init2  # starting with 1 and 1

    for i in range(2, n0):
        list_of_gensum[i] = list_of_gensum[i - 1] + list_of_gensum[i - 2]

    sum_value = list_of_gensum[n0 - 1]
    return sum_value

def i_am_done():
    print("program finished")
    quit()

""" Program Start Here """

print('The program will generate:')
print('     Fibonacci Series')
print('     Lucas Series')
print('     General Sum Series')
print('Default values for N1 and N2 will generate Fibonacci Series.\n')
print('Input Series Number:')
n0 = click.prompt('input n0', type = int, default = 10)

print('input n1, leave blank for Fibonacci\n input 2 for Lucas')
n1 = click .prompt('input n1', type = int, default = 0)

print('input n2, leave blank for Fibonacci\n input 1 for Lucas')
print('input your choice for General sum')
n2 =  click .prompt('input n2', type = int, default = 0)
print()



# sum_value = ""   #declare variable and set default to "0"
if n1 == 0  and n2 == 0:
    sum_value = fibonacci(n0, 1, 1) #(n0, n1, n2)
    print('Fibonacci Value = ', sum_value, '\n')
    i_am_done()


if n1 == 2 and n2 == 1:
    sum_value = lucas(n0, n1, n2)
    print('Lucas Value = ',sum_value,  '\n')
    i_am_done()


if n1 != 0 or n1 != 2:
    sum_value = gen_sum(n0, n1, n2)
    print('General Sum Value = ',sum_value, '\n')
    i_am_done()

