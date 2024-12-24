import os

from my_assertion import assert_true, assert_false
from fs.dir import Dir
from log import Log


class MSH:

    EXECUTABLE = "./out/msht"
    HOME = None
    CONFIG = "editor_command=echo"

    _BUILT = False

    @staticmethod
    def build():
        os.system("./.scripts/build ./out/msht -testing-mode")
        # check if the executable exists
        if not os.path.exists(MSH.EXECUTABLE):
            raise FileNotFoundError(
                "Executable not found after build: " + MSH.EXECUTABLE
            )
        MSH._BUILT = True

    @staticmethod
    def setup():
        MSH.HOME = Dir(".myshell-testing")
        MSH.HOME.add_dir("scripts").make()

        MSH.HOME.add_file(".conf", content=MSH.CONFIG).make()

    @staticmethod
    def run_suc(command: str):
        suc, output = MSH.run(command)
        if not assert_true(suc, raise_assertion_error=False):
            raise AssertionError(f"Command '{command}' failed: \n{output}")
        return output

    @staticmethod
    def run_fail(command: str):
        suc, output = MSH.run(command)
        if not assert_false(suc, raise_assertion_error=False):
            raise AssertionError(
                f"Command '{command}' succeeded (expected failure): \n{output}"
            )
        return output

    @staticmethod
    def run(command: str):
        if not MSH._BUILT:
            MSH.build()

        if command.startswith("msh"):
            command = command[4:]

        command = f"{MSH.EXECUTABLE} {command.strip()}"
        print(f"$ {command}")
        result = os.popen(command)
        output = Log(result.read())
        print(output)

        exit_code = result.close()
        suc = exit_code is None

        return suc, output

    @staticmethod
    def cleanup():
        MSH.HOME.delete()
