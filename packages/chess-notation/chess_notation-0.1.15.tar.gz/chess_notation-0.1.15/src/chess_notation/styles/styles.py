from typing import Literal

Check = Literal["NONE", "CHECK"]
Mate = Literal["NONE", "SHARP", "DOUBLE_CHECK"]
Castle = Literal["OO", "O-O"]
PawnCapture = Literal["de", "dxe", "de4", "dxe4", "xe4", "PxN"]
PieceCapture = Literal["Ne4", "Nxe4", "NxN"]

"""Pawn capture styles that convey unique information (start file only, end file only, both files, etc.)
I.e. no two styles include the same info
"""
UNIQ_PAWN_CAPTURES: list[PawnCapture] = ['de', 'dxe4', 'xe4', 'PxN']
"""
Piece capture styles that convey unique information (start file only, end file only, both files, etc.)
I.e. no two styles include the same info
"""
UNIQ_PIECE_CAPTURES: list[PieceCapture] = ['Ne4', 'Nxe4', 'NxN']