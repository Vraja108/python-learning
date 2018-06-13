# trying to make a small text-based game 

print('You wake up in a dark room. You can\'t remember how you got there. You can\'t remember anything.')
input()
print('Once your eyes have adjusted to the darkness, you can make out the silhouette of a door in front of you.')
print('The door is locked.')
input()
print('Do you...?\n(a) Knock on the door\n(b) Kick the door')

# knocked on door
while input() == 'a':
    print('You knock on the door. No one answers.')
    input()
    input('Well, that didn\'t work, so...')
    print('Do you...?\n(a) Knock on the door again\n(b) Kick the door')
# kicked door    
else:
    print('You kick the door in. It\'s not very strong. It swings right open.')
    input()
    str(input('The room is flooded with light. The sun is so bright it hurts your eyes. You step outside. You have no idea where you are but you see a road leading to a house.'
              '\nDo you follow the road? [y/n]: '))
    input()
    if input() == 'y':
        print('You follow')
    
#print('x')
#input()
#print('x')
#input()
#print('x')
#input()
#print('x')
#input()
#print('x')
#input()
#print('x')
