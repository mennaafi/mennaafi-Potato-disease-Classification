import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify, set_background


set_background('C:\project1\potato-disease\templates\bg.png')  


# set title
st.title('Potato disease Classification')

# set header
st.header('Please upload an image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model_path = "C:\project1\potato-disease\model1\model_v1.keras"  
model = load_model(model_path) 

# load class names  

class_names = {
    0: "Potato___Early_blight",
    1: "Potato___Late_blight",
    2: "Potato___healthy"
}

print(class_names) 

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=False, width=300)

    # classify image
    class_name = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))