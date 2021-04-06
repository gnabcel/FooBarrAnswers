## prepare-the-bunnies-escape

def solution(maze):
    steps = 999999
    for count, value in enumerate([j for i in maze for j in i]): ## wall tracker
        if value == 1:
            maze[count // len(maze)][count % len(maze)] = 0
            if counter(maze) != 0 and counter(maze) < steps:
                steps = counter(maze)
            maze[count // len(maze)][count % len(maze)] = 1
    return steps

def counter(maze):
    DestX = len(maze)
    x = 0
    y = 0
    steps = [0]
    while DestX * DestX - 1 not in steps :
        if x + 1 < DestX and maze[x + 1][y] == 0 and DestX*(x+1) + y not in steps: # check the down
            x += 1
            steps.append(DestX*x + y)
            continue
        if y + 1 < DestX and maze[x][y + 1] == 0 and DestX*x + y + 1 not in steps: # check the Right
            y += 1
            steps.append(DestX*x + y)
            continue
        if y - 1 >= 0 == maze[x][y - 1] and DestX*x + y - 1 not in steps: # check left
            y -= 1
            steps.append(DestX*x + y)
            continue
        steps = []
        break
    return len(steps)

# Test line:
# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

