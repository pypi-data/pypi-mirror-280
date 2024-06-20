import os

import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod, TrajectoryBaseMethod

class TRF(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'TRF'
    
    NAMES = {
        'TRF': 'TRF',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
        
class TXGB(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'TXGB'
    
    NAMES = {
        'TXGB': 'TXGBoost',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
class DeepeST(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'DeepeST'
    
    NAMES = {
        'DEEPEST': 'DeepeST',
        'DeepeST': 'DeepeST',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
class Tulvae(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'Tulvae'
    
    NAMES = {
        'Tulvae': 'Tulvae',
    }
    
    def __init__(self, idx, feature='poi'):
        super().__init__(idx)
        self.feature = feature
        
    def render(self):
        return [
            dbc.InputGroup(
                [ 
                    dbc.InputGroupText('Feature:'),
                    dbc.Input(type="text", value=self.feature, id={'type': 'exp-param1','index': self.idx}),
                ],
                className="mb-3",
            ),
        ]
    
    @property
    def name(self):
        name = self.PROVIDE
        name += '_' + '_'.join(self.feature.split(','))
        return name
    
    def title(self):
        return self.NAMES[self.PROVIDE] + ' (' + self.feature + ')'
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.feature = value
            
    def script(self, params, folder='${DIR}', data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        outfile = os.path.join(res_path, folder, folder+'.txt')
        exp_path = os.path.join(res_path, folder)
        
        cmd = f'MAT-TC.py -c "{self.PROVIDE}" -of "{self.feature}" "{data_path}" "{exp_path}"'
        if 'TC' in params.keys():
            cmd = 'timeout ' + params['TC'] +' '+ cmd
        
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
        
class Bituler(Tulvae, BaseMethod):
    
    PROVIDE = 'Bituler'
    
    NAMES = {
        'Bituler': 'BiTuler',
    }
    
    def __init__(self, idx, feature='poi'):
        super().__init__(idx, feature)