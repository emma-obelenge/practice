from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Emmanuel Obelenge'
        'title': 'Blog post 1'
        'content': 'Content for blog post 1'
        'date_posted': '23 June, 2024'
    },
    {
        'author': 'Reuben Nge'
        'title': 'Blog post 1'
        'content': 'Content for blog post 2'
        'date_posted': '29 June, 2024'
    }
]

@app.route("/")
@app.route("/home")
@app.route("/blog")
def blog():
    return(render_template('blog.html', posts=posts))

@app.route("/about")
def about():
    return(render_template('about.html', title='about'))