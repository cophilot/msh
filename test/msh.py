import os

from my_assertion import assert_true, assert_false


class MSH:

    EXECUTABLE = "./out/msht"
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
        print(f">> {command}")
        result = os.popen(command)
        output = result.read()
        exit_code = result.close()
        suc = True
        if exit_code is not None:
            suc = False
        return suc, output
