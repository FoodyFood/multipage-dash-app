import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html


# Figure out the requests prefix at start to make life easier
port=8050
username='email@example.com'
url_prefix= "/" # Set to f"/user/{username}/proxy/{port}/" to run in JupyterHub/CodeKitchen/NxCore


# Start the dahs with the prefix instead of in the app.config.update
app = dash.Dash(requests_pathname_prefix=url_prefix)


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        dbc.Nav(dbc.NavLink("Home", href=f"{url_prefix}")),
        dbc.Nav(dbc.NavLink("Dash 1", href=f"{url_prefix}dash1")),
        dbc.Nav(dbc.NavLink("Dash 2", href=f"{url_prefix}dash2")),
        dbc.Nav(dbc.NavLink("The Live Code", href=f"{url_prefix}code")),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="dash-content", style=CONTENT_STYLE)


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("dash-content", "children"), [Input("url", "pathname")])
def render_dash_content(pathname):
    print(f"Pathname: {pathname}") # I found this really helped me debug
    if pathname == f"{url_prefix}":
        return html.P(f"SUCCESS: This is the content of: {pathname} Case: home") # Replace this with your homepage dashboard
    elif pathname == f"{url_prefix}dash1":
        return html.P(f"SUCCESS: This is the content of: {pathname} Case: dash1") # Replace this with your first dashboard
    elif pathname == f"{url_prefix}dash2":
        return html.P(f"SUCCESS: This is the content of: {pathname} Case: dash2") # Replace this with your second dashboard
    elif pathname == f"{url_prefix}code":
        f = open('./main.py', 'r')
        return html.Pre(f.read())
    return html.P(f"404: Path was not recognized: {pathname} not found")


if __name__ == "__main__":
    app.run_server(debug=True, port=port)
