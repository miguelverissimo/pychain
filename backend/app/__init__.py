from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route("/")
def default():
    return "blockchain"


@app.route("/blockchain/")
def blockchain_route():
    return jsonify(blockchain.to_json())


@app.route("/blockchain/mine/")
def blockchain_mine_route():
    transaction_data = "stubbed_data"
    blockchain.add_block(transaction_data)

    return jsonify(blockchain.chain[-1].to_json())


app.run()
