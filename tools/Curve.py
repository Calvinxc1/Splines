import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

class Curve:
    def __init__(self, points):
        self._points = points[:,:,np.newaxis]
        
    @property
    def points(self):
        return self._points[:,:,0]
    
    def build_curve(self, t):
        curves = self._collapse_curves(self._points, t)
        while len(curves) > 1:
            curves = self._collapse_curves(curves, t)
        
        return curves[0,:,:]
    
    def _collapse_curves(self, curves, t):
        collapsed_curves = self._lerp(curves[:-1], curves[1:], t)
        return collapsed_curves
    
    @staticmethod
    def _lerp(start, end, t):
        return (t * start) + ((1-t) * end)
