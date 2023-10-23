# first we import random module
import random
# create a list to choice the things for the game
list_to_choice=['ROCK','PAPER','SCISSOR']

# create a while loop 
while(True):
    Computer_count=0      
    User_count=0
    
    User_Choice=int(input('''
If you start the Game please press the button : Given below

1 -> If you start the Game--->
2 -> If you exit this Game--->
                          '''))
    if User_Choice==1:
        for i in range(3):
            User_input=int(input('''
Please choose the anyone number: Given below
1 -> ROCK
2 -> PAPER
3 -> SCISSOR                                 
                                 '''))
            if User_input==1:
                user_choice='ROCK'
            elif User_input==2:
                user_choice='PAPER'
            elif User_input==3:
                user_choice='SCISSOR'
            else:
                print('This is invalid number->')    
            Computer_choice=random.choice(list_to_choice)
            if Computer_choice==user_choice:
                print('Computer Choice', Computer_choice)    
                print('User Choice', user_choice)
                print('Game Draw')    
            elif (user_choice=='ROCK' and Computer_choice=='SCISSOR') or (user_choice=='PAPER' and Computer_choice=='ROCK') or (user_choice=='SCISSOR' and Computer_choice=='PAPER'):
                print('Computer Choice', Computer_choice)    
                print('User Choice', user_choice)
                print('You won the Match')
                User_count+=1
            else:
                print('Computer Choice', Computer_choice)    
                print('User Choice', user_choice)
                print('Computer Win the Match') 
                Computer_count+=1 
                  
        if User_count==Computer_count:
            print('Match is Draw🤷‍♂️')
            print(User_count)  
            print(Computer_count)  
        elif(User_count>Computer_count):
            print(f'You win the match with this {User_count} number 👌')
            print(User_count)  
            print(Computer_count)  
        else:
            print(f'You win the match with this {Computer_count} number 🙏')  
            print(User_count)  
            print(Computer_count)           
            
    else:
        break
    