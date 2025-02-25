import os
import subprocess
from typing import List  # noqa: F401

# libqtile imports
from libqtile import hook
from libqtile.config import Drag, Group, Key, DropDown, ScratchPad
from libqtile.lazy import lazy

# custom imports
from screens import init_screens
from Layouts.layouts import layouts
from Layouts.floating import floating_layout
from Keybinds.launch import launch
from Keybinds.window_management import wind_mngmnt
from Keybinds.media import media
from popups import show_power_menu

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

@hook.subscribe.startup_once
def autostart():
    processes = [
      ['nm-applet'],
      ['blueman-applet'],
      ["xrandr", "--output", "DP-2", "--primary"],
      ["xrandr", "--output", "DP-4", "--right-of", "DP-2"],
      ['flameshot'],
      ['dunst'],
      ['parcellite']
    ]
    
    for p in processes:
        subprocess.Popen(p)

@hook.subscribe.startup
def autorun():
    processes = [
        ['nitrogen', '--restore']
    ]

    for p in processes:
        subprocess.Popen(p)

layout = layouts
floating = floating_layout

keys = wind_mngmnt + launch + media

groups = []
for i in range(0, 7):
    groups.append(
        Group(
            name=str(i+1),
            layout="monadtall",
            label="⬤ ",
        ))

dropdowns = [
    DropDown("Terminal", "alacritty -e tmux -u", x=0.05, y=0.2, width=0.9, height=0.6, opacity=0.9),
    DropDown("Ranger", "alacritty -e ranger", x=0.05, y=0.2, width=0.9, height=0.6, opacity=0.9),
    # DropDown("Qute", "qutebrowser", x=0.49, y=0.02, width=0.5, height=0.95, opacity=0.9),
    DropDown("Mail", "thunderbird", x=0.05, y=0.1, width=0.9, height=0.75, opacity=0.9, on_focus_lost_hide=False),
]

for i in dropdowns:
    i.floating = True

groups.append(
   ScratchPad('0', dropdowns),
)

for i in groups:

    if i.name != "0":
        keys.extend([
        #CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-7 AND STAY ON WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-7 AND FOLLOW MOVED WINDOW TO WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),

        # POWER MENU
            Key([mod, "shift"], "q", lazy.function(show_power_menu)),
        ])

keys.extend([
# SCRATCHPADS
    Key(['control'], "1", lazy.group['0'].dropdown_toggle('Ranger')),
    # Key(['control'], "2", lazy.group['0'].dropdown_toggle('Qute')),
    Key(['control'], "3", lazy.group['0'].dropdown_toggle('Terminal')),
    Key(['control'], "4", lazy.group['0'].dropdown_toggle('Mail')),
    
# ROFI
    # Use Rofi to see all the windows
    Key(["mod1"], "tab", lazy.spawn('rofi -show window'))
])

screens = init_screens()

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

main = None

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "Qtile"
