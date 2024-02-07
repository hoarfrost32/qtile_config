from libqtile.config import Key
from libqtile.command import lazy
from libqtile import extension

from .lazy_funcs import screencap

mod = "mod4"
mod1 = "alt"
mod2 = "control"

launch = [
# LAUNCH PROGRAMS

  # GUI PROGRAMS
    Key([mod], "i", lazy.spawn("code")),                  # IDE, VSCode for now.
    Key([mod], "b", lazy.spawn("firefox")),               # Browser.
    Key([mod], "d", lazy.spawn("thunar")),                # File Manager.
    Key([mod, "shift"], "s", screencap),                 # Screenshot but keybind same as in windows
    Key([], "Print", screencap),                          # Screenshot Utility.
    Key(["mod1"], "t", lazy.spawn("telegram-desktop")),   # Telegram.

  # TERMINAL/TUI PROGRAMS
    Key([mod], "t", lazy.spawn("alacritty")),                   # Alacritty.
    Key([mod], "m", lazy.spawn("alacritty -e ranger")),         # Ranger, a TUI file manager.

  # Run Dmenu
  Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">_",
        dmenu_bottom=True,
        font="Jetbrains Mono",
        background="#24273a",
        foreground='#7fbbb3',
        selected_background="#B3ABF0",
        selected_foreground="#24273a",
        fontsize = 12,
        dmenu_ignorecase=True,
    ))),
]