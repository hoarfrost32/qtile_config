from libqtile.config import Key

from .lazy_funcs import audio_controls, media_controls

mod = "mod4"
mod1 = "alt"
mod2 = "control"

media = [
    # AUDIO CONTROLS (mute still broken)
    Key(
        [], "XF86AudioRaiseVolume",
        audio_controls("5%+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        audio_controls("5%-")
    ),
    Key(
        [], "XF86AudioMute",
        audio_controls("toggle")
    ),

# MEDIA CONTROLS
    Key(
        [], "XF86AudioPlay",
        media_controls("play-pause")
    ),
    Key(
        [], "XF86AudioNext",
        media_controls("next")
    ),
    Key(
        [], "XF86AudioPrev",
        media_controls("previous")
    ),    
]