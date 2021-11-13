

class Lake:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def debug(self):
        result = ''
        for j in range(0, self.height):
            for i in range(0, self.width):
                result += '[ ]'
            result += '\n'
        return result
