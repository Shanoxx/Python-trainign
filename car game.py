print("Write 'help' to see help options")
x=''
started = False
while x != 'QUIT':
    x = input('What you want to do with your car ? ').upper()
    if x=='QUIT':
        print('Bye!')
        break
    elif x == 'HELP':
        print('''
Start engine write - START
Stop engine write - STOP
Turn left write - LEFT
Turn right write - RIGHT ''')
    elif x == 'START':
        if started:
            print('Your engine is already started!')
        else:
            started = True
            print('Your engine is started!')
    elif x == 'STOP':
        print('Your engine stopped!')
    elif x=='LEFT':
        print('You turn left!')
    elif x == 'RIGHT':
        print('You turn right!')
    else:
        print('Wrong command!')
