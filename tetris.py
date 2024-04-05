SHAPES = {
    'I': [(0, 0), (1, 0), (2, 0), (3, 0)],  # Long piece
    'J': [(1, 0), (1, 1), (1, 2), (0, 2)],
    'L': [(0, 0), (0, 1), (0, 2), (1, 2)],
    'O': [(0, 0), (0, 1), (1, 0), (1, 1)],  # Square
    'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    'T': [(0, 1), (1, 1), (2, 1), (1, 0)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)]
}

class block:
    
    def __init__(self, type):
        self.shape_coords = SHAPES[type]
        
        
    def rotate_clockwise(self):
        shape_coords =  [(-y, x) for x, y in self.shape_coords]
        while any([x < 0 for x, _ in shape_coords]):
            shape_coords = [(x + 1, y) for x, y in self.shape_coords]
        self.shape_coords = shape_coords
        
    
    def rotate_anticlockwise(self):
        shape_coords =  [(y, -x) for x, y in self.shape_coords]
        while any([y < 0 for _, y in shape_coords]):
            shape_coords = [(x, y + 1) for x, y in self.shape_coords]
        self.shape_coords = shape_coords