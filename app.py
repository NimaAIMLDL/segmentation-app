# Data
# Dash
import base64
import math
import os
from io import BytesIO as bio

import cv2
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input as inputer
from dash.dependencies import Output as outputer
from matplotlib import pyplot as plt

from components.data import *
# from components.config import cwd
from components.homepage import Homepage
from components.methodology import Methodology
from components.me import Me
from components.Leistung import sollar_cell_pixel_counter
from components.model import *
from components.TestUNET import model

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css',
    'https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;700&display=swap',
    'https://fonts.googleapis.com/css2?family=Squada+One&display=swap',
    'https://use.fontawesome.com/releases/v5.8.1/css/all.css']

external_scripts = [
    'https://code.jquery.com/jquery-3.5.1.min.js',
    'https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js'
]

meta_tags = [
    {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, maximum-scale=1",
    },
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    meta_tags=meta_tags
)

app.title = "Semantic Segmentation of Photovoltaic Panels in Aerial Photography"


app.index_string = """<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <script type='text/javascript' src='https://platform-api.sharethis.com/js/sharethis.js#property=5e9606b2a034e50012b52e4a&product=sop' async='async'></script>
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-1DYNFQVF7N"></script>
        </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""


server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(outputer('page-content', 'children'),
              [inputer('url', 'pathname')])
def display_page(pathname):
    """Display Page"""
    if pathname == '/methodology':
        return Methodology()
    if pathname == '/me':
        return Me()
    if pathname == '/home':
        return Homepage()
    if pathname == '/':
        return Homepage()
    else:
        return Homepage()


@app.callback(
    [outputer('overall_solar_anlage_pixels', 'children'),
     outputer('number_of_solar_panels', 'children'),
     outputer('total_power', 'children'),
     outputer('kWh_yaerly_energy_output', 'children'),
     outputer('kW_power', 'children')],
    [inputer("slider", "value"),
     inputer("dropdown", "value")])
def display_pv_data(value, pic):
    if int(value) == 1:
        return "{} {} {}".format(
            'Overall Solar Panels Pixels: ',
            '---------',
            ' pixels'
        ), "{} {}".format(
            'Number of Solar Panels: ',
            '---------',
        ), "{} {} {}".format(
            'Total Power: ~',
            '---------',
            ' kWp'
        ), "{} {} {}".format(
            'Annual Energy Output: ~',
            '---------',
            ' kWh'
        ), "{} {} {}".format(
            'Power: ',
            '---------',
            ' kW'
        )
    elif int(value) == 2:
        pred_img = cv2.imread('data/test/' + pic)
        pred_img_np = np.array(pred_img)
        pixel_count = sollar_cell_pixel_counter(pred_img_np)
        area = pixel_count*(0.087*0.087)
        Globalstrahlung = 1025  # Stuttgart
        Flächenfaktor = 1.11
        module_efficiency = 0.15
        PR_Wert = 0.75
        Average_Length = 1.651  # m
        Average_Width = 0.9906  # m
        Average_solar_Panel_Area = Average_Length*Average_Width  # m2
        Number_of_Solar_Panels = area/Average_solar_Panel_Area
        Gesamtleistung = area/6.67
        kWh_yaerly_energy_output = Gesamtleistung*Globalstrahlung
        kW_power = kWh_yaerly_energy_output/24
        return "{} {} {}".format(
            'Overall Solar Panels Pixels: ',
            pixel_count,
            ' pixels'
        ), "{} {}".format(
            'Number of Solar Panels: ',
            math.ceil(Number_of_Solar_Panels)
        ), "{} {} {}".format(
            'Total Power: ~',
            round(Gesamtleistung, 3),
            ' kWp'
        ), "{} {} {}".format(
            'Annual Energy Output: ~',
            round(kWh_yaerly_energy_output, 3),
            ' kWh'
        ), "{} {} {}".format(
            'Power: ',
            round(kW_power, 3),
            ' kW'
        )
    else:
        return "{} {} {}".format(
            'Overall Solar Panels Pixels: ',
            '---------',
            ' pixels'
        ), "{} {}".format(
            'Number of Solar Panels: ',
            '---------',
        ), "{} {} {}".format(
            'Total Power: ~',
            '---------',
            ' kWp'
        ), "{} {} {}".format(
            'Annual Energy Output: ~',
            '---------',
            ' kWh'
        ), "{} {} {}".format(
            'Power: ',
            '---------',
            ' kW'
        )


@app.callback(outputer('image', 'children'),
              [inputer('slider', 'value'),
               inputer('dropdown', 'value')])
def display_image(value, pic):
    if int(value) == 1:
        return html.Img(
            src='data:image/png;base64,{}'.format(
                base64.b64encode(
                    open('data/test/' + pic, 'rb').read()
                ).decode()
            ),
            style={
                'width': '400px',
                'text-align': 'center',
                'margin-top': '1rem',
                'margin-left': '0rem',
                'margin-right': '0rem',
                'margin-bottom': '1rem'
            },
        )
    elif int(value) == 2:
        testGene = testGenerator(img_path='data/test/', file=pic)
        results = model.predict_generator(
            testGene,
            verbose=1
        )
        buf = bio()  # in-memory files
        plt.imshow(results[0])
        plt.axis('off')
        # save to the above file object
        plt.savefig(buf, format="png", bbox_inches='tight')
        plt.close()
        # encode to html elements
        data = base64.b64encode(buf.getbuffer()).decode()
        # return "data:image/png;base64,{}".format(data)
        return html.Img(
            src='data:image/png;base64,{}'.format(
                data
            ),
            style={
                'width': '400px',
                'text-align': 'center',
                'margin-top': '0rem',
                'margin-left': '0rem',
                'margin-right': '0rem',
                'margin-bottom': '0rem'
            },
        )
    else:
        return html.Img(
            src='data:image/png;base64,{}'.format(
                base64.b64encode(
                    open('data/test/' + pic, 'rb').read()
                ).decode()
            ),
            style={
                'width': '400px',
                'text-align': 'center',
                'margin-top': '1rem',
                'margin-left': '0rem',
                'margin-right': '0rem',
                'margin-bottom': '1rem'
            },
        )


if __name__ == "__main__":
    app.run_server(debug=False)
