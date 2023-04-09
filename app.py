from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def get_input():
    if request.method == 'POST':
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        livingrooms = request.form['livingrooms']
        kitchen = request.form['kitchen']
        # porch = request.form['porch']
        # diningroom = request.form['diningroom']

        return redirect(url_for('get_results', bedrooms=bedrooms, bathrooms=bathrooms, livingrooms=livingrooms, kitchen=kitchen))
        # pass inputs to model
    return render_template('index.html') # show form

@app.route('/results')
# def get_results(bedrooms=1, bathrooms=1, livingrooms=1, kitchen=1):
def get_results():
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')
    livingrooms = request.args.get('livingrooms')
    kitchen = request.args.get('kitchen')
    # porch = request.args.get('porch')
    # diningroom = request.args.get('diningroom'
    return render_template('results.html', bedrooms=bedrooms, bathrooms=bathrooms, livingrooms=livingrooms, kitchen=kitchen, 
                           image='static/floorplan_default.jpg')