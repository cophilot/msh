from fs.fs_element import FSElement


class File(FSElement):

    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.content = ""

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_path(self):
        return super().get_path()
