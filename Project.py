import random
import string
import json


def first_level_selection():
    print('Please select from 1-2 below')
    print(f' 1. Staff Login\n'
          f' 2. Close App\n')
    choice = input('Enter your choice: ')

    if int(choice) == 1:
        access = login()
        if access:
            second_level_selection()
    elif int(choice) == 2:
        exit()
    else:
        print('Invalid Choice')
        first_level_selection()


def second_level_selection():
    session = open('session.txt', 'w+')
    print('Please select from 1-3 below')
    print(f' 1. Create New Bank Account\n'
          f' 2. Check Account Details\n'
          f' 3. Logout\n')
    ch = input('Enter your choice: ')

    if ch == '1':
        create_new_account()
    elif ch == '2':
        account_details()
    elif ch == '3':
        first_level_selection()
    else:
        print('Invalid Choice')
        second_level_selection()


def create_new_account():
    customer = open('customer.txt', 'a+')
    
    acctName = input('Enter Account Name: ')
    acctType = input('Enter Account Type: ')
    openbal = int(input('Enter Opening Balance: '))
    acctemail = input('Enter Account Email: ')
    acctno = ''.join(random.choice(string.digits) for i in range(10))

    print(f'The generated account number is {acctno}')

    customer_details = {
        'Account Name': acctName,
        'Account Type': acctType,
        'Opening Balance': openbal,
        'Account Email': acctemail,
        'Account Number': acctno
    }
    customer.write(f'Account Name: {acctName},'
                   f'Account Type: {acctType},'
                   f'Opening Balance: {openbal},'
                   f'Account Email: {acctemail},'
                   f'Account Number: {acctno}')
    customer.write('\n')
    customer.close()
    second_level_selection()


def account_details():
    account_number = input('Please input the account number you wish to query: ')
    customer = open('customer.txt', 'r+')
    for detail in customer:
        if account_number in detail:
            print(detail)
        else:
            print('Data not found')
            return login()
    
    customer.close()
    
    second_level_selection()
    pass

def login():
    holder = []
    container = []
    header = ['username', 'password', 'email', 'full name']
    staff = open('staff.txt', 'r')
    staffers = staff.readline()
    staffers = staffers.split('-')
    staff.close()

    for details in staffers:
        holder.append(details.split(','))

    for staff in holder:
        container.append(dict(zip(header, staff)))

    def check():
        trial = 3
        while trial > 0:
            trial -= 1
            input_username = input('Enter your username: ')
            input_password = input('Enter your Password: ')

            for employee in container:
                if input_username.lower() == employee['username'].strip():
                    if input_password == employee['password'].strip():
                        return True


            print('Wrong username or password inputted')

        return False

    return check()

first_level_selection()
