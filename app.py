from flask import Flask, render_template

app = Flask(__name__)

animals = ['dog', 'cat', 'sheep', 'cow', 'goat']
friends = ['Erma', 'Lydia', 'Edith']

posts = [
    {
        id:1,
        "author":"Edith",
        "title":"My first post",
        "content":"First blog content",
        "date_posted":"01.03.2019",
    },
    {
        id:2,
        "author":"Lydia",
        "title":"My second post",
        "content":"Second blog content",
        "date_posted":"01.03.2019",
    },
    {
        id:3,
        "author":"Barbara",
        "title":"My third post",
        "content":"Third blog content",
        "date_posted":"01.03.2019",
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', friends=friends)   

@app.route('/contact')
def contact():
    return render_template('contact.html')    