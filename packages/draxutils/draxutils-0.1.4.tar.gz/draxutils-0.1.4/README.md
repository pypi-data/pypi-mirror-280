Credit to https://www.kaggle.com/code/stassl/displaying-inline-images-in-pandas-dataframe.

Usage example:
```python
from datasets import load_dataset
# Load Fashion MNIST dataset
rows = load_dataset("zalando-datasets/fashion_mnist", split="test")
rows.set_format(type="pandas") # rows is a datasets.Dataset object from Hugging Face
df = rows[:]

from draxutils import show_pd
show_pd(df)
```