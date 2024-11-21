# Guess password

password = 'a123456'
guess_num = 0

while True:
    guess = input('Please input password: ')
    if guess == password:
        print('Sign in')
        break
    else:
        print('Password is wrong')
        print('You still have', 2 - guess_num, 'chances' )
        guess_num += 1
        if guess_num == 3:
            print('Fail to sign in')
            break


