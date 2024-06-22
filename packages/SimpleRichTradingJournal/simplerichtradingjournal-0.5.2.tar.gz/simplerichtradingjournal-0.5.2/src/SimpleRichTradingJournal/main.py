try:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent))
except Exception:
    raise

from multiprocessing import Process
from subprocess import Popen

from dash import Dash


__project_name__ = "Simple Rich Trading Journal"


def run():
    print("[ REDIRECT ]", sys.argv[0], "->", __file__)
    red = Popen([sys.executable, __file__] + sys.argv[1:], stdin=sys.stdin, stderr=sys.stderr, stdout=sys.stdout, )
    print("[ REDIRECT ]", "spawned", red.pid)
    while red.returncode is None:
        print("[ REDIRECT ]", "communicate", red.pid)
        red.communicate()
    print("[ REDIRECT ]", "exit", red.returncode)


class Server(Process):

    def run(self):
        import __env__
        import layout

        __env__.SERVER_PROC = self

        app = Dash(
            __project_name__,
            title=__env__.PROFILE or __project_name__,
            update_title="working...",
            assets_folder=__env__.DASH_ASSETS,
            assets_url_path=__env__._folder_profile_assets,
        )
        app.layout = layout.LAYOUT
        app._favicon = ".favicon.ico"
        try:
            import callbacks
        except Exception:
            raise

        app.run(debug=False, host=__env__.appHost, port=__env__.appPort)


if __name__ == "__main__":
    import __env__

    server_proc = Server(name="srtj-server")
    server_proc.start()

    print("\x1b[32m[ Server Process ]\x1b[m PID:", server_proc.pid, flush=True)

    __env__.CALL_GUI()

    print("\x1b[32m[ Main Process ]\x1b[m DONE", flush=True)
