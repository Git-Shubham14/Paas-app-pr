from flask import Flask

app = Flask(__name__)



style = """
<style>
    body{
        font-family: Arial;
        text-align:center;
        margin-top:100px;
    }



    .box{
        width:300px;
        margin:auto;
        padding:20px;
        border:1px solid #ccc;
        border-radius:8px;
    }

    a{
        text-decoration:none;
        margin:5px;
        color:black;
    }
</style>
"""

menu = """
<br><br>
<a href="/">Home</a>
<a href="/about">About</a>
<a href="/contact">Contact</a>
"""

@app.route("/")
def home():
    return style + """
    <div class="box">
        <h2>Home</h2>
        <p>Simple Flask App</p>
    """ + menu + "</div>"

@app.route("/about")
def about():
    return style + """
    <div class="box">
        <h2>About</h2>
        <p>About Page</p>
    """ + menu + "</div>"

@app.route("/contact")
def contact():
    return style + """
    <div class="box">
        <h2>Contact</h2>
        <p>demo@gmail.com</p>
    """ + menu + "</div>"

if __name__ == "__main__":
    app.run(port=3000,debug=True)