import os
from dash import dcc
import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod

class POI(BaseMethod):
    
    PROVIDE = 'poi'
    
    NAMES = {
        'poi':  'POI-S',
    
        'POI_1':  'POI (1)',
        'POI_2':  'POI (2)',
        'POI_3':  'POI (3)',
        'POI_1_2_3':  'POI (1+2+3)',
    }
    
    def __init__(self, idx, sequences=1, feature='poi'):
        super().__init__(idx)
        self.sequences = sequences
        self.feature = feature
    
    def render(self):
        return [
            dbc.Label('Sequence Sizes:'),
            dcc.Slider(value=self.sequences,
                id={
                    'type': 'exp-param1',
                    'index': self.idx
                },
                min=1, max=10, step=1,
                marks={i: '{}'.format(i) for i in range(1, 11)},
                updatemode='drag',
            ),
            dbc.InputGroup(
                [ 
                    dbc.InputGroupText('Feature:'),
                    dbc.Input(type="text", value=self.feature, id={'type': 'exp-param2','index': self.idx}),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.sequences = value
        if param_id == 2:
            self.feature = value
    
    @property
    def name(self):
        name = self.PROVIDE.upper()
        name += '_' + '_'.join(self.feature.split(','))
        name += '_' + '_'.join([str(i) for i in range(1,self.sequences+1)])
        return name
    
    def title(self):
        return self.NAMES[self.PROVIDE] + ' (' + self.feature + ', ' +('+'.join([str(i) for i in range(1,self.sequences+1)]))+ ')'
    
    def script(self, params, folder='${DIR}', data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        exp_path = os.path.join(res_path, folder)
        outfile = os.path.join(res_path, folder, folder+'.txt')
        
        sequences = ','.join([str(i) for i in range(1,self.sequences+1)])
        cmd = f'POIS.py -m "{self.PROVIDE}" -s "{sequences}" -f "{self.feature}" --classify "{data_path}" "{exp_path}"'
        if 'TC' in params.keys():
            cmd = 'timeout ' + params['TC'] +' '+ cmd
            
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
            
class NPOI(POI, BaseMethod):
    
    PROVIDE = 'npoi'
    
    NAMES = {
        'npoi': 'NPOI-S',
        
        'NPOI_1':  'NPOI (1)',
        'NPOI_2':  'NPOI (2)',
        'NPOI_3':  'NPOI (3)',
        'NPOI_1_2_3':  'NPOI (1+2+3)',
    }
    
    def __init__(self, idx, sequences=1, feature='poi'):
        super().__init__(idx, sequences, feature)
            
class WNPOI(POI, BaseMethod):
    
    PROVIDE = 'wnpoi'
    
    NAMES = {
        'wnpoi':  'WNPOI-S',
        
        'WNPOI_1':  'WNPOI (1)',
        'WNPOI_2':  'WNPOI (2)',
        'WNPOI_3':  'WNPOI (3)',
        'WNPOI_1_2_3':  'WNPOI (1+2+3)',
    }
    
    def __init__(self, idx, sequences=1, feature='poi'):
        super().__init__(idx, sequences, feature)