from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = jsonify("This is our Automatic Timetable Creation website."
                  " Team members: "
                  "Ahmed Nouralla, "
                  "Danila Danko, "
                  "Hasan Khadra, "
                  "Kamil Sabbagh, "
                  "Vladimir Bazilevich")

    msg.headers['Access-Control-Allow-Origin'] = '*'
    msg.headers['Access-Control-Allow-Headers'] = '*'
    return msg


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)