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

SCALE = 2
TOTAL_DURATION = 60

PLANET_1 = PLANETS["venus"]
PLANET_2 = PLANETS["earth"]


class PlanetDance(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane))
        self.wait()

        sun = Dot(color=YELLOW).move_to([0, 0, 0])
        planet1 = Dot(color=PLANET_1.get("color")).move_to([1 * SCALE, 0, 0])
        planet2 = Dot(color=PLANET_2.get("color")).move_to([1.5 * SCALE, 0, 0])

        self.play(Create(sun))
        self.play(Create(planet1))
        self.play(Create(planet2))
        self.wait()

        tracker = ValueTracker(0)

        def create_line(mob):
            value = tracker.get_value()
            if value != 1:
                tracker.set_value(value + 1)
                return

            tracker.set_value(0)
            line = Line(start=planet2.get_center(), end=planet1.get_center(), stroke_width=0.5)
            self.add(line)

        planet2.add_updater(create_line)

        planet1_rotations = 8
        planet2_rotations = 13

        self.play(
            Rotating(planet1, radians=TAU * planet1_rotations, about_point=[0, 0, 0], rate_func=linear, run_time=TOTAL_DURATION), 
            Rotating(planet2, radians=TAU * planet2_rotations, about_point=[0, 0, 0], rate_func=linear, run_time=TOTAL_DURATION)
        )
        self.wait()
