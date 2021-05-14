import base64

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from components.footer import Footer
from components.navbar import Navbar

nav = Navbar()
footer = Footer()
body = dbc.Container([
    html.Div([
        html.H1(
            'Methodology',
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
                                    src='data:image/png;base64,{}'.format(
                                        base64.b64encode(
                                            open(
                                                './assets/images/Picture1.png', 'rb').read()
                                        ).decode()
                                    ),
                                    style={
                                        'display': 'flex',
                                        'width': '75%',
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
                                'margin': '0.3rem'
                            },
                        ),
                        dbc.Row(
                            children=[
                                html.P(
                                    '''
                                    Data set creation: 274 aerial photos from Google Earth Pro (image patches and their masks) includes 160 positive and 114 negative examples. Location Stuttgart-Vaihingen, Germany.
                                    ''',
                                    style={
                                        'margin-top': '0.3rem'
                                    }
                                ),
                                html.P(
                                    '''
                                    Image Augmentation: number of training data is expanded from 274 to 1096 images using image augmentation methods.
                                    '''
                                ),
                                html.P(
                                    '''
                                    Implementation of Deep Convolutional Neural Network (DCNN): Implementation of U-Net for semantic segmentation using TensorFlow and Keras. The Model consists of 24 convolution layers, 4 max pooling layers, 13 batches Normalization layers as well as 4 cropping-Concatenate paths.
                                    '''
                                ),
                                html.P(
                                    '''
                                    Training on GPU.
                                    '''
                                ),
                                html.P(
                                    '''
                                    Test and validation: testing and validation of the trained U-Net on test and validation dataset. Location 72667 Schlaitdorf, Germany
                                    '''
                                ),
                                html.P(
                                    '''
                                    Calculating and estimating the PV data: Calculation of the PV area, total number of PV Modules, PV power and annual energy yield using OpenCV and comparison with the database Core energy market data register of the Federal Network Agency to validate the results
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


def Methodology():
    layout = html.Div([
        nav,
        body
    ], id="methodology")
    return layout
