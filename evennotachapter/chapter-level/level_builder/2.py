from asyncio import set_child_watcher
from turtle import shape
from pycat.core import Window, Sprite, KeyCode, Color
from pycat.base import NumpyImage as np
from pycat.base import Texture, MouseEvent, MouseButton
from typing import List, Callable, TypeVar
import pickle

from sklearn.preprocessing import scale


class SpriteGrid:

    T = TypeVar('T', bound=Sprite)

    @classmethod
    def create_from_data_file(cls,
                              w: Window,
                              file,
                              x: float = None,
                              y: float = None,
                              scale: float = 10,
                              cell_gap: float = 1,
                              cell_cls: Callable[..., T] = Sprite):
        size, scale,texture_arrays, array_index = pickle.load(open(file, 'rb'))
        grid = cls(w, size[0], size[1], x, y, scale, cell_gap, cell_cls)
        m, n = size
        for i in range(m):
            for j in range(n):
                cell = grid.__cells[i][j]
                cell.scale = scale
                width = cell.width
                array = texture_arrays[array_index[i][j]]
                t = np.get_texture_from_array(array)
                cell.texture = t
                cell.scale_to_width(width)
        return grid
    

    def __init__(self,
                 w: Window,
                 rows: int,
                 cols: int,
                 x: float = None,
                 y: float = None,
                 scale: float = 10,
                 cell_gap: float = 1,
                 cell_cls: Callable[..., T] = Sprite):

        self.__x = scale/2 if x is None else x
        self.__y = scale/2 if y is None else y
        self.__scale = scale
        self.__cell_gap = cell_gap
        self.__rows = rows
        self.__cols = cols
        self.__cells = [[w.create_sprite(cell_cls) for j in range(cols)]
                        for i in range(rows)]
        self.__update_cells()

    def __update_cells(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                s = self.__cells[i][j]
                s.scale_to_width(self.scale)
                s.x = self.x + (s.width+self.cell_gap)*j
                s.y = self.y + (s.height+self.cell_gap)*i

    def split_sprite_sheet(self, file: str):
        self.array = np.get_array_from_file(file)
        m, n, _ = self.array.shape  # pixels
        di = m // self.rows
        dj = n // self.cols
        sub_arrays = [[self.array[i*di:(i+1)*di, j*di:(j+1)*dj, :]
                      for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.__cells[i][j]
                cell.texture = np.get_texture_from_array(sub_arrays[i][j])
                cell.scale_to_width(self.scale)

    def export_data_file(self, file):
        pickle.dump(self.data, open(file, 'wb'))

    @property
    def data(self):
        size = (self.rows, self.cols)
        texture_dict = dict()
        array_index = [[0 for j in range(self.cols)] for i in range(self.rows)]
        texture_arrays = []  # stores the actual pixel data
        current_index = 0
        # we should add tag and layer data too!
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.__cells[i][j]
                t = cell.texture
                if t not in texture_dict:
                    texture_dict[t] = current_index
                    texture_arrays.append(np.get_array_from_texture(t))
                    current_index += 1
                array_index[i][j] = texture_dict[t]
        print(current_index)
        return (size, self.__cells[0][0].scale ,texture_arrays, array_index)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val: float):
        self.__x = val
        self.__update_cells()

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val: float):
        self.__y = val
        self.__update_cells()

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, val: float):
        self.__scale = val
        self.__update_cells()

    @property
    def cell_gap(self):
        return self.__cell_gap

    @cell_gap.setter
    def cell_gap(self, val: float):
        self.__cell_gap = val
        self.__update_cells()

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols


if __name__ == '__main__':
    class LevelCell(Sprite):
        def on_create(self):
            self.add_tag("Level Cell")
            w.subscribe(on_mouse_drag=self.on_mouse_drag)

        def delete(self):
            w.unsubscribe(on_mouse_drag=self.on_mouse_drag)
            super().delete()

        def on_mouse_drag(self, m: MouseEvent):
            if self.contains_point(m.position):
                width = self.width
                if m.button is MouseButton.LEFT:
                    if current_texture:
                        self.texture = current_texture
                        self.scale_to_width(width)
                else:
                    self.texture = None
                    self.color = Color.WHITE
                    self.scale_to_width(width)

    class SelectionCell(Sprite):
        def on_create(self):
            self.add_tag("level_sheet")

        def on_left_click(self):
            global current_texture
            current_texture = self.texture
            print("selected texture")

    class GridController(Sprite):
        def on_update(self, dt):
            if w.is_key_pressed(KeyCode.W):
                level_grid.y += 5
            if w.is_key_pressed(KeyCode.S):
                level_grid.y -= 5
            if w.is_key_pressed(KeyCode.A):
                level_grid.x -= 5
            if w.is_key_pressed(KeyCode.D):
                level_grid.x += 5
            if w.is_key_pressed(KeyCode.UP):
                level_grid.scale *= 1.01
            if w.is_key_pressed(KeyCode.DOWN):
                level_grid.scale *= 0.99

    class ExportButton(Sprite):
        def on_create(self):
            self.width = 100
            self.height = 50
            self.color = Color.RED
            self.x = 100
            self.y = w.height-50
            label = w.create_label(text='Export')
            label.color = Color.BLACK
            label.x = self.x - label.content_width/2
            label.y = self.y + label.content_height/2

        def on_left_click(self):
            print('export')
            level_grid.export_data_file('level_data')

    class ImportButton(Sprite):
        def on_create(self):
            self.width = 100
            self.height = 50
            self.color = Color.GREEN
            self.x = 100
            self.y = w.height-150
            label = w.create_label(text='Import')
            label.color = Color.BLACK
            label.x = self.x - label.content_width/2
            label.y = self.y + label.content_height/2

        def on_left_click(self):
            global level_grid
            w.delete_sprites_with_tag("Level Cell")
            print("import")
            level_grid = SpriteGrid.create_from_data_file(w,
                                                          'level_data',
                                                          scale=15,
                                                          x=600,
                                                          cell_gap=1,
                                                          cell_cls=LevelCell)

    class PageButton(Sprite):
        def on_create(self):
            self.width = 100
            self.height = 50
            self.color = Color.CYAN
            self.x = 100
            self.y = w.height-250
            label = w.create_label(text='NEXT')
            label.color = Color.BLACK
            label.x = self.x - label.content_width/2
            label.y = self.y + label.content_height/2
            self.file = 0

        def on_left_click(self):
            global selection_grid
            w.delete_sprites_with_tag("level_sheet")
            if self.file == 0:
                selection_grid = SpriteGrid(w, rows=7, cols=12, scale=30,
                                            cell_cls=SelectionCell)
                selection_grid.split_sprite_sheet('pattern.png')
                self.file += 1
            
            elif self.file == 1:
                selection_grid = SpriteGrid(w, rows=6, cols=4, scale=30,
                                            cell_cls=SelectionCell)
                selection_grid.split_sprite_sheet('ships_packed.png')
                self.file += 1
            
            elif self.file == 2:
                selection_grid = SpriteGrid(w, rows=10, cols=12, scale=30,
                                            cell_cls=SelectionCell)
                selection_grid.split_sprite_sheet('tiles_packed.png')
                self.file = 0
            

    w = Window(is_sharp_pixel_scaling=True, enforce_window_limits=False)
    current_texture: Texture = None
    selection_grid = SpriteGrid(w, rows=10, cols=12, scale=30,
                                cell_cls=SelectionCell)
    selection_grid.split_sprite_sheet('tiles_packed.png')
    # selection_grid = SpriteGrid(w, rows=22, cols=49, scale=10,
    #                             cell_cls=SelectionCell)
    # selection_grid.split_sprite_sheet('1bit.png')
    level_grid = SpriteGrid(w, rows=10, cols=20, scale=30, x=600, cell_gap=1,
                            cell_cls=LevelCell)
    w.create_sprite(ExportButton)
    w.create_sprite(ImportButton)
    w.create_sprite(GridController)
    w.create_sprite(PageButton)
    w.run()
