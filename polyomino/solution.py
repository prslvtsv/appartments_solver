from .pretty_poly import make_ascii

# from .pretty_poly.display_result import create_png


class Solution(object):
    def __init__(self, tiling, board):
        self.tiling = tiling
        self.board = board

    def display(self):
        return make_ascii(self.tiling)

    # def display_img(self):
    #     return create_png(self.tiling)

    def python(self):
        return "\n".join(self._gen_python())

    def _gen_python(self):
        yield "TILING = %s" % (repr(self.tiling),)
