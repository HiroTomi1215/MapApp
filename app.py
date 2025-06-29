from flask import Flask, render_template

app = Flask(__name__)

# 京都の観光地リスト（緯度・経度）
locations = [
    {"name": "清水寺", "lat": 34.9948, "lng": 135.7850},
    {"name": "金閣寺", "lat": 35.0394, "lng": 135.7292},
    {"name": "銀閣寺", "lat": 35.0272, "lng": 135.7986},
    {"name": "伏見稲荷大社", "lat": 34.9671, "lng": 135.7727},
    {"name": "嵐山", "lat": 35.0094, "lng": 135.6668}
]

@app.route('/')
def map_view():
    return render_template('map.html', locations=locations)

if __name__ == '__main__':
    app.run(debug=True)