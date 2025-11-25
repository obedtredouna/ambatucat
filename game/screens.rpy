# screens.rpy - Simple right-side control main menu (no custom images)
screen main_menu():

    # background: 
    add Solid("#111218")


    # Title area (center-left)
    frame:
        xalign 0.18
        yalign 0.30
        background None
        has vbox
        spacing 8

        text "AmbatoCat" size 56 color "#F8EBD7" xalign 0.0
        text "A short demo" size 18 color "#C9C9C9" xalign 0.0

    # Right-side control panel (the main focus)
    frame:
        style "menu_panel"
        xalign 0.82
        yalign 0.50
        has vbox
        spacing 14

        textbutton "Start" action Start() style "menu_button"
        textbutton "Load" action ShowMenu("load") style "menu_button"
        textbutton "Preferences" action ShowMenu("preferences") style "menu_button"
        textbutton "Credits" action Show("credits") style "menu_button"
        textbutton "Quit" action Quit(confirm=True) style "menu_button"

    # Footer small info (bottom-left)
    frame:
        background None
        xalign 0.02
        yalign 0.98
        has hbox
        spacing 12
        text "AmbatoCat — Demo v0.1" style "footer_text"
        textbutton "View script" action Function(renpy.exports.open_file, "sandbox:/mnt/data/AmbatoCat.docx") style "footer_button"

# Simple credits screen
screen credits():
    tag menu
    modal True
    zorder 50

    frame:
        style "credits_box"
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 8

        text "Credits" size 32
        text "Writer: Ped" size 18
        text "Demo UI: generated" size 14
        textbutton "Back" action Return() style "menu_button"
