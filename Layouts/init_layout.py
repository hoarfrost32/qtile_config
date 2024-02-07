import subprocess

def init_layout_theme():

    num_mon = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
    command = subprocess.run(
        num_mon,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )    

    if command.returncode != 0:
        connected_monitors = 1

    else:
        connected_monitors = int(command.stdout.decode("UTF-8"))

    if connected_monitors == 1:
        return {"margin":5,
                "border_width":1,
                "border_focus": "#B5ACF5",
                "border_normal": "#565C74"
                }
    else:
        return {"margin":8,
                "border_width":2,
                "border_focus": "#B5ACF5",
                "border_normal": "#565C74"
                }