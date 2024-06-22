from spotzero.dbus_handler import DBusHandler

dbus_handler = DBusHandler()


class Linux:
    def __init__(self):
        pass

    def play_uri(uri: str):
        dbus_handler.interface.OpenUri(uri)

    def skip_song():
        dbus_handler.interface.Next()

    def prev_song():
        dbus_handler.interface.Previous()

    def toggle_play():
        dbus_handler.interface.PlayPause()

    def resume():
        dbus_handler.interface.Play()

    def pause():
        dbus_handler.interface.Stop()

    def set_volume(value: float):
        dbus_handler.set_property("Volume", value)

    def change_volume(amount: float):
        current_volume = dbus_handler.get_property("Volume")
        dbus_handler.set_property("Volume", current_volume + amount)
