from flask import render_template

from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Eliza"}
    posts = [
        {
            "author": {"username": "Lucas"},
            "body": "Beautiful day in Curitiba!",
        },
        {
            "author": {"username": "Ana"},
            "body": "The Ghibli studio's movie was so cool!",
        },
    ]
    return render_template(
        "index.html",
        title="Home",
        user=user,
        posts=posts,
    )
