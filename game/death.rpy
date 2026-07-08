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

label alien_tired_of_waiting:
    # Hide the screen so it disappears before the dialogue
    hide screen trash_search_screen
    play sound answerwrong
    a "Why are you making me wait?! Are you hoarding the treasures for yourself, human?! Die!"
    jump death

label death:
    scene black with fade
    hide screen mood_counter
    play music "funnyend.mp3"
    show text "{size=150}{color=#a80000}{b}YOU DIED{/b}{/color}{/size}" at truecenter
    $ renpy.pause(hard=False)
    hide text
    show screen restart_confirm("chapter1")
    $ renpy.pause(hard=True)  # wait until player picks an option