import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks."""

    # Query the database for the user's portfolio
    portfolio = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM purchases
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, session["user_id"])

    # Get the current cash balance of the user
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

    # Calculate the total value of each stock and the grand total
    grand_total = cash
    for stock in portfolio:
        quote_info = lookup(stock["symbol"])
        stock["name"] = quote_info["name"]
        stock["price"] = quote_info["price"]
        stock["total_value"] = stock["price"] * stock["total_shares"]
        grand_total += stock["total_value"]

    # Render the portfolio template with the user's portfolio and cash balance
    return render_template("index.html", portfolio=portfolio, cash=cash, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 400)

        # Ensure shares were submitted
        elif not request.form.get("shares"):
            return apology("must provide number of shares", 400)

        # Ensure shares is a positive integer
        try:
            shares = int(request.form.get("shares"))
            if shares <= 0:
                raise ValueError()
        except ValueError:
            return apology("number of shares must be a positive integer", 400)

        # Lookup stock information
        quote_info = lookup(request.form.get("symbol"))

        # Check if the symbol is valid
        if not quote_info:
            return apology("invalid stock symbol", 400)

        # Get user's current cash balance
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        # Calculate the total cost of the purchase
        total_cost = quote_info["price"] * shares

        # Check if the user can afford the purchase
        if total_cost > user_cash:
            return apology("insufficient funds", 400)

        # Record the purchase in the database
        db.execute("INSERT INTO purchases (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], quote_info["symbol"], shares, quote_info["price"], datetime.now())

        # Update user's cash balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""

    # Query the database for the user's transaction history
    history = db.execute("""
        SELECT symbol, shares, price, timestamp
        FROM purchases
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, session["user_id"])

    # Render the history template with the user's transaction history
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 400)

        # Lookup stock information
        quote_info = lookup(request.form.get("symbol"))

        # Check if the symbol is valid
        if not quote_info:
            return apology("invalid stock symbol", 400)

        # Render the quoted template with stock information
        return render_template("quoted.html", symbol=quote_info["symbol"],
                               name=quote_info["name"], price=quote_info["price"])

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # Hash the password
        hashed_password = generate_password_hash(request.form.get("password"))

        # Insert the new user into the database
        result = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                            request.form.get("username"), hashed_password)

        # Check if the username already exists
        if not result:
            return apology("username already exists", 400)

        # Redirect user to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was selected
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must select a stock", 400)

        # Ensure shares were submitted
        elif not request.form.get("shares"):
            return apology("must provide number of shares", 400)

        # Ensure shares is a positive integer
        try:
            shares = int(request.form.get("shares"))
            if shares <= 0:
                raise ValueError()
        except ValueError:
            return apology("number of shares must be a positive integer", 400)

        # Query the database for the user's shares of the selected stock
        user_shares = db.execute("""
            SELECT SUM(shares) as total_shares
            FROM purchases
            WHERE user_id = ? AND symbol = ?
            GROUP BY symbol
            HAVING total_shares > 0
        """, session["user_id"], symbol)

        # Ensure the user owns that many shares of the stock
        if not user_shares or user_shares[0]["total_shares"] < shares:
            return apology("not enough shares to sell", 400)

        # Lookup stock information
        quote_info = lookup(symbol)

        # Calculate the total value of the sale
        total_value = quote_info["price"] * shares

        # Record the sale in the database
        db.execute("""
            INSERT INTO purchases (user_id, symbol, shares, price, timestamp)
            VALUES (?, ?, ?, ?, datetime('now'))
        """, session["user_id"], symbol, -shares, quote_info["price"])

        # Update user's cash balance
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_value, session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Query the database for the user's stocks to populate the select menu
        stocks = db.execute("""
            SELECT symbol
            FROM purchases
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, session["user_id"])

        # Render the sell template with the user's stocks
        return render_template("sell.html", stocks=stocks)
    
@app.route("/addcash", methods=["GET", "POST"])
@login_required
def addcash():
    """Add additional cash to user's account."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure additional cash amount was submitted
        additional_cash = request.form.get("additionalcash")
        if not additional_cash:
            return apology("must provide additional cash amount", 400)

        try:
            additional_cash = float(additional_cash)
            if additional_cash <= 0:
                raise ValueError()
        except ValueError:
            return apology("additional cash must be a positive number", 400)

        # Update the user's cash balance in the database
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", additional_cash, session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("addcash.html")
