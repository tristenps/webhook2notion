
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, content):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    #row.title = content

    # New Parser Delination
    i = 0
    for data in content:
        if i == 0:
            row.title = content[0]
        elif i == 1:
            row.desc = content[1]
        elif i == 2:
            row.client = content [2]
        i += 1



@app.route('/create_todo', methods=['GET'])
def create_todo():

    todo = request.args.get('todo')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, todo)
    return f'added {todo} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
