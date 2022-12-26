import requests
from flask import Flask, render_template,request

app = Flask(__name__)


urls = [
    "https://www.yahoo.co.jp",
    "https://www.google.co.jp",
    "https://twitter.com",
    "https://www.youtube.com",
    ]




@app.route("/", methods=['GET'])
def get():
    
    
    resUrl = []
    resStatus = []

    for u in urls:
    
        url = u
        response = requests.get(url)
        status = response.status_code
        resUrl.append(u)
        resStatus.append(status)
    
    return render_template('index.html', data = zip(resUrl,resStatus))

@app.route('/', methods=['POST'])
def post():


    name = request.form.get('name')
    urls.append(name)

    resUrl = []
    resStatus = []

    for u in urls:
    
        url = u
        response = requests.get(url)
        status = response.status_code
        resUrl.append(u)
        resStatus.append(status)
    
    return render_template('index.html', data = zip(resUrl,resStatus))




if __name__ == '__main__':
    app.run()


    
    



