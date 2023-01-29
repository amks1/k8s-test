from gevent import monkey
monkey.patch_all()

# import grpc._cython.cygrpc
# grpc._cython.cygrpc.init_grpc_gevent()

from flask import Flask
import os
import socket
import platform


def create_app(app_name=__name__):
	app = Flask(app_name, template_folder="templates", static_folder='static')
	#* General Configuration
	app.url_map.strict_slashes = False
	app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "12345")
	return app


app = create_app()


@app.route('/')
def index():
	return f"Hello World!<br>env:{os.environ.get('HOSTNAME')}<br>socket.hostname:{socket.gethostname()}<br>platform.node:{platform.node()}"


# app.run(host='0.0.0.0', port=7654)	## Uncomment for local testing
