def on_button_pressed_a():
    player.change(LedSpriteProperty.Y, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.Y, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.Y, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.Y, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.X, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.X, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.X, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.X, 1)
    basic.pause(100)
    player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index in range(4):
        for index2 in range(4):
            basic.pause(200)
            player.move(4)
        player.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

player: game.LedSprite = None
player = game.create_sprite(0, 0)

def on_forever():
    pass
basic.forever(on_forever)
