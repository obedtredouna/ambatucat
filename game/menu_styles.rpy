# menu_styles.rpy - Clean Ren'Py compatible styles

style menu_panel:
    background "#1B1F28"     # panel warna gelap
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
    hover_color "#FFF1D6"       # correct Ren'Py property
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
