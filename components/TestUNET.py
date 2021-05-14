import base64
import os
from pathlib import Path  # Object-oriented filesystem paths

import cv2
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from matplotlib import pyplot as plt

from components.config import cwd
from components.data import *
from components.model import *

img_path = (cwd / '../data/test/').resolve()

model = unet()
model.load_weights("5x-274Aug1096_iouMet_iouLoss_1e-3_unet_membrane.hdf5")



def TestUNET():
    testunet = html.Div([
        html.H1(
            'U-Net',
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
                                html.Div(
                                    children=[
                                        html.H5("Select Mode:"),
                                        dcc.Slider(
                                            id='slider',
                                            min=1,
                                            max=2,
                                            step=None,
                                            marks={
                                                1: 'Normal',
                                                2: 'Segmented'
                                            },
                                            value=1,
                                        ),
                                    ],
                                    className='col-3',
                                    style={
                                        'width': '25%',
                                        # 'display': 'inline-block',
                                    }
                                ),
                                html.Div(className='col-6'),
                                html.Div(
                                    children=[
                                        html.H5("Select Image:"),
                                        dcc.Dropdown(
                                            id='dropdown',
                                            options=[
                                                {'label': '1',
                                                 'value': '0.png'},
                                                {'label': '2',
                                                 'value': '1.png'},
                                                {'label': '3',
                                                 'value': '2.png'},
                                                {'label': '4',
                                                 'value': '3.png'},
                                                {'label': '5',
                                                 'value': '4.png'},
                                            ],
                                            value='0.png'
                                        ),
                                    ],
                                    className='col-3',
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
                        dbc.Row(
                            children=[
                                html.Div(
                                    children=[dcc.Loading(
                                        id="loading-1",
                                        type="default",
                                        children=[
                                            html.Div(
                                                id="slideshow-container",
                                                children=[
                                                    html.Div(
                                                        id="image",
                                                        style={
                                                            'margin': '0.3rem'
                                                        },
                                                    )
                                                ])
                                        ])],
                                    className='col-6'
                                ),
                                html.Div(
                                    children=[
                                        html.Hr(),
                                        html.H6(
                                            "Estimations of PV data from the U-Net segmentation",
                                            style={
                                                'margin': '0.3rem',
                                                'font-face': 'bold',
                                            },
                                        ),
                                        html.Hr(),
                                        html.P(
                                            id="overall_solar_anlage_pixels",
                                            style={
                                                'margin': '0rem',
                                                'display': 'flex',
                                                'padding': '0',
                                                'justify-content': 'left',
                                                'align-items': 'left',
                                                'font-size': '1.1rem',
                                                'color': '#3e3e40'
                                            }
                                        ),
                                        html.P(
                                            id="number_of_solar_panels",
                                            style={
                                                'margin': '0rem',
                                                'display': 'flex',
                                                'padding': '0',
                                                'justify-content': 'left',
                                                'align-items': 'left',
                                                'font-size': '1.1rem',
                                                'color': '#3e3e40'
                                            }
                                        ),
                                        html.P(
                                            id="total_power",
                                            style={
                                                'margin': '0rem',
                                                'display': 'flex',
                                                'padding': '0',
                                                'justify-content': 'left',
                                                'align-items': 'left',
                                                'font-size': '1.1rem',
                                                'color': '#3e3e40'
                                            }
                                        ),
                                        html.P(
                                            id="kWh_yaerly_energy_output",
                                            style={
                                                'margin': '0rem',
                                                'display': 'flex',
                                                'padding': '0',
                                                'justify-content': 'left',
                                                'align-items': 'left',
                                                'font-size': '1.1rem',
                                                'color': '#3e3e40'
                                            }
                                        ),
                                        html.P(
                                            id="kW_power",
                                            style={
                                                'margin': '0rem',
                                                'display': 'flex',
                                                'padding': '0',
                                                'justify-content': 'left',
                                                'align-items': 'left',
                                                'font-size': '1.1rem',
                                                'color': '#3e3e40'
                                            }
                                        ),
                                    ],
                                    className='col-6',
                                ),
                            ],
                            style={
                                'display': 'flex',
                                'justify-content': 'center',
                                'text-align': 'justify',
                                'text-align-last': 'center',
                                'margin': '0'
                            },
                        )
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
    ])
    return testunet
