from scene.scene import Scene
from task.task import Task
from task.map.initialize import Initialize
from task.map.scene_to_title import SceneToTitle
from manager.map_manager import MapManager


class SceneMap(Scene):

    def __init__(self):
        super().__init__()
        self.__next_scene = None
        self.__task: Task = None
        self.__map_manager = MapManager()

    def start(self):

        self.__task = Initialize(
            super().game_system,
            super().game_info,
            self.__map_manager
        )
        self.__task.start()

    def update(self):
        from scene.scene_title import SceneTitle

        self.__task.update()

        next_task = self.__task.get_next_task()
        if next_task is not None:
            self.__task.exit()
            task = next_task
            self.__task = task
            self.__map_manager.game_system.reset_timer()
            task.start()
            print("task:" + task.__class__.__name__)

        if isinstance(next_task, SceneToTitle):
            self.__next_scene = SceneTitle()

    def draw(self):
        self.__task.draw()

    def exit(self):
        pass

    def get_next_scene(self):
        return self.__next_scene
