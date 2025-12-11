# AmbatoCat - (Prolog, Ep 1, Ep 2)
# Versi update by Rymess

# --- Definisi Gambar ---
image bg alley = "images/background/bg_alley_dark.png"
image bg room = "images/background/bg_warm_room.png"

init python:
    renpy.music.register_channel("bgm", "music", True)
    renpy.music.register_channel("sfx", "sfx", False)

# --- Definisi Karakter Tambahan ---
# Menambahkan karakter baru untuk Toba (t) dan Kucing Asing (k)
define t = Character("Toba", color="#F5DEB3")
define k = Character("Kucing Asing", color="#B2BABB")


label start:
    jump prolog


# === SCENE 1 : PROLOG ===
label prolog:

    scene bg alley with fade
    play bgm "audio/backsound/sad/Sadness/Sadness.wav" loop fadein 1.0

    show amba dirty_sad at center
    "Amba, seekor kucing hitam kecil, duduk meringkuk di balik tumpukan kardus. Bulunya kotor dan matanya terlihat lelah."
    "Angin dingin berhembus, membuat Amba menggigil."

    a "disini dingin banget, aku lapar sekali…."
    
    hide amba dirty_sad with dissolve

    "Amba mencoba berjalan, langkahnya gontai. Dia melihat ke arah tong sampah yang terbuka."
    "Dia mendekat perlahan, tetapi tiba-tiba seseorang keluar dari warung di dekatnya. Orang itu melihat Amba."
    
    "(Penjual warung melempar botol plastik ke arah Amba. Amba kaget dan melompat mundur, lari menjauh dengan cepat.)"
        
    show amba dirty_sad at center
    a "padahal aku hanya ingin mencari makanan sisa, kenapa selalu begini"

    "Amba meringkuk kedinginan di dalam sebuah kotak kardus yang sudah basah. Suara tetesan air dan angin kencang membuat suasana semakin suram."
    
    # Mengganti musik ke suara hujan
    stop bgm fadeout 1.0
    play bgm "audio/sound effect/rain/rain.wav" loop fadein 1.0
    
    show amba dirty_sad at center
    a "hari ini aku cuman baru makan sekali, besok aku harus cari makan dimana ya?"
    
    play sfx "audio/sound effect/step/running steps.wav"
    "(kemudian amba mendengar suara Langkah kaki besar yang mendekat, awalnya dia merasa takut karena dia tidak tau apa yang menghampirinya)"
    stop sfx fadeout 0.5

    show amba dirty_shock at center
    a "suara apa itu? Sial aku harus bersembunyi"
    
    "(ternyata ada seorang pria yang mendekat perlahan. Amba bersiap untuk lari, tetapi pria itu tidak menunjukkan tanda-tanda ancaman.)"

    show amba dirty_shock at left
    show owner smile at right with dissolve
    
    o "Hei, tenanglah, aku hanya ingin membantumu."

    "(Pria itu meletakkan sebuah mangkuk kecil berisi makanan kucing di depannya. Aroma lezat itu membuat Amba tak bisa menahan diri.)"

    ab "makanan? Apa ini untukku...?"

    "(setelah Amba selesai makan. Pria itu mengelus lembut kepalanya.)"
    
    show amba dirty_neutral at left
    
    "(Amba kaget, tapi tidak lari. Elusan itu terasa... nyaman.)"
    ab "Sudah lama sekali aku tidak merasakan sentuhan selembut ini."

    "(Pria itu menggendong Amba dengan hati-hati dan membawanya masuk ke dalam rumah.)"
    
    stop bgm fadeout 1.5

    scene bg room with fade
    
    play bgm "audio/warm_theme.ogg" loop fadein 1.0

    show amba dirty_neutral at center
    "Rumah itu hangat dan terang. Bau makanan dan sabun tercium di mana-mana."

    a "tempat apa ini? Kenapa terasa hangat sekali disini?"
    "(Amba kemudian melihat pemilik rumah tersebut memberinya makanan lagi, kemudian sampai mengelus-ngelusnya)"
    a "kurasa dia adalah orang yang baik, aku bersyukur sekali kalau bisa tinggal disini"

    hide amba dirty_neutral
    
    pause 1.0
    jump episode_1


# === SCENE 2 : EPISODE 1 ===
label episode_1:

    scene bg room
    
    play bgm "audio/backsound/happy/loops/almost-time-for-christmas_loop-05.wav" loop
    with dissolve

    "Amba selesai dimandikan. Bulunya yang hitam kini bersih dan mengkilap."
    
    show amba cheer at center
    
    "Pemilik memasang kalung sederhana bertuliskan 'Amba'."

    show owner smile at right
    o "Kau akan jadi kucing paling bersih di kota, Amba."
    hide owner smile
    
    "(Amba masih gelisah. Ia adalah anak kucing yang sangat mandiri, terbiasa dengan bahaya.)"
    "(Ia mencoba bersembunyi di bawah sofa, mengamati Pemilik dari kejauhan.)"
    
    show amba sad at center
    
    ab "Dia baik, tapi aku tidak boleh lengah. Di jalanan, kebaikan bisa berubah menjadi jebakan."
    
    "(Pemilik meletakkan mainan tikus kecil di lantai dan mundur.)"
    "(Amba, didorong oleh naluri anak kucingnya, mulai bermain. Rasa takutnya perlahan digantikan oleh rasa ingin tahu.)"
    
    show amba cheer at center
    play sfx "audio/toy_mouse.ogg"
    
    "(Amba menyentuh tikus mainan itu dengan hati-hati.)"
    "Ia teringat betapa kerasnya ia harus berjuang hanya untuk mencium aroma sisa makanan. Sekarang, mainan ini terasa seperti kemewahan yang tak terbayangkan."

    ab "Ini... bermain? Aku tidak ingat kapan terakhir kali aku merasa bebas bermain tanpa takut dikejar."

    "(Amba tidur meringkuk di bantal barunya, tetapi mimpinya masih dipenuhi suara klakson dan dinginnya hujan.)"
    "(Ia terbangun kaget dan langsung mencari celah untuk lari, tetapi kehangatan ruangan menahannya.)"
    
    show amba sad at center with vpunch
    pause 0.5
    show amba cheer at center
    
    "(Amba duduk di jendela, melihat ke gang sempit. Ia bergumam pelan pada dirinya sendiri.)"
    
    a "Aku tidak bisa percaya ini nyata. Aku harus waspada."
    
    stop bgm fadeout 1.5

    pause 0.5
    scene black with fade
    pause 0.5

    jump episode_2


# === SCENE 3 : EPISODE 2 ===
label episode_2:

    scene bg room with dissolve
    
    play bgm "audio/backsound/happy/loops/almost-time-for-christmas_loop-05.wav" loop
    
    "(Didalam rumah, fokus di pintu belakang dan dapur.)"
    
    show amba cheer at center
    
    "(Beberapa hari berlalu. Amba mulai terikat dengan Pemilik, yang memberinya nama panggilan 'Si Hitam Kecil'.)"
    "Amba menikmati sesi elusan lembut dan tidur siang yang panjang."
    
    play music "audio/sound effect/rain/rain.wav" loop fadein 1.0
    
    "(Suara hujan deras di luar. Amba sedang makan dengan lahap, menikmati kehangatan dan rasa kenyang.)"
    "(Tiba-tiba, ia mendengar suara 'meong' yang lemah dan putus asa dari luar, tepat di pintu belakang.)"
    
    play sfx "audio/sound effect/cat/Cat 2.wav"
    
    show amba cheer at center
    a "(Mendongak kaget) Suara itu..."
    
    "(Amba mendekat ke pintu. Bau basah, dingin, dan kelaparan menusuk hidungnya.)"
    "Ia tahu persis bau itu—bau dirinya yang dulu."
    
    "(Amba melihat celah kecil di bawah pintu. Dari sana, ia melihat sepasang mata kecil, cokelat keemasan, yang memandangnya penuh harap.)"
    "Itu adalah anak kucing, seumuran dengannya, basah kuyup dan menggigil."
    
    play sfx "audio/sound effect/cat/Cat 2.wav"
    k "(Meong, sangat pelan) Tolong..."
    
    "(Amba teringat kehangatan bantalnya. Ia tidak tahan.)"
    "(Ia mendorong mangkuk makanannya yang masih penuh ke dekat pintu.)"
    
    show amba cry at center
    
    "(Ia menggaruk pintu dengan cemas, mencoba menarik perhatian Pemilik.)"
    play sfx "audio/sound effect/cat/Cat 1.wav"
    
    "(Pemilik mendengar keributan dan membuka pintu. Anak kucing cokelat itu langsung lari.)"
    show owner smile at right
    
    "(Pemilik melihat mangkuk yang didorong Amba dan mengerti.)"
    
    o "Kau ingin dia ikut masuk, ya? Kau anak yang baik."
    
    hide owner smile
    
    "(Pemilik mengambil payung dan dengan hati-hati mencari anak kucing itu di tengah hujan.)"
    
    window hide
    show amba cry at center
    "Mencari di tengah hujan..."
    pause 2.0
    window show
    
    "(Setelah beberapa menit, Pemilik kembali membawa anak kucing cokelat keemasan yang menggigil. Ia segera mengeringkannya.)"
    stop music fadeout 1.0

    show owner smile at right
    show toba wet_sad at left
    
    o "Aku akan memanggilmu Toba. Sekarang kalian punya teman."
    
    hide owner smile
    
    "(Toba, setelah kering dan diberi makan, langsung menempel pada Amba.)"
    
    show amba cheer at center
    show toba normal_happy at left
    
    "(Amba awalnya kaku, tapi segera menjilati kepala Toba. Persahabatan instan yang lahir dari kesamaan nasib.)"
    
    t "(Sambil bersandar pada Amba) Terima kasih. Aku kedinginan sekali. Aku pikir aku akan mati di sana."
    
    ab "(Batin, lega) Aku tidak sendirian lagi."
    
    "(Amba dan Toba meringkuk bersama, lonceng baru di leher Toba berbunyi pelan saat mereka tidur.)"
    "Mereka berdua anak kucing jalanan yang kini menemukan perlindungan bersama."

    stop bgm fadeout 1.5

    pause 0.5
    scene black with fade
    pause 0.5

    return

# === STUDI KASUS: Input + Kondisional ===
label ending_test:

    # Ask the player for a choice using renpy.input
    $ pilihan = renpy.input("Amba melihat dua jalan. Ke mana ia harus pergi?\n(ketik: rumah / gang)")
    $ pilihan = pilihan.strip().lower()

    # Simple confirmation line
    "Kau memilih: [pilihan]."

    # Conditional flow
    if pilihan == "rumah":
        jump ending_baik
    elif pilihan == "gang":
        jump ending_buruk
    else:
        "Amba bingung dengan pilihan itu..."
        jump ending_test


label ending_baik:
    scene bg room with fade
    play bgm "audio/warm_theme.ogg" loop

    show amba cheer at center
    "Amba memilih kembali ke rumah, tempat yang hangat dan aman."

    o "Kau kembali? Anak pintar."
    "Amba tidur dengan damai malam itu."

    "== GOOD ENDING =="
    return


label ending_buruk:
    scene bg alley with fade
    play bgm "audio/backsound/sad/Sadness/Sadness.wav" loop

    show amba dirty_sad at center
    "Amba kembali ke gang sempit yang gelap..."

    "Hujan turun. Tidak ada makanan. Tidak ada kehangatan."
    a "Harusnya aku tidak kembali ke sini..."

    "== BAD ENDING =="
    return
