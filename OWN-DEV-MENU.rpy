label OWN_dev_menu:
    hide noise
    hide vignette
    hide OWN_ghost_monika
    python:
        items = [
            ("QTE mouse ver","OWN_qte_mouse_test",False, False),
            #("","",False, False),
            #("","",False, False),
            #("","",False, False),
            #("","",False, False),
        ]
        final_args = [
            ("Close",False,False, False, 4)
        ]


    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, *final_args)

    if _return == False:
        jump ch30_loop


label OWN_qte_mouse_test:
    $ cont = 0
    $ arr_keys = ["q","w","o","p"]
    call OWN_qte_setup(0.5, 0.5, 0.01, random.choice(arr_keys), random.randint(1,9) * 0.1, random.randint(1,9) * 0.1)

    while cont == 1:
        call OWN_qte_setup(0.5, 0.5, 0.01, random.choice(arr_keys), random.randint(1,9) * 0.1, random.randint(1,9) * 0.1)

    jump OWN_dev_menu
    return