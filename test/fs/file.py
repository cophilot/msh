from fs.fs_element import FSElement
from my_assertion import assert_true


class File(FSElement):
    def __init__(self, name, parent=None, content=""):
        super().__init__(name, parent)
        self.content = content

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def has_line(self, line, can_be_substring=False):
        lines = ""
        with open(self.get_path(), "r") as f:
            lines = f.readlines()
        found = False
        for l in lines:
            if (can_be_substring and line in l) or l.strip() == line:
                found = True
                break
        assert_true(found)
        return self

    def make(self):
        with open(self.get_path(), "w") as f:
            f.write(self.content)

    def get_path(self):
        return super().get_path()
