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
#Test
# The game starts here.

label start:
    # Player Stats
    $ player_max_hp = 1000
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
            call dice_roll
            # Player's Turn
            menu:
                "Attack":
                    if d10 >= 9:                                                # 20% crit
                        $ player_attack_value = d6 + d4
                        $ enemy_hp -= player_attack_value
                        "That ought'a leave a mark, Critical Hit!  You hit for [player_attack_value] damage!"
                    elif d10 >= 5:                                              # 40%  hit
                        $ player_attack_value =  d4                                        
                        $ enemy_hp -= player_attack_value
                        "That's a strong hit!  Enemy takes [player_attack_value] hp!"
                    else:                                                       # 40%  miss
                        "You miss!"  

                "Don't Attack":
                    "You Don't Attack"

            if enemy_hp <= 0 and player_hp > 5:
                    "You destroyed the enemy!"
                    jump simple_end    
            elif enemy_hp <=0 and player_hp <= 5:
                    "You barely made it out alive"
                    jump simple_end
        # Enemy Turn
            call dice_roll

            if d20 >= 19:                                            # 20% Crit                                                                                     
                $ player_hp -= d10
                "The Enemy makes a wild attack for [d10] damage!"
            elif d20 <=2:                                            # 20% Heal for 4
                $ enemy_hp += d4
                if enemy_hp < enemy_max_hp:
                    "The Enemy heals itself, raising [d4] hp!"
                else: # Full heal
                    $ enemy_hp = enemy_max_hp
                    "The Enemy fully heals itself back to full hp!"
            else:                                                    # 60% Standard Attack                                                                           
                $ player_hp -= d4
                "The Enemy attacks for [d4] damage!"

        "You Died!"    

    menu simple_end:
        "Play this level again?":
            jump simple_battle
        "Back to Main Menu":
            jump start                

    # This ends the game.

    return
