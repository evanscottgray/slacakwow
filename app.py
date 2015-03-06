# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from flask import Flask
from flask import request
import requests

app = Flask(__name__)


def get_allergies():
        URL = 'http://saallergy.info/today'
        HEADERS = {'accept': 'application/json'}
        r = requests.get(URL, headers=HEADERS)
        data = r.json()
        date = data['results'][0]['date']
        text = 'Allergies for %s: ' % date
        for a in data['results']:
            text = text + '%s - %s (%s) | ' % (a['allergen'], a['level'],
                                               a['count'])
        text = text.rstrip(' ')
        text = text.rstrip('|')
        return text
        
        
@app.route("/allergies")
def allergies():
    allergies_str = get_allergies()
    return allergies_str

if __name__ == "__main__":
    app.run(host='0.0.0.0')
