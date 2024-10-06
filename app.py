from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    myvalue = 'New value'
    cal = 34*23
    list = [1,20,3,55,3]
    return render_template('index.html',list = list)

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True )
