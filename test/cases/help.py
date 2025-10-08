from msh import MSH
from test_case import TestCase


class HelpTestCase(TestCase):
    def __init__(self):
        super().__init__("help")

    def run(self):

        #  help|h - Get help for myshell

        MSH.run_suc("help")
        MSH.run_fail("help notacommand")
        
        all_commands = MSH.get_all_commands()
        for c in all_commands:
            log = MSH.run_suc(f"help {c.name}")
            log.has_line(merge_name_and_short_form(c.name, c.short_form), can_be_substring=True)
            for not_c in all_commands:
                if not_c.name == c.name:
                    continue
                log.not_has_line(merge_name_and_short_form(not_c.name, not_c.short_form), can_be_substring=True)

def merge_name_and_short_form(name, short_form):
    if short_form:
        return f"{name}|{short_form}"
    return name