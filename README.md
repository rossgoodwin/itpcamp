# Creative Text Manipulation with Python
### Sunday, June 7, 1-5pm @ ITP Camp

![Code Shakespeare](http://i.imgur.com/JoSJnyw.jpg)

Code poetry. Computational creative writing. Digital poetics. Electronic literature.

All of these names refer to creative manipulation of words with computer code.

This workshop will serve as an introduction to natural language processing, with a focus on creative applications of the technologies introduced. The first part of the workshop will provide a crash course in Python basics, including the syntax and features that make the language a popular choice for handling, analyzing, and manipulating text. The rest of the workshop will focus on [Pattern](http://www.clips.ua.ac.be/pages/pattern), a powerful Python library for natural language processing, as well as other tools and resources available for creative text manipulation.

Topics covered will include (but won't be limited to): 
* Word tokenization 
* Markov chains (Ngram generators) 
* Sentence parsing / part-of-speech tagging 
* Sentiment, mood, and modality analysis 
* Stop words and stemming 
* Term Frequency-Inverse Document Frequency (TF-IDF) analysis

At least some minimal experience with programming (in any language) is recommended.

In addition to a text editor (I recommend [Sublime Text](http://www.sublimetext.com/)), please ensure your computer has Python installed. You can verify this by entering "python" (without quotes) in the Terminal. If, for some reason, you find that you do not have Python installed, please follow the instructions for installing version 2.7.9 at [python.org](http://www.python.org). (Don't install Python 3.)

You'll also need to install pip, the Python package manager. On Mac, run the following command in the terminal to do so: 
    $ sudo easy_install pip

Finally, use pip to install the virtualenv library (its purpose will be explained at the beginning of the workshop): 
    $ sudo pip install virtualenv


## Electronic Text Primer

### A few of my recent projects...
* [word.camera](https://word.camera)
* [text clock](http://rossgoodwin.com/clock)


## Python Crash Course

    $ python
    >> print "hello world!"
    ...
    >> import this
    ...

![ride the snake](http://i.imgur.com/71f0mB2.gif)
![ride the snake](http://i.imgur.com/lRxcHLA.gif)

### Virtual Environment & iPython Notebook

    $ virtualenv env
    $ source env/bin/activate
    $ pip install "ipython[notebook]"
    $ ipython notebook

### Syntax
* WHITESPACE!!! `from __future__ import braces`
* Variables
* if / elif / else
* Loops
* Functions
* Classes & objects
* Libraries

### Data structures
* Strings
* Lists
* Dictionaries
* Sets
* Tuples `a,b = b,a`

### Idioms
* Formatting strings `"testing %i, %i, %i!" % (1, 2, 3)`
* List and dictionary comprehensions
* Important Keywords
 * in
 * lambda
 * try / except
 * with
 * yield
* [Code Like a Pythonista](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)


### Resources
* [Learn Python the Hard Way](http://learnpythonthehardway.org/book/)
* [/r/LearnPython](http://reddit.com/r/learnpython)
* [Official Python Tutorial](https://docs.python.org/2/tutorial/)

## Pattern


