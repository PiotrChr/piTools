from infrastructure.controller.controller import Controller
from layout.view import homeFrame


class UtilsController(Controller):
    def __init__(self, layout):
        super().__init__(layout)

    def start_screen_keyboard(self):
        self.not_yet_implemented()

    def go_home(self):
        self.templating.raise_frame(
            self.layout.get(homeFrame.HomeFrame.__name__)
        )
