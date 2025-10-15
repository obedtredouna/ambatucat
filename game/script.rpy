# AmbatoCat - 2 Scene (Prolog & Episode 1)
# By Ped

# Image definitions
image bg alley = "images/background/bg_alley_dark.png"
image bg room = "images/background/bg_warm_room.png"

init python:
    renpy.music.register_channel("bgm", "music", True)
    renpy.music.register_channel("sfx", "sfx", False)

label start:

    # === SCENE 1 : PROLOG ===
    scene bg alley with fade

    play bgm "audio/alley_ambience.ogg" loop

    show amba dirty_neutral at center
    a "Disini dingin banget... aku lapar sekali..."

    play sfx "audio/trash_can.ogg"
    show amba dirty_sad
    a "Padahal aku hanya ingin mencari makanan sisa... kenapa selalu begini..."

    play bgm "audio/rain.ogg" loop fadein 1.0
    show amba dirty_neutral
    a "Hari ini aku cuma baru makan sekali... besok aku harus cari makan di mana ya?"
    
    show amba dirty_shock
    a "Suara apa itu...? Sial, aku harus bersembunyi!"

    play sfx "audio/footsteps.ogg"

    show owner smile at right
    o "Hei, tenanglah, aku hanya ingin membantumu."

    stop sfx fadeout 1.0
    play bgm "audio/gentle_theme.ogg" fadein 1.0

    show amba dirty_shock
    a "Makanan...? Apa ini untukku...?"

    
    stop bgm fadeout 1.5

    pause 0.5
    scene black with fade
    pause 0.5

    # === SCENE 2 : EPISODE 1 ===
    scene bg room
    play bgm "audio/warm_theme.ogg" loop
    with dissolve

    show amba dirty_neutral
    a "Tempat apa ini...? Kenapa terasa hangat sekali disini...?"

    show amba dirty_neutral
    a "Kurasa dia orang baik... aku bersyukur kalau bisa tinggal disini."

    show amba dirty_neutral at center
    show owner smile at right

    o "Kau akan jadi kucing paling bersih di kota, Amba."

    show amba sad
    a "(Batin) Dia baik, tapi aku tidak boleh lengah... di jalanan, kebaikan bisa berubah jadi jebakan."

    hide owner smile
    show amba neutral
    play sfx "audio/toy_mouse.ogg"
    a "(Batin) Ini... bermain? Aku tidak ingat kapan terakhir kali aku merasa bebas seperti ini."

    show amba neutral
    play sfx "audio/soft_meow.ogg"
    a "Aku tidak bisa percaya ini nyata... tapi aku harus tetap waspada."

    stop bgm fadeout 2.0
    scene black with fade
    pause 1.0

    "— END OF DEMO —"

    return
