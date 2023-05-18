from datetime import datetime
from pytz import timezone
from folium.plugins import BeautifyIcon
from typing import get_args, get_origin, Literal

ICON_SHAPE = Literal[None, "circle", "marker", "circle-dot", "rectangle", "rectangle-dot", "doughnut"]


def enforce_literals(function):
    """Decorator to make sure no one passes in an invalid string."""
    def wrapper(*args, **kwargs): # This is the function that will be returned
        # Loop through the arguments and check if they are valid
        for i in range(len(function.__annotations__.items())):
            name, type_ = list(function.__annotations__.items())[i]
            value = args[i]
            options = get_args(type_)
            if get_origin(type_) is Literal and value not in options: # If it is a list of possible strings and if the value is not in the list
                raise AssertionError(f"'{value}' is not in {options} for '{name}'") # Raise error
        function(*args, **kwargs) # Call the function
    return wrapper


def toDateTime(str_time) -> datetime:
    """Converts a string time to a datetime object.
    # Parameters:
    str_time: :class:`str`
        The string time to convert.
    """
    str_time = str_time.replace("T", "-").replace("Z", "")
    date = datetime.strptime(str_time, "%Y-%m-%d-%H:%M:%S").replace(tzinfo=timezone('UTC'))
    date = date.astimezone(timezone('US/Pacific'))
    return date

# @enforce_literals
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
    ) -> BeautifyIcon:
    """Creates a BeautifyIcon object.
    # Parameters:
    icon: :class:`str` = None
        The icon to use from either glyphicons or font-awesome.

    icon_shape: :class:`str` = "circle"
        The shape of the icon. Valid options are "marker", "circle-dot", "rectangle", "rectangle-dot", "doughnut".
   
    border_width: :class:`int` = 3
        The width of the border of the icon.

    border_color: :class:`str` = "#000"
        The color of the border of the icon.

    text_color: :class:`str` = "#000"
        The color of the text of the icon.

    background_color: :class:`str` = "#FFF"
        The background color of the icon.

    inner_icon_style: :class:`str` = ""
        The style of the inner icon. Must be CSS styling.

    spin: :class:`bool` = False
        Whether or not the icon should spin.

    number: :class:`int` = None
        The number to display on the icon. If None, no number will be displayed.

    icon_size: :class:`list` = [22, 22]
        The size of the icon in pixels.

    icon_anchor: :class:`list` = []
        The anchor of the icon. If empty, it will be centered.

    **kwargs: :class:`Any`
        Any other arguments to pass to the BeautifyIcon object.

    # Returns:
    :class:`BeautifyIcon`
        The BeautifyIcon object.
    """
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
        **kwargs
        )
