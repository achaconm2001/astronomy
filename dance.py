from manim import *
from planets import PLANETS

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
