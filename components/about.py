import dash_html_components as html
import dash_bootstrap_components as dbc


def About():
    about = html.Div([
        html.Div([
            html.H4(
                'Semantic Segmentation of Photovoltaic Panels in Aerial Photography',
                className="font-xl bold default_inverse",
                style={
                    'text-align': 'center',
                }
            ),
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.P('''
                            Renewable energies and decentralized energy producers play an important role in the energy transition. The share of renewable energies in energy generation rises continuously. With the increasing share of renewable energies, the number of decentralized energy producers grows, which can cause problems for distribution networks due to their fluctuating power generation and their widespread expansion.
                            '''
                                   ),
                            html.P('''
                            These problems and challenges can be resolved through intelligent control of consumers. Due to that, the forecast of the generation capacity is required as input data. However, the data on the expansion of the decentralized producers, in particular of the PV systems such as generation capacity and location, is not available or is just available too rudimentarily. Therefore, the methods of computer vision namely remote sensing employing deep learning are used. For this purpose, a deep learning model for the identification and semantic segmentation of PV systems is implemented and the results (segmentation maps) are used to estimate the PV data such as PV area, total number of PV modules, PV power and annual energy yield.
                            '''
                                   ),
                            html.P(
                                '''
                            Visit my GitHub to get the codes, 
                            we believe that together, we can go furthest.
                            '''
                            ),
                        ],
                            className="font-sm",
                        ),
                        html.Div(className="bottom32 dt_hide"),
                    ], lg=12, sm=12),
                ]),
                dbc.Row(
                    dbc.Col(
                        html.Div([
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-github "),
                                    href="https://github.com/NimaAIMLDL",
                                    target="_blank"
                                )
                            ),
                        ], className="about_logos font-lg"),
                        width=12
                    )

                )
            ], className="about_content padding32")
        ], className="terciary_bg radius8 relative about")
    ], className="padding16")
    return about
