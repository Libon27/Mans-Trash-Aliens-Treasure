default search_count = 0

screen restart_confirm(target_label):
    modal True
    zorder 200

    frame:
        align (0.5, 0.5)
        padding (40, 40)

        vbox:
            spacing 20
            text "Do you want to try again?" size 40

            hbox:
                spacing 100
                align (0.5,0.5)
                textbutton "Yes" action [Hide("restart_confirm"), SetVariable("alien_mood", 1), SetVariable("search_count", 0),Jump(target_label)]
                textbutton "No" action MainMenu()

screen win_end(target_label):
    modal True
    zorder 200

    frame:
        align (0.5, 0.5)
        padding (40, 40)

        vbox:
            spacing 20
            text "You won!!\n Play again?" size 40

            hbox:
                spacing 100
                align (0.5,0.5)
                textbutton "Yes" action [Hide("win_end"), SetVariable("alien_mood", 1), SetVariable("search_count", 0),Jump(target_label)]
                textbutton "No" action MainMenu()

label alien_tired_of_waiting:
    # Hide the screen so it disappears before the dialogue
    hide screen trash_search_screen
    play sound answerwrong
    show alien angry
    a "Why are you making me wait?! Are you hoarding the treasures for yourself, human?! Die!"
    jump death

label death:
    scene black with fade
    play sound gun
    hide screen mood_counter
    play music "funnyend.mp3"
    show text "{size=150}{color=#a80000}{b}YOU DIED{/b}{/color}{/size}" at truecenter
    $ renpy.pause(hard=False)
    hide text
    show screen restart_confirm("chapter1")
    $ renpy.pause(hard=True)  # wait until player picks an option


label ending:
    scene black with fade
    hide alien
    stop music
    stop sound

    screen info_dialog(message, size=40):
        modal True
        zorder 200

        frame:
            align (0.5, 0.5)
            padding (40, 40)
            xmaximum 0.7
            ymaximum 0.7

            vbox:
                spacing 20
                text message size size

                hbox:
                    align (0.5, 0.5)
                    textbutton "Okay" action Return()

    call screen info_dialog("The alien seems pretty happy")
    
    show sean base
    s "..."
    s "He's let his guard down."
    s "Now's my chance!!"

    hide sean

    screen trash_escape():
        # A vbox stacks items vertically
        vbox:
            align (0.5, 0.5) # Centers the box in the middle of the screen
            spacing 20       # Adds a 20-pixel gap between the image and text
        
            # The clickable trash can image
            imagebutton:
                idle "trashcan.png"            
                action Return()
                xalign 0.5           
            
            # The clickable text box/button below it
            textbutton "Search":
                background Frame(Solid("#222222"), 10, 10)
                action Return()
                text_size 90         
                xalign 0.5
    
    default ending_pool = [        
        ("a working Phone!", Item('Phone', 'Naaa, now way, this game is rigged! How could you randomly find a working phone with full battery and excellent connection in a trash dumping site?', 'images/Items/phone.png', category="Rig"), 1, 'images/Items/phone.png')
    ]

    show screen trash_escape
    play sound trash
    with vpunch

    $ randomly_picked_bundle = renpy.random.choice(ending_pool)
    $ item_name = randomly_picked_bundle[0]
    $ actual_item = randomly_picked_bundle[1]
    $ item_quantity = randomly_picked_bundle[2]
    $ item_image_path = randomly_picked_bundle[3]

    show expression item_image_path at truecenter
    hide screen trash_escape
    s "I found [item_name]"
    hide expression item_image_path

    show sean win
    play sound telephone
    s "Siike!"
    hide screen mood_counter

    scene white
    show sean win
    play sound fbi
    pause 5.0

    hide sean
    play music "extermination.mp3"
    show text "{size=150}{color=#a80000}{b}ALIEN EXTERMINATION IN PROGRESS{/b}{/color}{/size}" at truecenter
    $ renpy.pause(hard=False)
    
    scene black with fade
    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ alien_mood = 1
    show screen win_end("prologue")
    $ renpy.pause(hard=True)

return