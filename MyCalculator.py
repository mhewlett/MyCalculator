import os

# Show use of functions with various operations based on input. Results with formatted strings.
def calculate(i, n1, n2):
    if i == 1:
        return '{} + {} = {}'.format(n1, n2, n1 + n2)
    elif i == 2:
        return '{} - {} = {}'.format(n1, n2, n1 - n2)
    elif i == 3:
        return '{} * {} = {}'.format(n1, n2, n1 * n2)
    elif i == 4:
        return '{} / {} = {}'.format(n1, n2, (n1 / n2))
    elif i == 5:
        return '{} ^ {} = {}'.format(n1, n2, n1 ** n2)
    else:
        return 'Thanks for nothing'

# Function allowing user to type 'exit' to quit program at any point
def exit(x):
    if x.lower() == 'exit':
        quit()

# Check for exits and/or garbage inputs instead of Y or N
def check(m):
    exit(m)
    while m.lower() != 'y' and m.lower() != 'n':
        print('Enter a valid response.')
        m = input('(Y or N) ')
        exit(m)
    return m

# Check if user is found in the directory
print('Would you like to access the directory?')
sfile = input('(Y or N) ')
check(sfile)
if sfile.lower() == 'n':
    print('Closing directory')
elif sfile.lower() == 'y':
    user1 = input('Enter your first name: ')
    exit(user1)
    user2 = input('Enter your last name: ')
    exit(user2)
    username = user1[0].lower() + user2.lower()
    os.chdir('C:\\Users')
    li = os.listdir()

    while username not in li:
        print('User not found')
        cont = input('Would you like to continue? (Y or N): ')
        check(cont)
        if cont.lower() == 'y':
            sfile = 'n'
            break
        else:
            input('Closing program.')
            quit()

# Navigate to directory
if sfile == 'y':
    os.chdir('C:\\Users\\' + username + '\\')
    print()
    print(os.getcwd(), '-', 'User found')

# Setup program to begin in a loop for multiple uses based on user's preference
response = 'y'
while response.lower() == 'y':

    # Ask user if they want to review previous entries
    if sfile.lower() == 'y':
        read = input('Would you like to review the previous logged entries? (Y or N) ')
        check(read)
        if read.lower() == 'y':
            with open('MyCalculations.txt', 'r') as f:
                for line in f:
                    print(line)

    # Variable assignment and entry validation
    print('\nEnter 2 digits'.upper())
    num1 = input('Number 1: ')
    exit(num1)
    while not num1.isdigit:
        num1 = input('Enter a valid number: ')
    num2 = input ('Number 2: ')
    exit(num2)
    while not num2.isdigit():
        num2 = input('Enter a valid number: ')
        exit(num2)
    print('\nNumber 1 is {}. Number 2 is {}.'.format(num1, num2))

    # Choice of operation assignment
    choices = ['(1) Add', '(2) Subtract', '(3) Multiply', '(4) Divide', '(5) Exponential']
    print(choices)
    x = input('Select an operation: ')
    exit(x)

    # Call function and cast to proper data type
    calculated = calculate(int(x), int(num1), int(num2))
    print(calculated)

    # Check if user wants to print results to file
    if sfile == 'y':
        print('\nWould you like to record these results?')
        record = input('(Y or N) ')
        check(record)
        if record.lower() == 'y':
            with open('MyCalculations.txt', 'a') as f:
                f.write('\n')
                f.write(calculated.rstrip('\n'))

    # Determine user's choice to continue or quit
    print('\nRun program again?\n')
    response = input('(Y or N) ')
    check(response)
    if response.lower() == 'n':
        input('Adios turd nuggets ;P')