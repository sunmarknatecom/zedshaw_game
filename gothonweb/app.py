from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST','GET'])
def index():
    인사말 = "Hello World"
    # 이름 = request.args.get('name', '아무개')

    # if 이름:
    #     인사말 = f'안녕, {이름}'

    # else:
    #     인사말 = '안녕, 여러분'

    # return render_template("index.html", 인사말=인사말)
    if request.method == "POST":
        이름 = request.form['name']
        인사 = request.form['greet']
        인사말 = f"{인사}, {이름}"
        return render_template("index.html", 인사말=인사말)
    else:
        return render_template("hello_form.html")
if __name__ == "__main__":
    app.run()