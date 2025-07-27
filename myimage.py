import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Mounika Image Processor", layout="wide")

# Title
st.title("Mounika Image - Multi-Color Channel Visualizer")

# Load image from local path
@st.cache_data
def load_image():
    
    path=r"C:\Users\HAI\Downloads\mouni.JPG"
    
    return Image.open(path).convert("RGB")

# Load and display image
Mounika = load_image()
st.image(Mounika, caption="Original Mounika Image", use_container_width=True)

# Convert to NumPy array
Mounika_np = np.array(Mounika)
R, G, B = Mounika_np[:, :, 0], Mounika_np[:, :, 1], Mounika_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(Mounika_np)
green_img = np.zeros_like(Mounika_np)
blue_img = np.zeros_like(Mounika_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

priyanka_gray = Mounika.convert("L")
priyanka_gray_np = np.array(priyanka_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(priyanka_gray_np, cmap=colormap)
plt.axis("off")

# DO NOT USE: plt.show()
# USE THIS INSTEAD:
st.pyplot(fig)