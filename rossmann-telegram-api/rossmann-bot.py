from sre_parse import parse_template
import pandas as pd
import json
import requests
from flask import Flask, request, Response
import os

# constants
TOKEN = '5702485702:AAEsX3xRLP0o-RXyfZ4GcJMja2uv-Jfax0Q'
# Info about the bot
'https://api.telegram.org/bot5702485702:AAEsX3xRLP0o-RXyfZ4GcJMja2uv-Jfax0Q/getMe'

# get updates
'https://api.telegram.org/bot5702485702:AAEsX3xRLP0o-RXyfZ4GcJMja2uv-Jfax0Q/getUpdates'

# Webhook
'https://api.telegram.org/bot5702485702:AAEsX3xRLP0o-RXyfZ4GcJMja2uv-Jfax0Q/setWebhook?url=https://rossmannapp-telegram-api.rj.r.appspot.com'

# send messages
'https://api.telegram.org/bot5702485702:AAEsX3xRLP0o-RXyfZ4GcJMja2uv-Jfax0Q/sendMessage?chat_id=1148619044&text=Hi!'

def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)
    r = requests.post(url, json={'text': text})
    print('Status Code {}'.format(r.status_code))

    return None

def load_dataset(store_id):
    # loading dataset
    df10 = pd.read_csv(r"data\test.csv")
    df_stores_raw = pd.read_csv("data\store.csv", low_memory=False)

    # merge test dataset + store
    df_test = pd.merge(df10, df_stores_raw, how='left', on='Store')

    # choose store for prediction
    df_test = df_test[df_test['Store'] == store_id]

    if not df_test.empty:
        # remove closed days
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id', axis=1)

        # convert Dataframe to json
        data = json.dumps(df_test.to_dict(orient='records'))
    else:
        data = 'error'

    return data

def predict(data):    
    # API Call
    #url = 'http://192.168.1.9:5000/rossmann/predict'
    url2 = 'https://rossmannapp-telegram-api.rj.r.appspot.com/' # Link from google cloud
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post(url=url2,data=data, headers = header)
    print(f'Status code {r.status_code}')

    df_resp = pd.DataFrame(r.json(), columns=r.json()[0].keys())

    return df_resp

def parse_message(message):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    store_id = store_id.replace('/','')

    try:
        store_id = int(store_id)
    except ValueError:
        send_message(chat_id, 'Store ID is Wrong')
        store_id = 'error'

    return chat_id, store_id

# API Initialize
app = Flask(__name__)

@app.rout('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message(message)

        if store_id != 'error':
            # loading data
            data = load_dataset(store_id=store_id)

            if data != 'error':

                # prediction
                df_resp = predict(data)

                # calculation
                df_pred = df_resp[['store','prediction']].groupby('store').sum().reset_index()

                msg = "Store number {} will sell R$ {:,.2f}".format(df_pred['store'].values[0], 
                                                           df_pred['prediction'].values[0])
                send_message(chat_id, msg)


                # send message

            else:
                send_message(chat_id=chat_id, text='Store Not Available')
                return Response('Ok', status=200)
        else:
            send_message(chat_id, 'Store ID is Wrong')

            return Response('Ok', status=200)

    else:
        return '<h1> Rossmann Telegram BOT </h1>'

if __name__=='__main__':
    app.run(debug=True)
