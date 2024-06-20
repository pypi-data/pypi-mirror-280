import os
import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod, MoveletsBaseMethod

class UltraMovelets(MoveletsBaseMethod, BaseMethod):
    
    PROVIDE = 'U'
    
    NAMES = {
        'U': 'UltraMovelets', 
        
        'ultra': 'UltraMovelets', 
    }

    def __init__(self, idx, isTau=False, tau=0.9):
        BaseMethod.__init__(self, idx)
        MoveletsBaseMethod.__init__(self, isTau=isTau, tau=tau)
        
    def render(self):
        return [
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isTau, id={'type': 'exp-param1','index': self.idx})), 
                    dbc.InputGroupText('Optional τ parameter'),
                    dbc.InputGroupText('TAU (%):'),
                    dbc.Input(type="number", min=0.01, max=1, step=0.01, value=self.tau, id={'type': 'exp-param2','index': self.idx}),
                    dbc.InputGroupText('Scale: 0.01 to 1.00'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isTau = value
            if not self.isTau:
                self.tau = 0
            else:
                self.tau = self.temp_tau

        if param_id == 2:
            self.temp_tau = value
            if self.isTau:
                self.tau = value
    
    @property
    def version(self):
        return ' -version ultra'

class RandomMovelets(MoveletsBaseMethod, BaseMethod):
    
    PROVIDE = 'R'
    
    NAMES = {
        'R': 'RandomMovelets',
        
        'RL': 'RandomMovelets-Log',
        'random': 'RandomMovelets',
        'random+Log': 'RandomMovelets-Log',
    }
    
    def __init__(self, idx, isLog=True):
        BaseMethod.__init__(self, idx)
        MoveletsBaseMethod.__init__(self, isLog=isLog)
    
    def render(self):
        return [
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isLog, id={'type': 'exp-param1','index': self.idx})), 
                    dbc.InputGroupText('Use Log (limit the subtrajectory size to the natural log of trajectory size)'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isLog = value
    
    @property
    def version(self):
        return ' -version random'