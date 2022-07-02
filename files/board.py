import pygame
from .piece import Piece
from .constants import BLACK, BLUE, COLS, GREY, RADIUS, ROWS, RED, SQUARE_SIZE, WHITE

class Board:

    def __init__(self):
        self.board = []
        # self.selected_piece = None
        self.red_left = self.blue_left = 16
        self.valids = {(0,0):[(0,2),(1,1)], 
                        (0,2):[(0,0), (0,4),(1,2)],
                        (0,4):[(0,2),(1,3)],
                        (1,1):[(0,0),(1,2),(2,2)],
                        (1,2):[(0,2),(1,1),(1,3),(2,2)],
                        (1,3):[(0,4),(1,2),(2,2)],
                        (2,0):[(2,1),(3,0),(3,1)],
                        (2,1):[(2,0),(2,2),(3,1)],
                        (2,2):[(1,1),(1,2),(1,3),(2,1),(2,3),(3,1),(3,2),(3,3)],
                        (2,3):[(2,2),(2,4),(3,3)],
                        (2,4):[(2,3),(3,3),(3,4)],
                        (3,0):[(2,0),(3,1),(4,0)],
                        (3,1):[(2,0),(2,1),(2,2),(3,0),(3,2),(4,0),(4,1),(4,2)],
                        (3,2):[(2,2),(3,1),(3,3),(4,2)],
                        (3,3):[(2,2),(2,3),(2,4),(3,2),(3,4),(4,2),(4,3),(4,4)],
                        (3,4):[(2,4),(3,3),(4,4)],
                        (4,0):[(3,0),(3,1),(4,1),(5,0),(5,1)],
                        (4,1):[(3,1),(4,0),(4,2),(5,1)],
                        (4,2):[(3,1),(3,2),(3,3),(4,1),(4,3),(5,1),(5,2),(5,3)],
                        (4,3):[(3,3),(4,2),(4,4),(5,3)],
                        (4,4):[(3,3),(3,4),(4,3),(5,3),(5,4)],
                        (5,0):[(4,0),(5,1),(6,0)],
                        (5,1):[(4,0),(4,1),(4,2),(5,0),(5,2),(6,0),(6,1),(6,2)],
                        (5,2):[(4,2),(5,1),(5,3),(6,2)],
                        (5,3):[(4,2),(4,3),(4,4),(5,2),(5,3),(5,4),(6,2),(6,3),(6,4)],
                        (5,4):[(4,4),(5,3),(6,4)],
                        (6,0):[(5,0),(5,1),(6,1)],
                        (6,1):[(5,1),(6,0),(6,2)],
                        (6,2):[(5,1),(5,2),(5,3),(6,1),(6,3),(7,1),(7,2),(7,3)],
                        (6,3):[(5,2),(6,2),(6,4)],
                        (6,4):[(5,3),(5,4),(6,3)],
                        (7,1):[(6,2),(7,2),(8,0)],
                        (7,2):[(6,2),(7,1),(7,3),(8,2)],
                        (7,3):[(6,2),(7,2),(8,4)],
                        (8,0):[(7,1),(8,2)],
                        (8,2):[(7,2),(8,0),(8,4)],
                        (8,4):[(7,3),(8,2)]}
        # self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_line(self,point1,point2,win):
        y1,x1 = point1
        y2,x2 = point2
        pygame.draw.line(win, BLACK, (x1*SQUARE_SIZE + SQUARE_SIZE//2, y1*SQUARE_SIZE + SQUARE_SIZE//2), (x2*SQUARE_SIZE + SQUARE_SIZE//2, y2*SQUARE_SIZE + SQUARE_SIZE//2),2)

    def draw_points(self,win):
        PADDING = 15
        OUTLINE  = 2
        win.fill(WHITE)
        point_list = []
        point_list1 = [(0,0),(1,1),(2,0),(3,0),(4,0),(5,0),(6,0),(7,1),(8,0),(0,2),(2,4),(2,1),(2,3)]
        point_list2= [[(0,4),(4,4)],[(1,3)],[(2,4),(6,4),(6,0)],[(3,4)],[(0,4),(4,4),(8,4)],[(5,4)],[(2,4),(6,4)],[(7,3)],[(4,4),(8,4)],[(8,2)],[(6,4)],[(6,1)],[(6,3)]]
        blank_list = [(0,1),(0,3),(1,0),(1,4),(7,0),(7,4),(8,1),(8,3)]
        for col in range(COLS):
            for row in range(ROWS):
                point_list.append((row*SQUARE_SIZE + SQUARE_SIZE//2, col*SQUARE_SIZE + SQUARE_SIZE//2))
                
                # pygame.draw.rect(win,RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if (col,row) not in blank_list:
                    pygame.draw.circle(win, GREY, (row*SQUARE_SIZE + SQUARE_SIZE//2, col*SQUARE_SIZE + SQUARE_SIZE//2), radius= RADIUS)
                else:
                    continue

        for i in range(len(point_list1)):
            point1 = point_list1[i]
            point2_list= point_list2[i]
            for point2 in point2_list:
                self.draw_line(point1,point2,win)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(COLS):
            self.board.append([])
            for col in range(ROWS):
                if row==0:
                    if col==0 or col==2 or col==4:
                        self.board[row].append(Piece(row,col,BLUE))
                    else:
                        self.board[row].append(-1)
                elif row==1:
                    if col==1 or col==2 or col==3:
                        self.board[row].append(Piece(row,col,BLUE))
                    else:
                        self.board[row].append(-1)
                elif row ==2 or row ==3:
                    self.board[row].append(Piece(row,col,BLUE))
                elif row == 4:
                    self.board[row].append(0)
                elif row ==5 or row ==6:
                    self.board[row].append(Piece(row,col,RED))
                elif row==7:
                    if col==1 or col==2 or col==3:
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(-1)

                elif row==8:
                    if col==0 or col==2 or col==4:
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(-1)
                else:
                    self.board[row].append(0)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col] ,self.board[piece.row][piece.col]
        piece.move(row,col)
        print(self.board[row][col])
        print(self.board)

    def draw(self,win):
        self.draw_points(win)
        for row in range(COLS):
            for col in range(ROWS):
                piece = self.board[row][col]
                if piece != 0 and piece !=-1:
                    piece.draw(win)

        

    def remove(self, piece):
        self.board[piece.row][piece.col] = 0
        if piece != 0:
            if piece.color == RED:
                self.red_left -= 1
            else:
                self.blue_left -= 1
    
    def winner(self):
        if self.red_left <= 0:
            return BLUE
        elif self.blue_left <= 0:
            return RED
        
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        up = piece.row - 1
        down = piece.row +1

        current_pos = (piece.row,piece.col)
        print(current_pos)
        moves = self.valids[current_pos]
        print(moves)
        valid_moves = self._traverse(moves,piece.color,piece)

        # if piece.color == RED :
        #     moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
        #     moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        # if piece.color == WHITE or piece.king:
        #     moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
        #     moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return valid_moves

    def _traverse(self,moves,color,piece):
        valids = []
        catch = 0
        skipped = {}
        for move in moves:
            r = move[0]
            c = move[1]

            current = self.board[r][c]
            if current==0:
                valids.append(move)
                skipped[move] = 0
            elif current != -1 and current!=0 and current.color != color :
                print(current.color)
                print(color)
                direction = [move[0]-piece.row,move[1]-piece.col]

                if  move[0] + direction[0] >=0 and move[1]+ direction[1]>=0 and move[0] + direction[0] < COLS and move[1]+ direction[1]  < ROWS:
                    print("moves: " + str(move[0] + direction[0]) + " " + str(move[1] + direction[1]))
                    next = self.board[move[0] + direction[0]][move[1] + direction[1]]

                    print()
                    print(next)
                    if next ==0:
                        catch+=1
                        valids.append((move[0] + direction[0],move[1]+ direction[1]))
                        skipped[(move[0] + direction[0],move[1]+ direction[1])] = (move[0],move[1])


        return  [valids,skipped,catch]


