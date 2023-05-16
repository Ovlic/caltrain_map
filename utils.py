from datetime import datetime
from pytz import timezone
from typing import Union
from folium.plugins import BeautifyIcon

def toDateTime(str_time):
    str_time = str_time.replace("T", "-").replace("Z", "")
    date = datetime.strptime(str_time, "%Y-%m-%d-%H:%M:%S").replace(tzinfo=timezone('UTC'))
    date = date.astimezone(timezone('US/Pacific'))
    return date

def makeBeautifyIcon(
    icon:str=None,
    icon_shape:str=None,
    border_width:int=3,
    border_color:str="#000",
    text_color:str="#000",
    background_color:str="#FFF",
    inner_icon_style:str="",
    spin:bool=False,
    number:int=None,
    icon_size:list=[22, 22],
    icon_anchor:list=[],
    **kwargs
    ):
    """BeautifyIcon(icon: Any | None = None, icon_shape: Any | None = None, border_width: int = 3, border_color: str = "#000", text_color: str = "#000", background_color: str = "#FFF", inner_icon_style: str = "", spin: bool = False, number: Any | None = None, **kwargs: Any)"""
    
    if icon_anchor == []: # So it aligns to center instead
        icon_anchor = [icon_size[0]/2, icon_size[1]/2]
    
    return BeautifyIcon(
        icon=icon,
        border_color=border_color,
        text_color=text_color,
        icon_shape=icon_shape,
        inner_icon_style=inner_icon_style,
        icon_size=icon_size,
        icon_anchor=icon_anchor,
        )
