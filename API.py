from flask import Flask, request, jsonify
import torch




from flask import Flask

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)


"""
import os

app = Flask(__name__)


@app.route('/detect', methods=['POST'])
def detect_objects():
    if request.method == "POST":
        # Check if the request has the file part
        if "file" not in request.files:
            return "No file part"

        # Get the file object
        file = request.files["file"]

        # Check if the file is an image
        if file.content_type not in ["image/jpeg", "image/png"]:
            return "File is not an image"

        # Save the file
        file_name = secure_filename(file.filename)
        file.save(os.path.join("uploads", file_name))
        os.system("python detect.py --weights best.pt --img 640 --conf 0.25 --source \"file.filename\"")


        return "File uploaded successfully"




    #python detect.py --weights best.pt --img 640 --conf 0.25 --source "00.jpg"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

"""