from flask import Flask, request, jsonify
from io import BytesIO
from PIL import Image
import numpy as np

app = Flask(__name__)


@app.route('/prt', methods=['Get'])

def prt():
    
        return "<h1>yas</h1>",400
    

@app.route('/upload', methods=['POST'])





def upload():
    if 'image' not in request.files:
        return 'No image file found.', 400
    
    image_file = request.files['image']
    
    try:
        image = Image.open(image_file)
        image_array = np.array(image)
        
        # Perform any necessary processing on the image_array
        # For example, you can resize, convert format, or perform other transformations
        
        # Convert the image_array back to bytes
        image_bytes = Image.fromarray(image_array).tobytes()
        
        return jsonify({'message': 'Image uploaded and processed successfully.'}), 200
    except Exception as e:
        print(e)
        return 'Error processing the image.', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
