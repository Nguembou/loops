input.onButtonPressed(Button.A, function () {
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
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 4; index++) {
        for (let index = 0; index < 4; index++) {
            player.move(1)
            basic.pause(200)
        }
        player.turn(Direction.Right, 90)
    }
})
let player: game.LedSprite = null
player = game.createSprite(0, 0)
basic.forever(function () {
	
})
