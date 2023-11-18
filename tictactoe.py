def sum(p, q, r):
    return p + q + r


def deshBoard(aState, bState):
    zero = 'X' if aState[0] else ('O' if bState[0] else 0)
    one = 'X' if aState[1] else ('O' if bState[1] else 1)
    two = 'X' if aState[2] else ('O' if bState[2] else 2)
    three = 'X' if aState[3] else ('O' if bState[3] else 3)
    four = 'X' if aState[4] else ('O' if bState[4] else 4)
    five = 'X' if aState[5] else ('O' if bState[5] else 5)
    six = 'X' if aState[6] else ('O' if bState[6] else 6)
    seven = 'X' if aState[7] else ('O' if bState[7] else 7)
    eight = 'X' if aState[8] else ('O' if bState[8] else 8)
    print(   f"{zero} | {one} | {two} "   )
    print(   "--|---|---")
    print(   f"{three} | {four} | {five} "   )
    print(   f"--|---|---"  )
    print(   f"{six} | {seven} | {eight} \n"  )


def checkWin(aState, bState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(aState[win[0]], aState[win[1]], aState[win[2]]) == 3:
            print("  !X Won the match!  \n")
            return 1
        if sum(bState[win[0]], bState[win[1]], bState[win[2]]) == 3:
            print("  !O Won the match!  \n")
            return 0
    return -1


if __name__ == "__main__":
    aState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    bState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("   ***Welcome to Tic Tac Toe Game***   ")
    print("     --- Let's Begin To Play ---   \n")
    while True:
        deshBoard(aState, bState)
        if turn == 1:
            print(" X's Chance \n")
            value = int(input("Enter the value : \n"))
            aState[value] = 1
        else:
            print(" O's Chance ")
            value = int(input("Enter the value : \n"))
            bState[value] = 1
        cwin = checkWin(aState, bState)
        if cwin != -1:
            print("Match over")
            break

        turn = 1 - turn
