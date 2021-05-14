import dash_html_components as html
import dash_trich_components as dtc
import dash_bootstrap_components as dbc


def Navbar():
    navbar = html.Div(
        [
            html.Div(
                [
                    html.Div(html.Div(
                        html.A(
                            'Home', className="logo", href="/home",
                        )), className='col-4'
                    ),
                    html.Div(
                        dtc.ThemeToggle(),
                        className='col-4'
                    ),
                    html.Div(
                        dbc.NavbarSimple(
                            dbc.Row(
                                children=[
                                    dbc.DropdownMenu(
                                        nav=True,
                                        in_navbar=True,
                                        label="Menu",
                                        children=[
                                            dbc.DropdownMenuItem(
                                                "Methodology", href="/methodology"),
                                            dbc.DropdownMenuItem(
                                                "About Me", href="/me"),
                                        ],
                                    ),
                                ],
                                no_gutters=True,
                                className="ml-auto flex-nowrap mt-3 mt-md-0 bg-transparent",
                                align="center",
                                style={
                                    'position': 'static'
                                }
                            ),
                            className="ml-auto flex-nowrap mt-3 mt-md-0 bg-transparent",
                            style={
                                'position': 'static'
                            }
                        ),
                        className='col-4'
                    ),


                ], className="container flex_row_btw",
                style={
                    'box-shadow': 'none'
                }
            ),
        ],
        className="navbar"
    )
    return navbar
