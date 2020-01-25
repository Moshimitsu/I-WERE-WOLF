label scene3:

    scene bg house with dissolve

    "Room was filled with conversations and music. Everyone was laughing happily"
    "When we entered room, everyone greeted us with enthusiasm."

    who "What's up, boys!"

    show akito normal at slightlyLeft with dissolve
    show ami normal at slightlyRight with dissolve

    moshi "Oh.{w} It's you."

    show ami irritated

    ami "What do you mean \"Oh, it's you\" as if I just happened to be at {b}my own house{/b}?"
    moshi "Well, it's not actually yours, but your parents'..."

    # play sound
    # sounds doesn't loop

    play sound "punch.mp3"
    show bg house with hpunch
    play sound "roblox death sound.mp3"

    moshi "Ouch, it {i}hurt{/i}."
    ami "It was supposed to."
    moshi "You're cruel!"

    show akito thoughtful

    akito "And you have no life."
    moshi "You too?! I thought we are poptart buddies!"

    show ami wideSmile

    ami "{i}What{/i}-buddies?"

    show akito thoughtfulIrritated

    akito "Just shut up."
    moshi "Now you're embarassed? You should have been earlier when you lied to me, you frizkin' strawberry poptart!"

    show akito thoughtfulAngry

    akito "Oh, man..."
    ami "Oh, come on, Ichikawa. Don't tell me Moshimitsu isn't funny, right?"

    menu:
        "Is she making fun of me or what?":
            moshi "What do you mean, Yoshimoto?..."
            "I don't know why but what she told made me feel like an idiot."
            "Is she treating me as someone whose whole purpose is to entertain her?"

            show akito thoughtful

            akito "His sense of humour is kinda...{p}Unique."
            moshi "At least I have some, not like you, grumps."
            "I could feel his murderous glare towards me."

            $ neutral_points += 1

        "OF COURSE I AM, DUH-":
            moshi "OF COURSE I AM, DUH-"

            show akito thoughtfulIrritated
            show ami angryBlush

            "Akito looked confused.{p}Ami looked confused.{p}I felt confused."
            "I NEED TO COME UP WITH SOMETHING."
            "Got ya!... Haha... Ha..."

            show akito thoughtful

            akito "Yeah, you're right. Undoubtedly amazing."

            $ akito_points += 1

    moshi "Whatever! You were looking for us or wanted us for something?"

    show ami normal

    ami "I just wanted to check on both of you. Everyone is slowly getting ready to go out."
    "I checked the time. I was getting really late."
    ami "I thought it would be better if you also came back..."
    "Despite her smile she looked kinda sad or even... lifeless."
    "I wonder what make like this."

    menu:
        "She should take better care of herself.":
            "When I saw her last time, she was enthusiastic about this whole party."
            "Probably the whole organizing is more exhausting than I imagined."
            "No wonder. There are so many people that even I am fed up with all of this stuff."
            moshi "Yoshimoto, are you okay?"
            "She looked at me completely surprised."

            show ami shocked

            ami "What do you mean?"

            show akito normal

            akito "He has a point. You look like shit."

            show ami normal

            ami "Oh, it's nothing. I just had a lot of preparations for today and still have bunch of things to do when everyone will be gone."

            $ neutral_points += 1

        "She's still kinda cute...":

            "She was lost in thoughts and almost forgot about us."
            "It was funny that she was constantly moving her nose from side to side."
            "Or even cute, I would say."
            "I really do hope she's okay. It would be terrible if anything happened to her."

            moshi "You should really take some rest, silly."

            show ami shocked
            show akito shocked

            "Have I really just said that out loud?"
            "Crap."

            show akito thoughtful
            show ami normal

            ami "Don't worry, piggy-head. I'm a tough girl."
            akito "Yeah. Tough but silly."

            $ ami_points += 1

    show akito normal

    akito "We can stay and help you with cleaning when everyone goes."
    ami "Oh, you don't have to, I'll do fine by myself."
    "I impatiently waved a hand at her trying to make her stop talking."
    moshi "It's easy: we do the work, you just give out sweets. It's a deal."

    show akito thoughtful

    akito "This time I have to support what he says. Just let us clean the mess."
    "She looked at me, then at Ichikawa and finally sighed, giving up."
    akito "Fine, fine, just do your way."
    "I smiled at Ichikawa happily."
    "Since we're here, we can do something good."

    show ami normal

    ami "Okay, guys. If you stay, I'm going to see whether the house is still intact."

    hide ami with dissolve
    show akito normal at center with dissolve

    "And then she went somewhere."
    akito "..."
    moshi "..."
    akito "..."
    moshi "So..."
    akito "?"
    moshi "What about my poptarts you promised?"

    show akito thoughtfulIrritated

    akito "Oh God..."

    scene bg black with fade

    play sound "one eternity later.mp3"

    # pause the game for 2.5 seconds

    pause 2.5

jump scene4
