# memory
Use FReMP stack to build memory app and deploy on Kubernetes

## 🤔 Run on docker (without deploy on k8s)
```bash=
$ docker-compose up
```
This one command boots up a local server for Flask (on port 5000) and React (on port 3000). Head over to
```bash=
http://localhost:3000/ 
http://localhost:5000/ 
```

## 😎 Run on minikube
Download minikube with Homebrew and start minikube
```bash=
$ brew install minikube
$ minikube start
```

Change directory to kubernetes and create the yaml file
```bash=
$ cd kubernetes
$ kubectl apply -f .
```

Use minikube tunnel to connect LoadBalancer services
```bash=
$ minikube tunnel
```

Then you can use memory app for 127.0.0.1:3000
