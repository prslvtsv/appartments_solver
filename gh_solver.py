# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 06:14:32 2022

@author: prslvtsv
"""
import polyomino as poly
import polyomino.constant as const
from polyomino.piece import display
from polyomino.board import Rectangle, Chessboard, Irregular
from polyomino.tileset import many


domino = const.DOMINO
monomino = const.MONOMINO
tr = const.TETROMINOS["J"]

floor = Rectangle(13, 3).remove_all(
    [
        (6, 0),
        (7, 0),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1),
        (7, 1),
        (8, 1),
        (9, 1),
        (10, 1),
    ]
)

print(floor.display())

problem_a = floor.tile_with_set(
    many(domino).and_repeated_exactly(4, monomino)
).with_heuristics()
problem_b = floor.tile_with_set(
    many(domino).and_repeated_exactly(2, tr).and_repeated_exactly(4, monomino)
).with_heuristics()


sa = problem_a.solve()
sb = problem_b.solve()

print(sa.display())
print(sb.display())
