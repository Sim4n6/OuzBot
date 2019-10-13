# Ouz Bot
A twitter bot for analyzing some stats using tweepy.

#### commands

```
pipenv run black . # to code format using black, all source files located in "."
pipenv run pre-commit run --all-files
```

```
# Set up of pre-commit and pre-push hooks once
pipenv run pre-commit install -t pre-commit
```

```
docker build -t updated_image .
docker images 
docker run -it -p 5000:5000 --name=Container_name updated_image:latest flask run --host=0.0.0.0
docker ps
```

#### References 

Based on :
 - <https://sourcery.ai/blog/python-best-practices/> 
 - <https://docs.python-guide.org/writing/structure/>
 - <https://tweepy.readthedocs.io/en/latest/>
 - <https://developer.twitter.com/>
