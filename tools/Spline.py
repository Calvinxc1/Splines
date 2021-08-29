import numpy as np

from .Curve import Curve

class Spline:
    def __init__(self):
        self.curves = []
    
    def add_to_curve(self, points, close=False):
        if self.curves:
            points = self._close_curve(self.curves[-1].points, points, self.curves[0].points) \
                if close else self._extend_curve(self.curves[-1].points, points)
        self.curves.append(Curve(points))
        
    @staticmethod
    def _extend_curve(prior_points, points):
        new_points = np.stack([
            prior_points[-1],
            (2*prior_points[-1]) - prior_points[-2],
            *points,
        ])
        return new_points
    
    def _close_curve(self, prior_points, points, close_points):
        new_points = np.stack([
            *self._extend_curve(prior_points, points),
            (2*close_points[0]) - close_points[1],
            close_points[0],
        ])
        return new_points
    
    def build(self, res=1e-3):
        t = self._build_t(res)
        spline = np.concatenate([curve.build_curve(t) for curve in self.curves], axis=1)
        return spline
    
    @staticmethod
    def _build_t(res=1e-3):
        return np.arange(0, 1+res, res)
