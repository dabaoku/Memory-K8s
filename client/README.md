### Run app on localhost(for window)

Install npm packages

```bash=
$ npm install
```

Run app

```bash=
$ npm start
```

### Run app on dokcer

Build docker image

```bash=
$ docker build -t client:latest -f Dockerfile .
```

Run docker container

```bash=
$ docker run -it -p 3000:3000 client
```
