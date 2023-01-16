import random

#Declaring lists with accepted inputs
DECKSTRENGTH = ("Power", "Technical", "Defense")
EXTRASTYLE = ("fusion", "synchro", "xyz", "link", "random", "none")
MAINSTYLE = ("ritual", "pendulum", "random", "none")
ATTRIBUTE = ("dark", "earth", "fire", "light", "water","wind", "mixed", "random")
SERIES = ("dm", "gx", "5ds", "zexal", "arc-v", "vrains", "none", "random")
DECKSIZE = ("consistency", "options", "random", "none")

print(f"Welcome to the Yu-Gi-Oh! Deck Guide. We will random generate a deck theme based on your inputs.")

#deck playstyle is random set here - this is the only element out of the user's control
user_deck_style = "".join(random.choice(DECKSTRENGTH))

#these print messages are for testing purposes only. they are commented out otherwise
#print(user_deck_style)

#validation for user inputs. ignores case and checks if user input is in the list before continuing onto the next question
while True:
    try:
        user_main_style = input(f"\nPlease select a main deck gimmick - Ritual, Pendulum, Random, or none: ")
    except ValueError:
        print("\nInvalid choice. Please type only Ritual, Pendulum, Random, or none: ")
        continue
    if user_main_style.casefold() in MAINSTYLE:
        break
    else:
        print("\nInvalid choice. Please type only Ritual, Pendulum, Random, or none: ")

#where applicable, random selectio nis used. weights are added to ensure random itself isn't picked again
if user_main_style.casefold() == "random":
    user_main_style = "".join(random.choices(MAINSTYLE, weights=(50, 50, 0, 50), k=1))

if user_main_style.casefold() == "none":
    user_main_style = ""

#print(user_main_style)

while True:
    try:
        user_extra_style = input(f"\nPlease select a extra deck type: Fusion, Synchro, XYZ, Link, Random, or none: ")
    except ValueError:
        print("\nInvalid choice. Please type only Fusion, Synchro, XYZ, Link, random, or none: ")
        continue
    if user_extra_style.casefold() in EXTRASTYLE:
        break
    else:
        print("\nInvalid choice. Please type only Fusion, Synchro, XYZ, Link, Random, or none: ")

if user_extra_style.casefold() == "random":
    user_extra_style = "".join(random.choices(EXTRASTYLE, weights=(50, 50, 50, 50, 0, 50), k=1))

#ensures the extra deck part of the final output is gramatically correct
if user_extra_style.casefold() == "none":
    indefinite = "an"
elif user_extra_style.casefold() == "xyz":
    indefinite = "an"
elif user_extra_style.casefold() == "fusion":
    indefinite = "a"
elif user_extra_style.casefold() == "synchro":
    indefinite = "a"
elif user_extra_style.casefold() == "link":
    indefinite = "a"

if user_extra_style.casefold() == "none":
    user_extra_style = "empty"

#print(user_extra_style)

while True:
    try:
        user_deck_size = input(f"\nWhat do you prefer in a main deck? - Consistency, Options, or Random: ")
    except ValueError:
        print("\nInvalid choice. Please type only Consistency, Options, or Random: ")
        continue
    if user_deck_size.casefold() in DECKSIZE:
        break
    else:
        print("\nInvalid choice. Please type only Consistency, Options, or Random: ")

#player decks must have min.40 and max.60 cards, or anything inbetween
if user_deck_size.casefold() == "consistency":
    user_deck_size = "40"
elif user_deck_size.casefold() == "options":
    user_deck_size = "60"
elif user_deck_size.casefold() == "random":
    ri = random.randint(40, 60)
    user_deck_size = str(ri)

#print(user_deck_size)

while True:
    try:
        user_fave_attribute = input(f"\nPlease select a preffered Attribute: DARK, EARTH, FIRE, LIGHT, WATER, WIND, Mixed, or Random: ")
    except ValueError:
        print("\nInvalid choice. Please type only DARK, EARTH, FIRE, LIGHT, WATER, WIND, Mixed, or Random: ")
        continue
    if user_fave_attribute.casefold() in ATTRIBUTE:
        break
    else:
        print("\nInvalid choice. Please type only DARK, EARTH, FIRE, LIGHT, WATER, WIND, Mixed, or Random: ")

if user_fave_attribute.casefold() == "random":
    user_fave_attribute = "".join(random.choices(ATTRIBUTE, weights=(50,50,50,50,50,50,50,0)))

#print(user_fave_attribute)

while True:
    try:
        user_fave_series = input(f"\nFinally, are you a fan of the anime? \nIf so, pick your favorite series from the following:\nDM, GX, 5Ds, Zexal, Arc-V, Vrains\n\nIf you don't like the anime, type none. If you have no preference, type Random: \n")
    except ValueError:
        print("\nInvalid choice. Please don't make me type that all out again :(")
        continue
    if user_fave_series.casefold() in SERIES:
        break
    else:
        print("\nInvalid choice. Please don't make me type that all out again :(")

if user_fave_series.casefold() == "random":
    user_fave_series = "".join(random.choices(SERIES, weights=(50, 50, 50, 50, 50, 50, 50, 0), k=1))

#print(user_fave_series)

#attribute and series are used together to determine what archtype the deck focuses on
if user_fave_series.casefold().casefold() == "dm":
    if user_fave_attribute.casefold() == "light":
        DECKTHEME = ("Face Card Knights", "Blue-Eyes", "Silent Swordsman", "Silent Magician", "LIGHT Fairy/Téa Gardner", "Valkyrie", "A-to-Z")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "earth":
        DECKTHEME = ("Magnet Warrior", "Orgoth Dice", "Amazoness", "Battleguard", "Exchange of the Spirit/Ishizu Ishtar", "Gadget", "Buster Blader")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "wind":
        user_deck_theme = "Harpie Lady"
    elif user_fave_attribute.casefold() == "fire":
        user_deck_theme = "Jurrac/Rex Raptor fire Dinosaur"
    elif user_fave_attribute.casefold() == "water":
        user_deck_theme = "Umi Control/Mako Tsunami"
    elif user_fave_attribute.casefold() == "dark":
        DECKTHEME = ("Dark Magician", "Red-Eyes", "Eyes Restrict", "Jinzo", "Exodia", "dark Machine/Bandit Keith", "dark Zombie/Bonz", "dark Fiend/PaniK", "Destiny Board")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "mixed":
        DECKTHEME = ("Insect/Weevil Underwood", "Dinosaur/Rex Raptor", "Chaos", "Black Luster Soldier", "Joey Wheeler", "Toon", "Slifer the Sky Dragon", "Obelisk the Tormentor", "The Winged Dragon of Ra", "Guardian")
        user_deck_theme = random.choice(DECKTHEME)

if user_fave_series.casefold() == "gx":
    if user_fave_attribute.casefold() == "light":
        DECKTHEME = ("Arcana Force", "Cyber Angel", "Cyber Dragon", "Ojama", "A-to-Z")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "earth":
        DECKTHEME = ("Ancient Gear", "Fossil", "Koala", "Venom")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "wind":
        user_deck_theme = "Armed Dragon"
    elif user_fave_attribute.casefold() == "fire":
        DECKTHEME = ("Volcanic", "Horus")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "water":
        DECKTHEME = ("Ice Barrier", "Frog", "Water Dragon")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "dark":
        DECKTHEME = ("Cyberdark", "Dark Scorpion", "Dark World", "Destiny HERO", "Vampire", "Archfiend", "Gravekeeper's")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "mixed":
        DECKTHEME = ("HERO", "Vehicroid", "B.E.S", "Mill", "Monarchs")
        user_deck_theme = random.choice(DECKTHEME)

if user_fave_series.casefold() == "5ds":
    if user_fave_attribute.casefold() == "light":
        DECKTHEME = ("Watt", "Batteryman")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "earth":
        DECKTHEME = ("Iron Chain", "Goyo", "Machina", "Naturia")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "wind":
        user_deck_theme = "Stardust Dragon"
    elif user_fave_attribute.casefold() == "fire":
        DECKTHEME = ("Flamvell", "Rose Dragon")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "water":
        user_deck_theme = "Trishula Ice Barriers"
    elif user_fave_attribute.casefold() == "dark":
        DECKTHEME = ("Infernity", "Blackwing", "Reptilliane", "Ally of Justice")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "mixed":
        DECKTHEME = ("Fortune Lady", "Junk","Synchron", "Earthbound Immortals", "Signer Dragons", "Morphtronic", "Resonators", "Malefic", "Aesir/Nordic", "T.G", "Noble Knights")
        user_deck_theme = random.choice(DECKTHEME)

if user_fave_series.casefold() == "zexal":
    if user_fave_attribute.casefold() == "light":
        DECKTHEME = ("Utopia / ZS", "Photon/Galaxy-Eyes", "Numeron", "Star Seraph")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "earth":
        DECKTHEME = ("Onomat", "Heroic", "Raccoon")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "wind":
        DECKTHEME = ("Mecha Phantom Beasts")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "fire":
        DECKTHEME = ("Battlin' Boxer", "Fire Fist")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "water":
        DECKTHEME = ("Shark", "Dinomist")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "dark":
        DECKTHEME = ("Gimmick Puppet", "Umbral Horror", "Malicevorous", "Gorgonic")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "mixed":
        DECKTHEME = ("Heraldic", "Hand")
        user_deck_theme = random.choice(DECKTHEME)

if user_fave_series.casefold() == "arc-v":
    if user_fave_attribute.casefold() == "light":
        DECKTHEME = ("Constellar", "Melodius")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "earth":
        DECKTHEME = ("Gem-Knight", "X-Saber")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "wind":
        DECKTHEME = ("Yosenju", "Speedroid", "Windwitch", "Lyrilusc", "Battlewasp")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "fire":
        DECKTHEME = ("Igknight", "Metalfoes")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "water":
        DECKTHEME = ("Greydle")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "dark":
        DECKTHEME = ("Flower Cardian", "Lunalight","Predaplant", "Raidraptor", "The Phantom Knights")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "mixed":
        DECKTHEME = ("Dimension Dragons", "pendulum Magicians", "D/D/D", "Superheavy Samurai")
        user_deck_theme = random.choice(DECKTHEME)

if user_fave_series.casefold() == "vrains":
    if user_fave_attribute.casefold() == "light":
        DECKTHEME = ("Trickstar")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "earth":
        DECKTHEME = ("Gouki")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "wind":
        DECKTHEME = ("Simorgh")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "fire":
        DECKTHEME = ("Salamangreat")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "water":
        DECKTHEME = ("Marincess", "Crystron")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "dark":
        DECKTHEME = ("Codebreaker", "Tindangle", "Rokket/Borrel")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "mixed":
        DECKTHEME = ("@ignister", "Altergeist", "Dinowrestler", "Code Talker")
        user_deck_theme = random.choice(DECKTHEME)

if user_fave_series.casefold() == "none":
    if user_fave_attribute.casefold() == "light":
        DECKTHEME = ("Fabled", "Hieratic", "tellarknight", "Lightray", "Artifact", "Eldlich")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "earth":
        DECKTHEME = ("Karakuri", "Madolche", "Megalith", "G Golem", "Qli", "Scrap", "Subterror", "Traptrix", "Zoodiac")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "wind":
        DECKTHEME = ("Dragunity", "Gusto", "ritual Beasts", "Floowandereeze")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "fire":
        DECKTHEME = ("Laval", "Shiranui", "Fire King")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "water":
        DECKTHEME = ("Atlantean", "Mermail", "Gishki", "Nekroz", "Paleozoic","Ghoti")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "dark":
        DECKTHEME = ("Darklord", "Danger!", "Inzektor", "Tearalament")
        user_deck_theme = random.choice(DECKTHEME)
    elif user_fave_attribute.casefold() == "mixed":
        DECKTHEME = ("(Twi)Lightsworn", "Chaos", "Six Samurai", "Mystic Mine", "Runick")
        user_deck_theme = random.choice(DECKTHEME)

#print(user_deck_theme)

#final output capitalizes the found results and concatenates them all together
print ("\nYour deck will be a " + user_deck_style.capitalize() + " focused, " + user_deck_size + " card " + user_main_style.capitalize() + " " + user_deck_theme + " deck with " + indefinite + " " + user_extra_style.capitalize() + " extra deck.")
