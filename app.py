
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, title = 'New Task', desc = 'Blank', \
    client = 'example'):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    #row.title = content

    # New Attempt
    row.title = title
    row.desc = desc
    row.client = client

    #Changed file more



@app.route('/create_todo', methods=['GET'])
def create_todo():

    title = request.args.get('title')
    desc = request.args.get('desc')
    client = request.args.get('client')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, title, desc, client)
    return f'added {todo} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
