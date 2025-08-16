def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
        music.PlaybackMode.IN_BACKGROUND)
    for index in range(2):
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        basic.pause(100)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if input.light_level() < 50:
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_DOWN),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            . . # # .
            . . . # #
            . . . # #
            . . . # #
            . . # # .
            """)
    else:
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            """)
    basic.pause(5000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
        music.PlaybackMode.IN_BACKGROUND)
    basic.clear_screen()
    basic.pause(100)
    basic.show_string("Hello!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.SURPRISED)
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_icon(IconNames.HAPPY)