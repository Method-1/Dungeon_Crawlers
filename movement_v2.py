from DungeonWorld import DungeonMap
from pickle_menu import *
from monster_treasure import *


class Movement:
    def __init__(self, startzone, endzone):
        self.start = (startzone[0], startzone[1])
        self.goal = endzone
        self.player = startzone
        self.walls = (0, 0)
        self.clean = ("\n" * 100)
        self.finished = 1

    def move_player(self, d, startzone, mapsize, a):
        x = self.player[0]
        y = self.player[1]
        pos = startzone

        if d == 'd':
            pos = (x + 1, y)
            banner_text("You move to the right...")

        elif d == 'a':
            pos = (x - 1, y)
            banner_text("You move to the left...")

        elif d == 'w':
            pos = (x, y - 1)
            banner_text("You take the stairs up...")

        elif d == 's':
            pos = (x, y + 1)
            banner_text("You take the stairs down...")

        else:
            pass

        print("------------------------")
        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print(self.clean)
            banner_text("You have made it to a very large mechanical door of sort, with a lever right next to it...")
            banner_text("there is also sunbeams coming in from the bottom of the door...")
            banner_text('"This must be the exit!" You think to yourself\n')
            last_choice = int(input("But do you greed more treasure or leave with what you have?\n1 = Stay\n2 = Leave\n"))

            if last_choice == 1:
                banner_text("You have decided to stay and return to the previous room...")
                input()
                self.player = (x, y)
                pos = self.player
                print(self.clean)

            else:
                # EXIT GAME! HIGHSCORE! SAVE CHARACTER!
                banner_text("You pull the lever and is met with fresh air and sound of outside, you leave the dungeon")
                input()
                quit_game()

        if (pos[1] < 0) or (pos[0] < 0) or (pos[0] > (mapsize - 1)) or (pos[1] > (mapsize - 1)):
            print(self.clean)
            print("As you leave the room, darkness sweeps over you! When you finally manage to find your bearings, your back in the previous room again...")
            input("Something doesn't let you leave this way... (OUTSIDE BOUNDS)")
            print(self.clean)
            self.player = (x, y)
            pos = self.player
        else:
            a.board[self.goal[1]][self.goal[0]] = "E"
            a.board[self.player[1]][self.player[0]] = "O"
            a.board[y][x] = "-"
            a.board[self.start[1]][self.start[0]] = "S"

def allowed(self, d):
    allowed_movement = 'wasd'
    test = d
    while True:
        try:
            if test in allowed_movement and len(test) != 0 and len(test) == 1:
                break
            else:
                input("\nYou think to yourself, is that really a direction? (INPUT ERROR)\n")
                return test
        except:
            print("Input Error")
            return test


def ok(mapsize, startzone, endzone):
    c = Movement(startzone, endzone)
    a = DungeonMap(mapsize)

    while c.player != c.goal:
        a.display_map()
        d = input("Which way? (d, a, w, s)  >>")
        c.move_player(d, startzone, mapsize, a)
