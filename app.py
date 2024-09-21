from flask import Flask, render_template, request
import json
from services import graph


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form
        N = int(data["vertices"])
        edges = json.loads(data["edges"])
        START = int(data["start"])
        END = int(data["end"])
        MAX_STOPS = int(data["max_stops"])

        g = graph(N)

        for edge in edges:
            g.add_edge(edge[0], edge[1], edge[2])

        distance, path = g.bellman(START, END, MAX_STOPS)
        # Convert path to a string for the template
        path_str = " -> ".join(map(str, path)) if path else "No Path Found"

        return render_template("result.html", distance=distance, path=path)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
