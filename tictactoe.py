
class Tic_Tac_Toe:
    #class Tic_Tac_Toe
    def __init__(self):
        self.board = [" "]*9

    def print_board(self):
        print("""
          {} | {} | {}
         ____|____|______
          {} | {} | {}
         ____|____|______
          {} | {} | {}
        """.format(*self.board))



    def available_moves(self):
        moves = []
        for x in range(0, len(self.board)):
            if self.board[x] == " ":
                moves.append(x)
        return moves



    def move(self, position, player):
        self.board[position] = player

    def check_win(self,player):
        combinations = ([0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6])
        win=False

        for combo in combinations:
            if self.board[combo[0]]==self.board[combo[1]]==self.board[combo[2]]==player:
                win=True
        return win       

    def game_over(self):
        if self.check_win("X")==True or self.check_win("O")==True:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    def minimax(self, node,  player):

        if node.game_over():
            if node.check_win("X") ==True:
                return 0
            elif node.check_win("O") ==True :
                return 100
            else:
                return 50

        if player == "O":
            bestValue = 0
            for move in node.available_moves():
                node.move(move, player)
                moveValue = self.minimax(node,  "X")
                node.move(move, " ")
                bestValue = max(bestValue, moveValue)
            return bestValue
        
        if player == "X":
            bestValue = 100
            for move in node.available_moves():
                node.move(move, player)
                moveValue = self.minimax(node,  "O")
                node.move(move, " ")
                bestValue = min(bestValue, moveValue)
            return bestValue

def cpu_move(board):

    choices = []
    
    for moves in board.available_moves():
        board.move(moves, "O")
        moveValue = board.minimax(board, "X")
        board.move(moves, " ")

        if moveValue >50:
            choices = [moves]
        elif moveValue == 50:
            if not choices:
                choices.append(moves)

    return choices[0]




def main():
    game = Tic_Tac_Toe()

    while game.game_over()!=True:
        human = int(raw_input("You are X......... Choose a number from 1 to 9: "))
        game.move(human-1, "X")
        game.print_board()

        if game.game_over() == True:
            break

        cpu = cpu_move(game)
        game.move(cpu, "O")
        game.print_board()

    if game.check_win("X") == True:
        print"X won"
    elif game.check_win("O") ==True:
        print "O won"
    elif game.game_over() == True:
        print "match tie"
if __name__=="__main__":
    main()
