import subprocess

from libqtile import bar, widget
from libqtile.config import Screen
from qtile_extras.widget.decorations import PowerLineDecoration

from Widgets.widgets import widgets_list1
from Widgets.scnd_widgets import widgets_list2
from color import init_colors
    
colors = init_colors()

def init_screens():
    screens = [
            Screen(
                top=bar.Bar(
                    widgets=widgets_list1, size=30, opacity=0.8, margin = [10, 10, 3, 10],
                ),
            ), 
        ] 
    
    num_mon = "xrandr --listactivemonitors | grep + | wc -l"
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
        del widgets_list1[5:6]
        screens.insert(0, Screen(bottom=bar.Bar(widgets=widgets_list1, size=30, opacity=0.8, margin = [0, 0, 0, 0])))
        screens.pop() 
 
    else:

        for _ in range(1, connected_monitors):

            del widgets_list2[12:14]

            screens.append(Screen(bottom=bar.Bar(widgets=widgets_list2, size=30, opacity=0.8, margin = [0, 0, 0, 0])))

    return screens 
