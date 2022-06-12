# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 06:14:32 2022

@author: prslvtsv
"""
import sys
import argparse
from polyomino.board import Rectangle
from polyomino.tileset import Tileset
from polyomino.tileset import many, any_number_of, all_optional

# import exact_cover as exc

# print(dir(exc))
def construct_board_removed(size, removed):

    torem = [(int(r.split(",")[0]), int(r.split(",")[1])) for r in removed.split(":")]

    return Rectangle(size[0], size[1]).remove_all(torem)


def construct_tileset(tiles):
    result = []
    tset = tiles.split("..")

    for t in tset:
        tt = [(int(r.split(",")[0]), int(r.split(",")[1])) for r in t.split(":")]
        result.append(tt)
    # print(result)
    return any_number_of(result).with_reflections()


def construct_tileset_explicit(mandatory=[], optional=[], filler=[]):
    return Tileset(mandatory, optional, filler, True)


def output_board(b):
    print(b.squares)


def output_solution(s):
    print(s.tiling)


def solve_explicit_set(board, tileset):
    problem = board.tile_with_set(tileset).with_heuristics()
    return problem.solve()


def prepare_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", "-s", type=int, nargs=2, required=True)
    parser.add_argument("--remove", "-r", type=str, required=True)
    parser.add_argument("--mandatory", "-m", type=str)
    parser.add_argument("--optional", "-o", type=str)
    parser.add_argument("--filler", "-f", type=str)

    return parser.parse_args()


def parse_tile(lst):
    if lst is None:
        return []
    return [
        [(int(r.split(",")[0]), int(r.split(",")[1])) for r in st.split(":")]
        for st in lst.split("..")
    ]


def main():

    args = prepare_args()
    mandatory = parse_tile(args.mandatory)
    optional = parse_tile(args.optional)
    filler = parse_tile(args.filler)

    board = construct_board_removed(args.size, args.remove)
    output_board(board)

    tileset = construct_tileset_explicit(mandatory, optional, filler)

    solution = solve_explicit_set(board, tileset)
    # print(solution.display())
    output_solution(solution)


if __name__ == "__main__":

    main()
