Brick [![Build Status](https://secure.travis-ci.org/garindra/brick.png)](https://secure.travis-ci.org/garindra/brick.png)
=====

`brick` is a pure Python block-based templating system. 

###Examples

Let's see some example:
    
    from brick import Block
    from brick.tags import *

    class LikeButton(Block):  
        
        def construct(self):
            b = []

            with Div(class_=['like-btn']).into(b):
                b += A(href="#")("Like")

            return b
    
    like_button = LikeButton()

    like_button.render()
    >> <div class="like-btn"><a href="#">Like</a></div>

###Installation
`brick` is an official PyPi module, so you can use it simply with pip by doing:

    pip install brick

###PyPI Page
[http://pypi.python.org/pypi/brick](http://pypi.python.org/pypi/brick)

###Prerequisites
`brick` is currently well tested on Python 2.5, 2.6 and 2.7.

###Run unit tests
If you have the `nose` Python unit tester library installed and want to run the unit test suite for this library, then simply run this command:
    
    nosetests

###Travis CI
You can track the project's CI status on Travis at : [http://travis-ci.org/#!/garindra/brick](http://travis-ci.org/#!/garindra/brick)

###License
MIT 2.0

###Inspiration
This library is heavily inspired by the public description of Quora's webnode2 found [here](http://www.quora.com/Shreyes-Seshasai/Posts/Tech-Talk-webnode2-and-LiveNode).

###Authors
- Garindra Prahandono (garindraprahandono@gmail.com)
