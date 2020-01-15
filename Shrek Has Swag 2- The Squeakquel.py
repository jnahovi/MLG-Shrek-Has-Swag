# -*- coding: utf-8 -*-
import os,sys
import time
import random
from random import randint
import webbrowser
import pyfiglet

global name
global weapon



def titleCard():
    shrek_banner = pyfiglet.figlet_format("Shrek Has Swag 2: The Squeakquel")
    print(shrek_banner)
    time.sleep(3);
    print "Welcome to the atrocity of a game that is, Shrek Has Swag"
    time.sleep(2)
    print "Believe it or not, this is the second Shrek Has Swag"
    time.sleep(2)
    print "Very disappointing... I know..."
    time.sleep(2)
    print "Oh well here we are, time to open up the story..."
    time.sleep(3)
    setup()

def setup():
    global playerHP
    global playerMP
    global playerWeap
    global playerATK
    global lastSpot
    playerHP = randint(500,800)
    playerMP = randint(500, 1000)
    name = raw_input("What is your name, noble hero? ")
    time.sleep(2)
    print name, "... that's a horrible name..."
    time.sleep(2)
    playerWeap = raw_input("What weapon would you like. A gun, knife, or brass knuckles? ")
    print("____________________________________________________________")
    setScene = pyfiglet.figlet_format("Nazi Germany, 1941 AD")
    setBeginningDay = pyfiglet.figlet_format("4 / 20 / 1941")
    print(setScene)
    print("____________________________________________________________")
    time.sleep(2)
    print(setBeginningDay)
    print("____________________________________________________________")
    time.sleep(2)
    print "Your clan, previously known as FaZe Clan (now known as the ET Killaz), have ordered you to find Shrek"
    time.sleep(3)
    print "You are one of your clan's strongest members, boasting", playerHP, "HP and" , playerMP, "MP"
    time.sleep(4)
    print "Shrek, known to all as the thiccest man in all the land, has been captured by Adolf Hitler."
    time.sleep(3)
    print "Hitler plans to use Shrek's gurtholicious power to invade Russia in the winter"
    time.sleep(3)
    print "Your clan leader, Joey Muños (Level 100 Mafia Boss), has ordered you"
    print "to find Shrek"
    time.sleep(6)
    print "In a furious monologue, Führer Muños describes the suffering of his people,"
    print "the Oompa-Loompas, and how Shrek had saved them from the brink of extinction."
    time.sleep(6)
    print "He described the suffering the Oompa-Loompas endured under the evil thumb of Shaggy,"
    print "an all powerful demi-god capable of destroying galaxies"
    time.sleep(6)
    print "He had used the Oompa Loompas as slaves, and their only job was to make crappy"
    print "iFunny memes to bring Shaggy more V-Bucks"
    time.sleep(6)
    print "In a moment of pure heroism, our glorious leader Joey (The Mighty Morphin Fedora Ranger)"
    print "organized a rebellion against the tyrannical Shaggy"
    time.sleep(6)
    print "He had promised to stop Shaggy's never-ending greed for more V-Bucks (which was starting"
    print "to turn into a craving for the more valuable Ro-buck)"
    time.sleep(7)
    print "Through the power of his fedora, he described his loss against the seemingly invincible"
    print "Shaggy, who through the use of his juul, ripped the fattest cloud of chloroform, almost killing our leader"
    time.sleep(7)
    print "Hearing our leader's chanting of Mo Bamba (Similar to pleaing for help (which fun fact in german translates"
    print "ŠíckÖ MÖde), Shrek decended from the heavens above, challenging Shaggy to a Yu-Gi-Oh duel"
    time.sleep(7)
    print "Shrek demolished Shaggy in the duel, and along with the help of the Lord Dr. Phil, Shaggy was sent to"
    print "the Ranch"
    time.sleep(4)
    print "After our leaders beautiful monologue on Shrek's grandeur, you now know how much this rescue means to Führer"
    print "Muños"
    time.sleep(5)
    print "You set out on your quest to rescue Shrek from Hitler"
    time.sleep(5)
    print("____________________________________________________________")
    startLocation = pyfiglet.figlet_format("Berlin, Germany")
    print (startLocation)
    print("____________________________________________________________")
    time.sleep(4)
    print "You've entered the wrecked town of Berlin"
    time.sleep(3)
    print "The misuse of Shrek's power is slowly causing destruction to the city"
    time.sleep(4)
    print "The massive amount of Fortnite played by Hitler is making everyone develop autism (much like Ninja)"
    time.sleep(4)
    print "You go out on the town, looking for clues on Shrek's wherabouts"
    time.sleep(4)
    print "You enter an alley in West Berlin, looking for clues to find Shrek"
    time.sleep(4)
    print "\"Hey, looks like we have ourselves a hero\""
    time.sleep(3)
    print "You turn around, and you see a gangbanger, ready to fight"
    time.sleep(4)
    print "It appears to be a Level 1 Crook"
    time.sleep(3)
    print "You roll up your sleeves, ready for a fight"
    lastSpot = 1
    time.sleep(3)
    enemySpawn(1)
    

def enemySpawn(LVL):
    global HP
    global MP
    global ATK
    global Weap
    global Type
    global concussionCount
    global bleedCount
    concussionCount = 0
    bleedCount = 0
    if (LVL >= 1 and LVL <= 5):
        HP = LVL * 10
        MP = LVL * 11
    elif(LVL >= 6 and LVL < 10):
        HP =  LVL * 12
        MP = LVL * 13
    elif(LVL >= 10):
        HP = LVL * 14
        MP = LVL * 15
    modifier = random.randint(1,6)
    weapList = ["pistol", "sword", "dual daggers","AK-47", "AR-15", "Machine Gun", "Dual Uzis", "knife", "fists", "bat", "brass knuckles"]
    random.shuffle(weapList)
    Weap = weapList[1]
    if (Weap == "pistol" or Weap == "AK-47" or Weap == "AR-15" or Weap == "Machine Gun" or Weap == "Dual Uzis"):
        ATK = 4 * modifier * LVL
        Type = "gun"
        enemyAttack()
    elif(Weap == "sword" or Weap == "dual daggers" or Weap == "knife"):
        ATK = 3 * modifier * LVL
        Type = "blade"
        enemyAttack()
    elif(Weap == "fists" or Weap == "brass knuckles" or Weap == "bat"):
        ATK = 2 * modifier * LVL
        Type = "blunt"
        enemyAttack()

def enemyAttack():
    global HP
    global MP
    global ATK
    global Type
    global concussionCount
    global bleedCount
    global playerHP
    global playerMP
    global playerWeap
    attackRandom = randint(1,3)
    missChance = randint(1,12)
    if Type == "blunt":
        concussionChance = randint(1,6)
        if (missChance < 4):
            print "Your opponent swings, but you dodge, and the enemy flies forward"
        else:
            print "Your opponent swings and lands a direct hit"
            playerHP = playerHP - ATK 
            time.sleep(3)
            print "You take", ATK, "damage"
            time.sleep(2)
            if (concussionChance >= 5):
                print "Critical Hit! The blow disorients you, stopping you from retaliating"
                playerHP = playerHP - (ATK * 2)
                time.sleep(2)
                concussionCount = concussionCount + 1
                if (concussionCount > 5):
                    print "After multiple concussions, you cannot carry on fighting"
                    time.sleep(4)
                    print "You drop to the ground, disoriented and defeated"
                    time.sleep(4)
                    youLose()
                else:
                    enemyAttack()
            time.sleep(2)
            print "You now have", playerHP, "HP and", playerMP, "MP"
    elif Type == "blade":
        bleedModifier = randint(1,5)
        if(missChance < 4):
            print "Your oppoents swings, but you dodge, and the enemy flies forward"
        else:
            print "Your opponents swings at you, the blade cutting through your skin"
            if (bleedModifier >= 4):
                playerHP = playerHP - ATK  - bleedModifier
                time.sleep(3)
                print "You take", ATK, "damage"
                time.sleep(2)
                print "Yikes! The blade cut deep into your skin, causing you to start bleeding out"
                time.sleep(4)
                print "Because you are bleeding out, you take an additional", bleedModifier, "damage"
                time.sleep(4)
                bleedCount = bleedCount + 1
                if(bleedCount > 5):
                    print "You begin to feel weary"
                    time.sleep(3)
                    print "The massive blood loss is making you feel dizzy and weak"
                    time.sleep(3)
                    print "You collpase, bleeding out onto the floor"
                    time.sleep(3)
                    youLose()
            else:
                playerHP = playerHP - ATK
                time.sleep(3)
                print "You take", ATK, "damage"
                time.sleep(2)
            print "You now have", playerHP, "HP and", playerMP, "MP"
    elif Type == "gun":
        organChance = randint(1,50)
        if (missChance < 4):
            print "You opponent shoots and misses"
        else:
            print "Your opponent fires, and a shot goes piercing through your body"
            if (organChance > 45):
                playerHP = playerHP - (ATK * 3)
                time.sleep(3)
                print "Critical Hit! You take 3x more damage because the shot pierced an organ"
                time.sleep(3)
                print "You take", ATK * 3, "damage"
            else:
                playerHP = playerHP - ATK
                time.sleep(3)
                print "You take", ATK, "damage"
                time.sleep(3)
            print "You now have", playerHP, "HP and", playerMP, "MP"
    playerTurn()

def playerTurn():
    global playerHP
    global playerMP
    global playerWeap
    global playerATK
    global HP
    global MP
    global ATK
    global lastSpot
    turnChoice = raw_input("Would you like to attack or heal up? ")
    if turnChoice == "attack":
        playerAttack()
    elif turnChoice == "heal":
        playerHeal()
        

def playerAttack():
    global playerHP
    global playerMP
    global playerWeap
    global playerATK
    global HP
    global MP
    global ATK
    global lastSpot
    randomCritGun = randint(1,15)
    randomCritKnife = randint(1,20)
    randomCritKnuck = randint(1,25)
    if playerWeap == "gun":
        playerATK = 4 *  randomCritGun
        if (playerHP <= 400):
            playerATK = playerATK / 2
        HP = HP - playerATK
        print "You fire a shot off on your opponent"
        time.sleep(3)
        print "You do", playerATK, "damage to your opponent"
        time.sleep(3)
        print "Your opponent is now at", HP, " health"
    elif playerWeap == "knife":
        playerATK = 3 * randomCritKnife
        if (playerHP <= 400):
            playerATK = playerATK / 2
        HP = HP - playerATK
        print "You slice at your opponent"
        time.sleep(4)
        print "You do", playerATK, "damage to your opponent"
        time.sleep(3)
        print "Your opponent is now at", HP, " health"
    elif playerWeap == "brass knuckles":
        playerATK = 2 * randomCritKnuck
        if (playerHP <= 400):
            playerATK = playerATK / 2
        HP = HP - playerATK
        print "You swing at your opponent with as much force as you can muster"
        time.sleep(4)
        print "You do", playerATK, " damage to your opponent"
        time.sleep(3)
        print "Your opponent is now at", HP, "health"
        time.sleep(2)
    if (HP <= 0):
        print "Your opponent falls to the ground, and just dies like a loser"
        time.sleep(4)
        if lastSpot == 1:
            afterAlley()
        elif lastSpot == 2:
            youWin()
    enemyAttack()

def playerHeal():
    global playerHP
    global playerMP
    global playerWeap
    global playerATK
    global HP
    global MP
    global ATK
    global lastSpot
    randomHealAmount = randint(1,100)
    playerHP = playerHP + randomHealAmount
    playerMP = playerMP - randomHealAmount
    time.sleep(2)
    print "You whip a chug jug from your pack and slup the heck out of it"
    time.sleep(4)
    print "You heal", randomHealAmount, "HP"
    enemyAttack()
    
            
def afterAlley():
    global lastSpot 
    print "You draw a face on your defeated enemy, reveling in their defeat"
    time.sleep(3)
    print "You check their body for some coins and/or weapons, and you stumble upon some V-Bucks"
    time.sleep(4)
    print "\"V-Bucks?\" you think. That's a forbidden currency"
    time.sleep(3)
    print "Suddenly, it hits you, why would Adolf Hitler want Shrek. For his power?"
    time.sleep(4)
    print "That can't be right, if anything using our master Führer Muños' power would bring better results."
    time.sleep(5)
    print "Unless, Adolf Hitler is the reincarnation of Shaggy"
    time.sleep(3)
    print "But how, wasn't he banished to the Ranch by the lords Dr. Phil and Shrek"
    time.sleep(4)
    print "Well, due to the rules of lazy plot writing, Shaggy found a way out of the ranch..."
    time.sleep(5)
    print "You draw the comparisons, Adolf Hitler is Shaggy."
    time.sleep(3)
    print "That explains the return of the V-Buck as currency and the capture of Shrek"
    time.sleep(4)
    print "Now, due to the rules of Newton's fourth law (A.K.A The Rule of Create Task Shortcuts)"
    time.sleep(4)
    print "I have to speed up this story, and so out of nowhere, you find yourself face to face with Hitler"
    time.sleep(4)
    print "He had popped into existence, ready to defeat you..."
    time.sleep(4)
    print "He appears to be a Level 5 Mafia Boss harnessing the power of a Level 25 Shrek"
    lastSpot = 2
    enemySpawn(5)
    

def youWin():
    print "OMG like you win and Shrek is now saved, lol thank you please give me an A on"
    print "the create task thank you I love you random AP grader (pls give me full marks)"
    time.sleep(10)
    titleCard()

def youLose():
    print "You lose lol"
    titleCard()
    
        
        
        
        
    
        
titleCard()
