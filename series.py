""" Recursive program to calculate Fibonacci, Lucas and General Sum Series"""

""" This program will take three inputs:
        Number of terms to calculate
        Initial value of 1st term
        Initial value of 2nd term
    After accepting the inputs, the program will calculate the sum series using 
    the values input and display the results as well as identify the type of 
    series (Fibonacci, Lucas or General Sum Series
"""

# Get number of terms to calculate
def get_nterms():
    """Gets the input integer and returns the value to the parsing funtion"""

    print('Enter a number between 0 and 31 exclusive or "0" to exit')
    nterms = int(input())
    return nterms

# Calculation engine

def do_calcs(nterms, first, second):
    """ This function is the recursive calculation function.
    
    The number of terms, first value and 2nd value are input.
     A list is built that computes the value of the series.
     The list is returned to the calling function.
     """
    results = [first,second]
    for  i in range (nterms):
#        print('nterms = ', i, 'first = ',first, 'second = ', second)
        summed_val = first + second
        first = second
        second = summed_val
        results.append(summed_val)
    return results



# get the inputs
nterms = get_nterms()


# parsing function
if nterms < 0:
    print('Input a positive integer')
    nterms == 0
    nterms = get_nterms()

if nterms > 30:
    print('Input a number < 31')
    nterms == 0
    nterms = get_nterms()

if 0 < nterms < 31:
    print('Input 1st term\n')
    first = int(input())
    print()
    print('Input 2nd term= \n')
    second = int(input())

    print('nterms = ', nterms, ' first = ', first, 'second = ', second)
    results = do_calcs(nterms, first, second)
    if results[:2] == [0,1]:
        print('Fibonacci Series')
    if results[:2] == [2,1]:
        print('Lucas Series')
    else:
        print('General Sum Series')
    print(results)

else:
   print('quit')
