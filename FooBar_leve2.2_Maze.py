## prepare-the-bunnies-escape

def solution(maze):
    DestX = len(maze[0])
    DestY = len(maze)
    x = 0
    y = 0
    steps = [0]

    while (x,y) is not (DestX - 1, DestY - 1):
        print(steps)
        if maze[x][y + 1] == 0 and y + 1 < DestY: # check the Right
            y += 1
            steps.append(DestX*x + y)
            continue
        if maze[x + 1][y] == 0 and x + 1 < DestX: # check the down
            x += 1
            steps.append(DestX*x + y)
            continue
        # if maze[x - 1][y] == 0 and : # check the down
        #     x += 1
        #     steps.append(DestX*x + y)
        #     continue
        print(x,y)
        print(steps.count())
    return steps.count()

asd = [1,2,3]
print(asd.count(element))
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))


