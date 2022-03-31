import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
from PIL import Image
import cv2
import os
import tensorflow.compat.v2 as tf
import tensorflow_hub as hub


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# app = Flask(__name__)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

def predict(file):
    img = Image.open(file)
    labelmap_url = "https://www.gstatic.com/aihub/tfhub/labelmaps/aiy_food_V1_labelmap.csv"
    input_shape = (224, 224)
    image = np.asarray(img, dtype="float")
    image = cv2.resize(image, dsize=input_shape, interpolation=cv2.INTER_CUBIC)
    # Scale values to [0, 1].
    image = image / image.max()
    image = image[:, :, :3]
    image = image[np.newaxis, ...]
    print(image.shape)
    print("# The model expects an input of (?, 224, 224, 3).")
    # images = np.expand_dims(image, 0)
    # This assumes you're using TF2.
    output = m(image)
    predicted_index = output.numpy().argmax()
    classes = list(pd.read_csv(labelmap_url)["name"])
    label = f"{classes[predicted_index]}"
    print(label)
    return label

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		label = predict(file)
		flash('Image successfully uploaded and displayed below')
		return render_template('upload.html', filename=filename, label=label)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
    

if __name__ == "__main__":
    m = hub.KerasLayer('https://tfhub.dev/google/aiy/vision/classifier/food_V1/1')
    app.run(host='0.0.0.0', port=8000, debug=True)