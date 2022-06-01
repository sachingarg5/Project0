from flask import render_template,session


def get_homepage():
    return render_template("home.html")

def get_log_out_page():
    session.pop('username',None)
    session.pop('info_id',None)
    return render_template("logout.html")