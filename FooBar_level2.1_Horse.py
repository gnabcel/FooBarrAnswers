# CHESS MOVE CABALLO

def valores(num):
    sol = []
    x = num // 8
    y = num % 8
    for z in (-2,+2):
        for w in (-1,+1):
            z1 = x + z
            z2 = y + w
            z3 = x + w
            z4 = y + z
            if 7 >= z1 >= 0 and 7 >= z2 >= 0:
                sol.append((z1 * 8 + z2))
            if 7 >= z3 >= 0 and 7 >= z4 >= 0:
                sol.append((z3 * 8 + z4))
    return sol

def solution(src, dest):
    numberMoves = 1
    possibles = valores(src)
    posNew = []
    posOld = [src]
    if src == dest:
        return 0
    else:
        while dest not in possibles:
            for x in possibles:
                for c in valores(x):
                    if c not in posOld and c not in posNew:
                        posNew.append(c)
            posOld.append(possibles)
            possibles = posNew
            posNew = []
            numberMoves += 1
    return numberMoves

# print(solution(0,1))

