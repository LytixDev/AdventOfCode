horisontal = vertical = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        cmd, val = line.split(" ")
        if cmd == "forward":
            horisontal += int(val)
        elif cmd == "down":
            vertical += int(val)
        else:
            vertical -= int(val)
    
print(horisontal * vertical)
