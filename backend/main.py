from flask import Flask, send_from_directory, request, jsonify, abort

from datetime import datetime

import models
from models import env as env
from models.calculation import calculate

app = Flask(__name__)

HUB = [-37.7116, 144.9646 - 0.1000]

@app.route('/')
def index_handle():
    return send_from_directory('html', 'main.html')


@app.route('/api', methods=['POST'])
def get_post():
    content = request.get_json(silent=True)
    id = content["id"]
    coords = []
    coords.append(content["lng"])
    coords.append(content["lat"])
    models.insert_coords(id, coords, False)
    json_data = calculate(HUB, models.get_coords())
    if json_data == None:
        abort(400)
    print(json_data)
    return jsonify(json_data)

@app.route('/js/<path:path>')
def js_handler(path):
    return send_from_directory('js', path)



def main():
    app.run(host=env.get_host(), port=env.get_port())
    
if __name__ == '__main__':
    
    env.set_test_env()
    #calculate(HUB, [[100, 100], [110, 110]])

    # models.add_fake_users()
    models.set_true()
    models.add_fake_coords()
    #models.insert_coords("user_0", [60, 70], False)
    
    #print(models.get_coords()) #
    #models.get_coords()
    main()