from flask import Flask, render_template, request
import json, spammer

app =  Flask(__name__)
 
@app.route('/attack', methods=['POST'])
def attack():
    data = json.loads(request.data) 
    print(data)
    spammer.send(data)
    return ''

@app.route('/')
def index():
    return render_template('index.html')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)