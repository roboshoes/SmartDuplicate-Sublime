SmartDuplicate
==============

SmartDuplicate is a Sublime Text 2 plug-in that allows duplicating lines while changing certain keywords.


Note
----

This is very early in development therefore there is a very limited amount of keywords. Also this is my first contact
with Python. I am pretty sure I did not do it in the most efficient or _python-y_ way possible.


Shortcut
--------

**[CTRL+SHIFT+d]** duplicates line using smart duplicate

_Note: This overwrites the default duplicate line shortcut._


Examples
--------

I wrote the first line of the pairs and hit **[CTRL+SHIFT+d]**.

```JavaScript
Grid.WIDTH = window.innerWidth();
Grid.HEIGHT = window.innerHeight();

element.x = other.width + 20 + element.width;
element.y = other.height + 20 + element.height;

target.x = stage.mouseX;
target.y = stage.mouseY;
```


Supported keywords
------------------

* `width` <-> `height` (case insensitive)
* `.x` <-> `.y`
* `.[word]X` <-> `.[word]Y`  (any word ending in a capital X or Y)

__Once again: work in progress. Constantly expanding and fine tuning the keywords__


Motivation
----------

I'm a front-end developer. It's been too many times that I duplicate a line and then go through and change all the
`.height` to `.width` etc.. In the manner of __automate all the things__ I thought I write a little plugin for the editor
of my choice.

Let me know what you think. No _you suck_-emails please.