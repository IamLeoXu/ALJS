from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# 数据文件路径
DATA_DIR = 'data'
MATCH_DIR = os.path.join(DATA_DIR, 'match')

# 加载JSON数据的辅助函数
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# 主页路由
@app.route('/')
def index():
    return render_template('index.html')

# 赛事纪录页面（加载 s1-s14 数据）
@app.route('/events')
def events():
    events_data = load_json(os.path.join(DATA_DIR, 'events.json'))
    return render_template('events.html', events=events_data)

# 参赛选手页面
@app.route('/players')
def players():
    players_data = load_json(os.path.join(DATA_DIR, 'players.json'))
    return render_template('players.html', players=players_data)

# 战绩记录页面
@app.route('/records')
def records():
    records_data = load_json(os.path.join(DATA_DIR, 'records.json'))
    return render_template('records.html', records=records_data)

# 比赛详情页面，动态加载赛季JSON（如 s1.json）
@app.route('/match/<season_id>')
def match(season_id):
    match_data = load_json(os.path.join(MATCH_DIR, f'{season_id}.json'))
    match_data['match_id'] = season_id.upper()  # 确保 match_id 为 S1 等
    return render_template('match.html', match=match_data)

# API端点，用于前端加载比赛数据
@app.route('/api/match/<season_id>')
def api_match(season_id):
    return jsonify(load_json(os.path.join(MATCH_DIR, f'{season_id}.json')))

if __name__ == '__main__':
    os.makedirs(MATCH_DIR, exist_ok=True)  # 确保比赛数据目录存在
    app.run(debug=True)