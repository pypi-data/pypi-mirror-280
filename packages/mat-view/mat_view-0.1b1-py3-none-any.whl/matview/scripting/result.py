import os
import pandas as pd
import glob2 as glob
from pathlib import Path

from tqdm.auto import tqdm

from matview.util.format import getComponent, convertJavaOrPyDate
from matview.scripting.component._base import BaseMethod

def history(respath, patterns=['model_*_summary.csv', '*.txt']):
    # List resulting files as hierarchy
    print('Listing Files ... ', end='')
    ls = listpath(respath, patterns)
    print('found experiments for', len(ls.keys()), 'datasets.')
    
    # Transform to a dict for each dataset as key, and list of experiments as value
    # (run, method, subset, log-file, summary-file)
    experiments = dict(map(lambda dataset: ds_experiments(ls, dataset, patterns), ls.keys()))
    
    rows = sum( \
        list(map(lambda kv: \
                 list(map(lambda e: metrics(kv[0], *e), tqdm(kv[1], desc='Reading Metrics - '+kv[0]))), \
                 experiments.items() #for dataset, exps in experiments.items(): \
        )), \
    [])
    
    # ---
    histres = pd.DataFrame(rows)
    # Post treatment:
    histres['name']   = histres['method'].map(str) + '-' + histres['model'].map(str)
    histres['key'] = histres['dataset'].map(str) + '-' + histres['subset'].map(str) + '-' + histres['run'].map(str)

    histres.sort_values(['dataset', 'subset', 'run', 'method', 'model'], inplace=True)

    # Ordering / Renaming:
    histres.reset_index(drop=True, inplace=True)
    histres['#'] = histres.index
    
    return histres

# ----------------------------------------------------------------------------------------------------------------
def getResultFiles(res_path, patterns = []): # Deprecated
    def findFiles(x):
        search = os.path.join(res_path, '**', x)
        return list(glob.glob(search, recursive=True))
       
    filesList = sum(list(map(lambda p: findFiles(p), patterns)), [])

    filesList = list(set(filesList))
    
#    filesList = list(filter(lambda file: 'POI' not in os.path.basename(file).split('-')[0], filesList))
    
    filesList.sort()
    
    return filesList

def listpath(path, patterns):
    def match(f, patterns):
        return any(map(lambda x: Path(f).match(x), patterns))
    
    files = {}
    for f in os.scandir(path):
        f2 = os.path.join(path, f)
        if os.path.isdir(f):
            d = os.path.basename(f2)
            subfiles = listpath(f2, patterns)
            if len(subfiles) > 0:
                files.update({d: subfiles})
        else:
            if match(f2, patterns):
                files.update({Path(f2): None})
    return files
     
def ds_experiments(ls, dataset, patterns):
    def process_files(run, method, files, patterns):
        txt = None
        summs = []

        subset = 'specific'
        if '_' in method:
            method, subset = method.split('_', 1)

        for f, v in files.items():
            if isinstance(f, Path) and f.match(patterns[0]):
                summs.append((subset, f))
            elif isinstance(f, Path) and f.match(patterns[1]):
                txt = f
            else: # has a model 
                for ff in v.keys():
                    if isinstance(ff, Path) and ff.match(patterns[0]):
                        summs.append((f, ff))

        return list(map(lambda x: (method, run, x[0], txt, x[1]), summs))  
    
    ones = ls[dataset]
    def process_method(one, patterns):
        if one.startswith('run'): # Has k-fold
            run = int(one.replace('run', ''))
            return sum(map(lambda two: process_files(run, two, ones[one][two], patterns), ones[one].keys()), [])
        else:
            run = 0
            return process_files(run, one, ones[one], patterns)
    exps = sum(map(lambda one: process_method(one, patterns), tqdm(ones.keys(), desc='Extracting Experiments - '+dataset)), [])
    return (dataset, exps)

def metrics(dataset, method, run=0, ssubset='specific', log=None, summary=None):
    
    met_dict = dict()
    met_dict.update( {
        '#': 0,
        'timestamp':getTimestamp(log), #gstati('endDate'),
        'dataset': dataset,
        'subset': 'specific', # This is the default, if you have different sets of the same dataset, change manually.
        'run': run,
        'subsubset': ssubset, # This indicates variations to the method configurations
        'random': 1, # Default, for future implementation.
        'method': method,
    } )
    
    if summary:
        met_dict.update({'model': summary.stem.split('_')[1].upper()}) # model can be replaced from the component readMetrics
        df = pd.read_csv(summary, index_col=[0])
        met_dict.update(dict(map(lambda col: ('metric:'+col, df[col].iloc[-1]), df.columns)))
        
#    mcomponents = BaseMethod.providedMethods()
#    mnames = sorted(list(mcomponents.keys()), key=len, reverse=True)
#    mnames = list(filter(lambda m: method.upper().startswith(m.upper()), mnames))
    mc = getComponent(method)
    if mc:
        met_dict.update( mc.readMetrics(log, met_dict) )
    
    met_dict.update( {
        'file': summary,
    } )
    
    return met_dict

# ----------------------------------------------------------------------------------------------------------------
def getTimestamp(file):
    txt = ''
    if file:
        txt = open(file, 'r').readline().rstrip('\n')
    return convertJavaOrPyDate(txt)

def containErrors(file):
    txt = open(file, 'r').read()
    return txt.find('Error: ') > -1 or txt.find('Traceback') > -1 
def containWarnings(file):
    txt = open(file, 'r').read()
    return txt.find('Warning') > -1 or txt.find('UndefinedMetricWarning:') > -1 or txt.find('Could not load dynamic library') > -1
def containTimeout(file):
    txt = open(file, 'r').read()
    return txt.find('Processing time:') < 0
        
def read_file(file):
    data = pd.read_csv(file, header = None, delimiter='-=-', engine='python', on_bad_lines='skip')     
    data.columns = ['content']
    #if self.method.startswith('MMp'): # This is by a bug on the output.
    #    data['content'] = data['content'].str.replace(' Selected Points: ','. Selected Points: ')
    return data

def get_last_number_of_ms(str_target, df):
    if df is None:
        return 0
    total = 0
    for index,row in df.iterrows():
        if str_target in row['content']:
            number = row['content'].split(str_target)[1]
            number = number.split(" milliseconds")[0]
            total = float(number)
    return total

def get_count_of_file(str_target, df):
    if df is None:
        return 0
    total = 0
    for index,row in df.iterrows():
        if str_target in row['content']:
            total = total + 1
    return total

def get_sum_of_file(str_target, df):
    if df is None:
        return 0
    total = 0
    for index,row in df.iterrows():
        if str_target in row['content']:
            number = row['content'].split(str_target)[1]
#            number = number.split(".")[0]
            number = number.replace('.', ' ').split()[0]
            total = total + int(number)
    return total

def get_max_number_of_file(str_target, df):
    if df is None:
        return 0
    total = 0
    for index,row in df.iterrows():
        if str_target in row['content']:
            number = row['content'].split(str_target)[1]
#            number = int(number.split(".")[0])
            number = int(number.replace('.', ' ').split()[0])
            total = max(total, number)
    return total

def get_min_number_of_file(str_target, df):
    if df is None:
        return 0
    total = float('inf')
    for index,row in df.iterrows():
        if str_target in row['content']:
            number = row['content'].split(str_target)[1]
#            number = int(number.split(".")[0])
            number = int(number.replace('.', ' ').split()[0])
            total = min(total, number)
    return total if total != float('inf') else 0