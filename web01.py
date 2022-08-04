from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/register', methods=['GET'])
def register():
    return render_template('/register.html')

#
# @app.route("/do/reg", methods=['GET'])
# def get_register():
#     return "注册成功"


@app.route("/post/reg", methods=["POST"])
def post_register():
    print(request.form)
    return "注册成功"


if __name__ == '__main__':
    app.run()
