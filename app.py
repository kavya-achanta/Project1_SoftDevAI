from flask import Flask, request, jsonify, render_template
from keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)

# Load the model
model = load_model("plant_pathology_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    img = request.files["file"].read()

    # Convert the byte data to a numpy array
    img = np.frombuffer(img, np.uint8)

    # Convert numpy array to image
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    
    # Ensure our image is in the format (batch_size, height, width, channels)
    img = np.reshape(img, (1, 224, 224, 3))
    
    # Make prediction
    predictions = model.predict(img)
    
    # Convert prediction to class labels
    class_names = ["healthy", "scab", "rust", "multiple_diseases"]
    predicted_class = class_names[np.argmax(predictions)]
    
    return jsonify({"prediction": predicted_class})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=443)
