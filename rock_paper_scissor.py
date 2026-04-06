import random
print("Welcome to Rock, Paper and Scissor!!!")
ans='y'
yp=bp=0
while ans.lower()=='y':
    num=random.randint(1,3)
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    choice=int(input("What is your choice???"))
    if choice==1:
        if num==1:
            print("Same Toss!! Both kept Rock")
            print("Your Score:",yp)
            print("Bot's Score:",bp)
        elif num==2:
            print("Oops!!, Your toss is rock and bot's toss is paper.")
            bp+=1
            print("Your Score:",yp)
            print("Bot's Score:",bp)
        else:
            print("Yay!!, Your toss is rock and bot's toss is scissor.")
            yp+=1
            print("Your Score:",yp)
            print("Bot's Score:",bp)
    elif choice==2:
        if num==1:
            print("Yay!!, Your toss is paper and bot's toss is rock")
            yp+=1
            print("Your Score:",yp)
            print("Bot's Score:",bp)
        elif num==2:
            print("Same Toss!! Both kept Paper")
            print("Your Score:",yp)
            print("Bot's Score:",bp)
        else:
            print("Oops!!, Your toss is paper and bot's toss is scissor")
            bp+=1
            print("Your Score:",yp)
            print("Bot's Score:",bp)
    elif choice==3:
        if num==1:
            print("Oops!!, Your toss is scissor and bot's toss is rock")
            bp+=1
            print("Your Score:",yp)
            print("Bot's Score:",bp)
        elif num==2:
            print("Yay!!, Your toss is scissor and bot's toss is paper")
            yp+=1
            print("Your Score:",yp)
            print("Bot's Score:",bp)
        else:
            print("Same toss!! Both kept scissor")
            print("Your Score:",yp)
            print("Bot's Score:",bp)
    else:
        print("Invalid Input try again!!")
    ans=input("Do you want to continue?? (Y?N)")
