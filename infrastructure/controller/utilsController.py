from infrastructure.controller.controller import Controller
from layout.view import homeFrame
from library import sysUtils


class UtilsController(Controller):
    def __init__(self, layout):
        super().__init__(layout)

    def start_screen_keyboard(self):
        # Todo: Add a condition for Pi / pass some systems_settings struct to it
        sysUtils.run_screen_keyboard()

    def go_home(self):
        self.templating.raise_frame(
            self.layout.get(homeFrame.HomeFrame.__name__)
        )
