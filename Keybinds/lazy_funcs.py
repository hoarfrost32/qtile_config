from libqtile.command import lazy
import subprocess

@lazy.function
def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

@lazy.function
def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

# End Session by either locking, restarting or shutting down.
@lazy.function
def end_session(qtile, end_how):
    if end_how == "lock_session":
        subprocess.run(["dm-tool lock"], shell=True)
    elif end_how == "shutdown":
        subprocess.run(["shutdown now"], shell=True)
    elif end_how == "restart":
        subprocess.run(["shutdown -r now"], shell=True)

@lazy.function
def screencap(qtile):
    subprocess.run(["flameshot gui"], shell = True)

@lazy.function
def audio_controls(qtile, control_how):
    cmd_to_run = "amixer -D default sset Master "
    cmd_to_run += control_how
    subprocess.run([cmd_to_run], shell=True)

@lazy.function
def media_controls(qtile, do_what):
    cmd_to_run = "playerctl "
    cmd_to_run += do_what
    subprocess.run([cmd_to_run], shell=True)