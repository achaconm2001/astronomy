from math import radians
from manimlib import *


SCALE = 1


class VenusDance(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(ShowCreation(plane))
        self.wait()

        sun = Dot(color=YELLOW).move_to([0, 0, 0])
        venus = Dot(color=YELLOW_E).move_to([1 * SCALE, 0, 0])
        earth = Dot(color=BLUE).move_to([1.5 * SCALE, 0, 0])

        self.play(ShowCreation(sun))
        self.play(ShowCreation(venus))
        self.play(ShowCreation(earth))
        self.wait()

        tracker = ValueTracker(0)

        def create_line(mob):
            value = tracker.get_value()
            if value != 1:
                tracker.set_value(value + 1)
                return

            tracker.set_value(0)
            line = Line(start=earth.get_center(),
                        end=venus.get_center(), stroke_width=0.1)
            self.add(line)

        earth.add_updater(create_line)

        seconds = 30

        self.play(Rotating(venus, angle=TAU * 13, about_point=[0, 0, 0], run_time=seconds), Rotating(
            earth, angle=TAU * 8, about_point=[0, 0, 0], run_time=seconds))
        self.wait()
