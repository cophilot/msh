class MSHTestingDebugger:

    IS_ENABLED = False

    @staticmethod
    def stop_execution():
        if not MSHTestingDebugger.IS_ENABLED:
            return
        print("Execution stopped. Press Enter to continue...")
        input()
