class Log:
    def __init__(self, output):
        self.output = output
        self.lines = []
        for line in output.split("\n"):
            if line != "":
                self.lines.append(line)

    def length(self):
        return len(self.lines)

    def __str__(self):
        r = ""
        for line in self.lines:
            r += ">> " + line + "\n"
        return r

    def __repr__(self):
        return self.__str__()
