# pygifconvt

## Table of Contents
  * [Installation](#installation)
  * [Quick start](#quick-start)
  * [Features](#features)
  
## Installation

Download using pip via pypi.

```bash
$ pip install gifconvert_basic_tomas --upgrade
  or
$ pip install git+https://github.com/tomasjoa21/gifconvert_basic_tomas.git
```
(Mac/homebrew users may need to use ``pip3``)


## Quick start
```python
 >>> from gifconvert_basic_tomas.pngtogif import GifConverter as gfc
 >>> c = gfc("your original images path", 'your gif output path', (320,240))
 >>> c.convert_gif()
```

## Features
  * Python library to convert single oder multiple frame gif images
  * OpenCV does not support gif images.