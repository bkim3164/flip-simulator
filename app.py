from flask import Flask, request, render_template_string
from treys import Deck, Evaluator, Card

app = Flask(__name__)
evaluator = Evaluator()

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Poker Flip Simulator</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        input { margin: 5px; }
    </style>
</head>
<body>
    <h1>Poker Flip Simulator</h1>
    <form method="POST">
        <label>Player 1 Hand (e.g. As,Kd):</label><br>
        <input type="text" name="p1"><br>
        <label>Player 2 Hand (e.g. Qh,Qc):</label><br>
        <input type="text" name="p2"><br>
        <button type="submit">Run Flip</button>
    </form>
    {% if result %}
        <h2>Board: {{ board }}</h2>
        <p>Player 1 score: {{ p1_score }}</p>
        <p>Player 2 score: {{ p2_score }}</p>
        <h2>{{ result }}</h2>
    {% endif %}
</body>
</html>
"""