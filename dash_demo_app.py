import glob

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

# read in most recent model build


# where `model_directory points to the folder the model is persisted in
interpreter = RasaNLUInterpreter('models/current/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('models/current/dialogue', interpreter=interpreter, action_endpoint=EndpointConfig(url="http://localhost:5055/webhook"))

# init app and add stylesheet
app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# init a list of the sessions conversation history
conv_hist = []

# app ui
app.layout = html.Div([
    html.H3('Testing Bot', style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Table([
                html.Tr([
                    # text input for user message
                    html.Td([dcc.Input(id='msg_input', value='hello', type='text')],
                            style={'valign': 'middle'}),
                    # message to send user message to bot backend
                    html.Td([html.Button('Send', id='send_button', type='submit')],
                            style={'valign': 'middle'})
                ])
            ])],
            style={'width': '325px', 'margin': '0 auto'}),
        html.Br(),
        html.Div(id='conversation')],
        id='screen',
        style={'width': '400px', 'margin': '0 auto'})
])


# trigger bot response to user inputted message on submit button click
@app.callback(
    Output(component_id='conversation', component_property='children'),
    [Input(component_id='send_button', component_property='n_clicks')],
    state=[State(component_id='msg_input', component_property='value')]
)
# function to add new user*bot interaction to conversation history
def update_conversation(n_clicks, text):
    global conv_hist

    # dont update on app load
    if n_clicks > 0:
        # call bot with user inputted text
        response = agent.handle_message(text)
        print(response)
        # user message aligned left
        rcvd = [html.H5(text, style={'text-align': 'left'})]
        # bot response aligned right and italics
        rspd = [html.H5(html.I(response[0].get("text")), style={'text-align': 'right'})]
        # append interaction to conversation history
        conv_hist = rcvd + rspd + [html.Hr()] + conv_hist

        return conv_hist
    else:
        return ''


@app.callback(
    Output(component_id='msg_input', component_property='value'),
    [Input(component_id='conversation', component_property='children')]
)
def clear_input(_):
    return ''


# run app
if __name__ == '__main__':
    app.run_server()
