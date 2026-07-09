#define config.voice_filename_format = "audio/speech/ch1/{filename}.ogg"
define s = Character(_("Sean"), color="#f09936")
define a = Character(_("Alien"), color="#458570")
define b = Character(_("Baba Yaga"), color="#db1f1f")
define e = Character(_("Eileen"))

image static = Movie(play="images/static.webm", size=(1920,1080), loop=False)

label prologue:
    
    window hide
    hide screen mood_counter
    
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
    scene alienarrival
    pause 1.5

    s "What is {atl=0.3,drop_text~#~ 1.5, bounce_text~10}THAT?{/atl}"
    play sound plankton
    play music "bg twist.mp3"

    s "Is that... {bt=2}an ALIEN{/bt} {bt=4}riding a{/bt} {bt=6}cow??!{/bt}"
    play sound what
    s "And... it's abducting a UFO... WHAAAT??!!"
    scene white
    play sound flashbang
    pause 2.0


######################################################

    show alien neutral
    with dissolve

    a "...Atmosphere breathable."

    a "Gravity acceptable."

    a "...Civilisation detected."

    scene black with fade
    show alien neutral
    with dissolve

    stop music fadeout 2.0
    a "Wake up, Human."
    a "Wake up!"

    show alien neutral
    with dissolve

    scene site1 with fade
    show alien neutral
    a "Remarkable."
    a "The dominant species has displayed its greatest cultural achievements."
    play music "bg waltz.mp3"

    hide alien
    show sean base
    play sound what_the_hell
    s "(WAT DA HAIL??!)"

    hide sean
    show alien neutral
    a "Only a highly advanced civilization would gather its most valuable artifacts into one sacred location."

    hide alien
    show sean base
    s "You're looking at a garbage dump."

    hide sean
    show alien neutral
    a "Your language appears primitive."

    hide alien
    show sean base
    s "No, seriously. People throw this stuff away."

    hide sean
    show alien neutral
    a "You are attempting to deceive an extraterrestrial intelligence."
    a "Bold."

    play sound guncharge
    "The alien raises an impossibly sleek energy pistol."

    show alien angry
    play music "bg twist.mp3"
    a "Silence."

    a "You have already been identified as the local curator."

    hide alien
    show sean base
    s "The local... what?"

    hide sean
    show alien neutral
    a "Curator."
    a "Keeper of Humanity's Treasures."

    hide alien
    show sean base
    s "I literally work at the dump."

    hide sean
    show alien angry
    a "An admirable disguise."
    a "But that won't work on me."

    show alien happy
    play sound guncharge
    pause 2.0

    hide alien
    show sean base
    s "{atl=0.3,drop_text~#~ 1.5, bounce_text~10}Sorry! Sorry!{/atl}"

    hide sean
    show alien base
    a "My mission is simple."
    a "You will retrieve the finest relics your civilization has to offer."
    a "You will present them to me for evaluation."

    play sound gun
    show alien angry
    a "Failure will result in your immediate vaporization."

    hide alien
    show sean base
    s "That seems a little extreme."

    hide sean
    show alien neutral
    a "I possess seventeen settings."
    a "The current one is 'slightly annoyed.'"
    stop music
    play sound alert

    hide alien
    show sean base
    s "...There are seventeen?"

    hide sean
    show alien neutral
    a "Correct."

    a "The final setting leaves very little to identify."

    hide alien
    show sean base
    s "..."

    play music "bg waltz.mp3"
    s "So... if I bring you random junk..."

    hide sean
    show alien angry
    a "Treasures."

    hide alien
    show sean base
    s "...Treasures..."

    s "...you won't shoot me?"

    hide sean
    show alien confused
    a "Assuming your offerings satisfy my refined standards."

    hide alien
    show sean base
    s "And if they don't?"

    play sound guncharge
    hide sean
    show alien happy
    a "Then I become considerably less diplomatic."

    hide alien
    show sean base
    play sound woow
    s "Fantastic."

    hide sean
    show alien neutral
    a "You may begin immediately."
    a "Do not insult me with common refuse."
    a "Go."

    menu:
        "Fight the Alien":
            jump death
        "Obey without trying":
            jump chapter1

return