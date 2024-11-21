# Guess password

password = 'a123456'
guess_num = 3
 
while guess_num > 0:
    guess = input('Please input password: ')
    if guess == password:
        print('Sign in')
        break
    else:
        guess_num -= 1
        print('Password is wrong')
        if guess_num > 0:
            print('You still have', guess_num, 'chances' )
        else:
            print('Fail to sign in')
            break



