import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod, MoveletsBaseMethod

class SuperMovelets(MoveletsBaseMethod, BaseMethod):
    
    PROVIDE = 'SM'
    
    NAMES = {    
        'SM': 'SuperMovelets',
        'SML': 'SuperMovelets-Log',
        'SMD': 'SuperMovelets-λ',
        'SMLD': 'SuperMovelets-Log-λ',
    }
    
    def __init__(self, idx, isLog=True, isLambda=True):
        BaseMethod.__init__(self, idx)
        MoveletsBaseMethod.__init__(self, isLog=isLog, isLambda=isLambda)
    
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
                    dbc.InputGroupText(dbc.Checkbox(value=self.isLambda, id={'type': 'exp-param2','index': self.idx})), 
                    dbc.InputGroupText('Use λ (discover a limit number for dimension combination)'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isLog = value

        if param_id == 2:
            self.isLambda = value
    
    @property
    def version(self):
        return ''
    
    @property
    def jar_name(self):
        return 'SUPERMovelets.jar'
    
    def pivots(self, params):
        if self.isPivots:
            return ' -pvt true -lp false -pp 10 -op false'
        return ''
    
    def desc_file(self, params):
        return params['dataset'] + "_v1.json"
    
    def cmd_line(self, params):
        # 0-java_opts; 1-program; 2-data_path; 3-res_path; 4-config; 5-extras
        cmd = 'java {0} -jar "{1}" -curpath "{2}" -respath "{3}" {4} {5}'
        if 'TC' in params.keys():
            cmd = 'timeout ' + params['TC'] +' '+ cmd
        return cmd
    
    def extras(self, params):
        return '-ed true -samples 1 -sampleSize 0.5 -medium "none" -output "discrete" -lowm "false"'