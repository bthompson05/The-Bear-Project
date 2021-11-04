import random
from sys import exit
# Power ups that are present in the game
possible_power_ups = ["Shrewd Negotiator", "Discount", "Double or Nothing", "Night Time"]
power_ups = ["Shrewd Negotiator", "Discount", "Double or Nothing", "Night Time"]
# Power ups that you hav purchased
power = ["Shrewd Negotiator"]
# Starting gold amount
gold = 600

def save():
    global gold
    score = gold
    # Gets the username the user wants to be saved as
    name = input("Enter a nickname for you score to be saved to:\n")
    scores = []
    added = False
    # Opens score with the read operator
    fp = open("scores.txt","r")
    #Reads each line of the file
    for line in fp.readlines():
        # Sorts list based on higest score by adding above or below based on score
        line_score = int(line.replace("\n","").split(" with a score of ")[1])
        if score > line_score and added == False:
            scores.append(name+" with a score of "+str(score)+"\n")
            added = True
        scores.append(line)
    if added == False:
        scores.append(name + " with a score of " + str(score) + "\n")
        # Closes file
    fp.close()
    # Re-opens with write operator
    fp = open("scores.txt","w")
    for scoreline in scores:
        #Replaces text with the new sorted one
        fp.writelines(scoreline)
    fp.close()

#The questions that are ran at the end of every room
def prerequisites(wins):
    # Sends user to the shop if they desire
    print("You have {} gold".format(gold))
    print("You have the following power-ups: {}".format(", ".join(power)))
    print("You currently have beaten {} rooms".format(wins))
    if input("Would you like to visit Cadbeary the shop?") == "yes":
        shop()
    if input("Would you like to do a challenge?") == "yes":
        challenges("game")


def challenges(test):
    # Question bank
    questions = ["Easy question. Bear. How do you spell it?", "What word is spelled incorrectly in every single dictionary?", "What will you actually find at the end of every rainbow?", "Some months have 31 days, others have 30 days, but how many have 28 days?", "Uncle Bill’s farm had a terrible storm and all but seven sheep were killed. How many sheep are still alive?", "What 5-letter word becomes shorter when you add two letters to it?", "What can you make that no one—not even you—can see?"]
    # Answers to question bank
    answers = ["it", "incorrectly", "w", "12", "7", "short", "noise"]
    # Generates a random question index from the list
    rand_question = random.randint(0, len(questions)-1)
    # Prints that question based on its index
    print(questions[rand_question])
    global gold
    # Checks if the answer is what the user inputted
    if test != "power_up":
        if answers[rand_question] == input("What's your answer:\n"):
            print("Congrats. You got it correct, 50")
            # Increases the users gold by 50
            gold += 50
        else:
            # Decreases the users gold by 25
            gold -= 25
    else:
        if answers[rand_question] == input("What's your answer:\n"):
            return True
        else:
            return False

def power_up_choice(bear_demands):
    # Checks if you have any power ups and gives relevant output
    if len(power) == 0:
        print("You have no available power-ups.")
    else:
        print("You have a", ", ".join(power))
    # Runs if the user would like to  use a power up
    if input("Would you like to use a power-up?") == "yes":
        print("Which of the following power-ups would you like to use?")
        # Prints the available power ups
        for i in range (0, len(power)):
            print("Choose", i, "for", power[i])
        # Asks the user for their choice
        choice = int(input("Make your power-up choice:\n"))
        print("You have chosen", power[choice])
        power_up = power[choice]
        # Removes the power-up from your list of available power ups
        power.remove(power_up)
        # Runs power_up_effect
        effect = power_up_effect(power_up, bear_demands)
        return effect

def power_up_effect(pu, demands):
    # Finds what index the chosen power up is in the choices
    effect_index = power_ups.index(pu)
    # Calls the function of the desired power_up
    if effect_index == 0:
        effect = power_up_0(demands)
        return effect
    if effect_index == 1:
        effect = power_up_1(demands)
        return effect
    if effect_index == 2:
        effect = power_up_2(demands)
        return effect
    if effect_index == 3:
        effect = power_up_3(demands)
        return effect

def power_up_0(demands):
    # Calculates a random percentage deduction
    deduct = round(random.uniform(0.5, 0.9), 1)
    # Calculates the new demands
    new_demands = round(demands * deduct)
    print("You and the bear negotiate a", str(round((1-deduct)*100)) + "% deduction. His new demands are", str(new_demands), "gold.")
    # Returns to the game the new demands
    print(new_demands)
    return new_demands

def power_up_1(demands):
    # Creates a random multiple of 50 up to half of the demands
    deduct = 50 * round((random.randint(demands/8, demands/2))/50)
    # New demands decided by old demands subtracted with the discount
    new_demands = demands - deduct
    print("You and the bear get along and he has decided to give you a discount of", str(deduct), "gold. His new demands are", str(new_demands), "gold.")
    return int(new_demands)

def power_up_2(demands):
    # Runs a challenge and runs result based on whether you get the quesiton correct or incorrect
    if challenges("power_up") == True:
        print("You survive. Out of respect for your genius, the bear has dropped its demands. You may proceed with all of your gold")
        return 0
    else:
        print("Game over.")

def power_up_3(demands):
    print("You manage to put the bear to sleep and sneak past him. Success, no gold lost")
    # Returns his new demands of 0 as the bear is not interacting
    return 0

def bear():
    print("You have encountered a bear. Let's see what the bear has in stall for you")
    bear_options = [bear_00, bear_01, bear_02, bear_03]
    # Picks a random function to call
    random.choice(bear_options)()

def bear_00():
    print("The bear is feeling merciless and very hungry.\nThe bear eats you.")
    # You die so the game over function is called
    game_over()

def bear_01():
    global gold
    print("The bear is hungry and wants to take most of your gold.")
    # Generates random number between 0.5 and 0.9 to 1 decimal place
    percent = round(random.uniform(0.5, 0.9), 1)
    # Multiplied by your gold to find the bears demands
    demands = round(percent * gold)
    print("The bear's demands are", str(demands), "gold.")
    #Decides whether you use a power-up and subtracts resulting demands
    if input("Would you like to use a power up? yes if so") =="yes":
        new_demands = int(power_up_choice(demands))
        gold -= new_demands
        print("The bear has taken", str(new_demands))
    else:
        gold -= demands
        print("The bear has taken", str(demands))

def bear_02():
    global gold
    print("The bear is not that hungry, so he wont take all of your gold")
    # Generates random number between 0.1 and 0.5 to 1 decimal place
    percent = round(random.uniform(0.1, 0.5), 1)
    print("The bear wants to take", str(percent*100), "of your gold.")
    # Multiplied by your gold to find the bears demands
    demands = round((percent) * gold)
    print("The bear's demands are", str(demands), "gold.")
    #Decides whether you use a power-up and subtracts resulting demands
    if input("Would you like to use a power up? yes if so") == "yes":
        new_demands = power_up_choice(demands)
        print(new_demands)
        print("The bear has taken", str(new_demands))
    else:
        gold -= demands
        print("The bear has taken", str(demands))

def bear_03():
    print("The bear is not hungry so you can keep your gold")

def shop():
    global possible_power_ups
    # Creates a local varialbe of all the available power-ups based on the global
    products = possible_power_ups
    # Set standard price, will update all else if changed
    price = 50
    special_product = special_offer_product(products)
    special_price = special_offer_price() * price
    print("Welcome to Cadbeary, the one stop shop for all of your power-ups.")
    print("Our current special offer is", special_product, "which costs", special_price, "gold.")
    print("The current avaiable power-ups are", ", ".join(products), "which if not stated otherwise cost", price, "gold.")
    if input("Would you like to buy a Cadbeary power-up? If so, type yes.") != "yes":
        print("See you next time!")
    else:
        for i in range (0, len(products)):
            # Iterates through the product list, assigning each item a number when printed
            print("Choose", i, "for", products[i])
        choice = int(input("Choose from 0 to 3"))
        # Determines whether it is the special offer price
        if products[choice] == special_product:
            cost = special_price
        else:
            cost = price
        print("You have bought", products[choice], "for", cost)
        global power
        # Adds the purchased power-up to the global list
        power.append(products[choice])
        global gold
        # Subtracts the cost from your gold
        gold -= cost
        # Removes the power-up from the global list to avoid being able ot re-purchase
        possible_power_ups.remove(products[choice])

def special_offer_product(products):
    # Random choice of product
    return random.choice(products)

def special_offer_price():
    return round(random.uniform(0.5, 0.9), 1)

def starter_room():
    if input("Welcome to the Bear Game. Would you like to read the instructions and rules? yes if so.") == "yes":
        # Reads the rules file and prints into terminal
        file = open("rules.txt", "r")
        contents = file.read()
        print(contents)
        file.close()
        print("\nNow let's continue.")
        int(input("First dilema. Do you want to go into Room 1 or Room 2?"))


def monty_hall():
    print("Behind one door is a pile of gold, behind the other two doors are bears. Guess a door which you think the gold is behind.")
    choice = int(input('Which door do you want to choose? (1,2,3): '))
    prizes = ['bear', 'gold', 'bear']
    # Randomizing the prizes
    random.shuffle(prizes)
    # Determining door without gold to open
    while True:
        opening_door = random.randrange(len(prizes))
        if prizes[opening_door] != 'gold' and choice - 1 != opening_door:
            break
    opening_door = opening_door + 1
    print('We are opening the door number', str(opening_door) +". Behind this door is a bear.")

    # Determining the door that they could switch to
    options = [1, 2, 3]
    options.remove(choice)
    options.remove(opening_door)
    switching_door = options[0]

    # Asking if the user would like to switch door
    print("Now, do you want to switch to door number", switching_door)
    answer = input()
    if answer == "yes":
        result = switching_door - 1
    else:
        result = choice - 1

    # Displaying the player's prize
    behind_door = prizes[result]
    print('And behind the door is a ...', behind_door)
    if behind_door == "bear":
        print("Now to meet the bear.")
        bear()
    if behind_door == "gold":
        # Creates a random gold reward between 50, 100, 150 or 200
        reward = 50 * round((random.randint(25, 200)) / 50)
        print("Congrats on avoiding the bear. You get", str(reward), "gold.")
        global gold
        gold += reward
        return True

def game_over():
    print("Unlucky your game is over. You are a loser and finish with 0 points.")
    exit(0)

def game():
    wins = 0    
    global gold
    starter_room()
    while True:
        if monty_hall() == True:
            # Adds to win variable based on what is returned
            wins +=1

        if gold > 0 and wins == 4:
            #Stops the game once you have reached the end
            print("Congrats. You've completed the game. You had {} gold.".format(gold))
            save()
            break
        if gold <1 :
            # Calles the game over function when you have no gold left
            game_over()
            break
        prerequisites(wins)

game()