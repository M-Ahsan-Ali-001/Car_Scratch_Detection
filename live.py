import cv2
import torch
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the YOLOv5s model
model = torch.load("best.pt")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    # Get the image from the request
    image = request.files["image"].read()

    # Perform object detection
    results = model(image)

    # Process the results and draw bounding boxes on the image
    processed_image = results.render()

    # Convert the processed image to bytes
    _, encoded_image = cv2.imencode(".jpg", processed_image)
    image_bytes = encoded_image.tobytes()

    # Render the image with the detected objects
    return render_template("index.html", image=image_bytes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
