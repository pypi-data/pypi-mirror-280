import os
from dash import html
from abc import ABC

from matclassification.methods._lib.metrics import *

# On demand import in readMetrics methods:
#from matview.scripting import result

from enum import Enum, auto
class Approach(Enum):
    SELF = '-'
    NN   = auto()
    RF   = auto()
    DT   = auto()
    SVM  = auto()
    XGB  = auto()

class BaseMethod(ABC):
    
    PROVIDE = '' # This should be the unique code for the method
    
    def __init__(self, idx):
        self.idx = idx
        
        self.model = Approach.SELF.value
        
    @staticmethod
    def wrappers():
        return dict(map(lambda cls: (cls.__name__, cls), BaseMethod.__subclasses__()))
    
    @staticmethod
    def providedMethods():
        mcomponents = dict(map(lambda cls: (cls.PROVIDE, cls), BaseMethod.__subclasses__()))
        mnames = sorted(list(mcomponents.keys()), key=len, reverse=True)
        return dict(map(lambda m: (m, mcomponents[m]), mnames))
#        return dict(map(lambda cls: (cls[1].PROVIDE, cls[1]), BaseMethod.wrappers().items()))
    
    @classmethod
    def decodeName(cls, method):
        if method in cls.NAMES.keys():
            return cls.NAMES[method] 
        else:
            return method
    
    @property
    def name(self):
        return self.PROVIDE
        
    def title(self):
        return self.NAMES[self.PROVIDE]
    
    def render(self):
        return [
            html.I(html.P("Method "+self.NAMES[self.PROVIDE]+" has default configuration.")),
        ]
    
    def generate(self, params, base, data=None, dataset=None, check_done=True):
        
        results = os.path.join('${BASE}', 'results', dataset)
        prog_path = os.path.join('${BASE}', 'programs')
        if not data:
            data = os.path.join('${BASE}', 'data', dataset)
        
        sh =  '#!/bin/bash\n'
        sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- \n'    
        sh += '# '+ self.title() +'\n'
        sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- \n'    
        sh += '# # # CONFIGURATIONS # # #\n'
        sh += 'BASE="'+base+'"\n'
        sh += 'DATAPATH="'+data+'"\n'
        sh += 'PROGPATH="'+prog_path+'"\n'
        sh += 'RESPATH="'+results+'"\n'
        sh += 'DIR="'+self.name+'"\n'
        sh += '\n'
        sh += '# # # BEGIN generated script # # #\n'
        
        data_path = '${DATAPATH}'
        res_path  = '${RESPATH}'
        prog_path = '${PROGPATH}'
        name = '${DIR}'
        
        if 'k' in params.keys():
            sh += '# Running '+str(params['k'])+'-fold experiments:\n'
            k = params['k'] if isinstance(params['k'], list) else list(range(1, params['k']+1))
            sh += 'for RUN in '+ ' '.join(['"run'+str(x)+'"' for x in k]) + '\n'
            sh += 'do\n'
            sh += '\n'
            
            data_path=os.path.join('${DATAPATH}','${RUN}')
            
        exp_path = os.path.join(res_path, name) # '${NAME}')

        if check_done:
            sh += '# Check if experiment was already done:\n'
            sh += 'if [ -d "'+exp_path+'" ]; then\n'
            sh += '   echo "'+exp_path+' ... [Is Done]"\n'
            sh += 'else\n'
            sh += '\n'
        
        sh += '# Create result directory:\n'
        sh += 'mkdir -p "'+exp_path+'"\n'
        sh += '\n'
        
        sh += '# Run method:\n'
        sh += self.script(dict(params, **{'dataset': dataset}), folder=name, data_path=data_path, res_path=res_path, prog_path=prog_path)

        sh += '\n'
        sh += 'echo "'+exp_path+' ... Done."\n'
        if check_done:
            sh += 'fi\n'
        if 'k' in params.keys():
            sh += 'done\n'
        sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- \n'      
        sh += '# # # END generated script # # #'
        
        return sh
    
    def downloadLine(self):
        return ''
    
    @staticmethod
    def readMetrics(log, metrics={}):
        from matview.scripting import result
        
        if 'model' in metrics.keys():
            if metrics['model'] in ['MRF', 'MRFHP', 'TRF']:
                metrics['model'] = Approach.RF.name
            elif metrics['model'] in ['MSVC']:
                metrics['model'] = Approach.SVM.name
            elif metrics['model'] in ['MDT']:
                metrics['model'] = Approach.DT.name
            elif metrics['model'] in ['MMLP']:
                metrics['model'] = Approach.NN.name
            else: # Self approaches: 'MARC', 'POI', 'NPOI', 'WNPOI' ....
                metrics['model'] = Approach.SELF.value
        
        if log:
            data = result.read_file(log)
            metrics.update({'error': result.containErrors(log) or result.containTimeout(log)})
            
            runtime = result.get_last_number_of_ms('Processing time: ', data)
            metrics.update({'metric:runtime': runtime})
        
        return metrics

class TrajectoryBaseMethod(ABC):

    def __init__(self):
        pass
        
    def script(self, params, folder='${DIR}', data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        outfile = os.path.join(res_path, folder, folder+'.txt')
        exp_path = os.path.join(res_path, folder)
        
        cmd = f'MAT-TC.py -c "{self.PROVIDE}" "{data_path}" "{exp_path}"'
        if 'TC' in params.keys():
            cmd = 'timeout ' + params['TC'] +' '+ cmd
        
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
    

class MoveletsBaseMethod(ABC):
    def __init__(self, isLog=None, isPivots=None, isTau=None, tau=None, isLambda=None):    
        self.isLog = isLog
        
        self.isPivots = isPivots
        
        self.isTau = isTau
        self.tau = tau
        self.temp_tau = tau
        
        self.isLambda = isLambda
    
    @property
    def name(self):
        name = self.PROVIDE
        if self.isPivots:
            name += 'p'
        if self.isLog:
            name += 'L'
        if self.isLambda:
            name += 'D'
        if self.isTau and self.tau != 0.9:
            name += 'T{}'.format(int(self.tau*100))
        return name
    
    def title(self):
        name = self.NAMES[self.PROVIDE]
        if self.isPivots:
#            name += 'Pivots'
            name = name.replace('Movelets', 'Pivots')
#        else:
#            name += 'Movelets'
        if self.isLog:
            name += '-Log'
        if self.isLambda:
            name += '-λ'
        if self.isTau and self.tau and self.tau != 0.9:
            name += ' τ={}%'.format(int(self.tau*100))
        return name
    
    @classmethod
    def decodeName(cls, method):
        t = None
        if 'T' in method:
            method, t = method.split('T')
        if method in cls.NAMES.keys():
            method = cls.NAMES[method] 
        
        if t and t != '':
            method = method.split(' ')[0] + ' τ={}%'.format(t) # careful, the name must follow a pattern: HT40, HpLT33, UT50, ...
        return method
        
    @property
    def version(self):
        cmd = ' -version ' + self.PROVIDE
        if self.isPivots:
            cmd += '-pivots'
        return cmd
    
    @property
    def jar_name(self):
        return 'MoveletDiscovery.jar'
    
    @property
    def classifiers(self):
        return 'MMLP,MRF,MSVC'
    
    
    def desc_file(self, params):
        return params['dataset'] + ".json"
    
    def cmd_line(self, params):
        # 0-java_opts; 1-program; 2-data_path; 3-res_path; 4-config; 5-extras
        return 'java {0} -jar "{1}" -curpath "{2}" -respath "{3}" {4} {5}'
    
    def extras(self, params):
        if 'TC' in params.keys():
            return '-tc ' + params['TC']
        return ''
    
    def cmd_nt(self, params):
        if 'nt' in params.keys():
            return f" -nt {params['nt']}"
        return ''
    def cmd_log(self, params):
        if not self.isLog:
            return ' -Ms -1'
        else:
            return ' -Ms -3'
    def cmd_pivots(self, params):
        return ''
    def cmd_tau(self, params):
        if self.isTau:
            return ' -TR ' + str(self.tau) # only TR (Relative Tau), the -TF (for fixed Tau) is Deprecated
        return ''
    def cmd_lambda(self, params):
        if self.isLambda:
            return ' -Al true'
        return ''
    
    def script(self, params, folder='${DIR}', data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        
        program = os.path.join(prog_path, self.jar_name)
        exp_path = os.path.join(res_path, folder)
        
        outfile = os.path.join(res_path, folder, folder+'.txt')
        
        java_opts = ''
        if 'GB' in params.keys():
            java_opts = f"-Xmx{int(params['GB'])}G"
            
        descriptor = os.path.join(data_path, self.desc_file(params))
        cmd = f'-descfile "{descriptor}"'
        
        cmd += self.version
        
        cmd += self.cmd_pivots(params)
        cmd += self.cmd_nt(params)
        cmd += self.cmd_log(params)
        cmd += self.cmd_tau(params)
        cmd += self.cmd_lambda(params)
        
#        f'java {java_opts} -jar "{program}" -curpath "{data_path}" -respath "{res_path}" ' + cmd
        cmd = self.cmd_line(params).format(java_opts, program, data_path, exp_path, cmd, self.extras(params))
        
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# Join the result train and test data:\n'
        cmd += f'MAT-MergeDatasets.py "{exp_path}" \n\n'
        
        cmd += '# Run MLP and RF classifiers:\n'
        cmd += f'MAT-MC.py -c "{self.classifiers}" "{exp_path}"\n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
    
    def downloadLine(self):
        url = 'https://raw.githubusercontent.com/mat-analysis/mat-classification/main/jarfiles'
        model = 'curl -o {1} {0}/{1} \n'
        return model.format(url, self.jar_name)
    
    
    @staticmethod
    def readMetrics(log, metrics_dict):
        from matview.scripting import result
        
        metrics_dict = BaseMethod.readMetrics(log, metrics_dict)
        
        if log:            
            list_stats = [
                ['metric:candidates',   'sum',   'Number of Candidates: '],
                ['metric:scored',       'sum',   'Scored Candidates: '],
                ['metric:recovered',    'sum',   'Recovered Candidates: '],
                ['metric:movelets',     'sum',   'Total of Movelets: '],
                
                ['metric:maxFeatures',  'max',     'Max number of Features: '],
                ['metric:minFeatures',  'min',     'Max number of Features: '],
                ['metric:avgFeatures',  'mean',    'Used Features: '],
                ['metric:maxSize',      'max',     'Limit Size: '],
                ['metric:maxSize',      'max',     'Max Size: '],
                
                ['metric:trajectoriesCompared',      'sum',   'Trajs. Looked: '],
                ['metric:trajectoriesPruned',        'sum',   'Trajs. Ignored: '],
                
                ['metric:nTrajectories',      'count',   'Trajectory: '],
                ['metric:maxTrajSize',        'max',     'Trajectory Size: '],
                ['metric:minTrajSize',        'min',     'Trajectory Size: '],
                ['metric:avgTrajSize',        'mean',    'Trajectory Size: '],
            ]
            
            def read_metric(str_target, operation, data):
                if operation == 'max':
                    return result.get_max_number_of_file(str_target, data) 

                elif operation == 'min':
                    return result.get_min_number_of_file(str_target, data) 

                elif operation == 'sum':
                    return result.get_sum_of_file(str_target, data) 

                elif operation == 'count':
                    return result.get_count_of_file(str_target, data) 

                elif operation == 'mean':
                    a = result.get_sum_of_file(str_target, data)
                    b = result.get_count_of_file(str_target, data)
                    if b > 0:
                        return a / b 
                return 0 
            
            data = result.read_file(log)
            metrics = dict(map(lambda stat: (stat[0], read_metric(stat[2], stat[1], data)), list_stats))
            metrics = dict(filter(lambda kv: kv[1] > 0, metrics.items()))
            metrics_dict.update(metrics)
            
        return metrics_dict