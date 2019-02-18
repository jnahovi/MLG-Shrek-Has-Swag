from time import *
from random import *
import os,sys
import time
import random
import webbrowser

def setup():
    global name
    global rep
    global HP
    global MP
    global finalRep
    global playerHealth
    global playerMagic
    global fleeTimes
    global villagerHelped
    villagerHelped = 0
    fleeTimes = 0
    HP = randint(30,50)
    MP = randint(30,50)
    playerHealth = HP
    playerMagic = MP
    rep = 0
    finalRep = rep
    print "First: A writ of passage. To be able to play MLG Shrek Has Swag Python"
    print "edition, you must make an MLG FaZe worthy name"
    time.sleep(4)
    name = raw_input ("What is your FaZe clan name? ")
    time.sleep(1)
    print "What's up, %s. Ready to be an MLG Pro?" % name
    time.sleep(3)
    weap()

def weap():
    global weapDam
    global chooseYourWeapon
    chooseYourWeapon = raw_input("What weapon would you like to wake up with? A quickscoper, a dorito, or a mountain dew bottle? ")
    randomWeapon = ["dorito", "quickscoper", "mountain dew bottle"]
    if chooseYourWeapon == "quickscoper":
        print "You have chosen the quickscoper m8. The quickscoper is only for MLG Pros with the lowest and highest possible damage values. Are you MLG pro enough to use it?"
        time.sleep(4)
        first_choice()
    elif chooseYourWeapon == "dorito":
        print "You have chosen the dorito m8. You are dummy accurate probably because you're a lil bitch ass. You are more consistent, but lose out on damage. Are you MLG Pro enough to use it?"
        time.sleep(4)
        first_choice()
    elif chooseYourWeapon == "mountain dew bottle":
        print "You do the lowest damage, but always hit you cheeky bastard... I would say are you MLG Pro enough to use it, but you always hit so damn it all..."
        time.sleep(4)
        first_choice()
    else:
        print "I don't know what the fuck you mean m8. Because you are dumb as fuck, I'll choose for you m8"
        shuffle(randomWeapon)
        time.sleep(3)
        chooseYourWeapon = randomWeapon[0]
        print "Your weapon is a" , chooseYourWeapon , "m8"
        time.sleep(2)
        first_choice()

def first_choice():
    global HP
    global MP
    global playerHealth
    global playerMagic
    global finalRep
    global rep
    global firstz_choice
    print "You wake with " + str(playerHealth) + " health and " + str(playerMagic) + " magic points"
    time.sleep(2)
    print "You currently have " + str(rep) + " reputation among Faze Clan"
    time.sleep(2)
    print "You have equipped the" , chooseYourWeapon
    time.sleep(2)
    print "In your sweaty non-MlG nerd gaming lounge, everybody is playing Vortnite, a"
    print "Harry Potter themed rip-off of PubG. You must find Faze clan. Would you like"
    print "to take the country road home to West Virginia, left to Shrek's swamp, or right"
    print "to Donald Trump's House"
    time.sleep(4)
    firstz_choice = raw_input("Where would you like to go? ")
    print "You go %s..." % firstz_choice
    time.sleep(3)
    if firstz_choice == "right":
        deathfromright()
    elif firstz_choice == "left":
        print "After a bit of walking, you enter a village in Shrek's Swamp..."
        time.sleep(2)
        NPCRandom()
    elif firstz_choice == "forward":
        print "After walking down the country road taking you home to West Virginia, you come across a village named Megaton..."
        time.sleep(2)
        NPCRandom()
    
def deathfromright():
    print "You travel to Donald Trump's house with " + str(playerHealth) + " HP"
    time.sleep(3)
    print "Once you arrive, you threaten to nuke Trump's sorry azz because he's not MLG"
    print "Suddenly, Trump uses his sanctions power, making you unable to move... for some reason"
    time.sleep(3)
    print "Because you didn't call him MLG, Trump decided to nuke your sorry ass"
    time.sleep(2)
    print "Sorry %s, you couldn't make it to faze clan" % name
    time.sleep(2)
    setup()

def NPCRandom():
    global NPCResponces
    global NPCNames
    global NPCNameChoices
    global rep
    NPCResponces = ["Hello Traveler, could you help me with something? ", "Are you from this village? Could you help me? ", "Please traveler, I desperately need your help! Can you help me? "]
    NPCNameChoices = ["FaZe Banks", "FaZe Danks", "FaZe Dave", "FaZe Rug", "FaZe Despacito", "FaZe Apex", "FaZe Rain", "FaZe Blaziken", "FaZe Kay", "FaZe iDubbz", "FaZe Ligma", "FaZe Fonsi"]
    random.shuffle(NPCResponces)
    random.shuffle(NPCNameChoices)
    NPCNames = NPCNameChoices[0]
    print "A villager named", NPCNames , "greets you..."
    time.sleep(2)
    helpChoice = raw_input(NPCResponces[0])
    if helpChoice == "yes":
        rep = rep + 5
        print "Thank you traveler, here's what I need you to do..."
        time.sleep(3)
        print "Because you agreed to help" , NPCNames, ", your reputation is now " + str(rep)
        time.sleep(3)
        startQuest()
    elif helpChoice == "no":
        rep = rep - 2
        print "That's a shame, I guess I'll find another MLG God to help"
        time.sleep(3)
        print "Because you are a n00b and didn't help" , NPCNames, "your rep is now " + str(rep)
        time.sleep(3) 
        retryOption = raw_input("Would you like to help another villager? ")
        if retryOption == "yes":
            NPCNameChoices.remove(NPCNameChoices[0])
            NPCRandom()
        if retryOption == "no":
            print "Because you are being a lil bitch, you must restart the game %s, maybe next time you won't be such a lil bitch"
            setup()

def startQuest():
    global NPCQuests
    global EnemyNames
    global direction
    global item
    global Enemy
    global Item
    global rep
    global NPCNameChoices
    EnemyNames = ["Aydi The Bulldog", "Aarry Ballen", "Adam Sandler", "MLGQuickscopeGod", "Ali-A", "Jake Paul", "KSI", "Xx_YoloSwag_xX", "Kanye West", "Cillary Hlinton", "Xx_420BlazeGodYurMom_xX", "Xx_CODPro_xX"]
    direction = ["north", "east", "west", "south"]
    item = ["sniper.", "blunt.", "MAGA hat.", "Chillary Clinton Mug.", "Snoop Dogg Mask."]
    shuffle(EnemyNames)
    shuffle(direction)
    shuffle(item)
    Enemy = EnemyNames[0]
    Item = item[0]
    Direction = direction[0]
    NPCQuests = ["You see, I was quickscoping some noobs, when an unknown entity took something of mine and ran away. I need you to find my item and kill who took it. ", "So you see, I was chilling in Cedar Rapids when some lil ass bitch took my shit. You need to get that shit back for me bro? "]
    shuffle(NPCQuests)
    randomQuest = NPCQuests[0]
    print randomQuest
    time.sleep(6)
    print "If I had to guess who or what took it, I would say" , Enemy,  "took it. I would be careful if I were you. He went" , Direction , "with my" , Item
    time.sleep(5)
    acceptQuests = raw_input("Do you accept the NPC's quest? ")
    if acceptQuests == "yes":
        print "You begin heading" ,Direction, "to find the crook that stole" , NPCNames, "'s" , Item ,".."
        time.sleep(3)
        EnemyAI()
    if acceptQuests == "no":
        print "Oh well then, guess your not MLG enough m8"
        rep = rep - 5
        time.sleep(2)
        print "Why you being a lil bitch ass m8, you won't make it into FaZe Clan with that attitude."
        helpAgain = raw_input("Would you like to help another villager? ")
        if helpAgain == "yes":
            NPCRandom()
            NPCNameChoices.remove(NPCNameChoices[0])
        else:
            print "Because you are being such a lil bitch, you must restart the game you n00b"
            setup()
            
def enemyDefeat():
    global enemyDamage
    global enemyHP
    global possibleSetting
    global currentSetting
    global playerHealth
    global playerMagic
    global chooseYourWeapon
    global NPCNames
    global Item
    global Enemy
    global firstz_choice
    global setorRandom
    if chooseYourWeapon == "quickscoper":
        if (setorRandom == 0):
            print "After your death dealing 420blazing noscope m8, that lil bitch" , Enemy , "fell unconscious, dropping" , NPCNames, "'s" , Item
            time.sleep(3)
            print "Good job m8, you are on your way to being part of FaZe Clan."
            time.sleep(2)
            if firstz_choice == "left":
                print "Hey m9, you should return to that village in Shrek's Swamp, and give" , NPCNames, " his " , Item
                stg1Complete()
            elif firstz_choice =="forward":
                print "Hey m9, you should return to the village and give" , NPCNames, "his " , Item
                stg1Complete()
        if (setorRandom == 1):
            print "You continue on your way to the next village"
            NPCRandom()
    elif chooseYourWeapon == "dorito":
        if (setorRandom == 0):
            print "After your death dealing dorito throw m8, that lil bitch" , Enemy , "fell to the ground, dropping" , NPCNames, "'s" , Item
            time.sleep(3)
            print "Good job m8, you are on your way to being part of FaZe Clan."
            time.sleep(2)
            if firstz_choice == "left":
                print "Hey m9, you should return to that village in Shrek's Swamp, and give" , NPCNames, " his " , Item
                stg1Complete()
            elif firstz_choice =="forward":
                print "Hey m9, you should return to the village and give" , NPCNames, "his " , 	Item
                stg1Complete()
        if (setorRandom == 1):
            print "You continue on your way to the next village"
            NPCRandom()
    elif chooseYourWeapon == "mountain dew bottle":
        if (setorRandom == 0):
            print "After your death dealing strike with the mountain dew bottle m8, that lil bitch" , Enemy , " fell to the ground, dropping" , NPCNames, "'s" , Item
            time.sleep(3)
            print "Good job m8, you are on your way to being part of FaZe Clan."
            time.sleep(2)
            if firstz_choice == "left":
                print "Hey m9, you should return to that village in Shrek's Swamp, and give" , NPCNames, " his " , Item
                stg1Complete()
            elif firstz_choice =="forward":
                print "Hey m9, you should return to Megaton and give" , NPCNames, "his " , Item
                stg1Complete()
        if (setorRandom == 1):
            print "You continue onward to your next village"
            NPCRandom()

def fleeBattle():
    global rep
    global Enemy
    global fleeChance
    global engageorflee
    global fleeTimes
    global startfightDecision
    if engageorflee == "flee" or startfightDecision == "no":
        print "You begin to run away from " , Enemy
        time.sleep(2)
        fleeChance = randint (1,10)
        if (fleeChance <= 7):
            print "As you are fleeing, you trip on some asshole smoking his blunt. Because it took your fat ass so long to get up, " , Enemy, "caught up with you."
            fleeTimes = fleeTimes + 1
            time.sleep(3)
            enemyAttack()
        elif (fleeChance > 7):
            print "You flee from" ,Enemy, " and return to the village. Right away, the villagers begin to boo and shoo you away. You have failed your mission"
            rep = rep - 5
            time.sleep(2)
            print "You have lost 5 points of rep. You are now at " + str(rep)
            fleeDecision = raw_input("Would you like to try and help another villager? ")
            if fleeDecision == "yes":
                time.sleep(1)
                NPCRandom()
            else:
                print "Because you are being such a lil bitch, you have to restart, cause you'll never get into FaZe clan with that attitude boi"
                time.sleep(3)
                setup()

def youChoose():
    global enemyDamage
    global enemyHP
    global possibleSetting
    global currentSetting
    global playerHealth
    global playerMagic
    global chooseYourWeapon
    global weaponDamage
    global engageorflee
    global startfightDecision
    engageorflee = raw_input("Would you like to attack, flee, or heal? ")
    if engageorflee == "attack":
        if chooseYourWeapon == "quickscoper":
            possibleweaponDamage = [0, 0, 0, 0, 2, 3, 5, 13, 18, 28, 32, 50, 100]
            shuffle(possibleweaponDamage)
            weaponDamage = possibleweaponDamage[0]
            print "You quickscope " ,Enemy, "'s sorry ass. After your mad quickscope, you do " , weaponDamage, "damage"
            time.sleep(2)
            enemyHP = enemyHP - weaponDamage
            print Enemy, "now has " ,enemyHP, " HP"
            time.sleep(3)
            if (enemyHP > 0):
                enemyAttack()
            elif (enemyHP <= 0):
                enemyDefeat()
        elif chooseYourWeapon == "dorito":
            possibleweaponDamage = [0, 3, 5, 7]
            shuffle(possibleweaponDamage)
            weaponDamage = possibleweaponDamage[0]
            print "You throw a dorito at " ,Enemy, "'s sorry ass. After your attack, you do " , weaponDamage, "damage"
            time.sleep(2)
            enemyHP = enemyHP - weaponDamage
            print Enemy, "now has", enemyHP, "HP"
            time.sleep(3)
            if (enemyHP > 0):
                enemyAttack()
            elif (enemyHP <= 0):
                enemyDefeat()
        elif chooseYourWeapon == "mountain dew bottle":
            possibleweaponDamage = 3
            weaponDamage = 3
            print "You swing your bottle and hit " ,Enemy, "'s sorry ass. After your mad swing, you do " , weaponDamage, "damage"
            time.sleep(2)
            enemyHP = enemyHP - weaponDamage
            print Enemy, "now has", enemyHP, "HP"
            time.sleep(3)
            if (enemyHP > 0):
                enemyAttack()
            elif (enemyHP <= 0):
                enemyDefeat()
    elif engageorflee == "flee":
        startfightDecision = "no"
        fleeBattle()
    elif engageorflee == "heal":
        heal()

def supriseAttack():
    global enemyDamage
    global enemyHP
    global possibleSetting
    global currentSetting
    global playerHealth
    global playerMagic
    global chooseYourWeapon
    global weaponDamage
    global startfightDecision
    global engageorflee
    startfightDecision = raw_input("Would you like to engage? ")
    if startfightDecision == "yes":
        print "Because" , Enemy , "got the drop on you, he gets to strike"
        enemyDamage = randint(1,5)
        time.sleep(2)
        print Enemy, "has " , enemyHP, " HP"
        time.sleep(2)
        print Enemy, "swings his weapon at you, doing " , enemyDamage , "damage"
        time.sleep(3)
        playerHealth = playerHealth - enemyDamage
        print "You now have " + str(playerHealth) + " HP"
        time.sleep(2)
        youChoose()
    elif startfightDecision == "no":
        engageorflee = "flee"
        fleeBattle()


def EnemyAI():
    global enemyDamage
    global enemyHP
    global possibleSetting
    global currentSetting
    global playerHealth
    global playerMagic
    global chooseYourWeapon
    global weaponDamage
    global setorRandom
    possibleSetting = ["swampy area", "dry wasteland", "wetland", "destroyed village"]
    shuffle(possibleSetting)
    currentSetting = possibleSetting[0]
    print "You enter a " , currentSetting , "trying to look for" , Enemy
    time.sleep(3)
    print "That lil bitch stole " , NPCNames , "'s" , Item, "He'll pay for that m8"
    time.sleep(2)
    print "Suddenly, out of nowhere, " , Enemy , "lands in front of you, ready to take you down"
    time.sleep(2)
    enemyHP = randint(10,15)
    setorRandom = 0
    supriseAttack()


def enemyAttack():
    global enemyDamage
    global enemyHP
    global playerHealth
    global playerMagic
    enemyDamage = randint(1,5)
    print Enemy, "swings his weapon at you, doing" , enemyDamage, " damage"
    time.sleep(3)
    playerHealth = playerHealth - enemyDamage
    print "You now have ", str(playerHealth), "HP and" , playerMagic, " MP"
    time.sleep(2)
    youChoose()

def heal():
    global playerHealth
    global playerMagic
    healAmount = randint(3,7)
    if (playerMagic <= 7):
        print "You try to pull out your phone, but the battery died. You can no longer use the power of Shrek Has Swag"
        enemyAttack()
    elif (playerMagic >= 7):
        playerMagic = playerMagic - healAmount
        playerHealth = playerHealth + healAmount
        print "You pull out your iPhone and watch some MLG Shrek Has Swag. You have healed" , healAmount, " HP"
        time.sleep(2)
        print "Because you used the power of Shrek, you lose" , healAmount, " MP"
        time.sleep(2)
        print "You now have" , str(playerHealth),"HP and" , playerMagic, "MP"
        enemyAttack()

def stg1Complete():
    global enemyDamage
    global enemyHP
    global possibleSetting
    global currentSetting
    global playerHealth
    global playerMagic
    global chooseYourWeapon
    global NPCNames
    global Item
    global Enemy
    global firstz_quest
    global rep
    global NPCNameChoices
    global EnemyNames
    global fleeTimes
    global villagerHelped
    time.sleep(2)
    print "You return to the village with" , NPCNames, "'s" , Item
    time.sleep(2)
    print "You walk up to" ,NPCNames, " and present him his" , Item , NPCNames, " says..."
    time.sleep(2)
    if (fleeTimes == 0):
        print "I'm very impressed traveler, sources told me you didn't try to flee once"
        rep = rep + 5
        time.sleep(2)
        print "You gain 5 more reputation points among FaZe Clan"
        time.sleep(2)
        print "Your rep among FaZe clan is now" , str(rep)
        time.sleep(3)
        print "You currently have" , playerHealth , "HP and" , playerMagic , "MP"
        time.sleep(2)
        NPCNameChoices.remove(NPCNameChoices[0])
        EnemyNames.remove(EnemyNames[0])
        villagerHelped = villagerHelped + 1
        randomStage()
    if (fleeTimes > 0):
        rep = rep + 5 - fleeTimes
        print "Thank you traveler for your help, but my sources tell me you tried to flee the battle. That's not very MLG traveler. Makes it a tad harder to get into FaZe Clan m8."
        time.sleep(2)
        print "You would usually recieve 5 rep points among FaZe Clan for succeeding, but because you fled, " , fleeTimes, "times, you only recieve", rep + 5 - fleeTimes, "rep points among FaZe Clan"
        time.sleep(2)
        print "Your rep among FaZe clan is now" , str(rep)
        time.sleep(3)
        print "You currently have, " , playerHealth , "HP and" , playerMagic , "MP"
        time.sleep(2)
        NPCNameChoices.remove(NPCNameChoices[0])
        EnemyNames.remove(EnemyNames[0])
        randomStage()
    
def randomStage():
    global stayorleave
    global villagerHelped
    time.sleep(2)
    if (villagerHelped == 1):
        print "You have a few options now that you have put yourself on the map"
        time.sleep(2)
        print "You could continue to help villagers here, or find directions to the next village?"
        time.sleep(2)
        stayorleave = raw_input("Would you like to ask for directions to the nearest village or help another villager here? ")
        if stayorleave == "directions":
            checkRep()
        elif stayorleave == "villager":
            checkRep()
    elif (villagerHelped > 1):
        print "Because you have helped another villager, you could either find directions to the nearest village or help another villager here?"
        stayorleave = raw_input("Would you like to ask for directions to the nearest village or help another villager here? ")
        if stayorleave == "directions":
            checkRep()
        elif stayorleave == "villager":
            checkRep()

def checkRep():
    global rep
    global stayorleave
    global name
    if (rep >= 50):
        time.sleep(2)
        print "Right before you head towards your next objective, a big fag boi in a thicc Shrek costume hands you a letter"
        time.sleep(3)
        print "You begin to open the letter, but it seems that it's been shut with dried mountain dew"
        time.sleep(2)
        print "After spending 30 fucking minutes prying at the letter with a dorito, the letter finally opens. It says..."
        time.sleep(3)
        print "What up %s. We are FaZe clan m8. We think that you are MLG enough to join us. Go to our lounge located in COD Land, and ask to speak with FaZe Flanks. Then, you can be well on your way to joining us m8." % name
        time.sleep(5)
        print "Right away, after asking for directions, you head to COD Land..."
        time.sleep(2)
    if (rep < 50):
        if stayorleave == "villager":
            NPCRandom()
        elif stayorleave == "directions":
            newvilDirections()

def newvilDirections():
    global compass
    global newrandomVil
    global randomvil1
    global randomvil2
    global randomvil3
    global randomvil4
    global cardinal1
    global cardinal2
    global cardinal3
    global cardinal4
    global randomEncounterChance
    newrandomVil = ["Hugh Mungus-ville", "Trump-ville", "Cedar Rapids", "Clint Hill-ville", "Whiterun", "Anvil", "Kvatch", "Winterhold", "Morthal", "Solitude", "Polly", "Sublime", "Bruma", "Riften", "Riverwood", "Falkreath", "Bravil", "Cheydinhal", "Skingrad", "Leyawiin", "Chrorrol", "Markarth", "Applewatch", "Dawnstar"]
    shuffle(newrandomVil)
    randomvil1 = newrandomVil[0]
    randomvil2 = newrandomVil[1]
    randomvil3 = newrandomVil[2]
    randomvil4 = newrandomVil[3]
    compass = ["north", "south", "west", "east"]
    shuffle(compass)
    cardinal1 = compass[0]
    cardinal2 = compass[1]
    cardinal3 = compass[2]
    cardinal4 = compass[3]
    time.sleep(1)
    print "You walk inside a map shop, and ask the person behind the counter for the nearest village locations. The owner says..."
    time.sleep(3)
    print "Well there are quite a few cities nearby."
    time.sleep(2)
    print "To the", cardinal1, "there's the village named" , randomvil1
    time.sleep(2)
    print "To the", cardinal2, "there's the village called" , randomvil2
    time.sleep(2)
    print "To the", cardinal3, "there's the village named" , randomvil3
    time.sleep(2)
    print "To the", cardinal4, "there's the village called" , randomvil4
    time.sleep(2)
    travelnewVillage = raw_input("What direction would you like to travel? ")
    if (travelnewVillage == cardinal1):
        time.sleep(2)
        print "You begin to head out of the shop. Once you leave, you begin to travel" , cardinal1, "toward" , randomvil1
        time.sleep(2)
        randomEncounterChance = randint(0,30)
        if (randomEncounterChance > 10):
            randomEncounter()
        else:
           print "You arrive at " , randomvil1
           time.sleep(2)
           NPCRandom()
    elif (travelnewVillage == cardinal2):
        time.sleep(2)
        print "You begin to head out of the shop. Once you leave, you begin to travel" , cardinal2, "toward" , randomvil2
        time.sleep(2)
        randomEncounterChance = randint(0,30)
        if (randomEncounterChance > 10):
            randomEncounter()
        else:
           print "You arrive at " , randomvil2
           time.sleep(2)
           NPCRandom()
    elif (travelnewVillage == cardinal3):
        time.sleep(2)
        print "You begin to head out of the shop. Once you leave, you begin to travel" , cardinal3, "toward" , randomvil3
        time.sleep(2)
        randomEncounterChance = randint(0,30)
        if (randomEncounterChance > 10):
            randomEncounter()
        else:
           print "You arrive at " , randomvil3
           time.sleep(2)
           NPCRandom()
    elif (travelnewVillage == cardinal4):
        time.sleep(2)
        print "You begin to head out of the shop. Once you leave, you begin to travel" , cardinal4, "toward" , randomvil4
        time.sleep(2)
        randomEncounterChance = randint(0,30)
        if (randomEncounterChance > 10):
            randomEncounter()
        else:
           print "You arrive at " , randomvil4
           time.sleep(2)
           NPCRandom

def randomEncounter():
    global EnemyNames
    global direction
    global item
    global Enemy
    global Item
    global rep
    global NPCNameChoices
    global setorRandom
    global enemyHP
    shuffle(EnemyNames)
    Enemy = EnemyNames[1]
    print "As you are travelling to your next village " , Enemy, "jumps right in front of you, ready to take you down"
    time.sleep(2)
    enemyHP = randint(5,10)
    setorRandom = 1
    supriseAttack()
 
setup()

    
