### Run app on dokcer

Build docker image

```bash=
$ docker build -t client:latest
$ docker build .
```

Run docker container

```bash=
$ docker run -it -p 3000:3000 client
```
