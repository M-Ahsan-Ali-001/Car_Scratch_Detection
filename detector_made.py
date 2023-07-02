import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os
import time
import re
import subprocess
title="ObjectDetection"


st.title(title)

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])







if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = np.array(image)

    resized_image = cv2.resize( img, (640, 640))
    resized_image = resized_image[:, :, ::-1]

    new_image_path = "image_find.jpg"
    cv2.imwrite(new_image_path, resized_image)

    image_rgbb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image_rgbb, caption='Original Image', use_column_width=True)
    command = 'python detect.py --weights "best.pt" --img 640 --conf 0.25 --source "image_find.jpg" > output.txt 2>&1'

    try:
        #subprocess.run(command, shell=True, check=True)
        os.system("python detect.py --weights \"best.pt\" --img 640 --conf 0.25 --source \"image_find.jpg\" > output.txt 2>&1")

 
    # Command executed successfully
    # Proceed to the next command
        filename = "output.txt"
        extracted_string=""
        matches=[]
# Read the content of the file
        with open(filename, "r") as file:
    # Iterate over each line in the file
             for line in file:
                  matches = re.findall(r'exp\d+', line)
        titlee=matches[0]
        st.title(titlee)
        pathimg = r"C:\Users\Anonymous Guy\Desktop\yolov5\runs\detect\\" + titlee + "\\image_find.jpg"
        imageDetected = cv2.imread(pathimg, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(imageDetected, cv2.COLOR_BGR2RGB)


        with col2:
           st.subheader("Detected Image")
        #filtered_image = Image.fromarray(filtered)
           st.image(image_rgb, caption='Detected Image', use_column_width=True)
    except :
    # Command execution failed
          st.title("adsasd")




    #os.system("python detect.py --weights \"best.pt\" --img 640 --conf 0.25 --source \"image_find.jpg\" > output.txt 2>&1")
 
#    print("Resized image saved as", new_image_path)
  
 
  

   

 
 # Open the text file for reading
    


  
    

