from my_assertion import assert_true, assert_false, assert_equal


class Log:
    def __init__(self, output):
        self.output = output
        self.lines = []
        for line in output.split("\n"):
            if line != "":
                self.lines.append(line)

    def length(self):
        return len(self.lines)

    def has_line(self, line):
        found = False
        for l in self.lines:
            l = l.strip()
            if l == line:
                found = True
                break
        assert_true(found)

    def __str__(self):
        r = ""
        for line in self.lines:
            r += ">> " + line + "\n"
        return r

    def __repr__(self):
        return self.__str__()
