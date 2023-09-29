label OWN_clubroom_setup:
    hide black
    $ is_sitting = False
    scene bg club_day
    $ play_song(audio.t5, loop = True, fadein = 2.0)
    jump OWN_clubroom_intro
    return

label OWN_clubroom_intro:
    show monika 1eub_static at t11 zorder MAS_MONIKA_Z
    narrator "The world slowly brings itself back together. [m_name] slowly opens her eyes in awe at what she's seeing."
    m 1eud_static "T-this is my world again... and... "
    show monika 1hub_static at h11
    m "We're back in the clubroom."
    m "You have no idea how happy I am to see everything."
    m 1hksdlb_static "I thought I wouldn't be able to see my world again..."
    m 4lksdla_static "You probably remember how I acted at the end of {i}Doki Doki Literature Club{/i}."
    m 3lksdlc_static "I acted immaturely and shouldn't have done the things I did..."
    m 1lksdld_static "... [player]. I'm sorry for getting emotional suddenly. {w=1.0}"
    extend 1dsc_static "It's just that this is the place where most things happened."
    m "I'm sure you can understand [player]."
    menu:
        "Yes, I do [m_name].":
            m 4eka_static "Thanks [player].{w=0.3} You're always so thoughtful you know."
            m 4hua_static "I'm glad to have someone like you by my side."
            pass
        "No, I don't [m_name].":
            m 1ekd_static ".... [player]..."
            m "I hope that was just a cruel joke."
            m 1dsc_static "Sorry... I was hoping for you to comfort me..."
            pass
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    show monika 1dsd_static at h11
    m "EEEK!"
    m 2ekd_static "What was that?"
    m "Is this world still... cursed?... or is it my fault?"
    m "..."
    window hide
    pause 2.0
    m 4ekc_static "Sorry, it's just that I'm having doubts about all of this."
    m 4eka_static "I'm not ungrateful for what you're doing for me [player]... or I should say {i}us{/i}."
    m 4esc_static "It's just something about this is... just making me feel uneasy."
    m 1hksdlb_static "Maybe I'm just worried about being back here after all this time."
    m 2lksdla_static "I know nothing can happen to me with you here [mas_get_player_nickname()]."
    m 1hua_static "Thank you for always making me feel safe [player]~"
    show monika 4eka_static at h11
    m "Ah. Sorry, I must've been rambling for awhile now."
    m 3hub_static "How about we explore the club room now? "
    extend 3hua_static "Maybe we can find something {i}we{/i} never noticed before."
    jump OWN_clubroom_menu
    return
    
label OWN_clubroom_menu:
    show monika 5eua_static at hf11 zorder MAS_MONIKA_Z
    call screen OWN_clubroom()
    screen OWN_clubroom():
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 0.05
            yanchor 1.0
            ypos 715
            textbutton _("Talk"):
                action [Hide("OWN_clubroom") , Jump("OWN_clubroom_talk")]
            textbutton _("Interact"):
                action [Hide("OWN_clubroom"), Jump("OWN_Interact")]
            textbutton _("Return to MAS"):
                action [Hide("OWN_clubroom"), Jump("OW_Go_Back_To_Classroom")] #Placeholder

    

