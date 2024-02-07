from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration

from color import init_colors
import os

home = os.path.expanduser('~')

colors = init_colors()

widgets_list2 = [
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
                padding = 8,
                foreground = colors[1],
                background = colors[2],
                decorations = [PowerLineDecoration(path='forward_slash', size=8)]
            ),
            widget.WindowName(
                    width=bar.CALCULATED,
                    padding = 15,
                    font="Jetbrains Mono Bold",
                    fontsize = 15,
                    foreground = colors[2],
                    background = colors[1],
                    max_chars = 98,
                    for_current_screen = False,
            ),
            widget.Spacer(background = colors[1], decorations = [PowerLineDecoration(path='forward_slash', size=8)]),
            widget.Sep(
                linewidth = 0,
                padding = 15,
                foreground = colors[1],
                background = colors[2],
            ),
            widget.Net(
                background=colors[2],
                font='Jetbrains Mono',
                fontsize=20,
                format='{down:.0f}{down_suffix} ↓ ',
                decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[3])]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 5,
                foreground = colors[1],
                background = colors[2],
                decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[3])]
            ),
            widget.Memory(
                font="Jetbrains Mono",
                format = '{MemUsed:.0f}M',
                update_interval = 1,
                fontsize = 20,
                background = colors[2],
                padding=0,
                decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[3])]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 9,
                foreground = colors[1],
                background = colors[2],
            ),
            widget.Clock(
                    background = colors[2],
                    font = "Jetbrains Mono",
                    fontsize = 20,
                    timezone = "Asia/Kolkata",
                    format="🕰 %H:%M",
                    padding = 0,
                    decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[4])]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 10,
                foreground = colors[1],
                background = colors[2],
            ),
            widget.Systray(
                background=colors[2],
                icon_size=25,
                padding = 5,
                decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[1])]
            ),
            widget.Sep(
                linewidth = 0,
                padding = 10,
                foreground = colors[2],
                background = colors[2],
            ),
            widget.TextBox(
                text=" ",
                background=colors[2],
                font="Jetbrains Mono",
                fontsize=18,
                padding=0,
                decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[3])]
            ),
            widget.Volume(
                background = colors[2],
                font = "Jetbrains Mono",
                fontsize = 18,
                decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[3])]
            ),
            widget.TextBox(
                text="   🗲",
                background=colors[2],
                font="Jetbrains Mono",
                fontsize=14,
                padding=0,
                decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[3])]
            ),
            widget.Battery(
                    font="Jetbrains Mono",
                    update_interval = 10,
                    fontsize = 16,
                    padding = 5,
                    show_short_text = False,
                    background = colors[2],
                    format = '{percent:1.0%}',
                    decorations = [BorderDecoration(border_width = [0, 0, 2, 0], colour=colors[3])]
            ),
        ]
