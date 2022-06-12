# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 06:14:32 2022

@author: prslvtsv
"""
import sys
import polyomino as poly
import polyomino.constant as const
from polyomino.piece import display
from polyomino.board import Rectangle, Chessboard, Irregular
from polyomino.tileset import many, any_number_of, all_optional

# import exact_cover as exc

# print(dir(exc))
def construct_removed(rect, removed):
    size = [int(r) for r in rect.split(",")]
    torem = [(int(r.split(",")[0]), int(r.split(",")[1])) for r in removed.split(":")]

    # print(size)
    # print(torem)
    board = Rectangle(size[0], size[1]).remove_all(torem)
    # print(board.display())
    # print(board.squares)
    return board


def construct_tileset(tiles):
    result = []
    tset = tiles.split("..")

    for t in tset:
        tt = [(int(r.split(",")[0]), int(r.split(",")[1])) for r in t.split(":")]
        result.append(tt)
    # print(result)
    return any_number_of(result).with_reflections()


def output_board(b):
    print(b.squares)


def output_solution(s):
    print(s.tiling)


def main(args=None):

    # domino = const.DOMINO
    # monomino = const.MONOMINO
    # tr = const.TETROMINOS["J"]
    if args is None:
        args = sys.argv[1:]
    board_to_tile = construct_removed(args[0], args[1])
    tileset = construct_tileset(args[2])
    # tileset = any_number_of(const.ALL_TROMINOS).and_one(domino).with_reflections()
    output_board(board_to_tile)

    problem = board_to_tile.tile_with_set(tileset).with_heuristics()
    # problem = board_to_tile.tile_with_set(tileset)
    solution = problem.solve()
    output_solution(solution)
    # print(solution.tiling)
    # print(solution.display())


if __name__ == "__main__":
    arg0 = "5,11"
    arg1 = "0,0:1,0:2,0:0,1:1,1:2,1:0,2:2,2:0,3:2,3:0,4:2,4:0,5:2,5:0,6:2,6:0,7:2,7:3,7:4,7:0,8:4,8:0,9:3,9:4,9:0,10"
    arg2 = "0,0:0,1|0,0:0,1:0,2|0,0:1,0:0,1:0,2|0,0:1,0:0,1:1,1:0,2:1,2|0,0:1,0:0,1:1,1:0,2:1,2"

    # for a in sys.argv[1:]:
    #     print(a)
    # main([arg0, arg1, arg2])
    main()
# domino = const.DOMINO
# monomino = const.MONOMINO
# tr = const.TETROMINOS["J"]
#
# floor = Rectangle(13, 3).remove_all(
#     [
#         (6, 0),
#         (7, 0),
#         (8, 0),
#         (2, 1),
#         (3, 1),
#         (4, 1),
#         (5, 1),
#         (6, 1),
#         (7, 1),
#         (8, 1),
#         (9, 1),
#         (10, 1),
#         (11, 1),
#     ]
# )
#
#
# problem_a = floor.tile_with_set(
#     many(domino).and_repeated_exactly(2, monomino)
# ).with_heuristics()
# problem_b = floor.tile_with_set(
#     many(domino).and_repeated_exactly(2, tr).and_repeated_exactly(2, monomino)
# ).with_heuristics()
#
#
# sa = problem_a.solve()
# sb = problem_b.solve()
#
# print("empty floor")
# print(floor.display(), end="\n\n")
# print("tiled with set 1")
# print(sa.display(), end="\n\n")
# print("tiled with set 2")
# print(sb.display(), end="\n\n")
