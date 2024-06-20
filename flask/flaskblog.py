from flask import Flask, render_template

app = Flask(__name__)

posts = [
            {

                'author': 'Emmanuel Obelenge',
                'title': 'Blog Post 1',
                'content': 'First post content',
                'date_posted': '19 June, 2024'
            },
            {

                'author': 'Reuben Nge',
                'title': 'Blog Post 2',
                'content': 'Second post content',
                'date_posted': '25 June, 2024'
            }
        ]

@app.route("/")
@app.route("/home")
def home():
    return (render_template('home.html', posts=posts))

@app.route("/about")
def about():
    return(render_template('about.html', title='About Emmazy'))

if __name__ == '__main__':
    app.run(debug=True)
