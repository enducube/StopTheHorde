"""
Stop The Horde by enducube
Based on a game concept made by Axolotl and enducube
"""

import random
import tcod

WIDTH, HEIGHT = 64,64

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def main():
    tileset = tcod.tileset.load_tilesheet(
        "data/tiles2.png",16,16,tcod.tileset.CHARMAP_CP437
    )

    with tcod.context.new(width=480,height=480,tileset=tileset) as context:
        console = context.new_console(WIDTH,HEIGHT,2)
        while True:
            console.clear()
            console.print(8,8,"@")
            context.present(console,keep_aspect=True)
            for event in tcod.event.get():
                print(event)
                if isinstance(event, tcod.event.Quit): # quit
                    raise SystemExit()


if __name__ == "__main__":
    main()