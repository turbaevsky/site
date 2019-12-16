import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app
from dash.dependencies import Input, Output, State
import dash

#from keras.models import load_model
from keras.preprocessing import sequence
import pickle
import os

from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model
from tensorflow import Session, get_default_graph

tf_config = os.environ.get('TF_CONFIG')
sess = Session(config=tf_config)
graph = get_default_graph()


# loading
with open('tokenizer.pickle', 'rb') as handle:
    t = pickle.load(handle)

set_session(sess)
model = load_model('sentiment.h5')


def check(txt, t=t, model=model):
	txt = t.texts_to_sequences([txt])
	#print(txt)
	txt = sequence.pad_sequences(txt, maxlen=40)
	#print(txt)
	global sess
	global graph
	with graph.as_default():
		set_session(sess)
		p = model.predict(txt)[0][0]
	#print(p)

	return 'positive' if p>=0.5 else 'negative'


body = dbc.Container(
[ html.H1("Natural Language Processing", id="nlp"),
    dbc.Row(
        [ 
        html.H2("Predictions"),
        html.P(
            """
        There is a simple Natural Language Processing Machine Learning models presented there. \
        Try to enter any phrase into the input field and let the system to assess the sentiment.
        Real application will work online and with all the formats including databases to track \
        Twitter, FaceBook etc.
        """
        ),
        dbc.Input(id="input_text", placeholder="Type something...", type="text", debounce=True, value = 'What a brilliant day!'),
        html.Label('Predicted sentiment: '),
        html.H4(id="predicted_sentiment", children = 'None'),
    ],
    ),
    ])


############################ callbacks #############################
@app.callback(Output('predicted_sentiment', 'children'),
              [Input('input_text', 'value')])
def update_output(txt):
	#print(txt)
	if txt is None:
		raise dash.exceptions.PreventUpdate
	else:
		return check(txt)


if __name__ == '__main__':
	print(check('What a brilliant day!'))