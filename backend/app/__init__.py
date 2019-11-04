from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()
for i in range(5):
    blockchain.add_block(f"block #{i}")


@app.route("/")
def default():
    return "blockchain"


@app.route("/blockchain")
def blockchain_route():
    return jsonify(blockchain.to_json())


app.run()
