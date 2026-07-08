# 1. Set the default mood score. 
# 'default' ensures the game remembers the score when saving/loading.
default alien_mood = 1

# 2. Create a custom Python function to handle score changes and death checks.
init python:
    def change_mood(amount):
        global alien_mood  # Tell Python we want to modify the global variable
        
        # Add the amount to the current mood (use a negative number to subtract)
        alien_mood += amount
        
        # Notify the player of the change (optional, but good for feedback!)
        if amount < 0:
            renpy.notify("Alien mood decreased!")
        elif amount > 0:
            renpy.notify("Alien mood increased!")

        # Check if the mood has hit 0 (or lower, just in case)
        if alien_mood <= 0:
            # renpy.jump automatically forces the game to go to the label
            renpy.jump("death")

screen mood_counter():
    frame:
        align (0.98, 0.10)  # top-right corner
        padding (10, 5)
        vbox:               # vertical layout (stacks top to bottom)
            spacing 5       # small gap between texts
            text "Alien's mood: [alien_mood]" size 50 color "#FFFFFF"


##################################
##########  SCRAP YARD  ##########
##################################

label rusted_muffler:
    show AlienFace4
    "The alien hefts it onto their shoulder like a bazooka, peering down the rusted pipe."
    "A cloud of black soot falls onto their face, which the Alien interpret as weaponized dark matter."
    play sound answercorrect
    a "A portable sonic-cannon! And it still leaks the dark-matter residue of a thousand eradicated foes! You humans are savages. I love it."
    $ change_mood(1)
    jump chapter1

label spark_plug:
    show AlienFace3
    "The alien pinches it delicately, treating it like a highly volatile explosive."
    "When the Alien demand the activation code and you can't provide it, the Alien feel insulted that you handed them a useless bomb."
    play sound answerwrong
    a "You mock me?! Handing me a Class-4 neural detonator without the biometric activation sequence?! Are you trying to get us both killed, flesh-bag?!"
    $ change_mood(-2)
    jump chapter1

label dead_car_battery:
    show AlienFace2
    "The Alien presses their ear against the plastic casing, shaking it slightly and hearing the dried acid slosh inside."
    "The Alien nods with deep, solemn respect."
    play sound answercorrect
    a "The fabled Plasma Core. To think you left your planetary energy reserves just lying in the dirt. I can feel the raw, untamed current whispering to me."
    $ change_mood(2)
    jump chapter1

label frayed_jumper_cables:
    show AlienFace4
    "The alien arrogantly snaps the copper teeth onto their own bio-armor, expecting a massive power surge."
    "Instead, the rusted copper creates a horrific short-circuit with their alien tech, shocking them violently."
    play sound answerwrong
    a "TREACHERY! YOU POISONED MY SUIT! DIE, ASSASSIN!"
    $ change_mood(-100)
    jump chapter1

label bent_license_plate:
    show AlienBase
    "The alien runs a scanner over the rusted letters, bowing slightly in reverence to the stamped numbers."
    play sound answercorrect
    a "Ah, the diplomatic credentials of your highest ruler, Lord 7B3-X99. I shall spare his life when the invasion begins."
    $ change_mood(1)
    jump chapter1

label engine_piston:
    show AlienFace4
    "The Alien wield it like a holy gavel or war hammer, slamming it against a rusted car hood to assert dominance."
    "The Alien are absolutely thrilled with this new melee weapon."
    play sound answercorrect
    a "A gravity-hammer of exquisite craftsmanship! I claim this weapon. Now, point me to the skull of your strongest champion!"
    $ change_mood(3)
    jump chapter1

label broken_radiator:
    show AlienFace3
    "The alien studies the intricate metal fins, running their hand across it and immediately slicing their alien fingers on the sharp, bent metal."
    "The Alien aim their gun right between your eyes."
    play sound answerwrong
    a "A booby-trapped data-slab?! You dare hand me a puzzle laced with micro-blades?! My royal blood leaks upon your garbage!"
    $ change_mood(-3)
    jump chapter1

label bent_bicycle_wheel:
    show AlienBase
    "The Alien spin the wheel on its axle. Mesmerized by the rotation, the Alien stare at it for an uncomfortable amount of time, gun slightly lowered."
    play sound answercorrect
    a "A perpetual motion gyroscope... manipulating the very fabric of time. Do not interrupt my calculations, human."
    $ change_mood(1)
    jump chapter1

label snapped_fan_belt:
    show AlienFace2
    "The alien loops it around their waist like a championship belt or a bandolier, standing tall and proud."
    play sound answercorrect
    a "The ceremonial sash of a fallen warlord. I will wear this to honor his defeat. Did you slay him, little creature?"
    $ change_mood(2)
    jump chapter1

label exhaust_pipe:
    show AlienFace3
    "The Alien speak directly into one end, listening to the metallic, hollow echo of their own voice from the other end."
    "The Alien find the tone insulting and assume the pipe is mocking them."
    play sound answerwrong
    a "This translation matrix is defective! It distorts my booming voice into a pathetic, reedy whine! Do not hand me broken comms gear!"
    $ change_mood(-1)
    jump chapter1


########################################
##########  RECYCLING CENTRE  ##########
########################################

label bubble_wrap:
    show AlienFace4
    "The alien accidentally steps on it and panics, then carefully pops one with their finger."
    "Suddenly addicted, the Alien start furiously popping them, giggling menacingly."
    play sound answercorrect
    a "Micro-explosions! Kinetic forcefields designed to trap the unwary. I am disabling them one by one. I am invincible!"
    $ change_mood(2)
    jump chapter1

label tangled_earphones:
    show AlienFace3
    "The alien recoils in horror, aggressively poking the tangled mess with the barrel of their gun, thinking it’s an organic parasite."
    play sound answerwrong
    a "A dormant brain-worm! Keep that symbiotic nightmare away from my auditory receptors! Have your people no ethics?!"
    $ change_mood(-2)
    jump chapter1

label smashed_smartphone:
    show AlienFace3
    "The Alien tap the cracked black screen furiously, getting increasingly frustrated."
    "The Alien aggressively shake it at you."
    play sound answerwrong
    a "This pocket-oracle is dead. Where is the AI housed within? Did it disengage to avoid capture? You have handed me a corpse!"
    $ change_mood(-1)
    jump chapter1

label empty_bleach_bottle:
    show AlienFace3
    "The alien unscrews the cap, takes one sniff of the chemical residue, and gags violently, eyes watering."
    "The Alien feel their honor has been attacked by cowardly tactics."
    play sound answerwrong
    a "By the Cosmos... a bio-weapon! To contain such a caustic nebula in a mere plastic vessel... you attack my olfactory vents like a coward!"
    $ change_mood(-3)
    jump chapter1

label scratched_cd:
    show AlienBase
    "The Alien hold it up to the light, watching the rainbow reflection on the back."
    "The Alien try to use it as a laser-deflecting shield."
    play sound answercorrect
    a "A monomolecular data-crystal! The refraction algorithms alone hold the secrets of your star-gates. I have seized your archives!"
    $ change_mood(1)
    jump chapter1

label cardboard_egg_carton:
    show AlienBase
    "The alien gently strokes the empty cups, looking around with a mix of awe and maternal instinct."
    play sound answercorrect
    a "Incubation pods. But the Alien are empty. Have the micro-drones already hatched? Are the Alien in the room with us right now?!"
    $ change_mood(1)
    jump chapter1

label crushed_soda_can:
    show AlienFace2
    "The alien tries to un-crush it, marveling at the lightweight material."
    "The Alien stick it on the end of their gun barrel like a silencer."
    play sound answercorrect
    a "Nano-armor plating. So thin, yet it retains its structural memory. This will upgrade my plasma rifle perfectly."
    $ change_mood(2)
    jump chapter1

label plastic_spork:
    show AlienFace2
    "The Alien inspect the hybrid tines and bowl shape, completely baffled by the engineering."
    "The Alien hold it up like a sacred artifact."
    play sound answercorrect
    a "A multi-tool of devastating efficiency. It pierces, yet it scoops. What dark genius engineered such a paradox?!"
    $ change_mood(3)
    jump chapter1

label leaking_aa_battery:
    show AlienFace3
    "The Alien notice the crusty white battery acid and treat it like highly radioactive material."
    "The Alien take a huge step back and aim their gun defensively."
    play sound answerwrong
    a "A ruptured fusion cell! The core is venting! Are you trying to melt my skeletal structure with gamma radiation?!"
    $ change_mood(-2)
    jump chapter1

label floppy_disk:
    show AlienFace4
    "The alien slides the metal shutter back and forth. Believing it to be a data drive, the Alien slide it into a slot on their armor's wrist-computer."
    "The archaic dust and magnetic strip instantly corrupt their life-support OS."
    play sound answerwrong
    a "I will now download your planetary defenses—wait. ERROR? SYSTEM PURGE?! You uploaded a lethal techno-virus into my mainframe! We die together!"
    $ change_mood(-100)
    jump chapter1


####################################
##########  THE LANDFILL  ##########
####################################

label squeaky_dog_toy:
    show AlienFace3
    "The alien squeezes it, and it gives a loud SQUEAK."
    "The alien gasps, appalled by your cruelty in handing them a 'living' prisoner."
    play sound answerwrong
    a "It cries out in pain! What tortured soul have you trapped within this rubbery flesh-prison?! You sicken me, human!"
    $ change_mood(-2)
    jump chapter1

label broken_mattress:
    show AlienFace3
    "The alien steps onto it, expecting an anti-gravity launch matrix."
    "A rusted spring snaps up and smacks them in the shin. the Alien feel deeply humiliated."
    play sound answerwrong
    a "Your launch-pad is defective! My leg has been compromised by a rogue coil! This is unacceptable hardware!"
    $ change_mood(-1)
    jump chapter1

label deflated_basketball:
    show AlienFace2
    "The alien picks up the flat, textured rubber."
    "Staring at the crushed sphere, the Alien are overcome with existential dread, significantly lowering their mood."
    play sound answerwrong
    a "A collapsed planetoid. Shrunk down to the size of my hand... How many billions perished when you deflated their world? You are a monster."
    $ change_mood(-3)
    jump chapter1

label cracked_lava_lamp:
    show AlienBase
    "The alien shakes the cold, congealed wax inside, thinking it’s a fellow alien specimen trapped in stasis."
    play sound answerwrong
    a "Hold on, brother! I will free you from this cryogenic stasis tube! Who did this to you? Was it this flesh-bag?!"
    $ change_mood(-100)
    jump chapter1

label toilet_seat:
    show AlienFace2
    "The alien casually places it over their own head, wearing it like a regal halo or a piece of heavy ceremonial collar armor."
    play sound answercorrect
    a "The Halo of Leadership! By right of conquest, I am now the Supreme Chancellor of this garbage-sector. Bow to me!"
    $ change_mood(3)
    jump chapter1

label rotting_teddy_bear:
    show AlienFace2
    "The alien strokes the matted fur, treating it with the utmost respect."
    "The Alien hold it up by the ear as a sign of respect for your warrior spirit."
    play sound answercorrect
    a "The severed head of an apex predator. You defeated this fearsome beast and kept its pelt? Perhaps I underestimated your combat prowess."
    $ change_mood(2)
    jump chapter1

label torn_umbrella:
    show AlienFace4
    "The Alien press the button and it violently snaps open (half-broken)."
    "The alien ducks, then realizes it's a tool, highly impressed."
    play sound answercorrect
    a "A deployable atmospheric dome! A kinetic shield! Incredible... though it seems the structural integrity has been tested in battle."
    $ change_mood(2)
    jump chapter1

label single_croc_shoe:
    show AlienBase
    "The alien puts their hand inside it, studying the holes."
    "The Alien pretend it’s a small, amphibious tank, driving it along the dirt while making laser noises."
    play sound answercorrect
    a "An amphibious assault vessel, perforated for maximum hydrodynamic flow. Where is the rest of the armada?!"
    $ change_mood(1)
    jump chapter1

label broken_toaster:
    show AlienFace3
    "The alien pushes the lever down. It pops back up. the Alien push it again."
    "The Alien glare at you, furious that you handed them broken utility gear."
    play sound answerwrong
    a "The cremation chamber is malfunctioning! How do you dispose of your enemies if the dual heat-slabs will not engage?!"
    $ change_mood(-1)
    jump chapter1

label disembodied_head:
    show AlienFace4
    "The alien finds it staring up from the mud. the Alien pick it up delicately, staring into its unblinking, painted eyes."
    "The alien's bravado completely shatters into paranoid madness."
    play sound answerwrong
    a "This deity... it does not blink. It knows no fear. IT IS JUDGING MY SOUL! You summoned a dark god to smite me! I MUST NEUTRALIZE THE SUMMONER!"
    $ change_mood(-100)
    jump chapter1