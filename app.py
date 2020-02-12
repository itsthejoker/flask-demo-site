from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi!"


@app.route('/html')
def a_basic_html_page():
    return render_template('basic_page.html')


@app.route('/htmlwithcss')
def lets_add_css():
    return render_template('adding_css.html')


@app.route('/letsgetfancy')
def and_now_for_the_fun_parts():
    return render_template('adding_bootstrap.html')
