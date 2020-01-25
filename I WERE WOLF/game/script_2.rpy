label scene2:

    "Aah, that was wonderful."
    "Of course she would be terrified."
    "Yoshii-kun is ugly-as-hell boy in our year. Even I know about his existence."
    "But she deserved that in the end."
    "Anyway..."
    "I wanna go home!"

    scene bg house with fade

    who "Here you are."
    "I jumped a little.{w} That was surprising."
    "I looked up at the stranger."
    "...Speak of the devil."

    show akito normal with dissolve

    "Of course it's that blond Ichikawa guy."
    akito "Forgot your tongue or you're just being rude?"
    "Ah...{w} he's already pissing me off."

    moshi "Hi.{p} Go to hell."

    show akito thoughtfulAngry

    akito "Really gentle guy, I see."
    moshi "Sorry. I'm not the one who's disturbing others."

    show akito normal

    akito "Pffft. I'm not disturbing, only trying to start a casual conversation."
    moshi "Kidding me? I doubt you would want to talk to me with no reason."
    akito "Mhm, why?"
    "I sighed once again."
    moshi "What about you trying to casually talk with me the other day and leave me alone now?"

    show akito smile

    akito "A promise?"

    menu:
        "Jeez, whatever, just leave me alone now.":
            "It's not like we are going to be besties, so a teeny weeny lie cannot do any harm.{p} Right?"
            moshi "Absolutely. You have my word."
            show akito thoughtful

            $ neutral_points += 1

        "Why should I care about a stranger?":
            "Trying not to be noticed, I crossed fingers."
            moshi "Of course."
            akito "..."

            show akito thoughtfulIrritated

            $ akito_points += 1

    akito "You liar."
    "He gave me an uneasy feeling.{w} Crap."
    moshi "Hmpf. Okay, then. What's your bussiness here? I'm kind of busy."

    show akito mock

    ".{w=0.3}.{w=0.3}.{w=0.3} wow..."
    ".{w=0.3}.{w=0.3}.{w=0.3} awesome..."
    "I've never seen someone who can mock me this hard with his eyes only before..."
    "{p}Okay. {p}There were few times, but it's different level now."
    akito "I see."
    moshi "I'm busy wasting my time here! What do you want?"

    hide akito mock with dissolve

    akito "Actually..."
    moshi "Huh?"
    "He leaned against the wall next to me. I could feel his warmth through connected arms."
    "I was kinda embarassed that guy stood so close next to me when there was so much space."
    "... you know, it's not like the wall is mine only?"

    show akito thoughtful with dissolve

    akito "Me too."

    menu:
        "Tell a joke":
            moshi "... you mean, you're busy with your girlfriends?"

            show akito irritated

            akito "..."
            moshi "..."
            moshi "'Cause you're so popular and stuff...{w} Lots of people like you, get it?... {w}Haha...{w} ha...{w} hah..."
            "It was supposed to be a joke, dude."

            show akito thoughtfulIrritated

            akito "No"

            hide akito thoughtfulIrritated with dissolve

            "When I'd started to feel like a totally dumbest person on the world, I heard a calm voice."

            $ akito_points += 1

        "Or not?":
            "For a moment I thought it would be genius, I mean, {b}{i}GENIUS{/i}{/b} to make fun of him and his fangirls - cause he's so popular and whatever."
            "But considering I'm totally not in the mood I would only make fun of myself. Probably."
            "Better safe than sorry, they say!"
            "And then I heard his calm voice."

            $ neutral_points += 1

    show akito thoughtful with dissolve

    if akito_points == 2:
        akito "I don't care about those so called {i}girlfriends{/i}. They bore me. The whole party too. I just came simply because Yoshimoto invited me."
    else:
        akito "I don't care about the whole party. It bores me. I just came simply because Yoshimoto invited me."

    moshi "...e too..."

    show akito mock

    akito "What are you mumbling there?"
    moshi "... you see, I also came here *cough*... because of the invitation."
    "Blonde guy raised an eyebrow."
    akito "You were forced or what?"
    moshi "... kind of?"

    show akito thoughtfulIrritated

    akito "Pffft..."
    moshi "What?"

    show akito smile

    akito "Hahaha"
    "He burst into laughter. I looked at him in disbelief. How could he?"
    moshi "Hey, I really had no choice!... Kinda?"
    akito "Really? How weak minded are you?"
    moshi "I..."
    akito "Someone used ropes to bring you there or what?"
    "Of course he's making fun of me!"
    moshi "You! If you have no serious bussiness with me, then shove off!"

    show akito normal

    "Boy raised his eyebrows, but seemed to take my angry words to heart."
    akito "Wanna play a game?"
    moshi "What game?... Whatever. The answer is - nope."

    show akito smile

    akito "We can pretend to participate and have some poptarts while complaining..."
    moshi "Poptarts."

    show akito mock

    akito "Oh...?"
    moshi "You've said poptart, right? Why are we still sitting here?"
    akito "..."
    akito "I should've known that."

    hide  akito mock with dissolve

    "And this way we followed our twisted fate straight to hell."

    scene bg black with fade

jump scene3
