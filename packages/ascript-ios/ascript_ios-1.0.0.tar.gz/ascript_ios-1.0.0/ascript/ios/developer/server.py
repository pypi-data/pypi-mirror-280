import os.path
import sys
from flask import Flask, render_template, request
from gevent import pywsgi

from ascript.ios.developer.api import api_module, api_file

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
template_folder = os.path.join(current_dir, 'assets\\templates')
static_folder = os.path.join(current_dir, 'assets\\templates\\static')
print(template_folder, static_folder)
static_url_path = '../../assets'

app = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder)

api_module.api(app)
api_file.api(app)

@app.route("/")
def page_home():
    return render_template("index.html")

@app.route("/modules.html")
def modules():
    return render_template("modules.html")

@app.route("/editor.html")
def editor():
    return render_template("editor.html")

@app.route("/api/<string:m>")
def page_hwnd():
    return render_template("hwnd.html")


@app.route("/colors")
def page_colors():
    return render_template("colors.html")


@app.route("/api/tool/capture")
def api_tool_capture():
    pass


def run():
    server = pywsgi.WSGIServer(('127.0.0.1', 9096), app)
    app.debug = True
    server.serve_forever()


def close():
    print("close")
