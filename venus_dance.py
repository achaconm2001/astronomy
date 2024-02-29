from math import radians
from manim import *


SCALE = 2
TOTAL_DURATION = 30


class VenusDance(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane))
        self.wait()

        sun = Dot(color=YELLOW).move_to([0, 0, 0])
        venus = Dot(color=YELLOW_E).move_to([1 * SCALE, 0, 0])
        earth = Dot(color=BLUE).move_to([1.5 * SCALE, 0, 0])

        self.play(Create(sun))
        self.play(Create(venus))
        self.play(Create(earth))
        self.wait()

        tracker = ValueTracker(0)

        def create_line(mob):
            value = tracker.get_value()
            if value != 1:
                tracker.set_value(value + 1)
                return

            tracker.set_value(0)
            line = Line(start=earth.get_center(),
                        end=venus.get_center(), stroke_width=0.5)
            self.add(line)

        earth.add_updater(create_line)

        seconds = 30
        venus_rotations = 8
        earth_rotations = 13

        self.play(
            Rotating(venus, radians=TAU * venus_rotations, about_point=[0, 0, 0], rate_func=linear, run_time=seconds), 
            Rotating(earth, radians=TAU * earth_rotations, about_point=[0, 0, 0], rate_func=linear, run_time=seconds)
        )
        self.wait()
