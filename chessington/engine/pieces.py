from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    def to_json(self) -> dict[str, Any]:
        return {
            "piece": self.__class__.__name__,
            "player": self.player._name_.lower()
        }

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board: Board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        moves = []

        if self.player == Player.BLACK:
            # Black pawn moves down (decreasing row)
            new_row = current_square.row - 1

            # 1. FORWARD MOVEMENT
            if new_row >= 0:
                one_square = Square.at(new_row, current_square.col)
                if board.get_piece(one_square) is None:
                    moves.append(one_square)

                    # Two-square move from starting position
                    if current_square.row == 6:
                        two_square_row = current_square.row - 2
                        if two_square_row >= 0:
                            two_squares = Square.at(two_square_row, current_square.col)
                            if board.get_piece(two_squares) is None:
                                moves.append(two_squares)

            # 2. DIAGONAL CAPTURE MOVES
            if new_row >= 0:  # Make sure we're not going off the board
                # Check diagonal left (column - 1)
                if current_square.col - 1 >= 0:  # Don't go off left edge
                    diagonal_left = Square.at(new_row, current_square.col - 1)
                    piece_on_diagonal = board.get_piece(diagonal_left)
                    # Can capture if there's an enemy piece (different player)
                    if piece_on_diagonal is not None and piece_on_diagonal.player != self.player:
                        moves.append(diagonal_left)

                # Check diagonal right (column + 1)
                if current_square.col + 1 <= 7:  # Don't go off right edge
                    diagonal_right = Square.at(new_row, current_square.col + 1)
                    piece_on_diagonal = board.get_piece(diagonal_right)
                    # Can capture if there's an enemy piece (different player)
                    if piece_on_diagonal is not None and piece_on_diagonal.player != self.player:
                        moves.append(diagonal_right)

        else:  # WHITE player
            # White pawn moves up (increasing row)
            new_row = current_square.row + 1

            # 1. FORWARD MOVEMENT
            if new_row <= 7:
                one_square = Square.at(new_row, current_square.col)
                if board.get_piece(one_square) is None:
                    moves.append(one_square)

                    # Two-square move from starting position
                    if current_square.row == 1:
                        two_square_row = current_square.row + 2
                        if two_square_row <= 7:
                            two_squares = Square.at(two_square_row, current_square.col)
                            if board.get_piece(two_squares) is None:
                                moves.append(two_squares)

            # 2. DIAGONAL CAPTURE MOVES
            if new_row <= 7:  # Make sure we're not going off the board
                # Check diagonal left (column - 1)
                if current_square.col - 1 >= 0:  # Don't go off left edge
                    diagonal_left = Square.at(new_row, current_square.col - 1)
                    piece_on_diagonal = board.get_piece(diagonal_left)
                    # Can capture if there's an enemy piece (different player)
                    if piece_on_diagonal is not None and piece_on_diagonal.player != self.player:
                        moves.append(diagonal_left)

                # Check diagonal right (column + 1)
                if current_square.col + 1 <= 7:  # Don't go off right edge
                    diagonal_right = Square.at(new_row, current_square.col + 1)
                    piece_on_diagonal = board.get_piece(diagonal_right)
                    # Can capture if there's an enemy piece (different player)
                    if piece_on_diagonal is not None and piece_on_diagonal.player != self.player:
                        moves.append(diagonal_right)

        return moves

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []
