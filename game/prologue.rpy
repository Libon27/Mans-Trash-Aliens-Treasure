#define config.voice_filename_format = "audio/speech/ch1/{filename}.ogg"
define s = Character(_("Sean"), color="#f09936")
define a = Character(_("Alien"), color="#458570")
define b = Character(_("Baba Yaga"), color="#db1f1f")
define e = Character(_("Eileen"))

image static = Movie(play="images/static.webm", size=(1920,1080), loop=False)

label prologue:
    
    window hide
    #play music "bg ambient suspense.ogg"
    #scene 1farmers with fade
    scene graduation1 with pushleft
    play sound woow
    s "Just like everyone else. I finally graduated college with lots of hopes and dreams."
    s "However..."

    scene graduation2
    play sound faah
    play music "sad-violin.mp3"

    pause 1.0
    s "I ended up somewhere unexpected."

    s "..."
    s "{bt=3}Why?{/bt} I asked myself."
    s "{sc=3}Why two decades of{/sc} {sc=10}education{/sc} {sc=2}just for{/sc} this..."
    s "{sc=3}Where are you,{/sc} {sc=10}sine, cos, tan?{/sc}"
    s "{sc=3}Where are you{/sc} {sc=10}Alexander Bonaparte, Napoleon the Great?{/sc}"
    s "{sc=3}Where are you{/sc} {sc=10}was, were, has been, yesn't been, had cannot?{/sc}"
    s "{sc=10}he she zir xem fee fie foe fum?{/sc}"

    stop music

    scene black
    show static
    pause 1.0

    scene black

    s "I haven't given up hope yet though."
    s "I still have a chance to recover the brain cells I lost during my education."

    scene babayaga
    play music "bg blues.mp3"
    pause 2.0
    b "Hmmm.... I sense a {glitch=1.1}{color=#0f0}{b}Troubled{/b}{/color}{/glitch} Young man."
    s "What?"
    b "Something {atl=bounce} BIG {/atl} will {sc=3}happen{/sc} to you {atl=0.3,drop_text~#~ 1.5, bounce_text~10}this year!{/atl}"
    s "Uh... {fi=0-0.5}okay?{/fi}"
    b "{gradient2=6-#ff0000-#ffff00-10-#ffff00-#00ff00-10-#00ff00-#00ffff-10-#00ffff-#0000ff-10-#0000ff-#ff00ff-10-#ff00ff-#ff0000-10}I see...{/gradient2}"
    s "{sc=3}What do you see?{/sc}"
    b "Hmm... {atl=0.3,drop_text~#~ 1.5, bounce_text~10}I see!{/atl}"
    s "{sc=3}Wha-what do you see??!!{/sc}"
    b "SHUT UP!"
    s "Sorry."
    b "{atl=0.3,drop_text~#~ 1.5, bounce_text~10}Where your sweat stains the earth,\n let the cow set hoof and the hidden\n shall awaken before your eyes!{/atl}"

    s "..."
    play sound paid
    pause 1.5
    b "..."
    b "Ahem ahem..."
    b "Valued customer!"
    b "Bring a cow to your workplace, and you'll see something \n{atl=bounce}EXTRAORDINARY!{/atl}"
    s "That's all?"
    b "{sc=1}That is all{/sc}. {sc=2}Now{/sc} {sc=3}go!{/sc}"

    stop music
    scene black with fade
    s "And so I did as I was told. And I waited."
    s "Until..."

    play sound horror

    s "What is THAT?"
    play sound plankton
    play music "bg twist.mp3"

    show BlackScreen
    s "Is that... {bt=2}an ALIEN{/bt} {bt=4}riding a{/bt} {bt=6}cow??!{/bt}"


return