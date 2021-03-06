
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)

def createNotionTask(token, collectionURL, title = 'New Task', desc = 'Blank', clt = 'Demo'):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()

    # Fill out the Row
    row.Title = title
    row.Desc = desc
    row.Client = clt

@app.route('/create_ticket', methods=['GET', 'POST'])
def create_todo():

    title = request.args.get('title')
    desc = request.args.get('desc')
    client = request.args.get('client')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, title, desc, client)
    return f'added {title} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
