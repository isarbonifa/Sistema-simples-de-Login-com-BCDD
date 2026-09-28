from app.middlewares.auth_middleware import guest_required, login_required
from app.repositories.user_repository import UserRepository
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
@guest_required
def login():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    # Usando o repositório para buscar o usuário
    user = UserRepository.get_by_username(username)

    if user and user["password"] == password:
      session["user"] = username
      flash("Login realizado com sucesso!", "success")
      return redirect(url_for("auth.welcome"))
    else:
      flash("Usuário ou senha incorretos.", "danger")

  return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
@guest_required
def register():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    # Verifica se já existe via repositório
    if UserRepository.get_by_username(username):
      flash("Este usuário já existe.", "warning")
      return redirect(url_for("auth.register"))

    # Cria o registro via repositório (CRUD - Create)
    UserRepository.create(username, password)
    flash("Cadastro realizado com sucesso! Faça login.", "success")
    return redirect(url_for("auth.login"))

  return render_template("register.html")


@auth_bp.route("/")
@login_required
def welcome():
  current_user = session.get("user")
  return render_template("welcome.html", username=current_user)


@auth_bp.route("/logout")
@login_required
def logout():
  session.pop("user", None)
  flash("Você saiu da conta.", "info")
  return redirect(url_for("auth.login"))