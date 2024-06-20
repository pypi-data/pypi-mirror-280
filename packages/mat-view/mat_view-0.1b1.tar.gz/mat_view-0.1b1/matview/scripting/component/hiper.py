import os
from abc import ABC

import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod, MoveletsBaseMethod

class HiperMovelets(MoveletsBaseMethod, BaseMethod):
    
    PROVIDE = 'H'
    
    NAMES = {
        'H': 'HiPerMovelets',
        
        'hiper': 'HiPerMovelets', 
        'hiper-pivots': 'HiPerPivots', 
        'hiper+Log': 'HiPerMovelets-Log',
        'hiper-pivots+Log': 'HiPerPivots-Log',
        
#        'H': 'HiPerMovelets τ=90%', 
        'HL': 'HiPerMovelets τ=90%',
        'HTR75': 'HiPerMovelets τ=75%', 
        'HTR75L': 'HiPerMovelets τ=75%',
        'HTR50': 'HiPerMovelets τ=50%', 
        'HTR50L': 'HiPerMovelets τ=50%',

        'Hp': 'HiPerPivots τ=90%', 
        'HpL': 'HiPerPivots τ=90%',
        'HpTR75': 'HiPerPivots τ=75%', 
        'HpTR75L': 'HiPerPivots τ=75%',
        'HpTR50': 'HiPerPivots τ=50%', 
        'HpTR50L': 'HiPerPivots τ=50%',
    }
    
    def __init__(self, idx, isLog=True, isPivots=False, isTau=False, tau=0.9):
        BaseMethod.__init__(self, idx)
        MoveletsBaseMethod.__init__(self, isLog=isLog, isPivots=isPivots, isTau=isTau, tau=tau)
    
    def render(self):
        return [
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isLog, id={'type': 'exp-param1','index': self.idx})), 
                    dbc.InputGroupText('Use Log (limit the subtrajectory size to the natural log of trajectory size)'),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isPivots, id={'type': 'exp-param2','index': self.idx})), 
                    dbc.InputGroupText('Use Pivots (HiPerMovelets-Pivots)'),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isTau, id={'type': 'exp-param3','index': self.idx})), 
                    dbc.InputGroupText('τ'),
                    dbc.InputGroupText('TAU (%):'),
                    dbc.Input(type="number", min=0.01, max=1, step=0.01, value=self.tau, id={'type': 'exp-param4','index': self.idx}),
                    dbc.InputGroupText('Scale: 0.01 to 1.00'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isLog = value

        if param_id == 2:
            self.isPivots = value

        if param_id == 3:
            self.isTau = value
            if not self.isTau:
                self.tau = 0.9
            else:
                self.tau = self.temp_tau

        if param_id == 4:
            self.temp_tau = value
            if self.isTau:
                self.tau = value
                
    @property
    def version(self):
        cmd = ' -version hiper'
        if self.isPivots:
            cmd += '-pivots'
        return cmd
