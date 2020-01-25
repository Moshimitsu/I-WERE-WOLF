label scene4:

    scene bg house with dissolve

    show ami wideSmile at slightlyRight with dissolve
    show akito normal at slightlyLeft with dissolve

    ami "Alright, now everyone is gone. Let's do this!"

    scene bg house with fade

    "We worked hard for over 40 minutes."
    "Those people sure are not taught how to clean after themselves!"
    "I was washing dishes when I felt someone patted me on shoulder."

    show ami normal at center with dissolve

    ami "Hi! How ya doing?"
    "I smiled at her ang focusing again in the work."
    moshi "I just have two more plates and that's all. Is there something else I can help?"

    show ami wideSmile

    ami "Actually, Akito and I have just finished our part, so everything is done now."

    show ami normal

    ami "Thanks..."

    "For a moment she looked like she wanted to say something."
    moshi "Yoshimoto...{w=1.5}{nw}"
    akito "Okay, guys, it's probably time to go home, don't you think?"

    show ami normal at slightlyRight with dissolve
    show akito normal at slightlyLeft with dissolve

    "I immediately shut my mouth when Ichikawa came."
    "What was that she wanted to say?..."
    akito "Are you finished?"
    "I put the last plate under the water and placed with other clean dishes."
    moshi "Yep. All done now."
    akito "So we'll be going now. Come here, poptart monster."
    "Well, actually..."

    menu:
        "Gimme a second":
            moshi "Gimme a second. I have to ask Yoshimoto about something."

            show ami shocked
            show akito thoughtful

            "Yoshimoto was kind of surprised. She clearly didn't expect that. Neither did I"
            akito "Okay. I'll be wainting in the hall."

            hide akito with dissolve
            show ami at center with dissolve

            ami "What is it?{w} Something wrong?"
            moshi "No, of course not! It's just that...{p}You wanted to say something earlier?"

            show ami normal

            "For a moment Yoshimoto lost all her usual confidence and she almost looked... shy?"
            ami "Well...{w} Actually..."
            moshi "Hm?"
            ami "Thanks..."
            moshi "No problem. It was fun helping you clean."

            "Yoshimoto looked in other direction, avoiding my gaze."

            ami "Thanks for coming here today..."

            hide ami with dissolve

            "And she stormed out of the room."

            $ ami_points += 1

        "Okay, let's go":
            "I dried hands with kitchen towel and stretched myself."

            moshi "Okay, let's go. It's already so late, better not waste anymore of Yoshimoto's time."

            show ami shocked

            ami "Uhm...{w} Thanks, guys!"
            akito "No problem, ma'am."

            hide ami with dissolve
            hide akito with dissolve

            $ neutral_points += 1

    # deciding about the ending through gathered points

    if ami_points == akito_points:
        jump neutralEnding
    if ami_points == 3:
        jump amiEnding
    if akito_points == 3:
        jump akitoEnding
    else:
        jump neutralEnding

# endings

label neutralEnding:

    "Akito and I quickly wore out jackets."

    show akito normal at center with dissolve

    akito "Bye, Yoshimoto! And thanks for the party."
    moshi "Yeah, thanks and bye!"

    hide akito with dissolve

    show ami normal at center with dissolve

    ami "Thanks, guys, for the help."
    akito "No problem!"

    scene bg black with dissolve

    "Ichikawa and I quickly parted and went our separate ways."
    "Even though we helped Yoshimoto, I still felt that the party was meaningless and a total waste of time."

    "Neutral ENDING \nTHE END"

    # returns to main screen

    return

label akitoEnding:

    "Ichikawa and I were getting ready when Yoshimoto came."

    show ami normal at center with dissolve

    ami "Thanks guys for the help."

    hide ami with dissolve
    show akito smile with dissolve

    akito "No problem. At least you can go to sleep at decent hour."

    hide akito with dissolve
    show ami wideSmile with dissolve

    ami "Ahaha, yeah, you have a point."
    moshi "Don't forget to take some rest."
    ami "Yep, don't worry, guys. I'll be a good girl and go to sleep when you leave."

    hide ami

    "We said goodbye to each other and Ichikawa and I went outside"

    scene bg black with dissolve
    show akito normal

    akito "It's ridiculous that the best part of the party was cleaning all this mess, don't you think?"
    moshi "Yeah, totally! Just hope Yoshimoto will be fine. She looked like a total shit."
    akito "Kind of."
    "We walked in silence for a while."
    akito "You know..."
    moshi "Huh?"
    akito "It was fun with you today."

    show akito smile

    moshi "Uhm... Thanks."
    akito "We could hang togheter more."
    "I was totally shocked. Ichikawa surprised me. I thought he cannot stand me at all."
    "I had no idea what to say."
    moshi "Uhm, yeah."
    akito "But try not to be a total moron next time."
    moshi "Oh, shut up, grumpsy prick!"

    hide akito with dissolve

    "Akito ENDING \nTHE END"

    return

label amiEnding:

    show akito normal at center with dissolve

    "Ichikawa was waiting for me in the hall already wearing jacket."
    akito "Hurry up. It's dangerous out there, we need to quickly come back."
    "I got ready and we were already going outside when Yoshimoto came."

    show ami normal at slightlyRight with dissolve
    show akito normal at slightlyLeft with dissolve

    ami "Moshimitsu, could you wait a little bit longer?"

    show akito thoughtful

    "I looked at her surprised. I had no idea why she wanted me to stay."
    akito "Okay, then I'm leaving."
    ami "Thanks again, Ichikawa."
    akito "No problem. Bye, guys."
    ami "Bye."
    moshi "Bye, grumpy."

    hide akito with dissolve
    show ami normal at center with dissolve

    "When Ichikawa left, I focused on Yoshimoto again."
    moshi "What is it, Yoshimoto?"

    scene bg house with fade
    show ami normal

    "Suddenly she came closer and gave me a peck on a cheeck."
    ami "I'm really happy you came."
    "She said that gently with faint blush on her cheeks."
    "I was totally shocked"
    ami "Do you wanna come over tomorrow?"
    "I felt my face turning red after hearing what she said. But it was... really nice this time."
    moshi "Uhm... Yeah"

    hide ami with dissolve

    "Ami ENDING \nTHE END"

    return
