class TaTeTi:
    def __init__(self, board=[' ' for _ in range(9)]):
        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    def full(self):
        for i in self._board:
            if i == ' ':
                return False
        return True
    
    def win(self):
        x = 0
        o = 0
        for i in self._board:
            if i == 'o':
                o = o + 1
                x = 0
            elif i == 'x':
                x = x + 1
                o = 0
            elif i == ' ':
                continue
            if x == 3 or o == 3:
                return True
            
        return False

    def validate(self, position):
        if self._board[position-1] == ' ':
            return True
        return False

    def draw_board(self):
        board = []
        num = 0
        for i in range(9):
            num = num + 1
            if self._board[i] != ' ':
                board.append(self._board[i])
            else:
                board.append(num)

        return '\n {} | {} | {} \n---+---+---\n {} | {} | {} \n---+---+---\n {} | {} | {} \n'.format(
            board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])

    def assign(self, position, piece):
        if self.validate(position):
            self._board[position-1] = piece
        else:
            raise(ValueError)
        