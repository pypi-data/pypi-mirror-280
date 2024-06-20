from dash import html

## ------------------------------------------------------------------------------------------------
def movelet_component(m, ident=0):
    
    n = m.size
    feats = m.attribute_names# list(m.attributes())
    
    # Width for elements:
    WD = max( map(lambda i: max(map(lambda j: len(str(m.points[i].aspects[j])), range(m.l))), range(n)) ) + 3
    
    WE = WD//3 # Width Extra chars
    HG = 25
    
    return html.Div(
        html.Div(
            html.Div([
                html.Span(
                    m.Miq, 
                    style={"float":"left", "position":"relative", "top":"-5px", "width": str(WD)+'ch'},
                ),
                html.Div('',
                         className="m-slider-rail",
#                         style={"left": str(int((100/n)))+"%","width":str(int((n-1)*100/n))+"%"}
                         style={"left": "{}%".format(100//n), "width": "{}%".format((n-1)*(100//n))}
                ),
                html.Div('', 
                         className="m-slider-track", # rc-slider-track-1
#                         style={"left": str(int((100/n)))+"%","right":"auto","width":str(int((n-1)*100/n))+"%",}
                         style={"left": "{}%".format(100//n), "width": "{}%".format((n-1)*(100//n))}
                ),
                
                html.Div([
                    html.Span('', className="", style={"left": "0%"})
                ]+list(map(lambda i: 
                           html.Span('', className="m-slider-dot m-slider-dot-active", style={"left": "{}%".format((i+1)*(100//n))}),
                range(n))), className="m-slider-step"),
                
                html.Div([
                    html.Span(
                        m.trajectory.T,
                        className="m-slider-mark-text m-slider-mark-text-active",
                        style={"transform": "translateX(-50%)", "left": "0%"}
                    )
                ]+list(map(lambda i: 
                    html.Span(m.points[i].p #'p'+str(m.start+i)
                    , className="m-slider-mark-text m-slider-mark-text-active"
                    , style={"transform": "translateX(-50%)", "left": "{}%".format((i+1)*100//n)}),
                range(n))), className="m-slider-mark"),
                
            ] + \
            list(map(lambda k: 
                
                html.Div([
                    html.Span(str(feats[k])
                    , className="m-slider-mark-text m-slider-mark-text-active"
                    , style={"transform": "translateX(-50%)", "left": "0%", "top": '{}px'.format(int(HG*(k+1))), "width": str(WD)+'ch'})
                ]+list(map(lambda i:
                    html.Span(str(m.points[i].aspects[k])
                    , className="m-slider-mark-text m-slider-mark-text-active"
                    , style={"transform": "translateX(-50%)", 
                             "left": '{}%'.format((i+1)*100//n), 
                             "top": '{}px'.format(HG*(k+1)),
                             "width": str(WD)+'ch', #"max-content",
                            }),
                range(n))), className="m-slider-mark"),
                
            range(len(feats)) ))
            , className="m-slider " #m-slider-with-marks
            , style={"position":"relative"})
        , style={"padding":"0px 25px 25px"})
    , style={
        "width": str((n*WD)+(2*WE))+"ch", 
        "height": '{}px'.format(HG*(len(feats)+2)),
        "paddingLeft": str(WE//2)+"ch", 
        "paddingRight": str(WE)+"ch", 
    })


## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
# Deprecated: ??
## ------------------------------------------------------------------------------------------------
def render_tree(ls_movs):
    ncor = 7
    def getTitleElem(x, ident=1):
        return html.A(id='tree-link', children=getMoveletBox(x.data, ident))
#         return html.A(id='tree-link', children=html.Span('{:3.2f}'.format(x.data.quality)+'%'))
    
    def render_element(root, ident=1):
        if len(root.children) > 0:
            return [getTitleElem(root, ident),
                    html.Ul(
                        [html.Li(render_element(x, ident+1)) for x in root.children]
                    )]
        else:
            return getTitleElem(root, ident)
    
    if len(ls_movs) > 0:
        tree = createTree(ls_movs)    
        return [ html.Div(html.Ul([html.Li(render_element(tree))]), className='tree') ]
    
    return [html.Span('No movelets to render a tree')]


## ------------------------------------------------------------------------------------------------
def render_quality_tree(ls_movs):
    ncor = 7
    def getTitleElem(x, ident=1):
        return html.A(id='tree-link', children=[
            html.Span('Mov-'+str(x.data.mid)),
            html.Br(),
            html.Span('{:3.2f}'.format(x.data.quality)+'%')
        ])
    
    def render_element(root, ident=1):
        if len(root.children) > 0:
            return [getTitleElem(root, ident),
                    html.Ul(
                        [html.Li(render_element(x, ident+1)) for x in root.children]
                    )]
        else:
            return getTitleElem(root, ident)
    
    if len(ls_movs) > 0:
        tree = createTree(ls_movs)    
        return [ html.Div(html.Ul([html.Li(render_element(tree))]), className='tree') ]
    
    return [html.Span('No movelets to render a tree')]