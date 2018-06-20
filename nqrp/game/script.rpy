# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define modi = Character("Modi", color="#900090")
define kc = Character("Kayce", color="#3050a0")
define casey = Character("Casey", color="#c0b9ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show case idle
    show case idle at right
    show case idle at left
    show case idle
    show case talk

    kc "..."

    kc "weed"

    show case idle at right
    show modi talk at left

    modi "weede"

    show case mad at right 

    kc "weede?"

    show case

    show modi mad at left

    modi "weed"

    show casey hap at center

    casey "weed"

    show case mad at right 

    kc "WEED"

    show modi talk at left

    modi "WEED"

    show casey talk at center

    casey "WEED"

    show case mad at right 

    kc "WEED"

    show modi talk at left

    modi "WEED"

    show casey talk at center

    casey "WEED"


    # These display lines of dialogue.


    # This ends the game.

    return
