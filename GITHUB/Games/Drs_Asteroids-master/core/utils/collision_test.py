import unittest
from entities.MovableCircle import MovableCircle
from core.utils.collision import are_circles_collided, is_point_inside_circle


class TestCollisionUtils(unittest.TestCase):
    def test_are_circles_collided_when_collided(self):
        self.assertTrue(are_circles_collided(MovableCircle(x=0, y=0, r=5), MovableCircle(x=1, y=1, r=5)))
        self.assertTrue(are_circles_collided(MovableCircle(x=4, y=4, r=2), MovableCircle(x=7, y=7, r=3)))
        self.assertTrue(are_circles_collided(MovableCircle(x=0, y=0, r=1), MovableCircle(x=0, y=0, r=1)))

    def test_are_circles_collided_when_not_collided(self):
        self.assertFalse(are_circles_collided(MovableCircle(x=0, y=0, r=1), MovableCircle(x=9, y=9, r=1)))
        self.assertFalse(are_circles_collided(MovableCircle(x=0, y=0, r=1), MovableCircle(x=3, y=3, r=1)))

    def test_is_point_inside_circle_when_is_in_circle(self):
        self.assertTrue(is_point_inside_circle(1, 2, MovableCircle(x=0, y=0, r=3)))
        self.assertTrue(is_point_inside_circle(1, 2, MovableCircle(x=1, y=2, r=1)))

    def test_is_point_inside_circle_when_is_not_in_circle(self):
        self.assertFalse(is_point_inside_circle(1, 2, MovableCircle(x=8, y=8, r=1)))
        self.assertFalse(is_point_inside_circle(2, 2, MovableCircle(x=0, y=0, r=1)))


if __name__ == "__main__":
    unittest.main()
