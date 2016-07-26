import time

def main():
    '''Main execution of the program'''
    main_menu = {
        '1. Print Integers': print_integers,
        '2. Print Fibonacci': print_fibonacci,
        '3. Print Primes': print_primes,
        '4. Quit': None
    }

    choice = prompt_menu(main_menu)
    func = main_menu[choice]

    if func == None: return

    func(prompt_amount())
    main()


def prompt_menu(menu):
    '''Accept a menu as a dictionary. Prompt user for part of a key'''
    choice = ""
    key_match = []
    # if not only 1 result, keep prompting
    while len(key_match) != 1:
        print('\nChoose an option:')
        [print(entry) for entry in sorted(menu.keys())]
        print()
        choice = input('> ')
        # get all keys for partial string match
        key_match = [key for key in menu.keys() if choice.lower() in key.lower()]
    return key_match[0]

def prompt_amount():
    '''Prompt for an integer value'''
    amount = -1
    while amount < 0:
        try:
            amount = input('Enter how many: ')
            amount = int(amount)
        except:
            amount = -1
    return amount


def slow_print(a_list):
    '''Print a list with some delay'''

    for n in a_list:
        print(n)
        time.sleep(.25)
    print('')


def print_integers(amount):
    '''Print integers from 1 to amount'''
    nums = [i for i in range(amount + 1)[1:]]
    slow_print(nums)


def fibs(amount):
    '''Generator for an amount of Fibonacci numbers'''
    a, b = 0, 1

    yield a
    yield b

    # starting after the first 2 numbers
    for i in range(amount - 2):
        a, b = b, a + b
        yield b

def print_fibonacci(amount):
    '''Print amount of Fibonacci numbers'''
    nums = [i for i in fibs(amount)]
    slow_print(nums)


def is_prime(num):
    '''Test if number is prime'''
    # All prime numbers, other than 2 & 3, are of the form 6n+/-1.
    # All composite numbers have prime factors
    if num == 2 or num == 3: return True
    if num < 2 or num % 2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False
    root = int(num ** 0.5)  # square root
    factor = 5
    while factor <= root:
        if num % factor == 0: return False
        if num % (factor + 2) == 0: return False
        factor += 6
    return True

def primes(amount):
    '''Generator for an amount of prime numbers'''
    count = 0
    num = 2
    while(count < amount):
        while(not is_prime(num)): num += 1
        yield num
        num += 1
        count += 1

def print_primes(amount):
    '''Print amount of prime numbers'''
    nums = [i for i in primes(amount)]
    slow_print(nums)


if __name__ == '__main__':
    main()
