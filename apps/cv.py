#from keras.models import Model
#from keras.preprocessing import image
#from keras.optimizers import SGD


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app
from dash.dependencies import Input, Output, State
import dash

import numpy as np
import cv2
#import datetime

import base64

from tensorflow.python.keras.backend import set_session
from tensorflow import Session, get_default_graph
import os

tf_config = os.environ.get('TF_CONFIG')
sess = Session(config=tf_config)
graph = get_default_graph()
set_session(sess)

#from keras.applications.mobilenet_v2 import MobileNetV2
#from keras.applications.mobilenet_v2 import decode_predictions
#model = MobileNetV2(weights='imagenet', include_top=True)
#sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
#model.compile(optimizer=sgd, loss='categorical_crossentropy')

# load YOLO model
from imageai.Detection import ObjectDetection
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()


def classify2(im):
	# classify with YOLO model
	global sess
	global graph
	with graph.as_default():
		set_session(sess)
		ret_img, detections = detector.detectObjectsFromImage(input_image=im, 
			input_type="array",
            output_type="array",
            minimum_percentage_probability=30)
	return ret_img, detections


body = dbc.Container(
[ html.H1("Computer Vision Systems", id="cv"),
    dbc.Row(
        [ 
            dbc.Col(
                [
                    html.H2("Image identification"),
                    html.P(
                        """
                    There is a Computer Vision Machine Learning models presented here. You can make your choise to 
                    classify the image based on your or pleloaded data.
                    You can put your image simply by dropping them into the dropping area or select the file. 
                    Real application supports all the formats including databases.
                    """
                    ),
                    #dbc.Button("View details", color="secondary"),

                    html.Label('Predicred value'),
                    html.Div(id="recognized"),
                ],
                md=4,
                ),
            dbc.Col(
                [
                    html.H2("Image"),
                    html.Div([
					    dcc.Upload(
					        id='upload-image',
					        children=html.Div([
					            'Drag and Drop or ',
					            html.A('Select Files')
					        ]),
					        style={
					            'width': '100%',
					            'height': '60px',
					            'lineHeight': '60px',
					            'borderWidth': '1px',
					            'borderStyle': 'dashed',
					            'borderRadius': '5px',
					            'textAlign': 'center',
					            'margin': '10px'
					        },
					        # Allow multiple files to be uploaded
					        multiple=False
					    ),
					    html.Div(id='output-image-upload'),
					    html.P(id='status')
					]),
                ]
            ),
        ]
    )
],
className="mt-4",
)


############################ callbacks #############################

@app.callback([Output('output-image-upload', 'children'),
			Output('status','children')],
            [Input('upload-image', 'contents')],
            [State('upload-image', 'filename'),
            State('upload-image', 'last_modified')])
def update_output(content, name, date):
	if content is not None:
		# returns image
		#img = parse_contents(content, name, date)
		# recognition
		content_type, content_string = content.split(',')
		print('source:',content_string[:200], len(content_string))
		img = base64.b64decode(content_string)
		img = np.fromstring(img, dtype=np.uint8)
		img = cv2.imdecode(img, 1)
		#im = cv2.resize(im, (224,224))
		img, detected = classify2(img)
		# detected objects
		out = 'detected: '
		for i in detected:
			out += '{} ({:.0f}%); '.format(i['name'], i["percentage_probability"])
		# image processing
		_, img = cv2.imencode('.jpg', img)
		img = base64.b64encode(img)
		img = content_type+','+img.decode("utf-8") 
		print('img:',img[:200],len(img))
		img = html.Div([html.Img(src=img)])
		#cv2.imshow('img', img)
		return img, out



if __name__ == '__main__':
	print(classify('test01.jpg'))