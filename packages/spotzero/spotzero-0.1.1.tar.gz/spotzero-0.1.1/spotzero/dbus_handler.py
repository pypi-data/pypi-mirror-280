import dbus
import sys


class DBusHandler:
    """
    Where to find every method/property: https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html

    A class that handles the DBus interface for the Media Player Daemon (MPD)
    on Linux.

    This class is used to interact with the player's interface through DBus.
    Through this class, you can call methods on the interface and read/write
    properties.

    Methods:
        self.interface (dbus.interface.Interface): The interface to the player.

    Reading/Writing Properties:
        `set_property(property, value):` Set the value of the given property.
        `get_property(property):` Get the value of the given property.

    """

    def __init__(self) -> None:
        self.session_bus = dbus.SessionBus()

        self.interface = self.get_interface("org.mpris.MediaPlayer2.Player")
        self.properties = self.get_interface("org.freedesktop.DBus.Properties")

    def get_interface(self, interface) -> dbus.Interface:
        try:
            interface = dbus.Interface(
                self.session_bus.get_object(
                    "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2"
                ),
                interface,
            )
        except dbus.exceptions.DBusException:
            # If we catch this exception, Spotify is not running.
            print(
                "\nSpotify was not found. Try restarting/opening it. This program requires Spotify APPLICATION open.\n"
            )
            sys.exit()

        return interface

    # METHOD HANDLING
    # self.interface.<method_name>(args) also works
    def call_method(self, method: str, *args) -> None:
        method = self.interface.get_dbus_method(method)(*args)

    def get_method(self, method: str):
        return self.interface.get_dbus_method(method)

    # PROPERTY HANDLING
    def set_property(self, property: str, value):
        """
        Make sure to provide the exact data type. If it requires a double, type 1.0 .
        """
        self.properties.Set("org.mpris.MediaPlayer2.Player", property, value)

    def get_property(self, property: str):
        return self.properties.Get("org.mpris.MediaPlayer2.Player", property)

    def _get_metadata(self):
        """
        Update the `self.metadate` variable
        """
        self.metadata = self.properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    # TODO:  possible remove this
    # def get_current_playing(self):
    #     self._get_metadata()  # TODO: double check that this has to be run every time
    #     playing = {}

    #     for key, value in self.metadata.items():
    #         if key == "xesam:album":
    #             playing["album"] = value

    #         elif key == "xesam:title":
    #             playing["title"] = value

    #         elif key == "xesam:artist":
    #             playing["artist"] = value[0]

    #     return "%s - %s [%s]" % (playing["artist"], playing["title"], playing["album"])
