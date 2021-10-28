import datetime
import hashlib
import json


# Part 1: Create a BlockChain Class
class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'prev_hash': previous_hash}

        self.chain.append(block)
        return block

    def get_prev_block(self):
        return self.chain[-1]       # return the Last Block from Chain

    def proof_work(self, prev_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha224(str(new_proof**2 + prev_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_valid_chain(self, chain):
        prev_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            curr_block = chain[block_index]
            if curr_block['prev_hash'] != self.hash(prev_block):
                return False
            prev_proof = prev_block['proof']
            proof = curr_block['proof']
            hash_operation = hashlib.sha224(str(proof ** 2 + prev_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            prev_block = curr_block
            block_index += 1
        return True













