from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)

from Keybinds.lazy_funcs import end_session
from color import init_colors

colors = init_colors()

def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="~/.config/qtile/icons/lock.png",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": end_session("lock_session")
            },
            highlight=colors[4],
        ),
        PopupImage(
            filename="~/.config/qtile/icons/restart.png",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": end_session("restart")
            },
            highlight=colors[4],
        ),
        PopupImage(
            filename="~/.config/qtile/icons/shutdown.png",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": end_session("shutdown")
            },
            highlight=colors[4],
        ),
        PopupText(
            text="Lock",
            fontsize=15,
            font="Jetbrains Mono",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Restart",
            fontsize=15,
            font="Jetbrains Mono",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            fontsize=15,
            font="Jetbrains Mono",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background=colors[2],
        border="#C29FEE",
        border_width=2,
        initial_focus=None,
    )

    layout.show(centered=True)