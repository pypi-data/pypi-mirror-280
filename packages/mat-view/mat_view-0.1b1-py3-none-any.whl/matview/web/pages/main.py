import os
import glob2 as glob

from dash import html
import dash_bootstrap_components as dbc

from matview.web.config import WEB_ROUTE, render_markdown_file, underDev

def render(pathname):
    if pathname[-2:] == 'md': #its a page!
        return render_page(pathname)
    
    else:
        def file_read(f):
            data = dict()
            data['filename'] = os.path.basename(f)
            
            with open(f) as file:
                data['title'] = file.readline().replace('#', '').strip()
                data['description'] = file.readline()
            
            return data
     
        files = glob.glob(os.path.dirname(__file__) + "/*.md")
        files = list(map(lambda f: file_read(f), files))

        return html.Div(className='row', style={'margin': '1rem'}, children=
            [
                html.H1('Pages'),
                html.Hr(),
                dbc.ListGroup(
                    [dbc.ListGroupItem([
                            html.Div(
                                [
                                    html.H5(f['title'], className="mb-1"),
#                                    html.Small("Yay!", className="text-success"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.P(f['description'], className="mb-1"),
                            html.Small(f['filename'], className="text-muted"),
                        ], href="/pages/"+ f['filename']
                    ) for f in files]
                ),
                html.P(id="counter"),
            ]
        )

def render_page(pathname):
    file = WEB_ROUTE + pathname
    if os.path.exists(file):
        return render_markdown_file(file, div=True)
    else:
        return underDev(pathname)