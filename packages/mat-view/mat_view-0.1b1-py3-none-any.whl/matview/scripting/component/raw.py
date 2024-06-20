import os
from abc import ABC

from matview.scripting.component._base import BaseMethod, MoveletsBaseMethod

class RawTrajectoryMethod(MoveletsBaseMethod):

    def __init__(self):
        MoveletsBaseMethod.__init__(self)
    
    def title(self):
        return self.NAMES[self.PROVIDE]
    
    @property
    def name(self):
        return self.PROVIDE
    
    @property
    def version(self):
        return ''
    
    @property
    def jar_name(self):
        return self.PROVIDE+'.jar'
    
    def cmd_pivots(self, params):
        return ''
    def cmd_log(self, params):
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
        return ''

class Dodge(RawTrajectoryMethod, BaseMethod):
    
    PROVIDE = 'Dodge'
    
    NAMES = {
        'Dodge': 'Dodge',
    }
    
    def __init__(self, idx):
        BaseMethod.__init__(self, idx)
        RawTrajectoryMethod.__init__(self)

class Xiao(RawTrajectoryMethod, BaseMethod):
    
    PROVIDE = 'Xiao'
    
    NAMES = {
        'Xiao': 'Xiao',
    }
    
    def __init__(self, idx):
        BaseMethod.__init__(self, idx)
        RawTrajectoryMethod.__init__(self)

class Zheng(RawTrajectoryMethod, BaseMethod):
    
    PROVIDE = 'Zheng'
    
    NAMES = {
        'Zheng': 'Zheng',
    }
    
    def __init__(self, idx):
        BaseMethod.__init__(self, idx)
        RawTrajectoryMethod.__init__(self)

class Movelets(RawTrajectoryMethod, BaseMethod):
    
    PROVIDE = 'M'
    
    NAMES = {
        'M': 'Movelets',
        'Movelets': 'Movelets',
    }
    
    def __init__(self, idx):
        BaseMethod.__init__(self, idx)
        RawTrajectoryMethod.__init__(self)
    
    def cmd_log(self, params):
        if not self.isLog:
            return ' -Ms -1'
        else:
            return ' -Ms -3'
    
    def extras(self, params):
        return '-q LSP -p false'
    
    @property
    def jar_name(self):
        return 'Movelets.jar'