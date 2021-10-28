from flask import Flask, jsonify

from mycoin.blockchain import BlockChain

app = Flask(__name__)
blockchain = BlockChain()


#  Mining a new Block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    prev_block = blockchain.get_prev_block()
    prev_proof = prev_block['proof']
    proof = blockchain.proof_work(prev_proof)
    prev_hash = blockchain.hash(prev_block)
    block = blockchain.create_block(proof, prev_hash)
    response = {'message': 'You MINED a BLOCK !!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'prev_hash': block['prev_hash']}
    return jsonify(response), 200


# Retrieve the Full BlockChain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


# Check if Chain is Valid
@app.route('/is_valid', methods=['GET'])
def is_valid():
    valid = blockchain.is_valid_chain(blockchain.chain)
    if valid:
        response = {'isValidChain': valid,
                    'message': 'BlockChain is Valid'}
    else:
        response = {'isValidChain': valid,
                    'message': 'BlockChain is Not Valid'}

    return jsonify(response), 200


# Run the App
# app.run('127.0.0.1', port=5000)   #LocalHOst
app.run('0.0.0.0', port=5000)       # Server IP for External
