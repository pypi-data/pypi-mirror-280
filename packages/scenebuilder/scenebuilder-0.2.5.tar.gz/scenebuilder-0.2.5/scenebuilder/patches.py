from numpy.typing import ArrayLike

import numpy as np
from matplotlib.patches import FancyArrow, Polygon
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

from scenebuilder.entities import Drone, Obstacle


class Arrow:
    """Class to create a FancyArrow object"""

    def __init__(self, start: ArrayLike, end: ArrayLike, ax: plt.Axes) -> None:
        self.start = np.array(start)
        self.end = np.array(end)
        self.arrow: FancyArrow = None
        self.ax = ax

    def create_arrow(self) -> FancyArrow:
        ds = self.end - self.start
        self.arrow = self.ax.arrow(
            *self.start,
            ds[0],
            ds[1],
            length_includes_head=True,
            head_width=0.2,
            head_length=0.2,
            fc="k",
            ec="k",
            linestyle="-"
        )
        return self.arrow

    def update_arrow_position(self, new_start: tuple, new_end: tuple):
        new_x_start, new_y_start = new_start
        new_x_end, new_y_end = new_end

        dx = new_x_end - new_x_start
        dy = new_y_end - new_y_start

        self.arrow.set_data(x=new_x_start, y=new_y_start, dx=dx, dy=dy)


class Marker:
    """Create an icon or marker patch to plot"""

    def __init__(self, position: ArrayLike, style: str) -> None:
        self.position = np.array(position)
        self.style = style
        self.marker: Line2D = None

    def create_marker(self) -> Line2D:
        self.marker = plt.plot(*self.position, self.style)[0]
        return self.marker

    def update_position(self, new_position: tuple):
        self.position = new_position
        self.marker.set_xdata([self.position[0]])
        self.marker.set_ydata([self.position[1]])


class DronePatch:
    """Graphical representation of the Drone including start and end markers and an arrow connecting the two"""

    def __init__(self, drone: Drone, ax: plt.Axes) -> None:
        self.drone = drone
        self.marker_start: Marker = None
        self.marker_end: Marker = None

        self.arrow: Arrow = None
        self.ax = ax

    def create_patches(self) -> tuple:
        # plot the arrow
        self.marker_start = Marker(
            self.drone.position[:2], "b*"
        )  # Initial position in blue

        self.marker_end = Marker(self.drone.goal[:2], "r*")  # Goal position in red

        # Add an arrow with a line using the 'arrow' function
        self.arrow = Arrow(self.drone.position[:2], self.drone.goal[:2], self.ax)

        # self.patches = (self.marker_start, self.marker_end, self.arrow)
        return (
            self.marker_start.create_marker(),
            self.marker_end.create_marker(),
            self.arrow.create_arrow(),
        )

    def remove(self) -> None:
        """Remove the three patches"""
        self.marker_start.marker.remove()
        self.marker_end.marker.remove()
        self.arrow.arrow.remove()

    def patches(self):
        return self.marker_start.marker, self.marker_end.marker, self.arrow.arrow

    def update(self) -> None:
        self.marker_start.update_position(self.drone.position[:2])
        self.marker_end.update_position(self.drone.goal[:2])
        self.arrow.update_arrow_position(self.drone.position[:2], self.drone.goal[:2])


class ObstaclePatch(Polygon):
    """
    Example usage:
    patch = BuildingPatch(ax, building_instance, facecolor='blue', edgecolor='red', linewidth=2.0)
    """

    def __init__(self, building: Obstacle, **kwargs) -> None:
        super().__init__(building.vertices, **kwargs)
        self.vertices = self.get_xy()
        # Storing original colors
        self.original_facecolor = self.get_facecolor()
        self.original_edgecolor = self.get_edgecolor()
        self.building = building

    def select(self):
        """Change appearance to represent selection."""
        # Change to a transparent red (or whatever visual cue you want for selection)
        self.set_facecolor((1, 0.4, 1, 0.7))
        self.set_edgecolor("black")

    def deselect(self):
        """Revert appearance to the original state."""
        self.set_facecolor(self.original_facecolor)
        self.set_edgecolor(self.original_edgecolor)

    def update_visual(self):
        """Update the visual representation based on the building state."""
        self.set_xy(self.building.vertices)
