define ch = DynamicCharacter('ch_name', image='chibika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default ch_name = "???"
default OWN_smallglitch = glitchtext(5)

define audio.yuri2 = "<loop 4.444>bgm/5_yuri2.ogg"
default persistent._OWN_first_time_opening = False
default persistent._OWN_chapter = 0 #Add to reset story
default persistent.OWN_has_seen_clubroom_monika = False #Add to reset story
default persistent.OWN_has_seen_corridor_monika = False

image OWN_transparent = "/Submods/OpenNightmare/images/transparent.png"
image bg creepy closet = "Submods/OpenNightmare/images/closet_creepy.png"
image cg captured = "Submods/OpenNightmare/images/test.jpg"
#Sayori images
image sayori happy_thoughts = Image("/Submods/OpenNightmare/images/fun_unny_happy_happy_fun.png")

#scared
image monika 1s_OWN = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "Submods/OpenNightmare/images/s.png")
image monika 2s_OWN = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "Submods/OpenNightmare/images/s.png")
image monika 3s_OWN = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "Submods/OpenNightmare/images/s.png")
image monika 4s_OWN = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "Submods/OpenNightmare/images/s.png")

#crying
image monika 1t_OWN = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "Submods/OpenNightmare/images/t.png")
image monika 2t_OWN = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "Submods/OpenNightmare/images/t.png")
image monika 3t_OWN = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "Submods/OpenNightmare/images/t.png")
image monika 4t_OWN = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "Submods/OpenNightmare/images/t.png")

#smile crying
image monika 1u_OWN = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "Submods/OpenNightmare/images/u.png")
image monika 2u_OWN = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "Submods/OpenNightmare/images/u.png")
image monika 3u_OWN = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "Submods/OpenNightmare/images/u.png")
image monika 4u_OWN = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "Submods/OpenNightmare/images/u.png")

#glitch
image monika g1_OWN:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    #"monika 3"

image monika g2_OWN:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat



init 5 python :
    import os
    def OWN_del_char(name):
        try: 
            os.remove(config.basedir + "game/Submods/OpenNightmare/characters" + name + ".chr")
        except: 
            pass
    def OWN_create_char(name):
        #this doesn't work, just added to remember
        try: 
            os.create(config.basedir + "game/Submods/OpenNightmare/characters" + name + ".chr")
        except: 
            pass


image OWN_ghost_monika:
    "mod_assets/other/ghost_monika.png"
    zoom 0.75

image bg broken:
    parallel:
        "Submods/OpenNightmare/images/HomeStatic0000.png"
        0.2
        "Submods/OpenNightmare/images/HomeStatic0001.png"
        0.2
        "Submods/OpenNightmare/images/HomeStatic0002.png"
        0.2
        "Submods/OpenNightmare/images/HomeStatic0003.png"
        0.2
        "Submods/OpenNightmare/images/HomeStatic0004.png"
        0.2
        "Submods/OpenNightmare/images/HomeStatic0005.png"
        0.2
        repeat


#QTE Screens

label OWN_qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):
    python:
        time_start = time_start # amount of time given
        time_max = time_max     # total amount of time
        interval = interval     # timer decreasing interval
        trigger_key = trigger_key # key/keyboard input to hit in the quick time event
        x_align = x_align       # x alignment of the bar/box
        y_align = y_align       # y alignment of the bar/box

    call screen qte_button
    $ cont = _return

    return

screen qte_button:

    button:
        action Return(0) #miss
        align (0.5, 0.5)
        background "OWN_transparent"

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])

    vbox:
        xalign x_align
        yalign y_align
        spacing 25

        button:
            action Return(1)
            xalign 0.5
            xysize (100, 100)
            background Frame("gui/poemgame/m_sticker_1.png", 10, 10)
            activate_sound "gui/sfx/hover.ogg"

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
