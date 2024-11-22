import random
from colorama import Fore, Back

print(Fore.RED+f"\n\nThis robot guesses numbers between 1 and 100.In this game, first choose a name for yourself and then play this game in two computer and user modes.Computer mode: In this mode, the computer considers a random number between 1 and 100 and you have to guess that number according to the computer's answers.User mode: In this mode, you consider a number between 1 and 100 and the computer suggests numbers in this numerical range to you, and you have to guide the computer to the correct answer with keywords larger or smaller.\n\n")

username = input(Fore.GREEN+"Let's start. What is Your Name? ")
username = str.lower(username)

if username == '': 
    input(f"\n\n"+Fore.GREEN+"What Is Your Name? ")
else : 
    status = {
        'PC': 0, 
        username: 0
    }


    while True: 
        begin = input(f"\n\n"+Fore.WHITE+Back.BLACK+'What do you want to do (Status,Play Game,Exit):')
        begin = str.lower(begin)

        match begin: 
            case 'status': 
                print(f"\n\n"+Fore.YELLOW+f'PC: {status["PC"]}\n{username}: {status[username]}')

            case 'play game': 
                game_mode = input(f"\n\n"+Fore.LIGHTBLUE_EX+'Please Enter Game Mode (PC, User): ')
                game_mode = str.upper(game_mode)

                if game_mode == 'PC': 
                    pc_num = random.randint(1,100)
                    while True: 
                        user_guess = input(f"\n\n"+Fore.LIGHTRED_EX+"Enter Your Guess: ")
                        user_guess = int(user_guess)
                        if pc_num > user_guess: 
                            print(f"\n\n"+Fore.LIGHTRED_EX+'Please Select an Grether than Number!')
                        elif pc_num < user_guess: 
                            print(f"\n\n"+Fore.LIGHTRED_EX+'Please Select an Less than Number!')
                        elif pc_num == user_guess: 
                            print(f"\n\n"+Fore.LIGHTRED_EX+'Congratulation! You Win')
                            status[username] += 1
                            break
                elif game_mode == "USER":
                    start = 1
                    End = 100
                    while True: 
                        pc_guess = random.randint(start,End)
                        print(pc_guess)
                        user_solve = input(f"\n\n"+Fore.MAGENTA+'Is my suggestion correct?(please answer with keywords greather or less or correct): ')
                        user_solve = str.lower(user_solve)
                        if user_solve == 'greather': 
                            start = pc_guess
                        elif user_solve == 'less': 
                            End = pc_guess
                        elif user_solve == 'correct': 
                            print(f"\n\n"+Fore.BLACK + Back.WHITE+'Thank you, it was a good game.')
                            status['PC'] += 1
                            break
            case 'exit': 
                print(f"\n\n\nIt was a good game.\n---------- bye ----------")
                break