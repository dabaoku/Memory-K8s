### Run app on localhost(for Mac)

Set up virtual environment 
```bash=
$ virtualenv env
$ source env/bin/activate
```

Install python package
```bash=
$ pip install -r requirements.txt
```
Run app
```bash=
$ python app.py
```

### Run app on docker
Build docker image
```bash=
$ docker build -t flask -f Dockerfile .
```

Run docker container 
```bash=
$ docker run -d -p 5000:9007 flask
```
