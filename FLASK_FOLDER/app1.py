#IMPORT Libraries
import numpy as np
import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the model
model = load_model("model.h5", compile=False)
app = Flask(__name__)

# default home page or route

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)  
        filepath = os.path.join(basepath, 'uploads', f.filename) 
        f.save(filepath)

        img = image.load_img(filepath, target_size=(299, 299))
        x = image.img_to_array(img) 
        print(x)
        x = np.expand_dims(x, axis=0)
        print(x) 

        y = model.predict(x)
        preds = np.argmax(y, axis=1)
        # preds = model.predict_classes(x)
        print("prediction", preds)
        index = ['COVID', 'Lung_Capacity', 'Normal', 'Viral Pneumonia']
        text = "The person suffer from : " + str(index[preds[0]])
        print(text)
    return render_template('pred.html', y=text)

if __name__ == '__main__':
    app.run(debug=False)
