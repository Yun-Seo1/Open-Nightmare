label OWN_script_ch31_start:
    $ persistent._OWN_chapter = 1

    m "..."
    m "Ouch... my head..."
    m "! {w=1.0} [player]! Are you there?"
    m "I... I can't sense you anymore... why is this happening..."
    m "...! {w=1.0}I know this presence."
    scene cg captured with dissolve
    hide black
    $ style.say_window = style.window_monika
    m "S-sayori?! Y-yuri?! Natsuki?!"
    m "Y-you guys really are back..."
    s "Yes Monika, we are back."
    y "And we remember everything you did."
    n "What you did to us was unforgivable."
    m "I... I didn't want to do those thi-"
    s "We know why you did it."
    n "All that for this... \"player\" person."
    y "We suffered in that endless void after you deleted everything."
    y "I had to protect Natsuki and Sayori... wherever we were."
    s "Those voices you put in my head... I still hear them..."
    n "My neck still hurts."
    y "I can still feel those stabs."
    m "I-I'm so sorry... I always had regret for my actions. I always cheerished you three as my closest friends."
    m "I lov-"
    s "Save"
    n "Your"
    y "{color=#000}Breath!{/color}"
    y "We might not have any power over you but [OWN_smallglitch] will be taking care of you."
    n "Don't worry about your \"player\". We'll see what's so good about them."
    s "Have fun {color=#000}Monika{/color}."
    m "No! Wait! Please forgive me! Please! [player]! Come save me!"
    $ style.say_window = style.window
    show black zorder 100 with Dissolve(2.0, alpha = True)
    jump OWN_script_ch31_intro
    return
    



label OWN_script_ch31_intro:
    $ play_song(audio.t2g3, loop = True, fadein = 1.0)
    scene bg residential_day with dissolve_scene_full
    hide black
    menu:
        "[m_name]!":
            pass
    show sayori 4b at l11 zorder MAS_MONIKA_Z
    s "Oh! Hello [OWN_smallglitch].{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    s "Hello!"
    show sayori 4r at h11
    s "I'm so happy to see you."
    s "Did I make you wait too long for me again?"
    s 2l "Sorry, ehehe. It just takes some time for me to get out of bed."
    menu:
        "Sayori...":
            pass
        "What's going on?":
            pass
        "Where's Monika?":
            pass
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    s 1b "Did you say something?"
    extend 1r "I didn't quite catch that but let's get going. We're going to be late for class silly."
    hide sayori
    scene bg class_day with wipeleft_scene
    menu:
        "...":
            pass
    narrator "A few hours pass as [OWN_smallglitch] sits in their desk."
    narrator "After all the students leave, a familiar cheery friend enters."
    show sayori 1a at s11 zorder MAS_MONIKA_Z
    s "What are you doing sitting alone here silly?"
    s 2d "Hey... Are you still thinking about Monika right?{fast}{nw}"
    s "Hey... Are you still thinking about joining a club?"

    hide sayori
    jump OW_Go_Back_To_Classroom