from ast import Str
import sys
from time import sleep

ANIMATE_DURATION = 0.0085
SLOW_ANIMATE_DURATION = 0.075

name = ""
nickname = ""

texts = {
    "welcome to server": '''
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
    ''',
    "bot intro": "Greeting!\nAs a proper lad i am, i shall introduce me self.\nMy name is Cy William Bot the 3rd (royal)\n...but everyone calls me CyBot!\nI was designed by this mad lad named 'Tom'\nWhom i shall call 'the Boss'!\nDesigned to make simple questions...i was\nI seek to know you better!\nSo let's begin!\n",
    "greet with name": f"Hello {name}! Nice meeting ya!\nGreat!!\nI have already known your name !Which is {name}...\nWhat is your nickname?\nIt's okay if you don't have one!\n",
    "birthday": f"So {nickname}, it would be rude to ask about this...\nBut what is your date of birth?\nYet again if you don't want to answer\n",
    "gender": f"So...{nickname}?\nWhat is your gender ?\nIf you don't like answering...\n",
}

questions = {
    1: "Do you wish to continue ? :",
    2: "What is your name ? M'lad ? ",
    3: "Just leave it blank and press Enter__",
    4: "Just leave it blank and press Enter__",
    5: "Just press Enter like the previous one__"
}

# TODO: could also add different way of saying the same thing (man, boy, male etc...)

# TODO: create another dictionary and add empty values for other questions, and then add things for new answer options
questionAnswerOption1 = {
    1: "Ello luv! We shall continue!",
    2: "",
    3: "Then! GoofyBoo i shall call you!",
    4: f"Terribly sorry...my dear {nickname},for being informal......",
    5: f"A nice young lad you are,{nickname}!"
}

# FIXME: The {nickname} things does not work properly with dictionaries
questionAnswerOption2 = {
    1: "Ah alright darling, we shall meet in another day!",
    2: "",
    3: "",
    4: "",
    5: f"A pretty young belle you are,{nickname}!"
}

questionAnswerOption3 = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "Okay dear if you don't wanna, it's cool!\nAs long as you are happy!"
}

questionNoAnswer = {
    1: "Hint:Use (Yes or No) with no space ",
    2: "",
    3: f"I shall call you {nickname}!Cos we're now friend!",
    4: "Oh great!\nI will definitely come to your birthday",
    5: f"That is not a gender innit ?\nYou must be mistaking..."
}

userAnswerOption1 = {
    1: "yes",
    2: "",
    3: "",
    4: "",
    5: "boy"
}

userAnswerOption2 = {
    1: "no",
    2: "",
    3: "",
    4: "",
    5: "girl"
}

userAnswerOption3 = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: ""
}


def question(number: int, name: str, nickname: str):
    # make sure it has been answered
    answered = False
    while not answered:
        # if not answered, loop
        answer = input(questions[number])

        # extract information in the special cases
        if number == 2:
            name = answer
            answered = True
            break
        elif number == 3:
            if not answer:
                nickname = "GoofyBoo"
            else:
                nickname = answer
                answered = True

        if answer.lower() == userAnswerOption1[number]:
            slow_txt_animate(questionAnswerOption1[number] + "\n")
            answered = True
        elif answer.lower() == userAnswerOption2[number]:
            slow_txt_animate(questionAnswerOption2[number] + "\n")
            answered = True
        elif answer.lower() == userAnswerOption3[number]:
            slow_txt_animate(questionAnswerOption3[number] + "\n")
        else:
            slow_txt_animate(questionNoAnswer[number] + "\n")

    returnList = [name, nickname]
    return returnList


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
    global name
    global nickname

    txt_animate(texts["welcome to server"])

    # continue
    question(1, name, nickname)

    slow_txt_animate(texts["bot intro"])

    # name
    tempVar = question(2, name, nickname)

    # update name
    name = tempVar[0]

    slow_txt_animate(texts["greet with name"])

    # nickname
    tempVar = question(3, name, nickname)

    # update nickname
    nickname = tempVar[1]

    slow_txt_animate(texts["birthday"])

    # date of birth
    question(4, name, nickname)

    slow_txt_animate(texts["gender"])

    # gender
    question(5, name, nickname)


if __name__ == "__main__":
    main()
#Hey good boy, i would love to hear more about your changes to my previous program, since i cannot work this code out lmao!
