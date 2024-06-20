from matview.plot.box import render as render_swarm

def render(df, column=None, methods_order=None, datasets_order=None, models_order=None):
    return render_swarm(df, column, methods_order, datasets_order, models_order, plot_type='swarm')