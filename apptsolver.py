# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 02:59:07 2022

@author: prslvtsv
"""
import polyomino as poly
import polyomino.constant as const
from polyomino.piece import display
from polyomino.board import Rectangle, Chessboard, Irregular
from polyomino.tileset import many


domino = const.DOMINO
monomino = const.MONOMINO
tr = const.TROMINOS["Right"]

chessboard = Chessboard()

problem_a = chessboard.tile_with_many(domino)
problem_b = chessboard.tile_with_set(
    many(tr).and_repeated_exactly(4, monomino)
).with_heuristics()
# problem_c = chessboard.tile_with_set(may(tr), reflecti)


sa = problem_a.solve()
sb = problem_b.solve()

print(sa.tiling)
print(sb.display())
