# slackwow
slack flask app

simple app to serve /commands in slack.

Right now this only serves allergy info for san antonio.
```
docker run -d -p 5000:5000 evanscottgray/slackwow
curl localhost:5000/allergies
```
