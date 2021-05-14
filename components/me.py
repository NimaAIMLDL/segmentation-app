import base64
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from components.navbar import Navbar
from components.footer import Footer

nav = Navbar()
footer = Footer()

body = dbc.Container([
    html.Div([
        html.H1(
            'Model Loss',
            className="font-xl bold",
            style={
                'text-align': 'center',
            }
        ),
        html.Div([
            dbc.Row(
                children=[
                    html.Div(
                        className='col-1'
                    ),
                    html.Div([
                        dbc.Row(
                            children=[
                                html.Img(
                                    src='data:image/jpg;base64,{}'.format(
                                        base64.b64encode(
                                            open(
                                                './assets/images/nima.jpeg', 'rb').read()
                                        ).decode()
                                    ),
                                    style={
                                        'display': 'flex',
                                        'width': '20%',
                                        'justify-content': 'center',
                                        'text-align': 'justify',
                                        'text-align-last': 'center',
                                        'margin': '0'
                                    },
                                ),
                            ],
                            style={
                                'display': 'flex',
                                'justify-content': 'center',
                                'text-align': 'justify',
                                'text-align-last': 'center',
                                'margin': '0.2rem'
                            },
                        ),
                        dbc.Row(
                            children=[
                                html.P(),
                                html.H3('Nima Beygi'),
                                html.P(
                                    '''
                                    I studied Master of Electrical Engineering at the University of Stuttgart in Germany. I am passionate about AI and solving real-world problems. 
                                    I am experienced in machine learning, deep learning, reinforcement learning, deep convolutional neural networks, image classification, image segmentation, and remote sensing.
                                    '''
                                ),
                                html.P(
                                    '''
                                    Address: Hafenstraße 74, 68159 Mannheim.
                                    '''
                                ),
                            ],
                            style={
                                'display': 'flex',
                                'justify-content': 'left',
                                'text-align': 'left',
                                'text-align-last': 'left',
                                'margin': '0.2rem'
                            },
                        ),
                    ],
                        style={
                        'margin-top': '1rem',
                    },
                        className='col-10'
                    ),
                    html.Div(
                        className='col-1'
                    ),
                ],
                style={
                    'display': 'flex',
                    'justify-content': 'center',
                    'text-align': 'justify',
                    'text-align-last': 'center',
                    'margin': '0'
                },
            ),
        ]
        ),
    ]),
    footer
], className="top32")


def Me():
    layout = html.Div([
        nav,
        body
    ], id="me")
    return layout
