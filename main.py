import json
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def form():
    return render_template_string(open('index.html').read())

@app.route('/submit', methods=['POST'])
def submit():
    assigned_match_num = request.form.get('assigned_match_num')
    usercode = request.form.get('usercode')
    alliences = request.form.get('alliences')
    place = request.form.get('place')

    unicode_sign = (assigned_match_num+usercode+alliences+place)

    kmatch = unicode_sign[0:2]
    kusercode = unicode_sign[2:6]
    kalliences = unicode_sign[6:7]
    kplace = unicode_sign[7:8]

    data = {
        "Match": kmatch,
        "User code": kusercode,
        "Alliences": kalliences,
        "Place": kplace
    }

    existing_data = []
    try:
        with open('data.json', 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    existing_data.append(data)

    with open('data.json', 'w') as f:
        json.dump(existing_data, f)

    return f"Data stored in JSON file."

if __name__ == '__main__':
    app.run()