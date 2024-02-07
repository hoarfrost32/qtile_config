from libqtile.config import Key
from libqtile.command import lazy

from .lazy_funcs import window_to_next_screen, window_to_previous_screen, end_session

mod = "mod4"
mod1 = "alt"
mod2 = "control"

wind_mngmnt = [

# KILL ACTIVE WINDOW
    Key([mod], "q", lazy.window.kill()),

# LOCK ACTIVE SESSION
    Key([mod], "l" , end_session("lock_session")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod], "f", lazy.layout.flip()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

# SUPER + SHIFT KEYBINDINGS

  #FULLSCREEN AND RESTART
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "r", lazy.reload_config()),

  # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE & BSP LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
 
  # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

# SUPER + CONTROL KEYBINDINGS

  # RESIZE UP, DOWN, LEFT, RIGHT

      Key([mod, "control"], "Right",
          lazy.layout.grow_right(),
          lazy.layout.grow(),
          lazy.layout.increase_ratio(),
          lazy.layout.delete(),
          ),
      Key([mod, "control"], "Left",
          lazy.layout.grow_left(),
          lazy.layout.shrink(),
          lazy.layout.decrease_ratio(),
          lazy.layout.add(),
          ),
      Key([mod, "control"], "Up",
          lazy.layout.grow_up(),
          lazy.layout.grow(),
          lazy.layout.decrease_nmaster(),
          ),
      Key([mod, "control"], "Down",
          lazy.layout.grow_down(),
          lazy.layout.shrink(),
          lazy.layout.increase_nmaster(),
          ),

  # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

  # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
]