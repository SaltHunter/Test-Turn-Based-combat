# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define e = Character("Eileen")

label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return # This defines the range in which damage is being dealt

# The game starts here.

label start:
    # Player Stats
    $ player_max_hp = 10
    $ player_hp = player_max_hp

    # Enemy Stats
    $ enemy_max_hp = 6
    $ enemy_hp = enemy_max_hp

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"


    label simple_battle:
        while player_hp > 0:
            # Player's Turn
            menu:
                "Attack":
                    $ enemy_hp -= 2
                    "That's a strong hit!  Enemy has [enemy_hp] hp!"
                    if enemy_hp <= 0:
                        "You win the combat encounter!"
                        jump simple_end
                "Don't Attack":
                    "You Don't Attack"        

        # Enemy Turn
            $ player_hp -= 2
            "The Enemy makes an attack, reducing you to [player_hp] hp!"

        "You Died!"    

    menu simple_end:
        "Play this level again?":
            jump simple_battle
        "Back to Main Menu":
            jump start                

    # This ends the game.

    return
