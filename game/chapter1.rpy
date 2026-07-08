screen trash_search_screen():
    # A vbox stacks items vertically
    vbox:
        align (0.5, 0.5) # Centers the box in the middle of the screen
        spacing 20       # Adds a 20-pixel gap between the image and text
        
        # The clickable trash can image
        imagebutton:
            idle "trashcan.png"
            # Jumps to death if clicked more than twice, otherwise increments and returns
            action If(search_count >= 2, Jump("alien_tired_of_waiting"), [SetVariable("search_count", search_count + 1), Return()])
            xalign 0.5           
            
        # The clickable text box/button below it
        textbutton "Search":
            background Frame(Solid("#222222"), 10, 10)
            action If(search_count >= 2, Jump("alien_tired_of_waiting"), [SetVariable("search_count", search_count + 1), Return()])
            text_size 90         
            xalign 0.5


label chapter1:

    show screen mood_counter
    if alien_mood <= 0:
        jump death

    scene site1
    play music "bg scomedy.mp3"
    
    a "Human, go thou forth and bring me treasures!"

label trash_menu:
    menu:
        "Scrap Yard":
            jump scrap_yard
        "Recycling Centre":
            jump recycling_centre
        "Landfill":
            jump landfill

label scrap_yard:
    scene site1
    default scrap_yard_pool = [
        ("a Rusted Muffler", Item('Rusted Muffler', 'A heavy cylindrical tube flaking orange rust. Smells vaguely of carbon and dashed road-trip dreams.', 'images/Items/rusted_muffler.png', category="Scrap Yard"), 1, 'images/Items/rusted_muffler.png'),
        ("a Spark Plug", Item('Spark Plug', 'A small ceramic and metal nub covered in thick engine grease. It used to ignite fuel; now it mostly just ignites alien paranoia.', 'images/Items/spark_plug.png', category="Scrap Yard"), 1, 'images/Items/spark_plug.png'),
        ("a Dead Car Battery", Item('Dead Car Battery', 'A heavy plastic block filled with sloshing, expired acid. Lifting it is a workout; dropping it on your toe is a tragedy.', 'images/Items/dead_car_battery.png', category="Scrap Yard"), 1, 'images/Items/dead_car_battery.png'),
        ("a Frayed Jumper Cables", Item('Frayed Jumper Cables', 'Thick rubber hoses terminating in rusty, jagged alligator clips. The dangerously exposed copper wiring looks incredibly sketchy.', 'images/Items/frayed_jumper_cables.png', category="Scrap Yard"), 1, 'images/Items/frayed_jumper_cables.png'),
        ("a Bent License Plate", Item('Bent License Plate', 'A warped piece of stamped aluminum reading "XYZ-123". The registration sticker expired a decade ago.', 'images/Items/bent_license_plate.png', category="Scrap Yard"), 1, 'images/Items/bent_license_plate.png'),
        ("an Engine Piston", Item('Engine Piston', 'A solid, greasy chunk of machined steel. Heavy enough to anchor a small boat or shatter a windshield.', 'images/Items/bent_license_plate.png', category="Scrap Yard"), 1, 'images/Items/bent_license_plate.png'),
        ("a Broken Radiator", Item('Broken Radiator', 'A cumbersome grid of bent metal fins and cracked plastic casing. It leaks a mysterious, sticky greenish fluid onto your shoes.', 'images/Items/broken_radiator.png', category="Scrap Yard"), 1, 'images/Items/broken_radiator.png'),
        ("a Bent Bicycle Wheel", Item('Bent Bicycle Wheel', 'A wire-spoked wheel warped into a tragic taco shape. It spins with a sad, wobbly squeak.', 'images/Items/bent_bicycle_wheel.png', category="Scrap Yard"), 1, 'images/Items/bent_bicycle_wheel.png'),
        ("a Snapped Fan Belt", Item('Snapped Fan Belt', 'A rigid loop of cracked, black rubber. Smells faintly of burnt ozone and highway breakdowns.', 'images/Items/snapped_fan_belt.png', category="Scrap Yard"), 1, 'images/Items/snapped_fan_belt.png'),
        ("a Exhaust Pipe with a Hole", Item('Exhaust Pipe', 'A curved, hollow steel pipe riddled with rust holes. Makes an excellent, if highly unsanitary, makeshift trumpet.', 'images/Items/exhaust_pipe.png', category="Scrap Yard"), 1, 'images/Items/exhaust_pipe.png')
    ]

    call screen trash_search_screen
    play sound trash
    with vpunch

    $ randomly_picked_bundle = renpy.random.choice(scrap_yard_pool)
    $ item_name = randomly_picked_bundle[0]
    $ actual_item = randomly_picked_bundle[1]
    $ item_quantity = randomly_picked_bundle[2]
    $ item_image_path = randomly_picked_bundle[3]

    show expression item_image_path at truecenter
    s "I found [item_name]."
    hide expression item_image_path

    $ Inventory.add_item(actual_item, item_quantity)

    # ~Show the inventory button on the screen, so the player can open it anytime, meow!~
    show screen Screen_InventoryButton

    # ~Display a simple message to indicate the start of the inventory, nya!~
    s "What do I give to the Alien?"

label recycling_centre:
    scene site2
    default recycling_centre_pool = [
        ("some Bubble Wrap", Item('Bubble Wrap', 'A crumpled sheet of plastic blisters. Highly addictive to pop, scientifically proven to reduce stress (or induce alien panic).', 'images/Items/bubble_wrap.png', category="Recycling Centre"), 1, 'images/Items/bubble_wrap.png'),
        ("some Tangled Earphones", Item('Tangled Earphones', 'A chaotic knot of thin white wires. Defines the laws of physics by violently tangling itself the moment you look away.', 'images/Items/tangled_earphones.png', category="Recycling Centre"), 1, 'images/Items/tangled_earphones.png'),
        ("a Smashed Smartphone", Item('Smashed Smartphone', 'A rectangular slab of dead tech with a beautifully shattered glass screen. Contains lost selfies and dead batteries.', 'images/Items/smashed_smartphone.png', category="Recycling Centre"), 1, 'images/Items/smashed_smartphone.png'),
        ("an Empty Bleach Bottle", Item('Empty Bleach Bottle', 'A white plastic jug with a faded warning label. The lingering chemical scent still burns the nostrils slightly.', 'images/Items/empty_bleach_bottle.png', category="Recycling Centre"), 1, 'images/Items/empty_bleach_bottle.png'),
        ("a Scratched CD", Item('Scratched CD', 'A reflective plastic disc covered in deep, circular scratches. Once held a 90s rom-com, now just reflects rainbows.', 'images/Items/scratched_cd.png', category="Recycling Centre"), 1, 'images/Items/scratched_cd.png'),
        ("a Cardboard Egg Carton", Item('Cardboard Egg Carton', 'A grey, molded pulp tray with twelve empty dimples. Surprisingly structurally sound despite smelling faintly of a fridge.', 'images/Items/cardboard_egg_carton.png', category="Recycling Centre"), 1, 'images/Items/cardboard_egg_carton.png'),
        ("a Crushed Soda Can", Item('Crushed Soda Can', 'A crumpled cylinder of faded aluminum. Still slightly sticky with evaporated high-fructose corn syrup.', 'images/Items/crushed_soda_can.png', category="Recycling Centre"), 1, 'images/Items/crushed_soda_can.png'),
        ("a Plastic Spork", Item('Plastic Spork', 'The ultimate dining compromise. Half spoon, half fork, entirely flimsy, and a masterclass in cheap plastic engineering.', 'images/Items/plastic_spork.png', category="Recycling Centre"), 1, 'images/Items/plastic_spork.png'),
        ("a Leaking AA Battery", Item('Leaking AA Battery', 'A tiny metal cylinder crusted in a powdery, corrosive white substance. You should probably wash your hands after holding this.', 'images/Items/leaking_aa_battery.png', category="Recycling Centre"), 1, 'images/Items/leaking_aa_battery.png'),
        ("a Floppy Disk", Item('Floppy Disk', 'A rigid square of 90s nostalgia with a slidey metal bit. Holds a whopping 1.44 megabytes of forgotten school projects.', 'images/Items/floppy_disk.png', category="Recycling Centre"), 1, 'images/Items/floppy_disk.png')
    ]

    call screen trash_search_screen
    play sound trash
    with vpunch

    $ randomly_picked_bundle = renpy.random.choice(recycling_centre_pool)
    $ item_name = randomly_picked_bundle[0]
    $ actual_item = randomly_picked_bundle[1]
    $ item_quantity = randomly_picked_bundle[2]
    $ item_image_path = randomly_picked_bundle[3]

    show expression item_image_path at truecenter
    s "I found [item_name]."
    hide expression item_image_path

    $ Inventory.add_item(actual_item, item_quantity)

    # ~Show the inventory button on the screen, so the player can open it anytime, meow!~
    show screen Screen_InventoryButton

    # ~Display a simple message to indicate the start of the inventory, nya!~
    s "What do I give to the Alien?"

label landfill:
    scene site3
    default landfill_pool = [
        ("a Squeaky Dog Toy", Item('Squeaky Dog Toy', 'A rubbery, brightly colored tube of fake meat. Emits a high-pitched, agonizing squeal when squeezed even slightly.', 'images/Items/squeaky_dog_toy.png', category="Landfill"), 1, 'images/Items/squeaky_dog_toy.png'),
        ("a Broken Spring-Loaded Mattress", Item('Broken Mattress', 'A stained, rectangular hazard of torn fabric and violently protruding rusty coils.', 'images/Items/broken_mattress.png', category="Landfill"), 1, 'images/Items/broken_mattress.png'),
        ("a Deflated Basketball", Item('Deflated Basketball', 'A flat, sad puddle of pebbled orange rubber. Has zero bounce and deeply negative morale.', 'images/Items/deflated_basketball.png', category="Landfill"), 1, 'images/Items/deflated_basketball.png'),
        ("a Cracked Lava Lamp", Item('Cracked Lava Lamp', 'A conical glass vessel containing cold, congealed globs of mysterious colored wax. It hasn\'t seen a dorm room in years.', 'images/Items/cracked_lava_lamp.png', category="Landfill"), 1, 'images/Items/cracked_lava_lamp.png'),
        ("a Toilet Seat", Item('Toilet Seat', 'A U-shaped piece of chipped, white plastic. It looks clean enough, but you still feel incredibly weird carrying it around.', 'images/Items/toilet_seat.png', category="Landfill"), 1, 'images/Items/toilet_seat.png'),
        ("a Rotting Teddy Bear", Item('Rotting Teddy Bear', 'A waterlogged plush toy missing an eye and half its stuffing. Radiates a deeply unsettling, haunted aura.', 'images/Items/rotting_teddy_bear.png', category="Landfill"), 1, 'images/Items/rotting_teddy_bear.png'),
        ("a Torn Umbrella", Item('Torn Umbrella', 'A skeletal mechanism of bent metal spokes and flappy, torn nylon. Barely qualifies as a rain shield anymore.', 'images/Items/torn_umbrella.png', category="Landfill"), 1, 'images/Items/torn_umbrella.png'),
        ("a Single Croc Shoe", Item('Single Croc Shoe', 'A brightly colored, foam-clog shoe riddled with holes. The absolute epitome of controversial human footwear.', 'images/Items/single_croc_shoe.png', category="Landfill"), 1, 'images/Items/single_croc_shoe.png'),
        ("a Broken Toaster", Item('Broken Toaster', 'A hollow, crumb-filled appliance with a jammed lever. Smells permanently of burnt bread and fire hazards.', 'images/Items/broken_toaster.png', category="Landfill"), 1, 'images/Items/broken_toaster.png'),
        ("a Disembodied Action Figure Head", Item('Disembodied Head', 'A tiny, plastic human head with pristine hair and a terrifyingly blank, unblinking smile. It feels like it\'s watching you.', 'images/Items/disembodied_head.png', category="Landfill"), 1, 'images/Items/disembodied_head.png')
    ]

    call screen trash_search_screen
    play sound trash
    with vpunch

    $ randomly_picked_bundle = renpy.random.choice(landfill_pool)
    $ item_name = randomly_picked_bundle[0]
    $ actual_item = randomly_picked_bundle[1]
    $ item_quantity = randomly_picked_bundle[2]
    $ item_image_path = randomly_picked_bundle[3]

    show expression item_image_path at truecenter
    s "I found [item_name]."
    hide expression item_image_path

    $ Inventory.add_item(actual_item, item_quantity)

    # ~Show the inventory button on the screen, so the player can open it anytime, meow!~
    show screen Screen_InventoryButton

    # ~Display a simple message to indicate the start of the inventory, nya!~
    s "What do I give to the Alien?"

return