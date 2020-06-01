import copy


class Cells:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[False for j in range(w)] for i in range(h)]
        self.clicked_cells = [[False for j in range(w)] for i in range(h)]

    def set_cell(self, x, y):
        self.clicked_cells[x][y] = True

    def get_next_condition(self, x, y):
        # possible cells
        xs = [x-1, x-1, x-1, x,   x,   x+1, x+1, x+1]
        ys = [y-1, y,   y+1, y-1, y+1, y-1, y,   y+1]
        # make values valid
        for i in range(len(xs)):
            xs[i] %= self.w
        for i in range(len(ys)):
            ys[i] %= self.h
        # count number of cells
        counter = 0
        for i in range(len(xs)):
            if self.cells[xs[i]][ys[i]]:
                counter += 1
        # three cells => born
        live = self.cells[x][y]
        if not live and counter == 3:
            return True
        elif not live:
            return False
        # die or live when 2 to 3 neighbors
        if counter == 2 or counter == 3:
            return True
        else:
            return False

    def get_next(self):
        # get new condition for all cells
        new_cells = [[False for j in range(self.w)] for i in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                new_cells[x][y] = self.get_next_condition(x, y)
        # add clicked cells
        for y in range(self.h):
            for x in range(self.w):
                click_value = self.clicked_cells[x][y]
                if click_value:
                    new_cells[x][y] = click_value
        # clear clicked_cells and overwrite cells with new
        self.clicked_cells = [[False for j in range(self.w)] for i in range(self.h)]
        self.cells = copy.deepcopy(new_cells)
        return new_cells
