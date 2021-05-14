import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from components.navbar import Navbar
from components.about import About
from components.stacks import Stacks
from components.TestUNET import TestUNET
from components.footer import Footer

nav = Navbar()
about = About()
stacks = Stacks()
footer = Footer()
TestUNET = TestUNET()

body = dbc.Container([
    about,
    stacks,
    TestUNET,
    footer
], className="top32")


def Homepage():
    layout = html.Div([
        nav,
        body
    ], id="homepage")
    return layout
