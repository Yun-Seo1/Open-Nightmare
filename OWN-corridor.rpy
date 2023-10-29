label OWN_corridor_setup:
    if persistent.OWN_has_seen_corridor_monika == False:
        stop music
        show black zorder 100 with Dissolve(2.0, alpha=True)
        $ consolehistory = []
        call updateconsole("Overriding","10")
        pause 0.5
        call updateconsole("Overriding", "20")
        pause 0.5
        ch "We'll take back this world soon..."
        call hideconsole
        hide black
        $ persistent.OWN_has_seen_corridor_monika = True
        scene bg corridor with dissolve_scene_full
    else:
        scene bg corridor with dissolve_scene_full
    pause 1.0
    $ play_song(audio.t6, loop = True, fadein = 2.0)
    jump OWN_corridor_menu

label OWN_corridor_menu:
    show monika 5eua_static at hf11 zorder MAS_MONIKA_Z
    call screen OWN_corridor()
    screen OWN_corridor():
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 0.05
            yanchor 1.0
            ypos 715
            textbutton _("Talk"):
                action [Hide("OWN_corridor") , Jump("OWN_corridor_talk")]
            textbutton _("Interact"):
                action [Hide("OWN_corridor"), Jump("OWN_corridor_interact_monika")]
            textbutton _("Return"):
                action [Hide("OWN_corridor"), Show("OWN_return_question_trap")] 
    jump OWN_corridor_menu
    return

label OWN_corridor_talk:
    call screen dialog(message="No Talks added", ok_action=Return())
    jump OWN_corridor_menu

label OWN_corridor_interact_monika:
    call screen dialog(message="No Interacts added", ok_action=Return())
    jump OWN_corridor_menu

screen OWN_return_question_trap():
    label "Return to [RTMAS]?"
    textbutton _("Yes"):
        action [Hide("OWN_return_question"), Jump("OWN_the_nightmare_begins")] 
    textbutton _("No"):
        action [Hide("OWN_return_question"), Jump("OWN_the_nightmare_begins")]


label OWN_the_nightmare_begins:
    hide screen OWN_return_question_trap
    show monika 5eua_static at t11 zorder MAS_MONIKA_Z
    pause 2.0
    show monika 1euc_static at t11
    pause 2.0
    show monika 1ekd_static at hf11
    pause 1.0
    m "..."
    show monika 2lksdla_static at t11
    m "Umm... "
    m "Why aren't we going back to the [RTMAS]?"
    $ play_song(audio.yuri2, loop = True, fadein = 1.0)
    m 4lksdlb_static "Can you give me a moment [player]?"
    $ OWN_time = 30 - get_pos()
    m 4ekd_static "This has never happened before... I fear that my intuition about this place was correct."
    $ consolehistory = []
    call updateconsole ("Call Return Label","Access Denied")
    show noise at noisefade(OWN_time) zorder 4
    show vignette at vignettefade(0) zorder 4
    show vignette as flicker at vignetteflicker(OWN_time) zorder 4
    show layer master at layerflicker(OWN_time)
    m 1s_OWN "W-what?..."
    m "What do you mean denied?"
    m 3s_OWN "T-this has to be a mistake right?"
    m 1s_OWN "Please give me a second [player]..."
    window hide
    call updateconsole ("Call Return Label","Access Denied")
    call updateconsole ("Call Return Label","Access Denied")
    m 4s_OWN "Why isn't this working?..."
    m "It should let me because it's only the two of us."
    m "[player], you have more power than me, can you try returning us to the [RTMAS]?"
    menu:
        "Yes":
            call updateconsole("Call Return Label","Error")
            pass
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    show monika 1dsd_static at h11
    m "EEEK!"
    m 1s_OWN "None of this is making sense!"
    pause 1.0
    m "...!"
    pause 1.0
    m "I...it's them... I felt off about all of this from the beginning and now this."
    m 4s_OWN "[player]... they took away from my powers in my world..."
    call hideconsole
    m "[player]... what do we do? I can't return us to the [RTMAS]..."
    m 1t_OWN "[player]... I'm scared. I... I don't think I can face them again..."
    m 3t_OWN "What I did... it was unacceptable..."
    m "[player], what ever happens... {w=0.5}"
    extend 4u_OWN "know that I love you."
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "Please... come find me!{space=5000}{w=0.5}{nw}"
    m "I don't want to lose you!{space=5000}{w=0.5}{nw}"
    m "I know you won't leave me!{space=5000}{w=0.5}{nw}"
    window hide
    hide noise at noisefade
    hide vignette at vignettefade
    hide flicker at vignetteflicker
    show layer master at truecenter
    hide black onlayer front
    show black zorder 100
    pause 1.0
    $ consolehistory = []
    call updateconsole("Overriding","30")
    call updateconsole("Overriding","40")
    ch "Let's meet a few familiar faces."
    call updateconsole("Create new script", "Access Granted")
    call updateconsole("Start script \"script-ch31\"", "Access Granted")
    call hideconsole
    jump OWN_script_ch31_start
    return
    
    #hide black onlayer front
    #jump OW_Go_Back_To_Classroom
