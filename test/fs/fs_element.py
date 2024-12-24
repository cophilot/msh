import os


class FSElement:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_path(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.get_path() + "/" + self.name

    def delete(self):
        os.system(f"rm -rf {self.get_path()}")

    def check(self):
        exists = os.path.exists(self.get_path())
        if not exists:
            raise AssertionError(f"Path {self.get_path()} does not exist")
        return self

    def check_not_exists(self):
        exists = os.path.exists(self.get_path())
        if exists:
            raise AssertionError(
                f"Path {self.get_path()} exists (expected not to exist)"
            )
