from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from waitress import serve


app = Flask(__name__)

CORS(app)


# Arbre de décision sous forme de dictionnaire
decision_tree = {
"Le patient est-il majeur ?":{
   "oui":"Est-il concient ?",
   "non":"Le mineur est-il concient ?"
},
"Le mineur est-il concient ?":{
    "oui":"Sa fréquence est-elle supérieur ou egal a 25 ?",
    "non":"Niveau 1"
},
"Sa fréquence est-elle supérieur ou egal a 25 ?":{
    "oui":"A-t-il quelque chose de casser ?",
    "non":"Niveau 1"
},
"A-t-il quelque chose de casser ?":{
    "oui":"Niveau 3",
    "non":"A-t-il une douleur supérieur a 6 ?"
},
"A-t-il une douleur supérieur a 6 ?":{
    "oui":"Niveau 1",
    "non":"Nveau 4"
},
"Est-il concient ?":{
    "oui":"Sa fréquence est-elle supérieur ou egal a 30 ?",
    "non":"Libérer ses voies aériennes. Respire-t-il ?"
},
"Libérer ses voies aériennes. Respire-t-il ?":{
    "oui":"Son rythme cardiaque est supérieur ou egal a 60 ?",
    "non":"Niveau 1"
},
"Son rythme cardiaque est supérieur ou egal a 60 ?":{
    "oui":"Niveau 3",
    "non":"Niveau 2"
},
"Sa fréquence est-elle supérieur ou egal a 30 ?":{
    "oui":"Son rythme cardiaque est supérieur ou egal a 60 ?",
    "non":"Niveau 2"
},
"Son rythme cardiaque est supérieur ou egal a 60 ?":{
    "oui":"Peut-il répondre aux ordres simples ?",
    "non":"Niveau 2"
},
"Peut-il répondre aux ordres simples ?":{
    "oui":"Niveau 5",
    "non":"Répond-t-il de manière partiel ?"
},
"Répond-t-il de manière partiel ?":{
    "oui":"Niveau 4",
    "non":"Niveau 2"
},
}

@app.route("/")
def index():
    return send_file("templates/index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    question = data.get("question")
    answer = data.get("answer")

    next_step = decision_tree.get(question, {}).get(answer, "Je n'ai pas compris.")

    return jsonify({"next_question": next_step})
def run():
    serve(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run()
