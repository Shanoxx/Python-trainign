x=9
z=3
c=0
print('Guess what!')
while c<z:
    v=int(input('Guess: '))
    c+=1
    if v==x:
        print('Bravo! You won!')
        break
else:
    print('You lose!')





