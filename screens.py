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
    
    num_mon = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
    command1 = subprocess.run(
        num_mon,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )    
    
    name_mon = "xrandr | grep -w 'connected' | cut -d ' ' -f 1"
    command2 = subprocess.run(
        name_mon,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if command1.returncode != 0:
        connected_monitors = 1

    else:
        connected_monitors = int(command1.stdout.decode("UTF-8"))

    if connected_monitors == 1:
        screens.pop(0)
        widgets_list1.pop(7)

        widgets_list1.insert(7,
            widget.WindowName(
                width=bar.CALCULATED,
                padding = 15,
                font="Jetbrains Mono Bold",
                fontsize = 15,
                foreground = colors[2],
                background = colors[1],
                max_chars = 50,
                for_current_screen = True,
        ))
        
        screens.append(Screen(bottom=bar.Bar(widgets=widgets_list2, size=30, opacity=0.8, margin = [0, 0, 0, 0])))
 
    else:

        disp_lst = (command2.stdout.decode("UTF-8")).split("\n")

        for _ in range(1, connected_monitors):
            if disp_lst[_] == "DP-4":

                w_l = widgets_list1.copy()

                del w_l[19:23]

                w_l.insert(19,             
                    widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[4],
                        decorations = [PowerLineDecoration(path='rounded_right', size=8, padding_x=20)]
                    )
                )

                del w_l[0]
                del w_l[0]

                screens.append(Screen(top=bar.Bar(widgets=w_l, size=30, opacity=0.8, margin = [10, 10, 3, 10])))

            else:
                screens.append(Screen())

    return screens 
