# Flask website demo

A quick walkthrough different types of webpages to show what's possible while still keeping the server simple. Feel free to modify pages and see what breaks and what changes!

Routes:

- localhost:5000/
  - The homepage. The simplest kind of page -- just raw text.
- localhost:5000/html
  - What happens if we take a template and put HTML in it?
- localhost:5000/htmlwithcss
  - Let's load a local CSS file and see what we can change!
- localhost:5000/letsgetfancy
  - Without changing anything on the server side, we add a splash of bootstrap to show what a few minutes of judicious CSS application can do to a page.

Install dependencies into a virtual environment with `poetry install`, then run the server with `poetry run flask run` (or `poetry shell` then `flask run`, up to you).
