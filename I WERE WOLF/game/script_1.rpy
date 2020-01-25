label scene1:

    # playing background music that loops

    play music "duck face.MP3" fadeout 1

    # dialogue line
    # shows character name and dialogue said by that person

    moshi "(sigh)"

    # shows background image

    scene bg house with fade

    "I sighed deeply leaning against the wall."
    "Even though the party is in the other side of the house, I can hear the rumble weirdly called music."
    "Oooh, I think my head is gonna explode real soon."
    "Wonder, how I ended up coming here?"
    "...okay, I DID GET an invitation from that girl, but still how?"

    # stops music with  2 second fade

    stop music fadeout 2
    scene bg black with fade

    "As I recall it was something like..."

    who "Oi! Teo!"

    play music "happy bgm.ogg"

    scene bg school with dissolve

    # shows character image with transition

    show ami normal with dissolve

    moshi "...hm? What it is, Yoshimoto-san?"
    "A cute looking girl with big breasts appeared in front of me."
    ami "I'm organising a party at my house next Saturday. You're coming, right?"
    moshi "That's so nice of you."

    show ami wideSmile

    ami "(smiles widely)"
    moshi "Of course, I'm not going."

    show ami irritated

    ami "(totally pissed off)"
    moshi "I'm going back to classroom then. Have fu-"

    # hide character image with transition

    hide ami irritated with dissolve

    "I felt someone's hand on my shoulder"

    show ami wideSmile with dissolve

    ami "...you see, if you reject my generous offer right now, there's a possibility of me accidentally asking third year stalker to take photos of you while changing clothes after PE lesson"
    moshi "Are you a pervert or what?"
    ami "...or having a shower..."
    moshi "Ugh, you really are one. But, wait, do you really think I will believe in your threats? You know, I would call you a fool if I weren't such a nice guy."
    "And then she casually showed me some photos."

    hide ami wideSmile with dissolve

    moshi "(le gasp)"
    "I took one of them from her. I could feel my hand slightly trembling."

    show ami wideSmile with dissolve

    ami "See? He's undoubtedly talented."
    moshi "That's immoral."

    show ami normal

    ami "Yeah. When we last talked he said that you were an extremely hard target and he wasn't able to chase you wearing less than pants and shirt."
    ami "I'm sure he'll accept my request and fulfill his duty as a school stalk... photographer."

    hide ami normal with dissolve

    "Calm down, Moshimitsu."
    "Calm.{w} Down."
    "I looked at myself in the photos. There were no more than two or three."
    "The other ones..."
    "Hm{w=1.0}.{w=1.0}.{w=1.0}.{w=2.0} Interesting..."
    moshi "So in other words..."

    show ami wideSmile with dissolve

    ami "Yeah~?"

    # shows choice menu
    # with choices player decides about the story and the ending of the game

    menu:

        # first choice

        "Say something mean about photos.":
            play sound "cartoon.mp3"
            show ami angry

            moshi "...your infamous hobby is collecting photos of half naked teenage boys and..."
            ami "Cut it out!{p=0.7}{nw}"
            "This time i obediently shut my mouth."
            "That must be really embarassing for a girl to say it aloud. I must respect her feelings. Kind of."
            hide ami angry with dissolve

            # incrementing a variable

            $ ami_points += 1

        # second choice

        "Whelp, better save it for myself, I guess.":
            "Actually I don't think it's so good to tease her.{w} She's a girl after all.{w} They're kinda sensitive.{w} She might even cry if I accused her of being pervert.{w} Or whatever."
            "Yeah, better remember it and save for later."
            "Who knows, maybe we'll be have {i}totall savage insult fight{/i} in the future or something."
            moshi "A-actually, nothing. I don't even know what I wanted to say anymore"

            show ami normal

            ami "Okay?"

            $ neutral_points += 1

            hide ami normal with dissolve


    "I looked down at the photos once again. There were some boys from our school. But one of them appeared more often."
    "He had blonde hair probably soft like a silk."
    "Fair skin that even porcelain dolls would envy him."
    "And those eyes... Distant and deep at the same time, light blue just like an arctic ice."
    "Everyone who says that he's not indecently handsome must be insane. That's why girls are crazy about him."

    # if-else statement

    if ami_points > 0:
        show ami angryBlush with dissolve
        ami "So, are you taking the risk or not?"
        "Yoshimoto said that angrily with madly red cheeks."
    else:
        show ami wideSmile with dissolve
        ami "So, are you taking the risk or not?"
        "Yoshimoto said that happily with confidence."

    "Looking at her, I pouted a little."
    moshi "I think I have no choice..."

    show ami normal

    ami "I knew you'd understand."
    moshi "...but ... Be sure Yoshi-kun will hear about you being madly in love with him."

    show ami wideSmile

    ami "Haha, that's nothing, you dummy. If you're coming at the party, then I'm fully satisf-"
    moshi "See ya later!"

    show ami shocked

    ami "W- Wha- Wait, what?!"

    hide ami shocked with dissolve

    play music "duck face.MP3" fadeout 1
    scene bg house with Dissolve(0.5)


jump scene2
