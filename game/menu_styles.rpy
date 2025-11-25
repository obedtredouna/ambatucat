# menu_styles.rpy - Clean Ren'Py compatible styles

style menu_panel:
    background "#1B1F28"
    xpadding 22
    ypadding 18
    xminimum 320
    yminimum 280

style menu_button:
    font "DejaVuSans.ttf"
    size 28
    color "#FFFFFF"
    background None
    xpadding 18
    ypadding 10
    hover_background "#FFFFFF20"
    hover_color "#FFF1D6"
    insensitive_color "#777777"

style footer_text:
    size 14
    color "#888B95"

style footer_button:
    size 14
    color "#A9ADB6"
    background None
    hover_color "#FFFFFF"

style credits_box:
    background "#000000C0"
    xpadding 28
    ypadding 24
    xmaximum 640

style modern_say_window:
    background "#12161AC0"
    xpadding 18
    ypadding 14
    xmaximum 1200
    xminimum 640
    yminimum 110

style modern_name:
    size 22
    bold True
    color "#FFDFAE"
    xalign 0.0

style modern_say_text_window:
    background None
    xpadding 0
    ypadding 0

style modern_say_text:
    size 24
    color "#FFFFFF"
    slow_cps 30

style modern_choice_button:
    font "DejaVuSans.ttf"
    size 24
    color "#FFFFFF"
    background "#1B1F28"
    xpadding 16
    ypadding 10
    xmargin 6        # FIXED: replace margin
    ymargin 6        # FIXED: replace margin
    hover_background "#FFFFFF20"
    insensitive_color "#777777"
