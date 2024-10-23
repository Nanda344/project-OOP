import random
class player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        pass

class randomcomputerplayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.aviable_mobes())
        return square    
class humanplayer(player)
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        valid_square = false
        val = None
        while not valid_square:
            square = input(f'giliran {self.letter}. masukan nomor kontak (0-8):')
            try:
                val = init(square)
                if val not in game.available_moves()
                    raise ValueError
                valid_square = True
            except ValueError:
                print('input tidak valid. coba lagi.')
        return val
class tictactoe:
    def __init__(self):
         self.boar = [' 'for _ in range(9)] #membuat papan 3x3
         self.current_winner = none #menyimpan pemenang
    @staticmethod
    def print_boar_nums():
        number_boar = [[str(i) for i in range(j*3, (j+1)*3)]  for j in range(3)] 
        for row in number_board:
            print('|'+'|'.join(row) +'|')
    def available_moves(self):
        retrun [i for i, spot in enumerate(self.board) if spot == '']

    def empety_squares(self):
        retrun ' ' in self.board

    def num_empty_squares(self):
        retrun self.board.count(' ')

    def make_move(self, square, letter):
        id self.board[square] == ' ':
        self.board[square] = letter
        if self.winner(square, letter):
            self.current_winner = letter

        return True
        return False

    def winner(self,square,letter):
        row_ind = square // 3
        row = self.board[now_ind*3(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8,]]
            if all([spot == letter for spot in row])

    


                
