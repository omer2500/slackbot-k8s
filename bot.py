from dotenv import load_dotenv
from flask import Flask,request
from execFunctions import list_pods, list_pod_version, get_pod_logs
from middleware.slackAuth import slackAuth

# Load env variables to python
load_dotenv()

# Init flask App
app = Flask(__name__)

# Auth middleware 
app.wsgi_app = slackAuth(app.wsgi_app)

@app.route('/getpods',methods=['POST'])
def getPods():
    try:
        text = request.environ['data']['text']
        response = list_pods(text)
        return response, 200
    except Exception as error:
        print(error)
        return "Sorry we had an issue", 500

@app.route('/version',methods=['POST'])
def getPodVersion():
    try:
        pod_name, namespace= request.environ['data']['text'].split(' ')
        response = list_pod_version(pod_name, namespace,)
        return response, 200
    except Exception as error:
        print(error)
        return "Sorry we had an issue", 500

@app.route('/getlogs',methods=['POST'])
def getLogs():
    try:
        pod_name, namespace, lines = request.environ['data']['text'].split(' ')
        response = get_pod_logs(pod_name, namespace, lines)
        return response, 200
    except Exception as error:
        print(error)
        return "Sorry we had an issue", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)