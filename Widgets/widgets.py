import os

from libqtile import bar

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

from color import init_colors

home = os.path.expanduser('~')

colors = init_colors()

widgets_list1 = [
            widget.QuickExit(
                background = colors[2],
                foreground = colors[3],
                font = "Jetbrains Mono",
                default_text = '⏻',
                fontsize = 22,
                padding = 11,
                countdown_start = 3,
                countdown_format = '⏻:{}s'
            ),
            widget.GroupBox(
                    font="Jetbrains Mono",
                    
                    # Margins
                    margin_y = 1.8,
                    margin_x = 10,

                    # Padding
                    padding_y = 0,
                    padding_x = 5,

                    # Disable drag
                    highlight_method = "text",
                    disable_drag = True,

                    # Fonts and Colors
                    fontsize = 16,
                    background = colors[2],
                    active = colors[3],
                    inactive = colors[1],
                    this_current_screen_border = colors[4],
                    
                    use_mouse_wheel = True,
            ),
            widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    foreground = colors[1],
                    background = colors[2]
            ),
            widget.CurrentLayoutIcon(
                background = colors[2],
                fontsize = 13,
                padding = 0,
                custom_icon_paths = ["~/.config/qtile/icons/"], 
            ),
            widget.Sep(
                linewidth = 0,
                padding = 4,
                foreground = colors[1],
                background = colors[2]
            ),
            widget.CurrentLayout(
                background = colors[2],
                foreground = colors[1],
                font = "Jetbrains Mono Bold",
                fontsize = 16,
                padding = 5,
            ),
            widget.Sep(
                linewidth = 0,
                padding = 5,
                foreground = colors[1],
                background = colors[2],
                decorations = [PowerLineDecoration(path='rounded_left', size=8)]
            ),
            widget.WindowName(
                    width=bar.CALCULATED,
                    padding = 15,
                    font="Jetbrains Mono Bold",
                    fontsize = 15,
                    foreground = colors[2],
                    background = colors[1],
                    max_chars = 150,
                    for_current_screen = True,
            ),
            widget.Spacer(background = colors[1]),
            widget.Sep(
                linewidth = 0,
                padding = 10,
                foreground = colors[1],
                background = colors[1],
                decorations = [PowerLineDecoration(path='rounded_right', size=8, padding_x=20)]
            ),
            widget.Net(
                background=colors[2],
                font='Jetbrains Mono',
                fontsize=20,
                format=' {down:.0f}{down_suffix} ↓ ',
            ),
            widget.Memory(
                font="Jetbrains Mono",
                format = '{MemUsed:.0f}M',
                update_interval = 1,
                fontsize = 20,
                background = colors[2],
                padding=5,
            ),
            widget.Sep(
                linewidth = 0,
                padding = 15,
                foreground = colors[1],
                background = colors[2],
                decorations = [PowerLineDecoration(path='rounded_right', size=8, padding_x=20)]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 8,
                foreground = colors[1],
                background = colors[3],
            ),
            widget.TextBox(
                text="🗓",
                background=colors[3],
                foreground=colors[2],
                font="Jetbrains Mono",
                fontsize=20,
                padding=0,
            ),
            widget.Clock(
                    foreground = colors[2],
                    background = colors[3],
                    fontsize = 20,
                    font = "Jetbrains Mono",
                    timezone = "Asia/Kolkata",
                    format="%d-%m-%Y",
                    padding=10,
            ),
            widget.Sep(
                linewidth = 0,
                padding = 8,
                foreground = colors[1],
                background = colors[3],
                decorations = [PowerLineDecoration(path='rounded_right', size=8, padding_x=20)]
            ),
            widget.AnalogueClock(
                background = colors[4],
                hour_length = 0.3,
                minute_length = 0.5,
                adjust_y = -7,
                decorations = [RectDecoration(colour=colors[2], radius=11, filled=True, padding_y=3)]
            ),
            widget.Clock(
                    foreground = colors[2],
                    background = colors[4],
                    font = "Jetbrains Mono",
                    fontsize = 20,
                    timezone = "Asia/Kolkata",
                    format=" %H:%M",
            ),
            widget.Sep(
                linewidth = 0,
                padding = 10,
                foreground = colors[1],
                background = colors[4],
                decorations = [PowerLineDecoration(path='rounded_right', size=8, padding_x=20)]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[1],
                background = colors[6],
            ),
            widget.Systray(
                    background=colors[6],
                    icon_size=25,
                    padding = 5,
            ),
            widget.Sep(
                linewidth = 0,
                padding = 10,
                foreground = colors[1],
                background = colors[6],
                decorations = [PowerLineDecoration(path='rounded_right', size=8, padding_x=20)]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 10,
                foreground = colors[1],
                background = colors[2],
            ),
            widget.TextBox(
                text=" ",
                background=colors[2],
                font="Jetbrains Mono",
                fontsize=18,
                padding=0,
            ),
            widget.Volume(
                    background = colors[2],
                    font = "Jetbrains Mono",
                    fontsize = 18,
            ),
            widget.TextBox(
                text="   🗲",
                background=colors[2],
                font="Jetbrains Mono",
                fontsize=14,
                padding=0,
            ),
            widget.Battery(
                    font="Jetbrains Mono",
                    update_interval = 10,
                    fontsize = 16,
                    padding = 5,
                    show_short_text = False,
                    background = colors[2],
                    format = '{percent:1.0%}',
            ),
        ]