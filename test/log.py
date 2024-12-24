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

    def has_lines(self, lines: list, ignore_whitespaces=False) -> "Log":
        for line in lines:
            self.has_line(line, ignore_whitespaces)
        return self

    def has_line(self, line: str, ignore_whitespaces=False, revert=False) -> "Log":

        def compare(l1, l2):
            l1 = l1.strip()
            l2 = l2.strip()
            if ignore_whitespaces:
                l1 = l1.replace(" ", "")
                l2 = l2.replace(" ", "")
            return l1 == l2

        found = False
        for l in self.lines:
            l = l.strip()
            if compare(l, line):
                found = True
                break

        if revert:
            found = not found

        assert_true(found)
        return self

    def __str__(self):
        r = ""
        for line in self.lines:
            r += ">> " + line + "\n"
        return r

    def __repr__(self):
        return self.__str__()
