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
            # Black pawn moves down (decreasing row numbers)
            one_square = Square.at(current_square.row - 1, current_square.col)
            if board.get_piece(one_square) is None:
                moves.append(one_square)

                # If pawn is at starting position (row 6), it can move two squares
                if current_square.row == 6:
                    two_squares = Square.at(current_square.row - 2, current_square.col)
                    if board.get_piece(two_squares) is None:
                        moves.append(two_squares)
        else:
            # White pawn moves up (increasing row numbers)
            one_square = Square.at(current_square.row + 1, current_square.col)
            if board.get_piece(one_square) is None:
                moves.append(one_square)

                # If pawn is at starting position (row 1), it can move two squares
                if current_square.row == 1:
                    two_squares = Square.at(current_square.row + 2, current_square.col)
                    if board.get_piece(two_squares) is None:
                        moves.append(two_squares)

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
