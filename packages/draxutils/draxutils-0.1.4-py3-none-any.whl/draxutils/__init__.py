
# myutils/__init__.py

import pandas as pd
from io import BytesIO
import base64
from PIL import Image

def get_thumbnail(path):
    """
    Generate a thumbnail of an image.

    Parameters:
    path (str): The file path to the image.

    Returns:
    PIL.Image: The thumbnail image.
    """
    i = Image.open(path)
    i.thumbnail((150, 150), Image.LANCZOS)
    return i

def image_base64(im):
    """
    Convert an image to a base64 string.

    Parameters:
    im (str or PIL.Image): The image or the path to the image.

    Returns:
    str: Base64 encoded string of the image.
    """
    if isinstance(im, str):
        im = get_thumbnail(im)
    with BytesIO() as buffer:
        im.save(buffer, 'jpeg')
        return base64.b64encode(buffer.getvalue()).decode()

def image_formatter(im):
    """
    Format an image for HTML display.

    Parameters:
    im (str or PIL.Image): The image or the path to the image.

    Returns:
    str: HTML string for displaying the image.
    """
    return f'<img src="data:image/jpeg;base64,{image_base64(im)}">'

def imglist_formatter(imglist):
    """
    Format a list of images for HTML display.

    Parameters:
    imglist (list): List of images or paths to images.

    Returns:
    str: HTML string for displaying the images.
    """
    if imglist[0] is None:
        return ""
    return " ".join([f'<img src="data:image/jpeg;base64,{image_base64(im)}">' for im in imglist])

def show_pd(df, image_key='image', masks_key='masks'):
    """
    Display a pandas DataFrame with formatted image columns in Jupyter Notebook.

    Parameters:
    df (pandas.DataFrame): The DataFrame to display.

    Returns:
    IPython.core.display.HTML: The HTML representation of the DataFrame.
    """
    from IPython.display import display, HTML
    return HTML(df.to_html(formatters={image_key: image_formatter,
                                       masks_key: imglist_formatter},
                           escape=False))

"""
Credit to https://www.kaggle.com/code/stassl/displaying-inline-images-in-pandas-dataframe.

Usage example:

from datasets import load_dataset
# Load Fashion MNIST dataset
rows = load_dataset("zalando-datasets/fashion_mnist", split="test")
rows.set_format(type="pandas") # rows is a datasets.Dataset object from Hugging Face
df = rows[:]

from cvutils import show_pd
show_pd(df)
"""