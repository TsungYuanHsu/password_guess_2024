# Guess password

password = 'a123456'
guess_num = 3
 
while True:
    guess = input('Please input password: ')
    if guess == password:
        print('Sign in')
        break
    else:
        guess_num -= 1
        print('Password is wrong')
        print('You still have', guess_num, 'chances' )
        if guess_num == 0:
            print('Fail to sign in')
            break


