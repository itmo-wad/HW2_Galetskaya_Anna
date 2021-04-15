from flask import Flask, render_template, send_from_directory
app = Flask(__name__)
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/31.ipg')
def im1():
    return app.send_static_file('31.jpg')
    
@app.route('/33.jpg')
def im2():
    return app.send_static_file('33.jpg')

@app.route('/static/')
def img(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)