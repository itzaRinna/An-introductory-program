import sys
from time import sleep

def txt_animate(text):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(0.01)
hello = '''
██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░██╗    
██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗██║    
███████║█████╗░░██║░░░░░██║░░░░░██║░░██║██║    
██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║╚═╝    
██║░░██║███████╗███████╗███████╗╚█████╔╝██╗    
╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░╚═╝    

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

░█████╗░██╗░░░██╗███████╗███████╗██████╗░░█████╗░
██╔══██╗╚██╗░██╔╝╚════██║██╔════╝██╔══██╗██╔══██╗
██║░░╚═╝░╚████╔╝░░░███╔═╝█████╗░░██████╔╝██║░░██║
██║░░██╗░░╚██╔╝░░██╔══╝░░██╔══╝░░██╔══██╗██║░░██║
╚█████╔╝░░░██║░░░███████╗███████╗██║░░██║╚█████╔╝
░╚════╝░░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░
'''
txt_animate(hello)

transition = " "
print(transition)

proceed = input("Do you wish to continue ? :")
if proceed.lower() == 'yes':
  print("Ello luv! We shall continue!")
elif proceed.lower() == 'no':
  print("Ah alright darling, we shall meet in another day!")
  exit()
else:
  print("Hint:Use (Yes or No)")
  exit()

print(transition)

def slow_txt_animate(text):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(0.09)

slow_txt_animate("Greeting!\nAs a proper lad i am, i shall introduce me self.\nMy name is Cy William Bot the 3rd (royal)\n...but everyone calls me CyBot!\nI was designed by this mad lad named 'Tom'\nWhom i shall call 'the Boss'!\nDesigned to make simple questions...i was\nI seek to know you better!")

print(transition)

slow_txt_animate("So let's begin!")

print(transition)

qst_1 = input("What is your name ? M'lad ? ")
slow_txt_animate("Hello {}! Nice meeting ya!".format(qst_1))

print(transition)

slow_txt_animate("Great\nI have already known your name!\nWhat is your nickname?\n")
qst_2 = input("It's okay if you don't have one! ")
if qst_2.lower() == "no i dont have one" or "no i don't have one" :
  print("Then Goofy i shall call you!")
elif qst_2.lower() == "sorry i dont have a nickname" or "sorry i don't have a nickname" :
  print("Then Cutie i shall call you!")