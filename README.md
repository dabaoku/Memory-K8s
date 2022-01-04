# memory
Use FReMP stack to build memory app and deploy on Kubernetes

## Run on docker (without deploy on k8s)
```bash=
$ docker-compose up
```
This one command boots up a local server for Flask (on port 5000) and React (on port 3000). Head over to
```bash=
http://localhost:3000/ 
http://localhost:5000/ 
```
## Run on minikube
Download minikube with Homebrew and start minikube
```bash=
$ brew install minikube
$ minikube start
```

Change directory to server/kubernetes and client/kubernetes to create the yaml file
```bash=
$ kubectl create -f deployment.yaml
$ kubectl create -f service.yaml
```

Use ***minikube service app-client-svc*** to check the memory app
```bash=
$ minikube service app-client-svc
```
