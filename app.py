from flask import Flask

app = Flask(__name__)




@app.get('/')
def f():
    return {'work':"done"}


app.run()