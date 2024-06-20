from matview.plot.bar import render as render_bar

def render(df, column=None, methods_order=None, datasets_order=None, models_order=None):
    return render_bar(df, column, methods_order, datasets_order, models_order, aggregate_ds=True)