from typing import Optional

from const import Key, Direction

from manager.map_manager import MapManager
from manager.input_manager import InputManager
from task.task import Task
from task.map.move import Move


class InputWait(Task):

    def __init__(self, map_manager: MapManager):
        self.__map_manager = map_manager
        self.__next_task = None

    def __isPush(self, key: int) -> bool:
        return InputManager.isPush(key)

    def __get_push_direction(self) -> int:

        if self.__isPush(Key.UP):
            return Direction.UP
        if self.__isPush(Key.RIGHT):
            return Direction.RIGHT
        if self.__isPush(Key.DOWN):
            return Direction.DOWN
        if self.__isPush(Key.LEFT):
            return Direction.LEFT
        return Direction.NEWTRAL

    def start(self):
        pass

    def update(self):
        mm = self.__map_manager
        player = mm.player
        game_system = mm.game_system

        if InputManager.isPush(Key.s):
            game_system.add_speed()

        direction = self.__get_push_direction()
        if not player.ready_move(direction):
            return

        self.__next_task = Move(self.__map_manager)

    def draw(self):
        mm = self.__map_manager
        mm.draw_map()
        mm.draw_parameter()
        mm.draw_floor_info()

    def exit(self):
        pass

    def get_next_task(self) -> Optional[Task]:
        return self.__next_task
