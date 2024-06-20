# ----------------------------------------------------------------------------------------------------------------
def getComponent(method):
    from matview.scripting.component._base import BaseMethod # --------------------------------->>> Local Import *****
    mcomponents = BaseMethod.providedMethods()
    return findComponent(method, mcomponents)

def findComponent(method, mcomponents):
    mnames = list(filter(lambda m: method.upper().startswith(m.upper()), mcomponents.keys()))
    if len(mnames) > 0:
        return mcomponents[mnames[0]]
    
    return False
# ----------------------------------------------------------------------------------------------------------------
class PlotConfig:
    def __init__(self, plotsize=(14,5), scale=1, suffix='', label_pos=[0,0], xrotation=25, label_rotation=70, 
                 mask=None, format_func=None, lim=None):
        self.plotsize = plotsize
        self.scale = scale
        self.suffix = suffix
        self.label_pos = label_pos
        self.xrotation = xrotation
        self.label_rotation = label_rotation
        self.mask = mask
        self.format_func = format_func
        self.lim = lim
        
        self.ticks = None
        
    def format_val(self, x):
        if self.format_func:
            return self.format_func(x)
        elif self.mask:
            return self.mask.format(x/self.scale)
        else:
            return '{:,.{}f}'.format(x/self.scale, 0)
        
    def format_axis(self, x):
        return self.format_val(x) + self.suffix

class HourConfig(PlotConfig):
    def __init__(self, plotsize=(14,5), scale=1, suffix='', label_pos=[0,0], xrotation=25, label_rotation=70, 
                 mask=None, lim=None):
        super().__init__(plotsize, scale, suffix, label_pos, xrotation, label_rotation, mask, self.format_func, lim)
        
    def format_func(self, x, milis_granularity=True):
        s = format_hour(x, milis_granularity)
        if milis_granularity:
            return s[:s.find('m')] if 'h' in s else (s[:s.find('m')+1] if 'm' in s else s)
        else:
            return s
    
    def format_axis(self, x):
        return self.format_func(x, False) + self.suffix
    
    def autoticks(self, maxVal):
        unit = 1000*60*60 # one hour
        interval = 1
        if maxVal//unit > 300:
            interval = 50
        elif maxVal//unit > 100:
            interval = 10
        elif maxVal//unit > 10:
            interval = 5
        elif maxVal/unit < 1:
            unit = 1000*60 # 1 minute
            interval = 1
            if maxVal//unit > 30:
                interval = 10
            elif maxVal//unit > 10:
                interval = 5
            elif maxVal/unit < 1:
                unit = 1000 # 1 second
                interval = 1
                if maxVal//unit > 30:
                    interval = 10
                elif maxVal//unit > 10:
                    interval = 5        
        
        lim = int((maxVal//unit)*1.2*unit)
        self.lim = (0, lim)
        self.ticks = list(range(0, lim, interval*unit))

# --- --- --- --- --- --- Helpers --- --- --- --- --- --- 
def format_hour(millis, milis_granularity=True):
    appnd = '*' if millis < 0 else ''
    millis = abs(millis)
    if millis > 0:
        hours, rem = divmod(millis, (1000*60*60))
        minutes, rem = divmod(rem, (1000*60))
        seconds, rem = divmod(rem, 1000)
        value = ''
        if hours > 0:
            value = value + ('%dh' % hours)
        if minutes > 0:
            value = value + (('%02dm' % minutes) if value != '' else ('%dm' % minutes))
        if seconds > 0:
            if milis_granularity and seconds < 10 and value == '': #present seconds and millis
                value = value + (('%02.2fs' % (seconds+rem/1000)) if value != '' else ('%.2fs' % (seconds+rem/1000)))
            else:
                value = value + (('%02ds' % seconds) if value != '' else ('%ds' % seconds))
        if value == '':
            value = value + (('%02.3fs' % (rem/1000)) if value != '' else ('%.3fs' % (rem/1000)))
        return value + appnd
    else: 
        return "0"
    
def format_float(value, pattern='{val:.3f}'):
    if value > 0:
        return pattern.format(val=value)
    else: 
        return "0"

def format_date(ts):
    from datetime import datetime
    
    try:
        return datetime.fromtimestamp(ts).strftime("%d/%m/%y-%H:%M:%S") if ts > -1 else '-'
    except TypeError:
        return ts
    
def convertJavaOrPyDate(date='', mask='%a %b %d %H:%M:%S {} %Y'):
    from datetime import datetime
    try:
        locale = date[::-1].split(' ', 2)
        locale = locale[1][::-1]

        return datetime.strptime(date, mask.format(locale))
    except:
        py_format = '%Y-%m-%d %H:%M:%S.%f'
        try:
            return datetime.strptime(date, py_format)
        except:
            pass
    
    return datetime.now()
    