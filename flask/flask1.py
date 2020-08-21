# from flask import Flask
# app = Flask(__name__);
#
# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello' +name;
#
# @app.route('/')
# def index():
#     return "Index Page Response:";
#
# if __name__ == '__main__':
#     app.run(debug = True);

# route
# from flask import Flask
# app = Flask(__name__);
#
# @app.route('/user/<int:userId>')
# def show_blog(userId):
#     return 'User Id:' +str(userId);
#
# @app.route('/temp/<float:tempVal>')
# def convert(tempVal):
#     print(type(tempVal));
#     Fah = (tempVal*1.8)+32;
#     return 'Temperature' +str(Fah);
#
# if __name__ == '__main__':
#     app.run();

# from flask import Flask,request
# app = Flask(__name__);
# @app.route('/')
# def hello():
#     name = request.args.get("name","Unknow");
#     return "Hello "+name;
# if __name__=="__main__":
#     app.run(debug=True);

from flask import Flask,request
app = Flask(__name__);

@app.route("/")
def hello():
    return "Hello How Are You";

@app.route("/about")
def aboutPage():
    return "Hello I am About Page";

@app.route("/profile")
def profilePage():
    return "I am profile and hello world"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0");
