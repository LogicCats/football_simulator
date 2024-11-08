from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Данные команд и игроков с характеристиками
teams = {
    "Team A": {
        "name": "Team A",
        "players": [
            {"name": "Player 1", "speed": 70, "accuracy": 80, "stamina": 75, "defense": 60},
            {"name": "Player 2", "speed": 65, "accuracy": 85, "stamina": 70, "defense": 65},
            {"name": "Player 3", "speed": 75, "accuracy": 60, "stamina": 80, "defense": 70}
        ]
    },
    "Team B": {
        "name": "Team B",
        "players": [
            {"name": "Player 4", "speed": 80, "accuracy": 75, "stamina": 60, "defense": 65},
            {"name": "Player 5", "speed": 60, "accuracy": 70, "stamina": 85, "defense": 75},
            {"name": "Player 6", "speed": 65, "accuracy": 65, "stamina": 70, "defense": 80}
        ]
    }
}

# Функция для генерации событий с учетом характеристик
def generate_event_description(team, player, minute):
    events = [
        f"{minute} мин: {player['name']} из команды {team} забивает блестящий гол!",
        f"{minute} мин: {player['name']} из команды {team} делает мощный удар, и это гол!",
        f"{minute} мин: {player['name']} ({team}) проходит защитников и отправляет мяч в сетку!",
        f"{minute} мин: Отличная игра {player['name']} из команды {team}, который забивает гол!",
        f"{minute} мин: {player['name']} из команды {team} успешно завершает атаку!"
    ]
    return random.choice(events)

# Обновленная функция для симуляции матча
def simulate_game(team1, team2):
    score_team1 = 0
    score_team2 = 0
    possession_team1 = random.randint(40, 60)
    possession_team2 = 100 - possession_team1
    fouls_team1 = random.randint(0, 5)
    fouls_team2 = random.randint(0, 5)
    events = []

    # Симуляция игры с учетом характеристик игроков
    for _ in range(random.randint(5, 10)):
        minute = random.randint(1, 90)
        scoring_team = team1 if random.choice([True, False]) else team2
        scoring_player = random.choice(teams[scoring_team]["players"])

        # Вероятность успешного гола основана на характеристиках
        chance_of_goal = scoring_player["accuracy"] + scoring_player["speed"] - scoring_player["defense"] * 0.5
        if random.randint(0, 100) < chance_of_goal:
            if scoring_team == team1:
                score_team1 += 1
            else:
                score_team2 += 1
            event = generate_event_description(scoring_team, scoring_player, minute)
            events.append(event)

    # Итоговый результат и статистика
    result = {
        "team1": team1,
        "team2": team2,
        "score_team1": score_team1,
        "score_team2": score_team2,
        "possession": {team1: possession_team1, team2: possession_team2},
        "fouls": {team1: fouls_team1, team2: fouls_team2},
        "events": sorted(events)
    }
    return result

# Страница для создания команды с характеристиками
@app.route('/create_team', methods=['GET', 'POST'])
def create_team():
    if request.method == 'POST':
        team_name = request.form['team_name']
        players = [
            {
                "name": request.form[f'player{i}_name'],
                "speed": int(request.form[f'player{i}_speed']),
                "accuracy": int(request.form[f'player{i}_accuracy']),
                "stamina": int(request.form[f'player{i}_stamina']),
                "defense": int(request.form[f'player{i}_defense'])
            }
            for i in range(1, 4)
        ]

        if team_name in teams:
            return render_template('create_team.html', error="Команда с таким названием уже существует!")
        teams[team_name] = {"name": team_name, "players": players}
        return redirect(url_for('index'))
    return render_template('create_team.html')

# Главная страница и старт игры
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        if team1 != team2:
            result = simulate_game(team1, team2)
            return render_template('result.html', result=result)
        else:
            return render_template('index.html', teams=teams, error="Выберите разные команды!")
    return render_template('index.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)

