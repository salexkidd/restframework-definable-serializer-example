# restframework-definable-serializer-example

# ❓What is this?

[restframework-definable-serializer](https://github.com/salexkidd/restframework-definable-serializer)
It's example of restframework-definable-serializer project.


# 💾Installation and runserver

We recommend use *env solution (pipenv or pyenv or each othe)

```
$ git clone https://github.com/salexkidd/restframework-definable-serializer-example.git
$ cd ./restframework-definable-serializer-example
$ pip install -r ./requirements.txt
$ ./manage.py migrate
$ ./manage.py loaddata ./fixtures/*.json
$ ./manage.runserver 0.0.0.0:8000
```

Please open the "http://localhost:8000" in the browser.

You see the login page. enter the ID and Password (See below)

* ID: admin
* Password: admin

<img height="50%" width="50%" src="https://github.com/salexkidd/restframework-definable-serializer-example/blob/master/imgs/login.png">

# 📷snapshot

## top page

<img height="50%" width="50%" src="https://github.com/salexkidd/restframework-definable-serializer-example/blob/master/imgs/top_page.png">

## survey page

<img height="50%" width="50%" src="https://github.com/salexkidd/restframework-definable-serializer-example/blob/master/imgs/survey_page.png">

## define survey serializer page

<img height="50%" width="50%" src="https://github.com/salexkidd/restframework-definable-serializer-example/blob/master/imgs/admin_page.png">

# 🚸Notice

THIS PRODUCT DO NOT RUN TO PRODUCTION SERVER !!


# LICENSE

Copyright 2017 salexkidd

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
