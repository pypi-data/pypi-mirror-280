try:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent))
except Exception:
    raise

from atexit import register, unregister
from multiprocessing import Process, util
from subprocess import Popen
from time import sleep

from dash import Dash

import __ini__

__project_name__ = "Simple Rich Trading Journal"


def run():
    print("\x1b[33m[ REDIRECT ]\x1b[m", sys.argv[0], "->", __file__)
    red = Popen([sys.executable, __file__] + sys.argv[1:], stdin=sys.stdin, stderr=sys.stderr, stdout=sys.stdout, )
    print("\x1b[33m[ REDIRECT ]\x1b[m", "spawned", red.pid)
    if not __ini__.FLAGS.detach:
        while red.returncode is None:
            print("\x1b[33m[ REDIRECT ]\x1b[m", "communicate", red.pid)
            try:
                red.communicate()
            except KeyboardInterrupt:
                break
        print("\x1b[33m[ REDIRECT ]\x1b[m", "exit", red.returncode)
    else:
        print("\x1b[33m[ REDIRECT ]\x1b[m", "detach")


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

        # suppress exception ##############################################################################

        unregister(util._exit_function)

        def atexit(*args, **kwargs):
            try:
                util._exit_function(*args, **kwargs)
            except KeyboardInterrupt:
                print("\n\x1b[32m[ Server Process ]\x1b[m PID:", self.pid, "exit", flush=True)

        register(atexit)

        ###################################################################################################
        
        if __ini__.FLAGS.quiet:

            print("[ Quiet ]")

            class null:

                @staticmethod
                def write(*_): return
                flush = write

            sys.stderr = null

        app.run(debug=False, host=__env__.appHost, port=__env__.appPort)


def _suppress_exc(*args, **kwargs):
    try:
        util._exit_function(*args, **kwargs)
    except KeyboardInterrupt:
        print("\n\x1b[32m[ Server Process ]\x1b[m", "exit 0", flush=True)


if __name__ == "__main__":
    import __env__

    if ping := __env__._ping():
        print(f"\x1b[33m[ PING ]\x1b[m", "was successful:", flush=True)
        print(ping.decode())
        print(f"\x1b[33m[ PING ]\x1b[m", "skip server start...", flush=True)
    else:
        server_proc = Server(name="srtj-server")
        server_proc.start()

        print("\x1b[32m[ Server Process ]\x1b[m PID:", server_proc.pid, flush=True)

        # suppress exception ##############################################################################

        unregister(util._exit_function)
        register(_suppress_exc)

        ###################################################################################################

        # wait for server #################################################################################

        __env__.make_pong_file(server_proc.pid)

        for i in range(1, 21):
            print(f"\x1b[33m[ PING ]\x1b[m", f"({i})", __env__.URL, flush=True)
            if __env__._ping():
                break
            sleep(.1)
        else:
            print(f"\x1b[33m[ PING ]\x1b[m", "no success, continue...", flush=True)

        ###################################################################################################

    __env__.CALL_GUI()

    print("\x1b[32m[ Main Process ]\x1b[m DONE", flush=True)
