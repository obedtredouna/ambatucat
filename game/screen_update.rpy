# game/screens.rpy
# Clean screens file for AmbatoCat - no 'margin' properties used
# Compatible with Ren'Py 8.4+

init python:
    import os
    def has_saves():
        try:
            d = renpy.config.savedir
            if not d:
                return False
            files = os.listdir(d)
            return any(not f.startswith(".") for f in files)
        except:
            return False



# Main menu
screen main_menu():
    add Solid("#111218")

    frame:
        background "gui/main_menu.png"

    frame:
        background None
        xalign 0.18
        yalign 0.30
        has vbox
        spacing 6
        text "AmbatoCat" size 56 color "#F8EBD7"
        text "A short demo" size 18 color "#C9C9C9"

    frame:
        style "menu_panel"
        xalign 0.82
        yalign 0.50
        has vbox
        spacing 14

        textbutton "Start" action Start() style "menu_button"
        textbutton "Continue" action Continue() sensitive has_saves() style "menu_button"
        textbutton "Load" action ShowMenu("load") style "menu_button"
        textbutton "Preferences" action ShowMenu("preferences") style "menu_button"
        textbutton "Credits" action Show("credits") style "menu_button"
        textbutton "Quit" action Quit(confirm=True) style "menu_button"

    frame:
        background None
        xalign 0.02
        yalign 0.98
        has hbox
        spacing 12
        text "AmbatoCat — Demo v0.1" style "footer_text"

# Credits
screen credits():
    tag menu
    modal True

    frame:
        style "credits_box"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 14
            xalign 0.5

            text "CREDITS" size 32 xalign 0.5

            null height 10

            text "Core Team" size 20 xalign 0.5

            text "Muhammad Fatham Mahabbah Haqiqi" size 16 xalign 0.5
            text "(7708223127)" size 13 xalign 0.5

            text "Syarif Ruhul Mujadid" size 16 xalign 0.5
            text "(7708220038)" size 13 xalign 0.5

            text "Obed Bari Tredouna" size 16 xalign 0.5
            text "(707082330166)" size 13 xalign 0.5

            null height 20

            textbutton "Back" action Hide("credits") style "menu_button" xalign 0.5




# Choice screen
screen choice(items):
    frame:
        xalign 0.5
        yalign 0.78
        has vbox
        spacing 8

        for i in items:
            textbutton i.caption action i.action style "modern_choice_button"
