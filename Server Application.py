from __future__ import print_function
from flask import Flask, request
import sys
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def test():
    global num
    if request.method == 'POST':
        num  = request.json['num']
        return str(num)
    elif request.method == 'GET':
        return str(num)

if __name__ == '__main__':
    num = 10
    app.run(host='0.0.0.0', port=80)