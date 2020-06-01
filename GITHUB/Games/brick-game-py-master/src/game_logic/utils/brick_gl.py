class BrickGl:
    
    def __init__(self, draw_atoms):
        self.draw_atoms = draw_atoms
        pass
    
    def horiz_line(self, h0, w0, length):
        args = [(h0, w) for w in range(w0, w0 + length)]
        self.draw_atoms(*args)
    
    def vert_line(self, h0, w0, length):
        args = [(h, w0) for h in range(h0, h0 + length)]
        self.draw_atoms(*args)
    
    def diagonal(self, h0, w0, length, reverse=False):
        if reverse:
            args = [(h0 + i, w0 - i) for i in range(length)]
        else:
            args = [(h0 + i, w0 + i) for i in range(length)]
        self.draw_atoms(*args)
    
    def _draw_A(self, h0, w0):
        self.diagonal(h0, w0, 3)
        self.diagonal(h0, w0, 3, reverse=True)
        self.horiz_line(h0 + 3, w0 - 2, 5)
        self.draw_atoms((h0 + 4, w0 - 2))
        self.draw_atoms((h0 + 4, w0 + 2))
    
    def _draw_B(self, h0, w0):
        self.vert_line(h0, w0-2, 5)
        self.horiz_line(h0, w0-2, 4)
        self.draw_atoms((h0 + 1, w0 + 2))
        self.horiz_line(h0 + 2, w0-2, 4)
        self.draw_atoms((h0 + 3, w0 + 2))
        self.horiz_line(h0 + 4, w0-2, 4)
    
    def _draw_C(self, h0, w0):
        self.horiz_line(h0, w0 - 2, 5)
        self.vert_line(h0, w0 - 2, 5)
        self.horiz_line(h0+4, w0 - 2, 5)
    
    def alphabet(self, ch, h0=3, w0=5):
        c = ch.upper()
        if c == 'A':
            self._draw_A(h0, w0)
        elif c == 'B':
            self._draw_B(h0, w0)
        elif c == 'C':
            self._draw_C(h0, w0)
