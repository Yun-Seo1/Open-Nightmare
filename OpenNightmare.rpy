image bg creepy closet = "Submods/OpenNightmare/images/closet_creepy.png"
image cg captured = "Submods/OpenNightmare/images/test.jpg"


label OWN_test_cg:
    hide monika
    scene cg captured with dissolve_scene_full
    m "It... can't be... I'm sorry for what I've done."
    jump OW_Start_Area

#NOTE:Everything above is testing stuff, will be removed later on

##########
#TODO LIST
##########

#TODO 1: Hide the calendar from the menu
#Use this: https://github.com/Monika-After-Story/MonikaModDev/blob/4d30921fe293e246ce2dd596cd840150f019a8bb/Monika%20After%20Story/game/script-islands-event.rpy#L1938


default OWN_smallglitch = glitchtext(5)
#############
#PYTHON STUFF
#############
init 5 python:
    def OWN_submenu():
        renpy.call_screen("OWN_MENU")

init 10002:
    screen mas_extramenu_area():
        zorder 52

        key "e" action Jump("mas_extra_menu_close")
        key "E" action Jump("mas_extra_menu_close")

        frame:
            area (0, 0, 1280, 720)
            background Solid("#0000007F")

        # close button
            textbutton _("Close"):
                area (60, 596, 120, 35)
                style "hkb_button"
                action Jump("mas_extra_menu_close")

        # zoom control
            frame:
                area (195, 450, 80, 255)
                style "mas_extra_menu_frame"
                vbox:
                    spacing 2
                    label "Zoom":
                        text_style "mas_extra_menu_label_text"
                        xalign 0.5

                # resets the zoom value back to default
                    textbutton _("Reset"):
                        style "mas_adjustable_button"
                        selected False
                        xsize 72
                        ysize 35
                        xalign 0.3
                        action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)

                # actual slider for adjusting zoom
                    bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                        style "mas_adjust_vbar"
                        xalign 0.5
                    $ store.mas_sprites.adjust_zoom()

        if store.mas_submod_utils.isSubmodInstalled("Open World"):
                frame:
                    area (310, 639, 202, 65)
                    style "mas_extra_menu_frame"
                    if persistent._mas_in_idle_mode == True:
                        textbutton ("Open World"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()

                    else:
                        textbutton ("Open World"):
                            xalign 0.5
                            yalign 0.5
                            action [Hide("mas_extramenu_area"), Jump("view_OW")] hover_sound gui.hover_sound

                frame:
                    area (310, 569, 202, 65)
                    style "mas_extra_menu_frame"
                    if persistent._mas_in_idle_mode == True:
                        textbutton ("Open Nightmare"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()

                    else:
                        textbutton ("Open Nightmare"):
                            xalign 0.5
                            yalign 0.5
                            action [Hide("mas_extramenu_area"), Jump("view_OWN")] hover_sound gui.hover_sound

        else:
            frame:
                    area (310, 639, 202, 65)
                    style "mas_extra_menu_frame"
                    if persistent._mas_in_idle_mode == True:
                        textbutton ("Open Nightmare"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()

                    else:
                        textbutton ("Open Nightmare"):
                            xalign 0.5
                            yalign 0.5
                            action [Hide("mas_extramenu_area"), Jump("view_OWN")] hover_sound gui.hover_sound
        if store.mas_submod_utils.isSubmodInstalled("BonkAMon"):
            frame:
                    area (520, 639, 202, 65)
                    if persistent._mas_in_idle_mode == True:
                        style "mas_extra_menu_frame"
                        textbutton ("Bonk Monika"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()
                    else:
                        style "mas_extra_menu_frame"
                        textbutton ("Bonk Monika"):
                            xalign 0.5
                            yalign 0.5
                            action [Hide("mas_extramenu_area"), Jump("view_bonkmenu")] hover_sound gui.hover_sound


label view_OWN:
    stop music
    call mas_change_weather(mas_weather_def, by_user=None,set_persistent=True)
    show noise zorder 3
    show vignette zorder 3
    $ play_song(audio.ghostmenu, loop = True)
    python:
        mas_RaiseShield_dlg()
        OWN_submenu()
    return

screen OWN_MENU():
    zorder 50
    style_prefix "hkb"
    hbox:
        grid 2 2:
            spacing 20
            xpos 527
            ypos 534
            textbutton ("Open [OWN_smallglitch]"): 
                xysize(120, None) 
                action Jump("OWN_temp") hover_sound gui.hover_sound
            textbutton ("Reset Story"):
                xysize(120,None)
                action NullAction() hover_sound gui.hover_sound
            textbutton ("GitHub") action Jump("OW_github") hover_sound gui.hover_sound
            textbutton ("Return") action Jump("OWN_hide_menu") hover_sound gui.hover_sound
    vbox: 
        xpos 1166
        ypos 0
        textbutton ("Dev Only") action Jump("OWN_dev_menu") hover_sound gui.hover_sound

label OWN_temp:
    m 2wta "You want to show me something?{nw}"
    $ _history_list.pop()
    menu:
        m "You want to show me something?{fast}"
        "Yes":
            m 1sua "Huh? You want to take me somewhere?"
            m 6sublo "You must have added something while I wasn't looking."
            m 6sublb "Alright, I can't wait to see what surprise you have for me, let's go."
            window hide
            hide monika
            show OWN_ghost_monika zorder 10
            stop music fadeout 4
            show black zorder 100 with Dissolve(5.0, alpha=True)
            pause 1.0
            $ enable_esc()
            $ HKBHideButtons()
            hide OWN_ghost_monika
            $ consolehistory = []
            call updateconsole("Accessing...", "20%")
            pause 1.5
            call updateconsole("Accessing...", "50%")
            pause 1.0
            ch "..."
            call updateconsole("Accessing...", "90%")
            ch "Hm..."
            call updateconsole("Accessing...", "100%")
            call updateconsole("Accessing...", "Access Granted")
            ch "Perfect...{w=1.0} They will suffice"
            call updateconsole("Restoring files...", "Restoration complete")
            ch "Welcome back."
            call hideconsole
            hide noise
            hide vignette
            call OWN_clubroom_setup
        "No":
            m 6ekblc "Oh... For a second you got me excited because it sounded like something special."
            m 6ekbld "It's okay, maybe some other time?"
            m 6ekblp "I really want to see what this is. I guess you can say it peaked my interest, ehehe~."
            jump ch30_loop

label OWN_hide_menu:
    hide noise
    hide vignette
    hide OWN_ghost_monika
    stop music
    $ play_song(persistent.current_track)
    jump ch30_loop

    