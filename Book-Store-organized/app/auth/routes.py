from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from app.auth.forms import RegistrationForm, LoginForm


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for("main.index"))

    form = RegistrationForm()
    print(form)
    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data,
        )
        user.set_password(form.password.data)  # Hash the password
        user.save_to_db()

        flash("Your account has been created! You can now log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", title="Register", form=form)

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("You have been logged in!", "success")
            return redirect(url_for("main.index"))
        else:
            flash("Login unsuccessful. Please check email and password.", "danger")

    return render_template("auth/login.html", title="Login", form=form)

@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))