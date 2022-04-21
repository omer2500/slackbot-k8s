# k8sbot

k8sbot is a bot that allow you to get information about your pods inside your cluster from slack.

## Table of Contents

- [Requirements](#Requirements)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Requirements

- python(3.8 and above)[https://www.python.org]
- minikube (for local development)

## Usage

In order to run the bot you should follow these steps:

- Clone the repo
- Create a slack bot app using the slack-bot-manifest.yaml file (file is optional)
- Get the secrets you need you need in order to run the bot server and add them to the secret.yaml file inside k8s-files folder
- Get a running k8s cluster
- build the docker image of the bot-server
- push the docker image to registry (optional)
- Apply all the files that are in the k8s folder

Feel free to remove any sections that aren't applicable to your project.


## Bot commands
In slack you can run these commands to use the bot

```
/getpods namespace

List pods by namespace 

/getlogs pod namespace tail
List logs of pod by tail

/version pod name
List version of a pod
```

## Local Development

For local development of the code itself run:

```
python3 -m venv ./venv && ./venv/soruce/bin/activate
```

then install requirements:
```
pip3 install -r requirements.txt
```
If you are using vscode you can just start debug session on bot.py file

## Local Development with docker 
create a minikube cluster and expose it from you machine with ngrok

## Support

Please [open an issue](https://github.com/fraction/readme-boilerplate/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).
