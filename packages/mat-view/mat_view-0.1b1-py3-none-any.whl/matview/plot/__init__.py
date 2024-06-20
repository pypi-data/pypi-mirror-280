import importlib

MODULE_NAMES = {
    'bar': 'Bar Plots',
    'bar_mean': 'Bar Plots (Mean)',
    'box': 'Box Plots',
    'swarm': 'Swarm Plots',
#    'line': 'Line Plots',
#    'line_rank': 'Line Ranks',
    'critical_difference': 'Critical Difference Rank',
}

def importPlotter(name):
    return getattr(importlib.import_module('matview.plot.'+name), 'render') 