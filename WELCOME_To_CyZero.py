import sys
from time import sleep

ANIMATE_DURATION = 0.0085
SLOW_ANIMATE_DURATION = 0.075


def txt_animate(text):
    for letter in text:
        print(letter, end="")
        sys.stdout.flush()
        sleep(ANIMATE_DURATION)


def slow_txt_animate(text):
    for letter in text:
        print(letter, end="")
        sys.stdout.flush()
        sleep(SLOW_ANIMATE_DURATION)


def main():
    hello = '''
      ██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░██╗    
      ██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗██║    
      ███████║█████╗░░██║░░░░░██║░░░░░██║░░██║██║    
      ██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║╚═╝    
      ██║░░██║███████╗███████╗███████╗╚█████╔╝██╗    
      ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░╚═╝    

      ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗   ████████╗░█████╗░
      ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝   ╚══██╔══╝██╔══██╗
      ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░   ░░░██║░░░██║░░██║
      ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░   ░░░██║░░░██║░░██║
      ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗   ░░░██║░░░╚█████╔╝
      ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝   ░░░╚═╝░░░░╚════╝░

      ░█████╗░██╗░░░██╗███████╗███████╗██████╗░░█████╗░
      ██╔══██╗╚██╗░██╔╝╚════██║██╔════╝██╔══██╗██╔══██╗
      ██║░░╚═╝░╚████╔╝░░░███╔═╝█████╗░░██████╔╝██║░░██║
      ██║░░██╗░░╚██╔╝░░██╔══╝░░██╔══╝░░██╔══██╗██║░░██║
      ╚█████╔╝░░░██║░░░███████╗███████╗██║░░██║╚█████╔╝
      ░╚════╝░░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░
    '''

    txt_animate(hello)
    

    proceed = input("Do you wish to continue ? :")
    if proceed.lower() == 'yes':
        print("Ello luv! We shall continue!")
    elif proceed.lower() == 'no':
        print("Ah alright darling, we shall meet in another day!")
        exit()
    else:
        print("Hint:Use (Yes or No) with no space")
        exit()
    

    slow_txt_animate("Greeting!\nAs a proper lad i am, i shall introduce me self.\nMy name is Cy William Bot the 3rd (royal)\n...but everyone calls me CyBot!\nI was developed by this mad lad named 'Tom'\nWhom i shall call 'the Boss'!\nDesigned to make simple questions...i was\nI seek to know you better!\n")


    slow_txt_animate("So let's begin!\n")
    

    qst_1 = input("What is your name ? M'lad ? ")
    slow_txt_animate("Hello {}! Nice meeting ya!\n".format(qst_1))


    slow_txt_animate(
        "Great!!\nI have already known your name !Which is {}...\nWhat is your nickname?\nIt's okay if you don't have one!\n".format(qst_1))


    qst_2 = input("Just leave it blank and press Enter__")
    if not qst_2:
        slow_txt_animate("Then! GoofyBoo i shall call you!\n")
        qst_2 ='GoofyBoo'
    else:
        slow_txt_animate("I shall call you {}!Cos we're now friend!\n".format(qst_2))

    slow_txt_animate("So {}, it would be rude to ask about this...\nBut what is your date of birth?\nYet again if you don't want to answer\n".format(qst_2))


    qst_3 = input("Just leave it blank and press Enter__")
    if not qst_3:
        slow_txt_animate("Terribly sorry...my dear {},for being informal......\n".format(qst_2))
    else:
        slow_txt_animate("Oh great!\nI will definitely come to your birthday\n")
    
    slow_txt_animate("So...{}?\nWhat is your gender ?\nIf you don't like answering...\n".format(qst_2))


    qst_4 = input("Just press Enter like the previous one__")
    if qst_4.lower() == 'boy':
        slow_txt_animate("A nice young lad you are,{}\n!".format(qst_2))
    elif qst_4.lower() == 'girl':
        slow_txt_animate("A pretty young belle you are,{}\n!".format(qst_2))
    elif qst_4 == '':
        slow_txt_animate("Okay dear if you don't wanna, it's cool!\nAs long as you are happy!")
    elif qst_4 == 'nonbinary':
        slow_txt_animate("A beautiful person you are,{}\n!".format(qst_2))
    elif qst_4 == 'transgender':
        slow_txt_animate("A strong beautiful person you are,{}\n".format(qst_2))
    else:
        slow_txt_animate("That is not a gender innit ?\nYou must be mistaking...\n")
        print('__please try again with the input( boy / girl / nonbinary )__')
    
    
    qst_5 = input("What is your sexuality?")
    if qst_5.lower() == "helicopter":
        slow_txt_animate("A meme lord you are !")
    elif qst_5.lower() == "heterosexual":
        slow_txt_animate("Okay! Good to hear")
    elif qst_5.lower() == "homosexual":
        slow_txt_animate("Okay! Good to hear")
    elif qst_5.lower() == "bisexual":
        slow_txt_animate("Okay! Good to hear")
    else:
        slow_txt_animate("I'm not familiar with that term, but i wish you happy!")
    
    
if __name__ == "__main__":
    main()
