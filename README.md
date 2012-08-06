Brick
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

###Inspiration
This library is heavily inspired by the public description of Quora's webnode2 found [here](http://www.quora.com/Shreyes-Seshasai/Posts/Tech-Talk-webnode2-and-LiveNode).

###License
MIT 2.0

###Authors
- Garindra Prahandono (garindraprahandono@gmail.com)
