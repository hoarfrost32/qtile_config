from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from libqtile import extension

from .lazy_funcs import screencap

mod = "mod4"
mod1 = "alt"
mod2 = "control"

launch = [
# LAUNCH PROGRAMS

  # GUI PROGRAMS
    Key([mod], "i", lazy.spawn("lapce")),                      # IDE, Lapce for now.
    Key([mod], "b", lazy.spawn("firefox")),                   # Browser.
    # KeyChord([mod], "b", [
    #   Key([], "p", lazy.function(
    #     lambda qtile: qtile.cmd_spawn("firefox --private-window")
    #   )),
    # ]),                                                       # Private Browser.
    Key([mod], "d", lazy.spawn("thunar")),                    # File Manager.
    Key([mod, "shift"], "s", screencap),                      # Screenshot but keybind same as in windows
    Key([], "Print", screencap),                              # Screenshot Utility.
    Key(["mod1"], "t", lazy.spawn("telegram-desktop")),       # Telegram.

  # TERMINAL/TUI PROGRAMS
    Key([mod], "t", lazy.spawn("alacritty")),                 # Alacritty.

  # Run rofi for window launching
  Key([mod], "r", lazy.spawn("rofi -show drun"))
]
