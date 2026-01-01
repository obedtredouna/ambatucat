# ==============================================================================
# SPLASH SCREEN CONFIGURATION
# ==============================================================================

label splashscreen:
    $ renpy.pause(0.5, hard=True)

    # Play Video Splash 1
    $ renpy.movie_cutscene("videos/splash_1.webm")

    # Play Video Splash 2
    $ renpy.movie_cutscene("videos/splash_2.webm")

    $ renpy.pause(0.5, hard=True)

    return

# ==============================================================================
# DEFINISI KARAKTER & VARIABEL
# ==============================================================================

# --- Definisi Karakter Tambahan ---
define narator = Character(None, kind=nvl) # Narasi

# --- Definisi Gambar ---
image bg alley dark = "images/background/bg_alley_dark.png"
image bg alley road = "images/background/bg_alley_Road.png"
image bg alley rain = "images/background/bg_road_dark.png"
image bg Toilet = "images/background/bg_cool_Toilet.png"
image bg got = "images/background/bg_got_dark.png"
image bg house warm = "images/background/bg_warm_house.png"
image bg road dark = "images/background/bg_road_dark.png"
image bg rooftop warm = "images/background/bg_rooftop_warm.png"
image bg room day = "images/background/bg_warm_room 2.png"
image bg under bed = "images/background/bg_warm_room 3.png"
image bg room warm = "images/background/bg_warm_room.png"
image bg ending = "images/background/Ending_Sequence.png"
image bg black = Solid("#000000")

# Variabel untuk tracking status
default trust_stat = 0
default wild_stat = 0
default toba_status = "unknown"

# Variabel musik dan efek suara
init python:
    renpy.music.register_channel("bgm", "music", True)
    renpy.music.register_channel("sfx", "sfx", False)

# Efek Kustom (Camera Shake)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# --- Transform & Callback untuk Efek Bicara ---
transform dim:
    linear 0.2 matrixcolor TintMatrix("#606060")

transform bright:
    linear 0.2 matrixcolor IdentityMatrix()

init python:
    def highlight_speaker(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "begin":
            speaker = renpy.get_say_image_tag()
            char_tags = ["amba", "owner", "toba", "penjual"]
            for tag in char_tags:
                if renpy.get_showing_tags(layer='master').__contains__(tag):
                    if tag == speaker:
                        renpy.show(tag, at_list=[bright])
                    else:
                        renpy.show(tag, at_list=[dim])
    config.all_character_callbacks.append(highlight_speaker)

# ==============================================================================
# PROLOG: KEHIDUPAN JALANAN
# ==============================================================================

label start:
    scene bg alley dark with fade
    play music "audio/Sound effect and backsound ambatucat/sad backsound/Sadness/Sadness.wav" fadein 1.0 loop
    
    # Narasi Lingkungan [Source: 5-7]
    "Gang sempit dan gelap di tengah kota. Suara deru kendaraan dari kejauhan."
    "Amba, seekor kucing hitam kecil, duduk meringkuk di balik tumpukan kardus. Bulunya kotor dan matanya terlihat lelah."
    "Angin dingin berhembus, membuat Amba menggigil."

    show amba dirty_neutral at center with dissolve

    ab "Di sini dingin banget, aku lapar sekali...."

    "Amba mencoba berjalan, langkahnya gontai. Dia melihat ke arah tong sampah yang terbuka."
    "Dia mendekat perlahan, tetapi tiba-tiba seseorang keluar dari warung di dekatnya. Orang itu melihat Amba."

    show penjual angry at right with moveinright
    penjual "(Teriakan kasar) Hus! Pergi sana, dasar kucing sial!"
    

    # Efek lemparan botol [Source: 11]
    play sound "audio/crash.ogg" 
    with hpunch
    hide penjual
    "Penjual warung melempar botol plastik ke arah Amba." 
    
    show amba dirty_shock at left with move
    "Amba kaget dan melompat mundur, lari menjauh dengan cepat."

    ab "Padahal aku hanya ingin mencari makanan sisa. Kenapa selalu begini?"

    # Scene Hujan [Source: 13-16]
    stop music fadeout 1.0
    play music "audio/Sound effect and backsound ambatucat/rain sound effect/Rain.wav" fadein 2.0 loop

    "Gang sempit. Hujan deras. Amba meringkuk kedinginan di dalam sebuah kotak kardus yang sudah basah."
    "Suara tetesan air dan angin kencang membuat suasana semakin suram."

    ab "Hari ini aku cuman baru makan sekali."
    amba "Besok aku harus cari makan di mana ya?"

    # Pertemuan dengan Majikan [Source: 17-26]
    "Amba mendengar suara langkah kaki besar yang mendekat. Awalnya dia merasa takut."

    ab "Suara apa itu? Sial, aku harus bersembunyi!"

    "Ternyata ada seorang pria yang mendekat perlahan. Amba bersiap untuk lari, tetapi pria itu tidak menunjukkan tanda-tanda ancaman."
    "Pria itu meletakkan sebuah mangkuk kecil berisi makanan kucing di depannya. Aroma lezat itu membuat Amba tak bisa menahan diri."

    ab "Makanan? Apa ini untukku...?"

    "Amba selesai makan. Pria itu mengelus lembut kepalanya. Amba kaget, tapi tidak lari."
    "Elusan itu terasa... nyaman."
    "Pria itu menggendong Amba dengan hati-hati dan membawanya masuk ke dalam rumah. Rumah itu hangat dan terang. Bau makanan dan sabun tercium di mana-mana."

    stop music fadeout 1.0

    scene bg room day with fade
    play music "audio/Sound effect and backsound ambatucat/happy backsound/loops/almost-time-for-christmas_loop-03.wav" fadein 1.0 loop

    show amba dirty_neutral at left with dissolve
    ab "Tempat apa ini? Kenapa terasa hangat sekali di sini?"

    show owner smile at right with dissolve
    "Majikan memberinya makanan lagi, kemudian sampai mengelus-ngelusnya."

    majikan "(Lembut) Mulai sekarang, kamu tinggal di sini. Aku akan menjagamu. Namamu Amba, ya?"
    
    "Majikan tersenyum tulus. Amba merasa dilema. Ini adalah kehidupan yang nyaman, tetapi dia harus selamanya terikat pada manusia, meninggalkan kebebasan yang dia kenal."

    majikan "(Mengajak) Bagaimana, Amba? Mau tinggal di rumahku?"

    # --- PERCABANGAN UTAMA PROLOG [Source: 27-28] ---
    menu:
        "Menerima Tawaran":
            jump prologue_accept

        "Menolak Tawaran":
            jump prologue_reject

label prologue_accept:
    # [Source: 30]
    "Amba menempelkan kepalanya di tangan Majikan, sebuah tanda setuju. Ia mendengkur pelan."
    jump episode1

label prologue_reject:
    # [Source: 33-43]
    stop music fadeout 1.0

    "Amba tiba-tiba melompat dari gendongan Majikan, panik dan bingung. Insting liar jalanannya muncul."
    "Dia berlari kencang keluar pintu yang sedikit terbuka."

    majikan "(Kaget) Tunggu! Amba!"

    hide owner with moveoutright
    scene bg alley rain with fade
    play music "audio/Sound effect and backsound ambatucat/sad backsound 2/Sad Piano - Blue X Music/WAV/Sad Piano (Looping Version).wav" fadein 1.0 loop
    show amba dirty_sad at center with dissolve

    ab "Tidak! Aku harus bebas! Aku tidak bisa terikat! Aku harus kembali ke jalanan."

    "Pemandangan: Amba kembali ke gang sempit. Hujan telah berhenti, tetapi malam terasa semakin dingin. Rasa lapar dan penyesalan mulai menusuk."

    ab "Aku menolaknya... tempat yang hangat itu... aku membuat kesalahan."

    "Amba berjalan sempoyongan. Dia mencoba mencari makanan lagi, tetapi dia terlalu lemah. Dia tidak bisa menemukan apa-apa. Dua hari berlalu tanpa makanan."

    scene bg got with fade
    "Pemandangan: Kolong jembatan yang sepi dan gelap. Tubuh Amba terbaring meringkuk, tidak bergerak."
    "Matanya tertutup. Tidak ada lagi deru napas. Angin dingin berhembus."

    ab "Dingin sekali... dan lapar... kurasa... aku tidak bisa... bertahan..."

    "Amba menghembuskan napas terakhirnya, sendirian di kegelapan."
    "{b}TAMAT – JALUR TRAGIS{/b}"
    stop music fadeout 2.0
    return

# ==============================================================================
# EPISODE 1: AWAL KEHANGATAN
# ==============================================================================

label episode1:
    scene bg room day with fade
    play music "audio/Sound effect and backsound ambatucat/happy backsound/loops/almost-time-for-christmas_loop-05.wav" fadein 1.0 loop

    # [Source: 49-56]
    "Amba selesai dimandikan. Bulunya yang hitam kini bersih dan mengkilap. PEMILIK memasang kalung sederhana bertuliskan 'Amba'."

    show amba cheer at left with dissolve
    show owner smile at right with dissolve

    majikan "(Sambil tersenyum) Kau akan jadi kucing paling bersih di kota, Amba."

    "Amba masih gelisah. Ia adalah anak kucing yang sangat mandiri, terbiasa dengan bahaya."
    
    hide owner with dissolve
    hide amba wiith moveoutleft
    scene bg under bed with fade
    "Ia mencoba bersembunyi di bawah sofa, mengamati Pemilik dari kejauhan."

    "Di balik kehangatan ini, naluri jalanan Amba berteriak. Ia masih curiga, masih menunggu jebakan."

    show amba sad at left with dissolve
    ab "Dia baik, tapi aku tidak boleh lengah. Di jalanan, kebaikan bisa berubah menjadi jebakan."

    # [Source: 57-62]
    show owner cheer at right with dissolve
    "PEMILIK meletakkan mainan tikus kecil berwarna abu-abu di lantai dan mundur, memberikan jarak."

    majikan "Ini untukmu. Mainlah, Amba."

    hide owner with moveoutright
    "Majikan keluar ruangan, meninggalkan Amba sendirian."
    "Sebuah mainan. Benda yang tidak pernah Amba kenal. Di saat ini, Amba merasa..."

    # [Source: 63-65]
    menu:
        "Mendekat perlahan, hati-hati.":
            jump ep1_curiosity

        "Mencari celah untuk kabur, mengabaikan mainan.":
            jump ep1_suspicion

label ep1_curiosity:
    # [Source: 66-73]
    $ trust_stat += 1
    show amba cheer at left with dissolve
    "Amba, didorong oleh naluri anak kucingnya, mulai bermain. Rasa takutnya perlahan digantikan oleh rasa ingin tahu."
    
    ab "Ini... bermain? Aku tidak ingat kapan terakhir kali aku merasa bebas bermain tanpa takut dikejar."
    ab "Dulu, mainan hanyalah sampah yang harus aku hindari."
    
    "Amba menyentuh tikus mainan itu dengan hati-hati. Kehangatan mulai mengisi dadanya."
    
    ab "Rasanya... nyaman. Mungkin aku bisa menurunkan sedikit kewaspadaanku. Hanya sedikit."
    jump ep1_sleep

label ep1_suspicion:
    # [Source: 74-80]
    $ wild_stat += 1
    "Amba mengabaikan mainan itu. Instingnya mengatakan ruangan ini adalah kandang yang menyenangkan."
    
    ab "Mainan? Buang-buang energi. Aku harus mencari celah. Pintu, jendela, di mana titik lemahnya?"
    
    "Amba mengelilingi ruangan, menemukan jendela yang tertutup rapat. Kecewa."
    
    ab "Aku terperangkap. Aku harus tetap waspada dan kuat. Jangan tertipu oleh makanan dan bantal lembut."
    jump ep1_sleep

label ep1_sleep:
    # [Source: 82-93]
    scene bg room warm with dissolve
    "Pemandangan: Malam hari. Amba tidur meringkuk di bantal barunya. Ia bergidik dalam tidurnya. Musik melankolis naik sedikit."
    
    "Meskipun tubuhnya hangat, mimpinya masih dipenuhi suara klakson yang keras, dinginnya hujan, dan teriakan Penjual Warung."
    
    "Amba terbangun kaget dan langsung mencari celah untuk lari, tetapi kehangatan ruangan dan kenyamanan bantal menahannya."
    
    ab "Hanya mimpi buruk... Sudah tidak ada hujan lagi."
    
    "Amba duduk di jendela, melihat ke gang sempit yang terlihat dari kejauhan. Kehidupan lamanya tampak gelap dan jauh."
    
    amba "(Bergumam pelan) Aku tidak bisa percaya ini nyata. Aku harus waspada... tapi..."

    menu:
        "Tapi aku tidak boleh membiarkan ini melunakkanku.":
            jump ep1_bad_end

        "Tapi kehangatan ini terasa terlalu berharga untuk dilepaskan.":
            jump ep1_accept

label ep1_bad_end:
    # [Source: 95-99]
    "Amba memutuskan untuk terus mencari celah dan kesempatan untuk kabur, meskipun ia menikmati makanan."
    $ wild_stat += 1
    
    ab "Aku akan makan, mengumpulkan tenaga, dan segera pergi. Aku tidak butuh siapa-siapa."
    jump episode2


label ep1_accept:
    # [Source: 100-104]
    "Amba memutuskan untuk menikmati kenyamanan sejenak, menunda rencana melarikan diri. Ia mulai membalas elusan Pemilik dengan dengkuran pelan."
    $ trust_stat += 1
    
    ab "Untuk saat ini... aku akan tetap di sini."
    jump episode2

# ==============================================================================
# EPISODE 2: IKATAN DAN PILIHAN
# ==============================================================================

label episode2:
    stop music fadeout 1.0
    scene bg room day with fade
    play music "audio/Sound effect and backsound ambatucat/rain sound effect/Rain.wav" fadein 2.0 loop
    show amba cheer at left with dissolve

    # [Source: 109-111]
    "Pemandangan: Beberapa hari berlalu. Amba (Si Hitam Kecil) mulai terikat dengan PEMILIK. Ia menikmati sesi elusan lembut dan tidur siang yang panjang."
    "Hari-hari Amba terasa seperti mimpi. Perut kenyang, tubuh hangat, dan tangan lembut yang selalu mengelus."
    "Jalanan terasa seperti dunia lain yang terlupakan."

    # [Source: 112-117]
    "Suara hujan deras di luar. Amba sedang makan dengan lahap. Tiba-tiba, ia mendengar suara 'meong' yang lemah dan putus asa dari luar, tepat di pintu belakang."
    
    ab "Suara itu..."
    
    "Amba mendekat ke pintu. Bau basah, dingin, dan kelaparan menusuk hidungnya. Bau dirinya yang dulu."
    "Amba melihat celah kecil di bawah pintu. Dari sana, ia melihat sepasang mata kecil, cokelat keemasan, yang memandangnya penuh harap."

    toba "(Meong, sangat pelan) Tolong..."
    
    show amba sad at left
    ab "Aku tahu rasa sakit itu. Aku tidak bisa membiarkannya."

    # [Source: 118-123]
    "Amba mendorong mangkuk makanannya yang masih penuh ke dekat pintu. Ia menggaruk pintu dengan cemas, mencoba menarik perhatian Pemilik."
    
    show owner smile at right with moveinright
    majikan "Ada apa, Si Hitam Kecil? Kenapa kau ribut?"
    
    "Pemilik melihat mangkuk yang didorong Amba dan tatapan Amba ke pintu. Pemilik mengerti."
    majikan "Kau ingin dia ikut masuk, ya? Kau anak yang baik."
    
    hide amba with dissolve
    hide owner with moveoutleft
    scene bg alley rain with fade
    "Pemilik mengambil payung dan mencari anak kucing itu di tengah hujan. Beberapa menit kemudian, Pemilik kembali membawa anak kucing cokelat keemasan yang menggigil."
    
    majikan "Aku akan memanggilmu Toba. Sekarang kalian punya teman."

    # [Source: 124-126]
    scene bg room day with dissolve
    show toba playfull at right
    show amba cheer at left

    "Toba, setelah kering dan diberi makan, langsung menempel pada Amba. Amba awalnya kaku, tapi segera menjilati kepala Toba."
    
    toba "(Sambil bersandar pada Amba) Terima kasih. Aku kedinginan sekali. Aku pikir aku akan mati di sana."
    ab "Aku tidak sendirian lagi."

    stop music fadeout 1.0

    hide amba with dissolve
    hide toba with dissolve

    play music "audio/Sound effect and backsound ambatucat/happy backsound/loops/almost-time-for-christmas_loop-01.wav" fadein 1.0 loop

    # [Source: 127-133]
    "Beberapa minggu berlalu. Toba dan Amba adalah teman yang tak terpisahkan. Namun, Toba adalah kucing yang lebih liar."
    
    show amba cheer at left
    show toba normal at right
    toba "(Berbisik, saat Pemilik tidur) Amba, ayo kita lari. Dinding ini terlalu sempit."
    toba "Aku dengar ada taman besar di seberang jalan. Kita bisa berburu tikus sungguhan!"
    
    ab "Aku punya makanan, keamanan... tapi Toba benar, di luar sana ada kebebasan."
    
    "Malam ini, Pemilik lupa mengunci rapat jendela dapur. Udara dingin masuk, membawa bau tanah basah dan rumput."
    "Toba sudah siap di ambang jendela."
    
    show toba walk at right
    toba "Ini kesempatan kita, Amba! Ayo!"
    hide toba with moveoutleft

    # --- PERCABANGAN AKHIR EPISODE 2 [Source: 134-136] ---
    # Developer Note: Jalur 'Yakinkan Toba' ditambahkan untuk menjembatani ke Episode 3.
    menu:
        "Melompat ke luar, kembali ke jalanan.":
            jump ep2_end_freedom

        "Mengabaikan ajakan Toba.":
            jump ep2_end_lonely
            
        "Yakinkan Toba untuk tetap tinggal":
            jump ep2_true_route

label ep2_end_freedom:
    # [Source: 139-147]
    "Amba ragu sejenak, menatap bantal lembutnya, lalu teringat tatapan mata Toba yang memohon di pintu belakang. Amba mengangguk mantap."
    ab "Aku sudah terlalu lama sendiri. Jika harus berjuang, lebih baik bersama teman."
    
    "Amba melompat keluar bersama Toba. Mereka berhasil melarikan diri, langsung disambut oleh hujan gerimis."
    hide amba with moveoutleft

    scene bg road dark with fade
    "Amba dan Toba berhasil mencapai taman besar. Kehidupan mereka kini keras, penuh risiko, dan selalu lapar."
    "Namun, mereka berdua tidak pernah berjarak. Mereka berbagi makanan, kehangatan, dan bahaya."
    
    "Pemandangan: Amba dan Toba meringkuk bersama di bawah semak belukar yang rimbun, bulu mereka basah. Toba mendengkur pelan di pelukan Amba."
    
    show amba cheer at left
    show toba normal at right

    ab "Kami bebas. Kami kedinginan, kami lapar, tapi kami bersama."
    ab "Ini adalah ikatan yang lebih kuat dari kehangatan sebuah rumah."
    "{b}THE END: Kebebasan Bersama{/b}"
    return

label ep2_end_lonely:
    # [Source: 149-159]
    "Amba memandang Toba dengan sedih, lalu menunduk. Ia berjalan perlahan kembali ke bantalnya. Keamanan jauh lebih penting daripada petualangan."
    
    ab "Tidak. Aku tidak akan kembali ke neraka itu. Aku tidak bisa melepaskan kenyamanan ini."
    
    "Toba melihat Amba. Matanya menunjukkan kekecewaan, tapi ia mengangguk mengerti."
    tb "Selamat tinggal, Si Hitam Kecil."
    
    "Toba melompat keluar sendirian."
    
    show owner sad at right with moveinright
    majikan "Toba nakal, ya? Syukurlah kau tetap di sini, anak baik."
    
    "Amba hidup nyaman dan aman. Namun, setiap kali hujan turun, ia selalu melihat ke luar jendela."
    "Ia menikmati kehangatan, tetapi ada ruang kosong di sebelahnya."
    "{b}THE END: Kehangatan yang Sepi{/b}"
    return

label ep2_true_route:
    # Logika jembatan ke Episode 3
    "Amba menatap Toba dalam-dalam. Ia tidak bergerak menuju jendela."
    amba "Toba, jangan. Lihat hujan di luar. Kita punya makanan di sini."
    toba "Tapi... kebebasan..."
    "Toba melihat keteguhan Amba dan mangkuk makanan yang penuh. Ia menghela napas, lalu melompat turun dari jendela kembali ke dalam."
    show toba normal at right with moveinright
    toba "Baiklah. Demi kau... aku akan mencoba bertahan di sini sedikit lagi."
    jump episode3

# ==============================================================================
# EPISODE 3: JANJI
# ==============================================================================

label episode3:
    scene bg under bed with fade
    play music "audio/Sound effect and backsound ambatucat/happy backsound/loops/almost-time-for-christmas_loop-03.wav" fadein 1.0 loop

    # [Source: 164-168]
    "Beberapa minggu berlalu. Amba dan Toba tak terpisahkan. Mereka bermain kejar-kejaran, belajar menggunakan kotak pasir, dan saling membersihkan."
    "Minggu demi minggu, persahabatan mereka tumbuh. Amba perlahan belajar untuk rileks berkat Toba."

    show toba chill at right
    show amba cheer at left
    
    toba "Hei Amba, lihat!" 
    with hpunch
    "(Toba menjatuhkan pensil dari meja.)"
    
    ab "Bodoh! Nanti Pemilik marah. Tapi... bagus juga."
    
    "Mereka tertawa dalam bahasa kucing, berlari menjauh dari 'kejahatan' kecil mereka."
    hide amba with moveoutleft
    hide toba with moveoutright

    # [Source: 169-171]
    show owner cheer at center
    "Pemilik memberikan kalung dengan lonceng perak kecil yang identik untuk Amba dan Toba."
    play sound "audio/bell_jingle.ogg"
    
    majikan "Ini. Agar aku selalu tahu di mana kalian berada. Dan kalian juga."
    
    "Lonceng itu menjadi simbol persahabatan mereka. Di mana ada bunyi lonceng Toba, di situ ada bunyi lonceng Amba."
    hide owner with dissolve

    # [Source: 172-178]
    scene bg room warm with fade
    "Suatu sore, Toba melihat seekor kupu-kupu terbang di luar jendela yang terbuka sedikit. Naluri anak kucingnya memanggil. Ia hampir melompat keluar."
    
    show amba sad at left
    show toba playfull at right
    
    amba "Toba, jangan! Di luar itu berbahaya! Kau dengar suara mobil tadi?"
    toba "Tapi... seru sekali! Aku hanya ingin sebentar saja."
    
    "Toba melihat mata Amba yang memohon dan memutuskan untuk mundur. Mereka duduk di jendela, melihat kupu-kupu itu terbang bebas di atas jalan raya yang ramai."
    
    toba "Aku harap suatu hari nanti, kita bisa melihatnya tanpa harus takut."
    amba "Kita sudah punya satu sama lain. Itu sudah cukup."
    
    "Amba dan Toba berjanji bahwa mereka tidak akan pernah pergi ke jalan raya yang ramai di depan rumah."
    jump episode4

# ==============================================================================
# EPISODE 4: DARAH DI ASPAL (KLIMAKS)
# ==============================================================================

label episode4:
    stop music fadeout 0.5
    scene bg room day
    show amba cheer at left
    play music "audio/Sound effect and backsound ambatucat/sad backsound/Sadness/Sadness.wav" fadein 1.0 loop

    # [Source: 184-191]
    "Pagi hari yang sibuk. Pemilik sedang bersiap-siap. Pintu depan terbuka sedikit karena Pemilik membawa barang keluar."
    "Tiba-tiba, Toba mencium aroma yang sangat kuat—bau ikan goreng sisa yang baru saja dibuang di tong sampah di seberang jalan."
    
    show toba walk at right
    show amba sad at left
    
    toba "(Mata lebar) Amba, aku menciumnya! Di sana! Sedikit saja."
    
    amba "Toba, tidak! Ingat janji kita!"

    toba "(Berlari ke pintu) Sebentar saja! Cepat pergi, cepat kembali!"
    hide toba with moveoutright

    "Toba melesat keluar. Loncengnya berbunyi keras, cepat, panik."
    play sound "audio/bell_fast.ogg"
    
    amba "TOBA!"

    "Di persimpangan janji dan bahaya, Amba harus memilih."

    menu:
        # Pilihan ini muncul jika naluri liar (Wild) lebih dominan atau seimbang
        "Mengejar Toba, berusaha menyelamatkannya." if wild_stat >= trust_stat:
            jump ep4_tragic_attempt

        # Pilihan ini muncul jika kepercayaan pada majikan (Trust) lebih dominan
        "Memilih untuk tetap di dalam, mengamankan diri." if trust_stat > wild_stat:
            jump ep4_betrayal
            
label ep4_tragic_attempt:
    # [Source: 196-208]
    
    play music "audio/Sound effect and backsound ambatucat/sad backsound 2/Sad Piano - Blue X Music/WAV/Sad Piano (Looping Version).wav" fadein 1.0 loop
    scene bg road dark with dissolve

    "Amba berlari kencang, mengejar Toba. Lonceng peraknya berbunyi tergesa-gesa."

    show toba walk at right
    "Amba melihat Toba sudah setengah jalan menyeberang, matanya terpaku pada tong sampah. Ia tidak melihat kendaraan yang datang."
    
    "Tiba-tiba, terdengar deru mesin yang sangat keras—sebuah mobil van hitam melaju kencang dari tikungan."
    
    amba "(Berlari kencang, menjerit pilu) LARI, TOBA!"
    
    show toba shocks at center
    "Toba mendengar suara Amba. Ia berbalik, panik, dan mencoba berlari kembali. Tapi sudah terlambat."
    
    play sound "audio/car_skid_crash.ogg"
    with hpunch
    
    scene bg black with fade
    "Mobil van itu menghantam Toba. Suara benturan keras, diikuti bunyi lonceng perak yang putus dan suara benda kecil yang jatuh."
    
    scene bg road dark with fade
    show amba sad at left with moveinleft
    show toba died at right with dissolve
    "Amba berhenti mendadak. Ia melihat tubuh Toba yang tergeletak diam di aspal. Darah mulai menyebar di bulu cokelat keemasannya."
    "Loncengnya diam. Suara mobil van itu menghilang."
    
    amba "(Merangkak mendekat, gemetar hebat) Toba... Toba, loncengmu..."
    
    "Amba menyentuh Toba dengan hidungnya. Toba tidak bergerak. Dingin. Amba mencium bau darah yang tajam."
    
    amba "(Jeritan kesedihan yang memilukan) KENAPA?! Kau bilang kau akan selalu bersamaku! Jalanan ini... jalanan ini mengambilmu!"
    
    "Pemilik berlari keluar, melihat adegan itu, dan memeluk Amba. Amba melawan, berusaha kembali ke Toba, namun ditahan kuat."
    
    ab "Aku sendirian lagi. Kehangatan itu... selalu sementara. Jalanan itu tidak pernah membiarkan kami tenang."
    
    "{b}THE END: Kematian Toba{/b}"
    jump episode5

label ep4_betrayal:
    # [Source: 210-220]

    play music "audio/Sound effect and backsound ambatucat/sad backsound 2/Sad Piano - Blue X Music/WAV/Sad Piano (Looping Version).wav" fadein 1.0 loop

    "Amba berhenti mendadak di ambang pintu. Ia menatap Toba yang berlari ke aspal, lalu menatap kembali kehangatan rumah. Ia memilih keamanan."
    show amba sad at left
    
    ab "Tidak! Aku tidak akan melanggar janjiku. Aku tidak bisa!"
    
    hide amba with moveoutleft
    "Amba mundur, masuk kembali ke dalam rumah. Ia melihat Toba menyeberang sendirian."
    "Terdengar deru mesin yang sangat keras—sebuah mobil van hitam melaju kencang dari tikungan."
    
    play sound "audio/car_skid_crash.ogg"
    "Amba menutup mata dan telinganya. Ia mendengar suara benturan keras, diikuti keheningan yang mematikan. Lonceng perak Toba tidak lagi terdengar."
    
    "Pemilik berlari keluar. Amba meringkuk ketakutan di bawah sofa. Pemilik kembali dengan wajah sedih, memeluk Amba."

    show amba sad at left with dissolve
    show owner sad at right with moveinright
    majikan "(Penuh duka) Oh, Amba... Toba..."
    
    hide amba with dissolve
    hide owner with dissolve

    scene bg room warm with fade
    "Beberapa hari kemudian. Amba sendirian di kamar yang hangat. Pemilik memperlakukannya dengan lebih lembut, tapi ada kesedihan yang tak terhindarkan."
    
    show amba sad at center
    ab "Aku selamat. Aku memegang janji untuk diriku sendiri. Tapi... aku membiarkan lonceng lain berhenti berbunyi."
    ab "Aku mengkhianati janji kami. Aku adalah pengecut."
    
    "{b}THE END: Keselamatan yang Menyakitkan{/b}"
    jump episode5

# ==============================================================================
# EPISODE 5: EPILOG
# ==============================================================================

label episode5:
    stop music fadeout 2.0
    scene bg rooftop warm with fade
    play music "audio/Sound effect and backsound ambatucat/Ending Song/Hindia - kids.mp3" volume 0.5 fadein 2.0

    # [Source: 224-235]
    "Rumah yang terasa sangat besar dan sepi."
    "Tiga hari setelah tragedi itu. Amba tidak mau makan. Ia hanya meringkuk di tempat tidur yang dulu ia bagi dengan Toba."
    "Rumah itu sunyi. Lonceng di leher Amba berbunyi sesekali, mengingatkannya pada bunyi lonceng yang hilang."
    
    show amba sad at center
    ab "Aku seharusnya menahannya lebih keras. Aku seharusnya lari bersamanya. Aku gagal. Aku tidak bisa menjaga satu-satunya temanku."
    
    show amba sad at left with moveinleft
    show owner sad at right with moveinright
    "Pemilik duduk di samping Amba, mengelus lembut. Amba tidak lari, tetapi juga tidak menanggapi. Ia menatap kosong ke sudut ruangan, seolah Toba masih ada di sana."
    
    "Amba melihat ke ambang jendela. Dulu, ia melihat kebebasan. Kini, ia hanya melihat bahaya dan kematian."
    "Ia mengerti bahwa kehangatan di dalam rumah ini bukanlah 'kurungan,' melainkan perlindungan yang dibayar mahal oleh pengorbanan Toba."
    
    ab "Toba meninggal karena kelaparan sesaat dan naluri liarnya. Aku tidak akan membiarkan kematiannya sia-sia."
    ab "Aku harus bertahan hidup. Aku harus menghargai rumah ini."
    
    "Amba bangkit. Ia berjalan ke mangkuk makanannya yang kosong. Ia makan dengan perlahan, tetapi pasti. Ia tahu ia harus kuat."
    
    "Amba mengambil mainan tikus kecil yang dulu ia mainkan bersama Toba. Ia meletakkannya di sampingnya."
    "Ia kemudian berjalan ke Pemilik dan menyandarkan kepalanya di kaki Pemilik. Untuk pertama kalinya, ia menunjukkan kepercayaan penuh."
    
    ab "Aku tidak akan pernah melupakan jalanan, Toba."
    ab "Tapi aku akan memilih untuk tetap di sini. Di sini aman."
    ab "Aku akan membawa ingatanku tentangmu dan bertahan, untuk kita berdua. Aku janji."
    
    "Amba tidur meringkuk, tetapi kini tidak kaget saat terbangun. Ia sendirian, tetapi ia kini mengerti arti dari rumah dan keselamatan."
    "Ia akan selamanya menjadi AmbatoCat—sebagian Amba yang waspada, sebagian Toba yang berharga, yang kini ia bawa dalam kenangan dan loncengnya yang sunyi."
    
    window hide
    scene bg ending with fade
    
    pause 2.0

    centered "{b}TAMAT{/b}\n\nTerima kasih telah memainkan AmbatoCat."
    stop music fadeout 5.0
    return