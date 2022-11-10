from flask import Flask, render_template, request
import CaboCha
c = CaboCha.Parser()
# create the app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/parse", methods=["POST"])
def parse():
    str_input = request.form.get('input')
    tree = c.parse(str_input)
    return tree.toString(CaboCha.FORMAT_LATTICE)

import argparse
parser = argparse.ArgumentParser(description='bottle server to collect streamed images')
parser.add_argument('--port', '-p', type=int, default=5000,
                    help='set the port number.')
parser.add_argument('--release', '-r', action='store_true', 
                    help='run the application in the release model. (if not set, it runs in a debug mode).')
parser.add_argument('--host', type=str, default='localhost',
                    help='set the host name')
parser.add_argument('--threaded', '-t', action='store_true',
                    help='run the application with threads.')
                    
#parser.add_argument('--db_file', type=str, default='./db/app.db',
#                    help='set the directory where camera configurations of yaml files are.')
#parser.add_argument('--global_config', type=str, default='./global_conf.yaml',
#                    help='set the global configuration by the yaml file.')

if __name__ == "__main__":
    args = parser.parse_args() 
    app.run(host=args.host, port=args.port, debug=not args.release, threaded=args.threaded)
        
