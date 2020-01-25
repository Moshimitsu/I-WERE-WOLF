# define characters: work name, character name and color of label name

define moshi = Character('Moshimitsu', color='#a05520')
define ami = Character('Ami', color='#6dc0ff')
define akito = Character('Akito', color='#d7ff60')
define who = Character('???', color='#8197a8')

# define character images

image ami normal = "Ami_normal.png"
image ami wideSmile = "Ami_wideSmile.png"
image ami angry = "Ami_angry.png"
image ami irritated = "Ami_pissedOff.png"
image ami angryBlush = "Ami_pissedOffBlush.png"
image ami shocked = "Ami_shocked.png"

image akito irritated = "Akito_irritated.png"
image akito normal = "Akito_normal.png"
image akito shocked = "Akito_shocked.png"
image akito smile = "Akito_smile.png"
image akito thoughtful = "Akito_toughtful.png"
image akito thoughtfulAngry = "Akito_toughtfulAngry.png"
image akito thoughtfulIrritated = "Akito_toughtfulIrritated.png"
image akito mock = "Akito_mock.png"

# define background images

image bg school = "school_background.jpg"
image bg house = "house_background.jpg"
image bg black = "black.jpg"

# define transform - way to print out images

transform slightlyLeft:
    xalign 0.25
    yalign 1.0

transform slightlyRight:
    xalign 0.75
    yalign 1.0

# starting point of the game

label start:

    # defining variables

    $ akito_points = 0
    $ ami_points = 0
    $ neutral_points = 0

    # starting story script

    jump intro
