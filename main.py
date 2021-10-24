from flask import Flask, jsonify

from strip_manager import StripManager

app = Flask(__name__)
strip_manager = StripManager.default()


@app.route("/led-strip")
def status():
    return jsonify(strip_manager.status())


@app.route("/led-strip", methods=['POST'])
def turn_on():
    strip_manager.solid_color(255, 64, 0)
    return jsonify(strip_manager.status())


@app.route("/led-strip", methods=['DELETE'])
def turn_off():
    strip_manager.clear()
    return jsonify(strip_manager.status())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
