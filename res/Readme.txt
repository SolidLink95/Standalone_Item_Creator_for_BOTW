Standalone Items Creator v1.0 by banan039

What is it?
Handy tool that creates standalone items. For now all weapons and armor pieces are supported. It produces a graphic pack containing:
-full directories structure (content\Model, content\Actor etc.),
-creating .sbactorpack files,
-Actorinfo entries,
-bfres and sbitemico files for new items (the models need to be changed manually in Switch Toolbox or other tool),
-save flags in Bootup.pack,
-proper names and descriptions visible in game,
-crafting requirements specified by user,

Moreover all items are automatically available to buy at Ancient Oven Cherry. After creating a mod pack You still need to install it with BCML!

The main directory is set up the same way as for Ice Spear: https://www.youtube.com/watch?v=WHY5h1Xa5d4
After configuring main directory, open config.ini and change:
-switch_path: absolute path to switch dump (should end with 'content')
-wiiu_path: absolute path to wiiu dump (should end with 'content')
-mods_path: the absolute path in which mod packs will be created.
-lang: the default language file
-mode: either switch or wiiu

There are 2 buttons at the top: Armor and Weapon. If you want to add weapon to pack press "Weapon", if armor piece - "Armor". In order to indicate which tab you are using, refer to text "Weapon data" or "Armor data" at the top.

Game Language: choose the language
Mod name: the name of the mod. Can't be left blank
Actor template: the template which the creator will base on. If any other subsequent fields will be left blank, the creator use the values from within the template.
Actor ID: The new ID of newly created item. I recommend keeping with default botw naming convention, for example Weapon_Sword_XXX where XXX is new unused number instead of My_pretty_pink_sword.
Sheath: the name of the sheath new weapon will use. This entry gets grayed out if you switch to Armor tab.
Attack/Defence: a value that determines how much attack will new weapon deal or how much new shield or armor piece will give.
Life: durability of the new item. Grayed out if you use Armor tab.
Is unbreakable: turn new item unbreakable (True) or not (False). Grayed out if you use Armor tab.
Elink: the effect of the weapon\armor. Leave empty if you want to keep the same elink from the template.
Slink: sound of the weapon\armor. Leave empty if you want to keep the same slink from the template.
Profile: the profile of the item. If left blank the creator will determine it basing on Actor name field.
Magic: if you are copying a rod, then you can choose one of the magic projectiles from the list. If You want to use some custom actor entry feel free to type it manually. Works only if you are copying a rod type item.
Infinite magic: choose whether the new rod type weapon will need a recharge after use or not. Works only if you are copying a rod type item. Does not affect shields.
Subtype: choose subtype of the weapon.
Price: choose how much new weapon will cost. Leave empty if you want to keep the same value from the template.
Item name: name your new item here, it is the name that will be displayed ingame.
Description: the description of the new item. Make sure to keep it short enough to fit botw popup windows (usually 4 lines long)

Crafting requirements: choose from the list the crafting costs of an item. If the field is left empty the default values (bokoblins body parts) will be put there.

The fields appearing only in Armor tab:
Effect: bonus which new armor piece will give. Leave empty if you want to keep the same value from the template.
Effect level: effect level. Setting higher than 2 or 3 may break the item. Leave empty if you want to keep the same value from the template.
Series: the armor series type. Leave empty if you want to keep the same value from the template.

On the right there is "Mod content" list. It specifies which items are in current mod pack.

The buttons on the botom, from left to right:
Exit: Exit
Options: there you must set default language, the content folder location and mods path where the mod packs will be created.
Clear: start creating anew, removes all items from "Mod content" list.
Add weapon/armor to pack: adds new item to "Mod content". If there are 2 items in the same mod pack with the same name creator will prompt if you want to overwrite the existing entry.
Save to file: saves current session to json file in jsons folder. The file name is the same as "Mod name" field. If "Mod field" is empty, current session will be saved as tmp.json
Open from file: load previously saved file into the creator
Create mod: creates a mod pack from current session.
Remove from mod: removes an item selected from "Mod content" list. 
Edit: loads the item selected from "Mod content" list. 
View Readme: display this message