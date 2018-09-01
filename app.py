from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Shobhit Sundriyal',
        'title': 'Blog Post 1',
        'content': 'Content of 1st post',
        'date_posted': 'August 30,2018'
    },
    {
        'author': 'Vicky Boss',
        'title': 'Blog Post 2',
        'content': 'Content of 2nd post',
        'date_posted': 'August 31,2018'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About Me')

if __name__ == '__main__':
    app.run(debug=True)
