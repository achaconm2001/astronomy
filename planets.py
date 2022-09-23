from math import radians
from manimlib import *


class Planets(Scene):
    def construct(self):
        self.camera.frame.set_width(100)

        plane = NumberPlane()
        self.play(ShowCreation(plane))
        self.wait()

        sun = Dot(color=YELLOW_C).move_to([0, 0, 0])
        mercury = Dot(color=GOLD_D).move_to([0.5, 0, 0])
        venus = Dot(color=YELLOW_E).move_to([1, 0, 0])
        earth = Dot(color=BLUE_C).move_to([1.5, 0, 0])
        mars = Dot(color=RED_C).move_to([2, 0, 0])
        jupiter = Dot(color=GOLD_C).move_to([7.8, 0, 0])
        saturn = Dot(color=GOLD_D).move_to([14.3, 0, 0])
        uranus = Dot(color=BLUE_D).move_to([28.8, 0, 0])
        neptune = Dot(color=BLUE_E).move_to([45, 0, 0])

        self.play(ShowCreation(sun))
        self.play(ShowCreation(mercury))
        self.play(ShowCreation(venus))
        self.play(ShowCreation(earth))
        self.play(ShowCreation(mars))
        self.play(ShowCreation(jupiter))
        self.play(ShowCreation(saturn))
        self.play(ShowCreation(uranus))
        self.play(ShowCreation(neptune))
        self.wait()
