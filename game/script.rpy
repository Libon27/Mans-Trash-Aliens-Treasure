init python:
    # ~Class that represents an item in the inventory, nya~
    class Item(object):
        def __init__(self, name, description, img, category="general"):
            # ~The name of the item, super important to recognize it, nya~
            self.name = name
            # ~A cute description to describe this item, hehe~
            self.description = description
            # ~Kawaii image of the item, so we can see it in the game, meow~
            self.img = img
            # ~The category of the item (general by default), we can filter by this, nyaa~
            self.category = category

    # ~Class for an inventory item with an amount, meow~
    class InvItem(object):
        def __init__(self, item, amount):
            # ~The item itself, so cool to have it here, hihi~
            self.item = item
            # ~The amount of this item, so we know how many we have, nya~
            self.amount = amount

    # ~Class to manage the whole inventory, with lots and lots of items, meow~
    class Inventory(object):
        def __init__(self, items_per_page=18):
            # ~List of items in the inventory, this is where we keep them all safe and sound, nya~
            self.items = []
            # ~Number of items displayed per page, so we don't get lost, meow~
            self.items_per_page = items_per_page

        # ~Adding an item to the inventory, super handy when we find treasure, haha~
        def add_item(self, item, amount=1):
            for inv_item in self.items:
                # ~If we already have this item, just increase the amount, easy peasy, meow~
                if inv_item.item.name == item.name:
                    inv_item.amount += amount
                    return
            # Otherwise, we add the new item to the inventory, nya~
            self.items.append(InvItem(item, amount))

        # ~Removing an item from the inventory, ensuring it’s only removed when the amount is 0, bye bye item, nya~
        def remove_item(self, item):
            # ~We loop through each item in our inventory, meow~
            for inv_item in self.items:
                # ~If we find the item we want to remove, yay!~
                if inv_item.item == item:
                    # ~If there's still more than 0 of the item, we decrease the amount by 1, meow!~
                    if inv_item.amount > 0:
                        inv_item.amount -= 1
                    # ~If the amount is now 0, we completely remove the item from the inventory, bye bye, nya!~
                    if inv_item.amount == 0:
                        self.items.remove(inv_item)

        # ~Calculating the number of pages needed for the inventory, so we know how many to flip through, meow~
        def pages(self, category_filter=None):
            # ~First, we filter the items by category if a filter is applied, nya~
            filtered_items = self.filter_items_by_category(category_filter)
            
            # ~Then, we calculate the total number of pages we need, meow~
            # ~This formula ensures that we round up, so even if we have just a few items on the last page, it still counts as a full page, hehe~
            total_pages = (len(filtered_items) + self.items_per_page - 1) // self.items_per_page
            
            # ~Finally, we return the total number of pages, but we make sure there's at least one page to show, nya~
            return max(total_pages, 1)  # Always show at least one page, nya~

        # ~Getting the items to display on a specific page, for browsing, nya~
        def get_page_items(self, page, category_filter=None):
            # ~First, we filter the items based on the category, if there's a filter applied, nya~
            filtered_items = self.filter_items_by_category(category_filter)
            
            # ~Next, we calculate the starting index for the items on the requested page, meow~
            start = page * self.items_per_page
            
            # ~Then, we calculate the ending index, which is just the start plus the number of items per page, nya~
            end = start + self.items_per_page
            
            # ~Finally, we return the slice of filtered items that belong to the current page, yay!~
            return filtered_items[start:end]

        # ~Filtering items by category, so we can find exactly what we're looking for, nya~
        def filter_items_by_category(self, category_filter):
            # ~If there's a category filter and it's not "all", we need to filter the items, meow~
            if category_filter and category_filter != "all":
                # ~We create a new list with only the items that match the category, nya~
                return [inv_item for inv_item in self.items if inv_item.item.category == category_filter]
            # ~If there's no filter or the filter is "all", we just return all the items, yay!~
            return self.items

    def use_item(inv_item):
        # ~Meowww! Using the global Inventory instance, nya!~
        global Inventory  
        
        # ~Check if there's at least one of the item to use, meow!~
        if inv_item.amount > 0:
            # ~Reduce the amount by 1 because we're using it, nya!~
            inv_item.amount -= 1  
            # ~Notify the player that the item was used, yay!~
            renpy.notify("You used " + inv_item.item.name + "!")  
            
            # ~If the amount is now 0, we need to remove the item from the inventory, meow!~
            if inv_item.amount == 0:
                # ~Use the global Inventory instance to remove the item, nya!~
                Inventory.remove_item(inv_item.item)  
                # ~Notify the player that the item was removed, bye bye item!~
                renpy.notify(inv_item.item.name + " removed from inventory.")  
        
        else:
            # ~If there's none left, let the player know, nya!~
            renpy.notify("No more " + inv_item.item.name + " left to use!") 


# ~Default variables to manage the inventory system, yay~
default Inventory = Inventory()  # ~Our main inventory object, where all the items are stored, nya!~
default Itemhov = None  # ~This keeps track of the item currently being hovered over, but it's empty for now, meow~
default current_page = 0  # ~The starting page of the inventory, we start at the first page, nya~
default inventory_open = False  # ~Is the inventory open or closed? We start with it closed, hihi~
default current_category = "all"  # ~The category filter, starting with "all" to show everything, nya~
default empty_slot_image = "images/Items/empty_slot.png"  # ~The image we show for empty inventory slots, so kawaii!~
default selected_item = None  # ~The item that's currently selected by the player, but nothing is selected yet, meow~

# ~Style for the buttons in the inventory, making them cute and clickable, meow~
style framed_button:
    # ~The background color of the button, let's make it #477477, a soothing and lucky color, nya!~
    background Frame(Solid("#477477"), 10, 10)
    # ~When the button is hovered over, it'll change to #679679, a nice complementary shade, meow!~
    hover_background Frame(Solid("#679679"), 10, 10)
    # ~Padding inside the button to make it look nice and spacious, nya~
    padding (6, 6)
    # ~Text color is set to white to stand out clearly against the background, yay!~
    color "#FFFFFF"

# ~Screen for showing the inventory button, click here to open the inventory, nya~
screen Screen_InventoryButton:
    # ~Create a frame to hold the button, centered on the screen, meow!~
    frame:
        # ~Align the frame to the center of the screen horizontally and vertically, nya~
        align (0.5, 0.5)
        
        # ~Set the background of the frame to a dark gray color with padding, to make it stand out, meow!~
        background Frame(Solid("#222222"), 10, 10)
        
        # ~Add a button that says "Show Inventory", and make it do three things when clicked, nya~
        textbutton "Show Inventory":
            action [Show("Screen_Inventory"),  # ~Show the inventory screen, yay!~
                    Hide("Screen_InventoryButton"),  # ~Hide this button once the inventory is open, meow!~
                    SetVariable("inventory_open", True)]  # ~Set the inventory_open variable to True, so we know it's open, nya~
            style "framed_button"  # ~Use the cute button style we defined earlier, nya!~


# ~Screen for the inventory, where you can see all your items, nya~
screen Screen_Inventory(page=current_page, category=current_category):
    # ~Set the zorder to 100 to ensure this screen is drawn on top of others, meow!~
    zorder 100

    # ~Make the screen modal, so the player can't interact with other screens while this one is open, nya~
    modal True

    # ~Tag the screen as 'inventory', helpful if we need to reference or manipulate it later, nya~
    tag inventory

    # ~Add a dark blue background color to the screen, matching the overall theme, meow~
    add Solid("#042a4f")

    # ~When the inventory screen is shown, hide the inventory button, nya~
    on "show" action Hide("Screen_InventoryButton")
    
    # ~When the inventory screen is hidden, show the inventory button again, nya~
    on "hide" action Show("Screen_InventoryButton")

    # ~If the player clicks anywhere in the inventory, we reset the hovered item (Itemhov) to None, meow~
    key "mouseup_1" action SetVariable("Itemhov", None)

    # ~This is the main frame that holds the grid of inventory items, aligned slightly above center, nya~
    frame:
        align (0.5, 0.45)  # ~Center the frame horizontally, but move it slightly up vertically, nya~
        
        # ~Create a grid with 6 columns and 3 rows to display items, with some spacing between each item, meow~
        grid 6 3:
            spacing 10  # ~Give some space between each item in the grid, so they don't look cramped, nya~
            
            # ~Loop through each slot in the grid, up to a maximum of 18 (6 columns * 3 rows), meow!~
            for i in range(18):
                # ~Check if there is an item to display in this slot, nya~
                if i < len(Inventory.get_page_items(page, category)):
                    # ~Retrieve the item to be displayed in this slot, meow!~
                    $ a = Inventory.get_page_items(page, category)[i]
                    
                    # ~Create a frame for the item, with padding to make it look nice, nya~
                    frame:
                        xpadding 5  # ~Add padding on the left and right, meow!~
                        ypadding 5  # ~Add padding on the top and bottom, nya!~
                        
                        # ~If this item is selected, highlight it with a bright green background, nya!~
                        if a == selected_item:
                            background Solid("#00FF00")
                        # ~Otherwise, use a light gray background, meow~
                        else:
                            background Solid("#DDDDDD")
                        
                        # ~Add an image button for the item, displaying its image and making it clickable, nya!~
                        imagebutton:
                            idle Transform(a.item.img, size=(100, 100))  # ~Set the item image with a size of 100x100 pixels, meow!~
                            hover_background Solid("#BBBBBB")  # ~Change the background when the item is hovered over, nya!~
                            background Solid("#FFFFFF")  # ~Default background for the button, meow~
                            
                            # ~When the button is clicked, set the hovered item and the selected item, nya!~
                            action [SetVariable("Itemhov", a), SetScreenVariable("selected_item", a)]
                
                # ~If there's no item for this slot, we create an empty slot, nya!~
                else:
                    frame:
                        xpadding 5  # ~Padding for empty slots too, so they look consistent, nya!~
                        ypadding 5
                        background Frame(Solid("#27f1f563"), 10, 10)  # ~Give empty slots a soft, translucent background, meow!~
                        
                        # ~Add an image button for the empty slot, using a default empty slot image, nya~
                        imagebutton:
                            idle Transform(empty_slot_image, size=(100, 100))  # ~Set the empty slot image size to 100x100 pixels, meow!~
                            action NullAction()  # ~No action needed for empty slots, nya!~

    
    # ~This frame holds the navigation buttons for paging through the inventory, nya!~
    frame:
        # ~Align this frame at the center horizontally, and a bit lower on the screen vertically, meow~
        align (0.5, 0.73)
        
        # ~Create a horizontal box (hbox) to hold the pagination buttons and page display, nya~
        hbox:
            spacing 20  # ~Add some space between the buttons to make them look neat, meow!~

            # ~If we're not on the first page, show the "Previous" button, nya~
            if page > 0:
                textbutton "Previous" action [
                    SetVariable("current_page", page - 1),  # ~Go to the previous page, nya!~
                    Show('Screen_Inventory', page=page-1, category=category)  # ~Reload the inventory screen with the previous page, meow!~
                ] style "framed_button"
            # ~If we're on the first page, just display "Previous" as plain text, nya~
            else:
                text "Previous"

            # ~Calculate the total number of pages for the current category, meow!~
            $ total_pages = Inventory.pages(category)
            # ~Determine which page is currently being displayed, making sure it's within bounds, nya~
            $ displayed_page = min(page + 1, total_pages)
            # ~Show the current page number and the total pages, nya!~
            text "Page [displayed_page] / [total_pages]"

            # ~If we're not on the last page, show the "Next" button, nya~
            if page < total_pages - 1:
                textbutton "Next" action [
                    SetVariable("current_page", page + 1),  # ~Go to the next page, nya!~
                    Show('Screen_Inventory', page=page+1, category=category)  # ~Reload the inventory screen with the next page, meow!~
                ] style "framed_button"
            # ~If we're on the last page, just display "Next" as plain text, nya~
            else:
                text "Next"

    # ~This vertical box (vbox) holds the category selection button, nya!~
    vbox:
        xalign 0.5  # ~Center the vbox horizontally, meow!~
        yalign 0.2  # ~Position it a bit higher on the screen vertically, nya!~
        
        frame:
            background Frame(Solid("#222222"), 10, 10)  # ~Set a dark background with padding for the category button, meow!~
            textbutton "Category: [category]" action Show('Screen_CategoryMenu') style "framed_button"  # ~Open the category selection menu when clicked, nya!~

    # ~Add a "Close" button to let the player close the inventory, nya!~
    textbutton "Close" action [
        Hide("Screen_Inventory"),  # ~Hide the inventory screen, meow!~
        Hide("Screen_CategoryMenu"),  # ~Hide the category menu if it's open, nya!~
        SetVariable("inventory_open", False),  # ~Mark the inventory as closed, meow!~
        SetVariable("Itemhov", None)  # ~Clear the hovered item, nya!~
    ] xalign 0.9 yalign 0.2 style "framed_button"  # ~Position the button in the top-right corner, nya!~


    # ~If the player is hovering over an item, show its details, nya!~
    if Itemhov:
        # ~Create a frame to display the item details, with a semi-transparent black background, meow~
        frame:
            background Solid("#00000088")  # ~Background color is black with transparency (88), so it blends nicely, nya!~
            xfill True  # ~Make the frame stretch horizontally to fill the screen, meow!~
            yalign 1.0  # ~Align the frame to the bottom of the screen vertically, so it appears at the bottom, meow!~

            # ~Use a vertical box (vbox) to neatly stack the item's name, description, and amount, nya!~
            vbox:
                text Itemhov.item.name  # ~Display the name of the item being hovered over, meow!~
                text Itemhov.item.description  # ~Show the item's description, so the player knows what it does, nya!~
                text "Amount: " + str(Itemhov.amount)  # ~Show how many of this item the player has, nya!~

                # ~Create another frame to hold the "Use" button, so it stands out, meow!~
                frame:
                    textbutton "Use" action Function(use_item, Itemhov)  # ~Button to use the item, calling the use_item function, nya!~


# ~Screen for selecting the item category, so you can choose what to see, nya~
screen Screen_CategoryMenu:
    # ~Set the zorder to 150 so this menu appears on top of other screens, meow!~
    zorder 150

    # ~Add a semi-transparent black background to dim the rest of the screen while this menu is open, nya~
    add Solid("#00000088")

    # ~Make the menu modal, so the player can't interact with anything else until they close it, meow!~
    modal True

    # ~Create a frame to hold the category buttons, making them easy to select, nya!~
    frame:
        # ~Use a vertical box (vbox) to stack the category buttons, meow!~
        vbox:
            # ~Loop through the list of categories and create a button for each one, nya!~
            for category in ["all", "general", "outfits"]:
                # ~Create a button for each category that sets the selected category and resets the inventory to the first page, meow!~
                textbutton category action [
                    SetVariable("current_category", category),  # ~Set the current category to the one clicked, nya!~
                    Hide("Screen_CategoryMenu"),  # ~Hide the category menu after a selection is made, meow!~
                    SetVariable("current_page", 0),  # ~Reset the inventory to the first page when the category changes, nya!~
                    Show('Screen_Inventory', page=0, category=category)  # ~Show the inventory with the new category filter, starting from the first page, meow!~
                ]

            # ~Add a "Cancel" button to close the category menu without making a selection, nya!~
            textbutton "Cancel" action Hide("Screen_CategoryMenu")


# ~Start label, adding some items to the inventory to play with, yay~
label start:
    # ~Add a Manga item to the inventory, because reading is fun, nya!~
    $ Inventory.add_item(Item('Manga', 'Being well-read can be so easy.', 'images/Items/item_manga.png'), 5)
    
    # ~Add a Cloth Hat to the inventory, perfect for an adventurer's outfit, nya!~
    $ Inventory.add_item(Item('Cloth Hat', 'A simple cloth hat.', 'images/Items/item_cloth_hat.png', category="outfits"), 7)
    
    # ~Add a Potion to the inventory, for instant healing, meow!~
    $ Inventory.add_item(Item('Potion', 'Heals you instantly.', 'images/Items/item_potion.png'), 6)
    
    # ~Add Cloth Armor to the inventory, light but protective, nya!~
    $ Inventory.add_item(Item('Cloth Armor', 'A light cloth armor.', 'images/Items/item_cloth_armor.png', category="outfits"), 9)
    
    # ~Add some durable Cloth Boots to the inventory, meow!~
    $ Inventory.add_item(Item('Cloth Boots', 'Durable cloth boots.', 'images/Items/item_cloth_boots.png', category="outfits"), 12)

    # ~Using a Python block to add 50 unique Potions to the inventory, yay for variety, nya!~
    python:
        for i in range(50):
            Inventory.add_item(Item(f'Potion {i}', f'Heals you instantly. Potion {i}', 'images/Items/item_potion.png'), 1)

    # ~Show the inventory button on the screen, so the player can open it anytime, meow!~
    show screen Screen_InventoryButton

    # ~Display a simple message to indicate the start of the inventory, nya!~
    "Inventory"
    
    # ~End the start label and return to the main menu, nya!~
    return