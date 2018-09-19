#Elvar Þór Sævarsson
#Verkefni 3
#10.9.2018

from bottle import *
import urllib.request,json
"""""
with open("gengi.json","r") as skra:
    gogn =json.load(skra)
print(gogn)
"""""

@route("/")
def index():
    return """
    <h2>Verkefni 4</h2>
    <p><a href="/a">Local Json</a></p>
    <p><a href="/b">Json API</a></p>     
    """

@route ("/a")
def index():
    return template("index.tpl")

with urllib.request.urlopen("http://apis.is/currency/")as url:
    data = json.loads(url.read().decode())

@route("/b")
def index():
    return template("index2.tpl", data=data)



########################################################################

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi síða finnst ekki</h2>"

run(host="localhost",port=8080,debug=True)


