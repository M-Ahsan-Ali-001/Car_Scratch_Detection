import torch
import torchvision
import cv2

# Load the YOLOv5 model from the .pt file
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
model.eval()

# Load the input image using OpenCV
image = cv2.imread('img3.jfif')

# Resize the image while maintaining the aspect ratio
width = 640
height = int(image.shape[0] * width / image.shape[1])
resized_image = cv2.resize(image, (width, height))

# Preprocess the image
#reprocessed_image = model.preprocess(resized_image)

# Perform object detection
results = model(resized_image)

# Access the bounding boxes, confidence scores, and class labels
boxes = results.xyxy[0]  # Bounding boxes
scores = results.names[0]  # Confidence scores
labels = results.names[0]  # Class labels

# Iterate over the detections and process them
#for box, score, label in zip(boxes, scores, labels):
 ##  label_text = f'{label} {score:.2f}'
   # color = (0, 255, 0)  # Green color for the bounding box
   # thickness = 2
   # cv2.rectangle(resized_image, (x1, y1), (x2, y2), color, thickness)
   # cv2.putText(resized_image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, thickness)

# Display the resized image with bounding boxes and labels


# To detect as many objects as you want, you can change the `for` loop to the following:

for i in range(len(boxes)):
     print(boxes[i])
     x1, y1, x2, y2 = boxes[i]
     label_text = f'{labels[i]} {scores[i]:.2f}'
     color = (0, 255, 0)  # Green color for the bounding box
     thickness = 2
     cv2.rectangle(resized_image, (x1, y1), (x2, y2), color, thickness)
     cv2.putText(resized_image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, thickness)

cv2.imshow('Object Detection', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()