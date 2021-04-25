from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import os
import datetime
from lighting import Lighting

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = 'storage'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/room')
def room():

    filename = request.args.get('filename', None)
    layers = int(request.args.get('layers', 0))
    version = request.args.get('version', '2')

    if not filename:
        flash('Missing filename argument')
        return redirect('/')
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        flash('File not exists')
        return redirect('/')
    matrix = []
    lines = open(file_path, 'r')
    for line in lines:
        row = []
        for char in line:
            if char in ['0', '1']:
                row.append(int(char))
        matrix.append(row)
    
    max_layers = 0
    layers_color = {}
    try:
        l = Lighting(matrix)
        if version == '1':
            l.v1()
        else:
            l.v2()
        matrix, max_layers, layers_color = l.light_on(layers=layers)
    except Exception as e:
        flash(str(e))
        return redirect('/')

    rt = render_template('room.html', 
        matrix=matrix, 
        layers=layers, 
        max_layers=max_layers, 
        layers_color=layers_color, 
        filename=filename)
    return rt

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['rooms']
    if f.filename == '':
        flash('No selected file')
        return redirect('/')
    filename = f"{datetime.datetime.now().timestamp()}"+secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return redirect(f'/room?filename={filename}&layers=0')


if  __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')