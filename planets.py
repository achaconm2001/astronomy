from math import radians
from manim import *

MILLION = 1_000_000

SUN = {
    "radius": 696_340,
    "distance_to_sun": 0,
    "color": YELLOW_C,
    "year_duration": 0
}

MERCURY = {
    "radius": 2_439.7,
    "distance_to_sun": 58 * MILLION,
    "color": GOLD_D,
    "year_duration": 88
}

VENUS = {
    "radius": 6_051.8,
    "distance_to_sun": 108.2 * MILLION,
    "color": YELLOW_E,
    "year_duration": 225
}

EARTH = {
    "radius": 6_370,
    "distance_to_sun": 149 * MILLION,
    "color": BLUE_C,
    "year_duration": 365
}

MARS = {
    "radius": 3_389.5,
    "distance_to_sun": 227.9 * MILLION,
    "color": RED_C,
    "year_duration": 687
}

JUPITER = {
    "radius": 69_911,
    "distance_to_sun": 778 * MILLION,
    "color": GOLD_D,
    "year_duration": 4_333
}

SATURN = {
    "radius": 58_232,
    "distance_to_sun": 1_434 * MILLION,
    "color": GOLD_D,
    "year_duration": 10_756
}

URANUS = {
    "radius": 25_362,
    "distance_to_sun": 2_871 * MILLION,
    "color": BLUE_C,
    "year_duration": 30_687
}


NEPTUNE = {
    "radius": 24_622,
    "distance_to_sun": 4_495 * MILLION,
    "color": BLUE_A,
    "year_duration": 60_190
}

PLANETS = {
    "sun": SUN,
    "mercury": MERCURY,
    "venus": VENUS,
    "earth": EARTH,
    "mars": MARS,
    "jupiter": JUPITER,
    "saturn": SATURN,
    "uranus": URANUS,
    "neptune": NEPTUNE
}


class PlanetsScale(Scene):
    def construct(self):
        self.camera.frame.set_width(50)
        self.camera.frame.move_to(23.5 * RIGHT)

        plane = NumberPlane(x_range=[-50, 50])
        self.play(Create(plane))
        self.wait()

        sun = Dot(color=YELLOW_C).move_to([0, 0, 0])
        mercury = Dot(color=GOLD_D).move_to([0.5, 0, 0])
        venus = Dot(color=YELLOW_E).move_to([1, 0, 0])
        earth = Dot(color=BLUE_C).move_to([1.5, 0, 0])
        mars = Dot(color=RED_C).move_to([2, 0, 0])
        jupiter = Dot(color=GOLD_C).move_to([7.8, 0, 0])
        saturn = Dot(color=GOLD_D).move_to([14.3, 0, 0])
        uranus = Dot(color=BLUE_D).move_to([28.8, 0, 0])
        neptune = Dot(color=BLUE_C).move_to([45, 0, 0])

        self.play(Create(sun))
        self.play(Create(mercury))
        self.play(Create(venus))
        self.play(Create(earth))
        self.play(Create(mars))
        self.play(Create(jupiter))
        self.play(Create(saturn))
        self.play(Create(uranus))
        self.play(Create(neptune))
        self.wait()


DISTANCE_RADIO = 50 * MILLION
INCLUDE_REAL_RADIUS = True
RADIUS_RADIO = MILLION / 10


def get_radius(real_radius):
    if not INCLUDE_REAL_RADIUS:
        return 0.2
    return real_radius / RADIUS_RADIO


def create_planet(planet):
    radius = get_radius(planet["radius"])
    distance_from_sun = planet["distance_to_sun"] / DISTANCE_RADIO
    if distance_from_sun != 0:
        distance_from_sun += get_radius(SUN["radius"])
    return Dot(color=planet["color"], radius=radius).move_to([distance_from_sun, 0, 0])


class PlanetsReal(Scene):
    def construct(self):
        self.camera.frame.set_width(100)
        self.camera.frame.move_to(47.5 * RIGHT)

        sun = create_planet(SUN)
        mercury = create_planet(MERCURY)
        venus = create_planet(VENUS)
        earth = create_planet(EARTH)
        mars = create_planet(MARS)
        jupiter = create_planet(JUPITER)
        saturn = create_planet(SATURN)
        uranus = create_planet(URANUS)
        neptune = create_planet(NEPTUNE)

        self.play(Create(sun))
        self.play(Create(mercury))
        self.play(Create(venus))
        self.play(Create(earth))
        self.play(Create(mars))
        self.play(Create(jupiter))
        self.play(Create(saturn))
        self.play(Create(uranus))
        self.play(Create(neptune))
        self.wait()
