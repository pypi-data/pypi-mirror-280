from libreflow.baseflow.ui.mytasks.mytasks import (
    MyTasksPageWidget      as BaseMyTasksPageWidget
)


class MyTasksPageWidget(BaseMyTasksPageWidget):

    def build(self):
        super(MyTasksPageWidget, self).build()
        self.content.header.fdt_button.hide()
