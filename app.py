#! /usr/bin/python3

"""
This is a simple Flask application for Summer 2022 IDS 170

John DeGood
degoodj@tcnj.edu
The College of New Jersey
Summer 2022
"""

from slab import concreteSlabMaxWallLoad
from flask import Flask, render_template, request

# perform the Civil Engineering concrete slab calculation
def compute(fc, k, te):
    # Calculate the concrete slab maximum wall load
    p = concreteSlabMaxWallLoad(fc, k, te)
    return p
 
# app.py
app = Flask(__name__)

# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

# handle venue POST and serve result web page
@app.route('/post-handler', methods=['POST'])
def post_handler():
    p = compute(float(request.form['fc_id']), float(request.form['k_id']), float(request.form['te_id']))
    return render_template('my-result.html', p=p)

if __name__ == '__main__':
    app.run(debug = True)
