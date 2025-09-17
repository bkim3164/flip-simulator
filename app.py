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
        <h2>{{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    board = []
    p1_score = p2_score = None

    if request.method == "POST":
        p1_str = request.form["p1"]
        p2_str = request.form["p2"]

        # Parse player hands
        p1 = [Card.new(card.strip()) for card in p1_str.split(",")]
        p2 = [Card.new(card.strip()) for card in p2_str.split(",")]

        # Build deck & remove chosen cards
        deck = Deck()
        for c in p1 + p2:
            deck.cards.remove(c)

        # Deal board (5 random cards)
        board = deck.draw(5)

        # Evaluate
        p1_score = evaluator.evaluate(board, p1)
        p2_score = evaluator.evaluate(board, p2)

        if p1_score < p2_score:
            result = "Player 1 Wins!"
        elif p2_score < p1_score:
            result = "Player 2 Wins!"
        else:
            result = "It's a Tie!"

        # Convert board to readable
        board = [Card.int_to_pretty_str(c) for c in board]

    return render_template_string(TEMPLATE, result=result, board=board)

if __name__ == "__main__":
    app.run(debug=True)