import colorsys
import json
from flask import Flask, jsonify, request

from strip_manager import StripManager

app = Flask(__name__)
strip_manager = StripManager.default()


@app.route("/led-strip")
def status():
    return jsonify(strip_manager.status())


@app.route("/led-strip", methods=['POST'])
def toggle():
    body = request.get_json()
    print(json.dumps(body,indent=2))
    hue = 0.0
    sat = 0.0
    brightness = 255
    if 'hue' in body:
        hue = body['hue'] / 360.0
    if 'sat' in body:
        sat = body['sat'] / 100.0
    if 'brightness' in body:
        brightness = int(body["brightness"])
    rgb = colorsys.hsv_to_rgb(hue, sat, 1.0)
    rgb_r = int(rgb[0] * 255)
    rgb_g = int(rgb[1] * 255)
    rgb_b = int(rgb[2] * 255)
    if body['on']:
        print(f'Setting colour to {rgb_r} {rgb_g} {rgb_b}')
        strip_manager.solid_color(rgb_r, rgb_g, rgb_b, brightness)
    else:
        strip_manager.clear()

    return jsonify(strip_manager.status())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
