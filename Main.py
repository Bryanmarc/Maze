from puzzles import maze

test = maze.Maze(3)

print("Plane Data: " + str(test.coordinates) + "\n")
print("Spawnpoint: " + test.spawnpoint.get() + "\n")
print("Player_Coords: " + test.player_coords.get() + "\n")
print("Endpoint: " + test.endpoint.get() + "\n")
print("Point Difference: " + str(test.point_difference) + "\n")

while(1):
    print("Coords: " + test.player_coords.get())
    a = str(input("Move> "))
    test.move(a.lower())

    if test.player_coords.get() == test.endpoint.get():
        test.success()
