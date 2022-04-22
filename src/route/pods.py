from service.pods import list_pods, list_pod_version, get_pod_logs
from flask import Blueprint, request

pods_blueprint = Blueprint('pods', __name__, template_folder='../templates/users')

@pods_blueprint.route('/getpods', methods=['POST'])
def getPods():
    try:
        text = request.environ['data']['text']
        response = list_pods(text)
        return response, 200
    except Exception as error:
        print(error)
        return "Sorry we had an issue", 500

@pods_blueprint.route('/version', methods=['POST'])
def getPodVersion():
    try:
        pod_name, namespace= request.environ['data']['text'].split(' ')
        response = list_pod_version(pod_name, namespace,)
        return response, 200
    except Exception as error:
        print(error)
        return "Sorry we had an issue", 500

@pods_blueprint.route('/getlogs', methods=['POST'])
def getLogs():
    try:
        pod_name, namespace, lines = request.environ['data']['text'].split(' ')
        response = get_pod_logs(pod_name, namespace, lines)
        return response, 200
    except Exception as error:
        print(error)
        return "Sorry we had an issue", 500