import tabulate
import random
import copy
import json

class Lighting:

    def __init__(self, matrix):
        self.matrix =  copy.deepcopy(matrix)
        self.matrixorg = copy.deepcopy(matrix)
        self.size_row = 0
        self.size_column = 0
        self.paths = {}
        self.__matrix_constraint()

    def __matrix_constraint(self):
        self.size_row = len(self.matrix)
        errors = []
        for index, row in enumerate(self.matrix):
            if index == 0:
                self.size_column = len(row)
            if self.size_column != len(row):
                errors.append(f"The line with index {index} only has {len(row)} columns, must be {self.size_column}")
        if len(errors):
            raise Exception(str(errors))

    def lighting_sorted(self):
        return sorted(self.paths, key= lambda i: len(self.paths[i]))

    def v1(self):
        def lighting_route( n, m, index, mode='top'): # 2,2
            if n < 0 or m < 0 or \
                n >= self.size_row or m  >= self.size_column or \
                self.matrix[n][m]:
                return
            new_index = f"{n},{m}"
            if index != new_index:
                if index in self.paths.keys():
                    self.paths[index].append(new_index)
                else:
                    self.paths.update({index:[ new_index]})
            if mode == 'bottom':
                return lighting_route(n+1, m, index, mode) # 3,2 abajo
            elif mode == 'left':
                return lighting_route(n, m-1, index, mode) # 2,1 izquierda
            elif mode == 'right':
                return lighting_route(n, m+1, index, mode) # 2,3 derecha
            return lighting_route(n-1, m, index, mode) # 1,2 arriba
        for indexN, column in enumerate(self.matrixorg):
            for indexM, value in enumerate(column):
                index = f"{indexN},{indexM}"
                lighting_route(indexN, indexM, index)
                lighting_route(indexN, indexM, index, mode='bottom')
                lighting_route(indexN, indexM, index, mode='left')
                lighting_route(indexN, indexM, index, mode='right')

    def rooms(self, wall=False, light=False, matrix=None):
        matrix = matrix or self.matrixorg
        print(tabulate.tabulate(matrix))
    
    def rand_color(self):
        hex = '0123456789ABCDEF'
        return "#"+''.join([random.choice(hex) for j in range(6)])

    def light_on(self, layers=0):
        ls = self.lighting_sorted()
        max_layers = len(ls)
        if layers > max_layers:
            raise Exception(f"Only has {max_layers-1} layers, starting from 0")
        colors = {}
        matrix = copy.deepcopy(self.matrixorg)
        def _light_on(index, value):
            n,m = index.split(',')
            matrix[int(n)][int(m)] = value
        
        for i, value in enumerate(reversed(ls)):
            if i <= layers:
                _light_on(value, value)
                colors[value] = self.rand_color()
                for room in self.paths.get(value):
                    _light_on(room, value)
        return matrix, max_layers, colors
    
    ### V2
    def v2(self):
        def lighting_route(n, m, index, mode='top'): # 2,2
            if n < 0 or m < 0 or \
                n >= self.size_row or m  >= self.size_column or \
                self.matrix[n][m]:
                return
            new_index = f"{n},{m}"
            if index != new_index:
                if index in self.paths.keys():
                    self.paths[index].append(new_index)
                else:
                    self.paths.update({index:[ new_index]})
                self.matrix[n][m] = 1
            if mode == 'bottom':
                return lighting_route(n+1, m, index, mode) # 3,2 abajo
            elif mode == 'left':
                return lighting_route(n, m-1, index, mode) # 2,1 izquierda
            elif mode == 'right':
                return lighting_route(n, m+1, index, mode) # 2,3 derecha
            return lighting_route(n-1, m, index, mode) # 1,2 arriba

        for indexN, row in enumerate(self.matrixorg):
            for indexM, col in enumerate(row):
                index = f"{indexN},{indexM}"
                lighting_route(indexN, indexM, index)
                lighting_route(indexN, indexM, index, mode='bottom')
                lighting_route(indexN, indexM, index, mode='left')
                lighting_route(indexN, indexM, index, mode='right')

#matrix = [
    [0, 0, 1,0,0],
    [0, 0, 0,0,0],
    [1, 0, 0,0,1],
    [0, 0, 0,0,0],
#]
#l = Lighting(matrix)
#l.rooms(wall=True)
#l.v1()
#matrix2, layers, colors = l.light_on()
#l.rooms(wall=True, light=True, matrix=matrix2)


#l.v2()
#matrix2, layers, colors = l.light_on( layers=2)
#l.rooms(wall=True, light=True, matrix=matrix2)