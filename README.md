<p align="center">
<img src="https://www.allaboutbirds.org/sgapp/images/silos/icon-pigeon.png" width="200px">
<p>

<h1 align="center">Apodo</h1>
<h3 align ="center">State of the art false name generator</h3>
<br>

</br>

Apodo is a false name generator. Handcrafted by artisanal programmers fed only
fresh morning dew and consternation free cashews. Apodo generates fake names
from a exhaustive selection of names.

Apodo comes in two forms. A standalone program and as a backend service; a REST API.

Features
--------
- Highly sophisticated unique alias name generation
- Cutting edge command-line graphics
- Light weight and efficient
- API is easy to integrate and use

Installation & Running
---
Apodo can be installed via cloning the repo from GitHub:
```
git clone https://github.com/ckruep/Apodo.git
```

The repo includes the standalone and Flask versions of Apodo.

Running the standalone version:

Navigate into the repo and then into the standalone folder:

    cd Apodo/Standalone

then run the file:

    python Apodo.py

Running the Flask version as you might have guessed, requires [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/):


Navigate down into the repo to the Flask folder:

    cd Apodo/flask

Activate the virtual enviornment:

    . venv/bin/activate

To test out the API go to:

http://127.0.0.1:5000/api/v1/resources/names/random_name

Support
-------
If you are having issues and want to let me know email me at:

Email me at: christiankruep@me.com


License
-------
MIT License

Copyright (c) 2020 Christian Kruep

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
