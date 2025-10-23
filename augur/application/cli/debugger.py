# debugger.py
# from os import getenv


def initialize_flask_server_debugger_if_needed(func_name=None):
    # if getenv("DEBUGGER") == "True":
    import multiprocessing

    if multiprocessing.current_process().pid > 1:
        import debugpy

        debugpy.listen(("0.0.0.0", 10001))
        print(
            f"⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳. You will be connected to [{func_name}]",
            flush=True,
        )
        debugpy.wait_for_client()
        print(
            f"🎉 VS Code debugger attached, enjoy debugging 🎉. You are connected to [{func_name}]",
            flush=True,
        )
