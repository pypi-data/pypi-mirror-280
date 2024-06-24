# base36py

`base36py` is a lightweight Python library for encoding and decoding numbers between base10 and base36. It provides functions to convert both integer and floating-point numbers to base36 strings and vice versa, supporting precise fractional conversions.

## Features

- Convert integers to base36 strings.
- Convert floating-point numbers to base36 strings with adjustable precision.
- Decode base36 strings back to integers or floating-point numbers.
- Easy to use and integrate into existing projects.

## Installation

You can install `base36py` via pip:

```sh
pip install base36py
```

## Usage

```python
from base36py import encode, decode

encoded = encode(1234.5678, precision=8)
print("Encoded:", encoded)
decoded = decode(encoded, precision=8)
print("Decoded:", decoded)
```