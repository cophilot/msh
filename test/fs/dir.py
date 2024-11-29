import os
from fs.fs_element import FSElement
from fs.file import File


class Dir(FSElement):

    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.children = []

    def add_childs(self, *childs):
        for child in childs:
            self.children.append(child)
            child.parent = self
        return self

    def add_dir(self, name):
        dir = Dir(name)
        return self.add_child(dir)

    def add_file(self, name, content=""):
        f = File(name, content)
        return self.add_child(f)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        return child

    def cd(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise FileNotFoundError(f"Directory '{name}' not found in '{self.name}'")

    def make(self):
        os.makedirs(self.get_path(), exist_ok=True)

    def get_path(self):
        return super().get_path()
