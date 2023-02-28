from flask import Flask, render_template, redirect, request
from flask import request
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def my_home():  # put application's code here
    return render_template('index.html')


@app.route('/result', methods = ['Post',"Get"])
def result():
    output = request.form.to_dict()
    name = output['name']
    return render_template('index.html',name=name)
#keep above






#keep below

if __name__ == '__main__':
    app.run()
