from flask import request,Flask,render_template, url_for,redirect,request,make_response
from time import gmtime, strftime, localtime
import urllib2,json
import database


app = Flask(__name__)
app.secret_key = "secret"