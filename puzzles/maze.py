import random
from utils import Coords
import math
import time

class Maze:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty is not None:
            # Setting size by difficulty
            if self.difficulty == 1:
                self.width = 5
                self.height = 5
            elif self.difficulty == 2:
                self.width = 7
                self.height = 7
            elif self.difficulty == 3:
                self.width = 11
                self.height = 11
            else:
                return print("ERROR: Out of index for maze puzzle difficulty. Please use difficulties 1(Easiest) to 3(Hardest)")

            # Generate the Plane
            self.coordinates = []
            for x in range(self.width):
                for y in range(self.height):
                    self.coordinates.append((x, y))

            self.spawnpoint = Coords.Coords(random.randint(0, self.width), random.randint(0, self.height))
            self.endpoint = Coords.Coords(random.randint(0, self.width), random.randint(0, self.height))
            self.point_difference = math.sqrt(math.pow((self.endpoint.get_x() - self.spawnpoint.get_x()), 2) + math.pow((self.endpoint.get_y() - self.spawnpoint.get_y()), 2))

            while(self.point_difference < (self.difficulty * 2)):
                self.spawnpoint = Coords.Coords(random.randint(0, self.width), random.randint(0, self.height))
                self.endpoint = Coords.Coords(random.randint(0, self.width), random.randint(0, self.height))
                self.point_difference = math.sqrt(math.pow((self.endpoint.get_x() - self.spawnpoint.get_x()), 2) + math.pow((self.endpoint.get_y() - self.spawnpoint.get_y()), 2))

            self.player_coords = self.spawnpoint
        else:
            print("ERROR: Please specify a maze difficulty")

    def move(self, direction):
        if direction == "north" or direction == "n":
            pointer = self.player_coords.get_y() + 1
            if not(pointer > self.height):
                self.player_coords.set_y(self.player_coords.get_y() + 1)
            else:
                return print("You cannot go past the border!")
        elif direction == "south" or direction == "s":
            pointer = self.player_coords.get_y() - 1
            if not(pointer < 0):
                self.player_coords.set_y(self.player_coords.get_y() - 1)
            else:
                return print("You cannot go past the border!")
        elif direction == "east" or direction == "e":
            pointer = self.player_coords.get_x() + 1
            if not(pointer > self.width):
                self.player_coords.set_x(self.player_coords.get_x() + 1)
            else:
                return print("You cannot go past the border!")
        elif direction == "west" or direction == "w":
            pointer = self.player_coords.get_x() - 1
            if not(pointer < 0):
                self.player_coords.set_x(self.player_coords.get_x() - 1)
            else:
                return print("You cannot go past the border!")

    def success(self):
        print("Congrats! You win!")
        time.sleep(5)
        quit()
    def failure(self):
        print("You have failed!")
