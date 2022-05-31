from flask import render_template, session
from service.login_service import check_login
from repository.user_info_dao import select_user_info_by_userid
def get_login_page():
    return render_template("login.html")

def check_user_login(login_input):
    user_login = check_login(login_input)

    if user_login is None:
        return "Failed login"
    else:
        session['username'] = user_login.username
        print(user_login.user_id)
        userdata=select_user_info_by_userid(user_login.user_id)
        print(userdata)
        session['info_id'] = userdata.info_id
        return render_template("account_page.html", username=user_login.username)