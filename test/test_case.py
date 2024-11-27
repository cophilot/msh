class TestCase:
    def __init__(self, name):
        self.name = name
        self.success = False

    def run(self):
        raise NotImplementedError
