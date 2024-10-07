from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    myvalue = 'New value'
    cal = 34*23
    list = [1,20,3,55,3]
    return render_template('index.html',list = list)

@app.route('/another')
def another():
    text = "Appling filters"
    return render_template('another.html',text = text)

@app.route('/go_to_another')
def go_to_another():
    return redirect(url_for('another'))
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True )
