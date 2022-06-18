# -*- coding: utf-8 -*-
"""Inner code from ghPython component running solver remotely

gh prepares string command input to pass args to solver

• INPUT sample
    "C:\ProgramData\Anaconda3\shell\condabin\conda-hook.ps1; conda activate C:\ProgramData\Anaconda3\envs\exc43;"; python C:\Users\GUEST\Documents\CODE\aective\sectiondev\appartments_solver\gh_solver_conditional.py -s 5 11 -r 3,0:4,0:3,1:4,1:1,2:3,2:4,2:1,3:3,3:4,3:1,4:3,4:4,4:1,5:3,5:4,5:1,6:3,6:4,6:1,7:1,8:2,8:1,9:2,9:1,10:2,10:3,10:4,10 -m 0,0:1,0:0,1:1,1:0,2:1,2..0,0:1,0:0,1:0,2 -f 0,0:0,1..0,0:0,1:0,2

• OUTPUT sample

    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 7), (3, 8), (3, 9), (4, 7), (4, 8), (4, 9)]
    [[(2, 0), (2, 1), (1, 0), (1, 1), (0, 0), (0, 1)], [(0, 2), (0, 3), (0, 4)], [(0, 5), (0, 6), (0, 7)], [(0, 8), (0, 9), (0, 10)], [(2, 2), (2, 3), (2, 4)], [(2, 7), (3, 7), (2, 6), (2, 5)], [(3, 8), (3, 9)], [(4, 7), (4, 8), (4, 9)]]


"""
import subprocess as sub


def execute_in_shell(cmd):

    process = sub.Popen(
        cmd,
        executable=terminal,
        stdin=sub.PIPE,
        stdout=sub.PIPE,
        stderr=sub.PIPE,
        shell=True,
    )
    stdout, stderr = process.communicate()
    print stdout
    return stdout


cmd = "; ".join([conda_activate, payload])
result = execute_in_shell(cmd).split("\n")
