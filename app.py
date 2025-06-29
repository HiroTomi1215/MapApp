from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 初期の観光地リスト（メモリ上）
locations = [
    {"name": "清水寺", "lat": 34.9948, "lng": 135.7850},
    {"name": "金閣寺", "lat": 35.0394, "lng": 135.7292},
    {"name": "銀閣寺", "lat": 35.0272, "lng": 135.7986},
    {"name": "伏見稲荷大社", "lat": 34.9671, "lng": 135.7727},
    {"name": "嵐山", "lat": 35.0094, "lng": 135.6668}
]

@app.route('/', methods=['GET', 'POST'])
def map_view():
    if request.method == 'POST':
        name = request.form.get('name')
        lat = request.form.get('lat')
        lng = request.form.get('lng')
        if name and lat and lng:
            try:
                locations.append({
                    "name": name,
                    "lat": float(lat),
                    "lng": float(lng)
                })
            except ValueError:
                pass  # 無効な数値は無視
        return redirect(url_for('map_view'))

    return render_template('map.html', locations=locations)

if __name__ == '__main__':
    app.run(debug=True)