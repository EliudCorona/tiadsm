from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/about-us")
def about_us():
    return render_template('about_us.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')

@app.route("/dashboar")
def dashboar():
    return render_template('dashboar.html')

@app.route("/layout_admin")
def layout_admin():
    return render_template('layout.admin_html')

def pagina_no_encontrada(error):
    return render_template('404.html')

if __name__ =='__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,port=5000)