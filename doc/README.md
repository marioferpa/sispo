I was confused by this documentation but I have figured it out: it's meant to be compiled using the "sphinx" python package. Install it using pip, then from /doc run "make html". I think that from Windows you need to use "make.bat html". If it requests some other package install it using pip.

When it's done you will see a "build" folder appear, inside there's a file called "html/index.html" that you can open with any web browser.
