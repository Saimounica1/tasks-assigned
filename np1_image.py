import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO #bytes io used for buffer memory to store or capture images )


def load_image_from_url(url):
      response = requests.get(url)
      return Image.open(BytesIO(response.content))


peacock_feathers_url = "https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg"

Peacock = load_image_from_url(peacock_feathers_url )


# display an original image
plt.figure(figsize=(6,4))
plt.imshow(Peacock)
plt.title('Peacock')
plt.axis( 'off')
plt.show()

# image to array
Peacock_np = np.array(Peacock)
print('Peacock Image shape', Peacock_np.shape)