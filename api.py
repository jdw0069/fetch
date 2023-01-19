from flask import Flask, request, jsonify
import uuid
from rules import rule1, rule2, rule3, rule4, rule5, rule6, rule7

app = Flask(__name__)

recepitsStorage= {}

@app.route("/receipts/process", methods=["POST"])
def process():
    content = request.get_json()
    recepitsStorage[str(uuid.uuid1().hex)] = content
    id = {
        "id": str(list(recepitsStorage.keys())[-1])
    }
    return jsonify(id), 200

    

@app.route("/receipts/<id>/points", methods=["GET"])
def points(id):
    points = {
        "points": totalPoints(id)
    }

    return jsonify(points), 200

def totalPoints(id):
    receipt = recepitsStorage[id]
    firstRule = rule1.retalierCharacters(receipt['retailer'])
    secondRule = rule2.totalAmountIsRound(receipt["total"])
    thirdRule = rule3.totalAmountIsMultipleOf25(receipt["total"])
    fourthRule = rule4.everyTwoItems(receipt["items"])
    fifthRule = rule5.itemDescriptionIsMultipleOf3(receipt["items"])
    sixthRule = rule6.isPurchaseDayOdd(receipt["purchaseDate"])
    seventhRule = rule7.purchaseTimeInWindow(receipt["purchaseTime"])
    summation = sum([firstRule, secondRule, thirdRule, fourthRule
    , fifthRule, sixthRule, seventhRule])
    return str(summation)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000)