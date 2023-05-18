from datetime import datetime
from pytz import timezone
from folium.plugins import BeautifyIcon
from typing import get_args, get_origin, Literal, Optional

ICON_SHAPE = Literal["circle", "marker", "circle-dot", "rectangle", "rectangle-dot", "doughnut"]


# This is a decorator that will be used to check if arguments are valid
def enforce_literals(function):
    def wrapper(*args, **kwargs): # This is the function that will be returned
        # Loop through the arguments and check if they are valid
        for i in range(len(function.__annotations__.items())):
            name, type_ = list(function.__annotations__.items())[i]
            if i >= len(args): # No more arguments
                if name not in kwargs: # Check if the item is in the kwargs
                    continue # Skip and let the function default to keyword argument
                value = kwargs[name] # There is a kwarg argument so use that
            else: # There is an argument
                value = args[i] # Use the argument
            print(f"name: {name}, type: {type_}, value: {value}")
            options = get_args(type_) # Get the possible options
            if get_origin(type_) is Literal and value not in options: # If it is a list of possible strings and if the value is not in the list
                raise AssertionError(f"'{value}' is not in {options} for '{name}'") # Raise error
        function(*args, **kwargs) # Call the original function
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
    icon: Optional[str] = None,
    icon_shape: Optional[ICON_SHAPE] = "circle",
    border_width: Optional[int] = 3,
    border_color: Optional[str] = "#000",
    text_color: Optional[str] = "#000",
    background_color: Optional[str] = "#FFF",
    inner_icon_style: Optional[str] = "",
    spin: Optional[bool] = False,
    number: Optional[int] = None,
    icon_size: Optional[list] = [22, 22],
    icon_anchor: Optional[list] = [],
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
    print(type(icon_shape))
    i = BeautifyIcon(
        icon=icon,
        border_color=border_color,
        text_color=text_color,
        icon_shape=str(icon_shape),
        inner_icon_style=inner_icon_style,
        icon_size=icon_size,
        icon_anchor=icon_anchor,
        **kwargs
        )
    print(i.options['iconShape'])
    return i
