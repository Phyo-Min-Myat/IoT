from flask import Flask,request,jsonify
app = Flask(__name__);
user_database = []
@app.route("/",method=["POST"])
def addUser():
    print(request.json);
    user_database.append(request.json);
    return "Success";

@app.route("/",method=["GET"])
def getUser():
    return jsonify(user_database);

@app.route("/<username>",method=["GET"])
def searchUserByName(username):
    result = [user for user in user_database
if user.get("username")==username]
    if result:
        return jsonify(result)
    else:
        return "User Not Found"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0");
