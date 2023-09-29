define ch = DynamicCharacter('ch_name', image='chibika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default ch_name = "???"

default persistent._OWN_chapter = 0

image OWN_transparent = "/Submods/OpenNightmare/images/transparent.png"

init 5 python :
    import os
    def OWN_del_char(name):
        try: 
            os.remove(config.basedir + "game/Submods/OpenNightmare/characters" + name + ".chr")
        except: 
            pass
    def OWN_create_char(name):
        #TODO: look for ways to create files using python
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
