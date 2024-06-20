import os
from dash import dcc
import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod, TrajectoryBaseMethod

class MARC(BaseMethod, TrajectoryBaseMethod): # TODO: marc params
    
    PROVIDE = 'MARC'
    
    NAMES = {
        'MARC': 'MARC',
    }
    
    MERGE_TYPE = ['add', 'average', 'concatenate']
    RNN_CELL   = ['gru', 'lstm']
    
    def __init__(self, idx, embedder_size=100, merge_type='concatenate', rnn_cell='lstm'):
        super().__init__(idx)
        self.embedder_size = embedder_size
        self.merge_type = merge_type
        self.rnn_cell = rnn_cell
    
    def render(self):
        return [
            dbc.InputGroup(
                [ 
                    dbc.InputGroupText('Embedder Size:'),
                    dbc.Input(type="number", step=1, value=self.embedder_size, id={'type': 'exp-param1','index': self.idx}),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText('Merge Type: '),
                    dbc.InputGroupText(dbc.InputGroup(
                        [
                            dcc.RadioItems(
                                id={'type': 'exp-param2','index': self.idx},
                                options=[
                                    {'label': ' '+y+' ', 'value': y} \
                                    for y in MARC.MERGE_TYPE
                                ],
                                value=self.merge_type,
                                inputStyle={'marginRight': '5px'},
                                labelStyle={'marginLeft': '1rem', 'display': 'inline-flex'},
                            ),

                        ],
                    ))
                ],
                className="mb-3",
            ),
            
            dbc.InputGroup(
                [
                    dbc.InputGroupText('RNN Cell: '),
                    dbc.InputGroupText(dbc.InputGroup(
                        [
                            dcc.RadioItems(
                                id={'type': 'exp-param3','index': self.idx},
                                options=[
                                    {'label': ' '+y+' ', 'value': y} \
                                    for y in MARC.RNN_CELL
                                ],
                                value=self.rnn_cell,
                                inputStyle={'marginRight': '5px'},
                                labelStyle={'marginLeft': '1rem', 'display': 'inline-flex'},
                            ),

                        ],
                    ))
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.embedder_size = value

        if param_id == 2:
            self.merge_type = value

        if param_id == 3:
            self.rnn_cell = value
    
    @property
    def name(self):
        name = self.PROVIDE
        conf = []
        if self.embedder_size != 100:
            conf.append(str(self.embedder_size))
        if self.merge_type != 'concatenate':
            conf.append(self.merge_type)
        if self.rnn_cell != 'lstm':
            conf.append(self.rnn_cell)
        if len(conf) > 0:
            name += '_' + '_'.join(conf)
        return name
    
    def title(self):
        return self.NAMES[self.PROVIDE] + ' ({}, {}, {})'.format(self.embedder_size, self.merge_type, self.rnn_cell)
    
    def script(self, params, folder='${DIR}', data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        exp_path = os.path.join(res_path, folder)
        outfile = os.path.join(res_path, folder, folder+'.txt')
        
        train = 'train.parquet'
        test  = 'test.parquet'
        if 'prefix' in params.keys():
            train = params['prefix'] + '_' + train
            test  = params['prefix'] + '_' + test
        
        train = os.path.join(data_path, train)
        test  = os.path.join(data_path, test)
        
        cmd = f'MARC.py "{train}" "{test}" "{exp_path}" -c "{self.PROVIDE}" --embedding-size {self.embedder_size} --merge-tipe {self.merge_type} --rnn-cell {self.rnn_cell} -mf "."'
        if 'TC' in params.keys():
            cmd = 'timeout ' + params['TC'] +' '+ cmd
        
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
