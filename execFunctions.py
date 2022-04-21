import subprocess
from helpers import calculatePodUpTime
from kubernetes import client
from datetime import datetime
from dateutil.tz import tzutc

v1 = client.CoreV1Api()
def list_pods(namespace_arg):
    """function that get all pods running inside namespace

    Args:
        namespace (string): namespace the pod is running

    Returns:
        return the pod name, version, upTime
    """
    namespace = namespace_arg if namespace_arg else "default"
    ret = v1.list_namespaced_pod(namespace=namespace)
    pods = ''
    for i in ret.items:
        upTime = calculatePodUpTime(i.status.container_statuses[0].state.running.started_at, datetime.now(tz=tzutc()))
        version = i.status.container_statuses[0].image
        podName = i.metadata.name
        pods = pods + f'• Name: {podName}, • Version: {version}, • UpTime: {upTime}\n'
    return pods

def list_pod_version(pod_name, namespace):
    """function that get version of a specific pod

    Args:
        pod_name (string): name of the pod
        namespace (string): namespace the pod is running

    Returns:
        return the version of the pod in code block
    """
    ret = v1.list_namespaced_pod(namespace=namespace)
    response = ""
    for i in ret.items:
        if pod_name in i.metadata.name:
            version = i.status.container_statuses[0].image
            response = response + f'```Version: {version}```'
    return response

def get_pod_logs(pod_name, namespace, tail):
    """function take return pod logs by pod name,namespace and tail length

    Args:
        pod_name (string): name of the pod
        namespace (string): namespace the pod is running
        tail (int): amount of log lines the function should get

    Returns:
        return logs as code block for slack
    """
    response = v1.read_namespaced_pod_log(namespace=namespace, name=pod_name, tail_lines=tail)
    return f"```{response}```"
