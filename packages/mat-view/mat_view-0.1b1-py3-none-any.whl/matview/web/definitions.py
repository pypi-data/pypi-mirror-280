# -------------------------------------------------------------------
MODEL_NAMES = {
    '-':   'Self', # Use - for any other type or no model
    'NN':  'Neural Network (NN)',
    'MLP': 'Neural Network (NN)',
    'RF':  'Random Forrest (RF)',
    'SVM': 'Support Vector Machine (SVM)',
    'SVC': 'Support Vector Machine (SVM)',
    'DT':  'Decision Tree (DT)',
    'XGB': 'XGBoost (XGB)',
}

METRIC_NAMES = {
    'f_score':          'F-Score',
    'f1_score':         'F-Measure',
    'f1_macro':         'F-Measure',
    
    'precision':        'Precision',
    'precision_macro':  'Precision',
    'recall':           'Recall',
    'recall_macro':     'Recall',
    'loss':             'Loss',
    
    'accuracy':      'Accuracy',
    'accuracyTop5':  'Accuracy Top 5',
    'accuracyTopK5': 'Accuracy Top 5',
    
    'balanced_accuracy':      'Balanced Accuracy',
    
    # TIME specific
    'clstime':       'Classification Time',
    'cls_time':      'Classification Time',
    'totaltime':     'Total Runtime',
    
    # Movelets specific
    'candidates':    'Number of Candidates',
    'movelets':      'Number of Movelets',
}

def metricName(code):
    code = code.replace('metric:', '')
    
    if code in METRIC_NAMES.keys():
        return METRIC_NAMES[code]
    
    name = code[0].upper()
    for c in code[1:]:
        if c.isupper():
            name += ' ' + c
        elif c.isdigit() and not name[-1].isdigit():
            name += ' ' + c
        elif c == '_':
            name += ' '
        elif name[-1] == ' ':
            name += c.upper()
        else:
            name += c
    
    return name

def datasetName(dataset, subset):
    if subset == 'specific':
        return dataset
    else:
        return dataset + ' ('+subset+')'