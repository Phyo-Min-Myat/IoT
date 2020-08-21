from flask import Flask,request,jsonify
app = Flask(__name__);

userdatabase = [];

@app.route("/",methods=["POST"])
def adduser():
    print(request.json);
    user_database.append(request.json);
    return "Success";

@app.route("/",methods=["GET"])
def getuser():
    return jsonify(user_database);

@app.route("/<username>",methods=["GET"])
def searchUserByName(username):
    result = [user for user in user_database if user.get("username")==username]
        if result:
            return jsonify(result);
        else:
            return "User Not Found!";

if __name__==__"main"__:
    app.run(debug=True,host="0.0.0.0");
