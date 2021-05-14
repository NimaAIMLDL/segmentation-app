import dash_html_components as html
import dash_bootstrap_components as dbc


def Footer():
    footer = html.Div(
        html.Div(
            dbc.Row([
                dbc.Col([
                    html.Div(
                        'Contact', className="uppercase bold font-xs padding4"),
                    html.Div(
                        html.A(
                            'nimabeigy@gmail.com',
                            href="mailto:nimabeigy@gmail.com",
                            target="_blank"
                        ), className="padding4"),
                    html.P(
                        "This work is done as part of the research work at the Institute for Energy Economics and Rational Energy Use (IER) at the University of Stuttgart, Germany.",
                        className="padding4"
                    ),
                ], lg=12, width=12),
            ], className="padding32"),
            className="primary_bg radius8"),
        className="padding16 default_inverse footer font-sm")

    return footer
