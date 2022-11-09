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

if __name__ == "__main__":
    app.run(debug=True,port=5000)
    
    
