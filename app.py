from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products", methods=["GET"])
def show_products():
    return render_template("products.html") # TODO load products dynamically


'''
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of selected stocks"""
    if request.method == "POST":
        user_id = session["user_id"]
        symbol = request.form.get("symbol").upper()
        shares_number_str = request.form.get("shares")

        error, status_code = process_transaction(user_id, symbol, shares_number_str, "BUY")

        if error:
            return apology(error, status_code)

        return redirect("/")

    return render_template("buy.html")
'''

if __name__ == "__main__":
    app.run()

# FLASK_DEBUG=1