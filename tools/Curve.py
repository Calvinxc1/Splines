import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

class Curve:
    def __init__(self, points):
        self._points = points[:,:,np.newaxis]
    
    def build_curve(self, t=None):
        if t is None: t = self._build_t()
        
        curves = self._collapse_curves(self._points, t)
        while len(curves) > 1:
            curves = self._collapse_curves(curves, t)
        
        return curves[0,:,:]
    
    @staticmethod
    def _build_t(res=1e-3):
        return np.arange(0, 1+res, res)
    
    def _collapse_curves(self, curves, t):
        collapsed_curves = self._lerp(curves[:-1], curves[1:], t)
        return collapsed_curves
    
    @staticmethod
    def _lerp(start, end, t):
        return (t * start) + ((1-t) * end)
    
    def plot(self, points=True, ax=None, figsize=(8,8)):
        x, y = self.build_curve()
        x_points, y_points = self._points[:,:,0].T
        
        if ax is None: _, ax = plt.subplots(figsize=figsize)
        sns.lineplot(x=x, y=y, color='#8da0cb', sort=False, ax=ax)
        if points: sns.scatterplot(x=x_points, y=y_points, color='#fc8d62', ax=ax)
        
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
