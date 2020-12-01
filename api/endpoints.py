from app import app
from flask import request, send_from_directory
from helpers.sqlConnection import get_table
from bson import json_util
import os
from random import choice

# http://www.manualweb.net/flask/request-flask/#:~:text=El%20objeto%20request%20nos%20servir%C3%A1,GET%20o%20par%C3%A1meteos%20tipo%20POST.

# Acceso a parámetros GET

# Request --> Objeto. Tiene una colección de .args y el método .get()



# Decorators
@app.route("/")
def hello_world():
    return {"hello": "World!"}

@app.route("/help")
def help():
    return {"welcome":"Welcome to my API"}

# Funciona
@app.route("/saluten/<person>")
def saluten(person):
    return f"Hello, {person}!"

# Creación de Users
@app.route("/user/create/<usernames>")
def create_user(username)
    print({"username":username})
    return id_username





# @app.route("/salute")
# def salute():
#     name = request.args.get("name") 
#     return f"Hello, {name}!!!"

# @app.route("/company")
# def comp():
#     name = request.args.get("name")
#     return json_util.dumps(get_company(name))

# @app.route("/insert/<collection>")
# def insert(collection):
#     return json_util.dumps(insert_data(collection, dict(request.args)))


# @app.route("/sql/<name>")
# def sql(name):
#     return json_util.dumps(list(get_table(name)))


# @app.route("/flash")
# def flash():
#     return open("w6d4-api/templates/meme.html","r").read()

# @app.route("/memes")
# def meme():
#     directory = os.path.join(os.getcwd(), "w6d4-api/memes")
#     print(directory)
#     files = choice(os.listdir("w6d4-api/memes"))
#     return send_from_directory(directory=directory, filename=files, as_attachment=True)

app.run()
