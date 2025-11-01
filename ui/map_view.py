import tkinter as tk
import tkintermapview

class MapView(tkintermapview.TkinterMapView):
    def __init__(self, parent, on_click_callback=None):
        super().__init__(parent, width=700, height=450, corner_radius=12)
        self.on_click_callback = on_click_callback
        # Vista mundial
        self.set_position(20, 0)
        self.set_zoom(2)
        # Click izquierdo
        self.add_left_click_map_command(self._handle_click)

    def _handle_click(self, coords):
        lat, lon = coords
        if self.on_click_callback:
            self.on_click_callback(lat, lon)

    def focus_to(self, lat: float, lon: float, zoom: int = 5):
        self.set_position(lat, lon)
        self.set_zoom(zoom)

