# Import Libraries below
import os
import cv2
import numpy as np
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# Define flask 
app = Flask(__name__)

# Define upload_form() and route the webapp 
@app.route('/')
def upload_form():
    return render_template('upload.html')


# Define upload_video() to get video in defined folder and route the webapp  
@app.route('/', methods=['POST'])
def upload_video():
    operation_selection = request.form['video_type_selection']
    video_file = request.files['file']
    filename = secure_filename(image_file.filename)
    with open(os.path.join('static/', filename),
                  'wb') as f:
        f.write(file_data)

    return render_template('upload.html', filename=filename)

# Define display_video() to Display video in defined folder and route the webapp  
@app.route('/display/<filename>')
def display_video(filename):

    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run(debug=True)
