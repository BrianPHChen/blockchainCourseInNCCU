import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce, block_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = block_hash

def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis Block", "0", "0", "0")

def next_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = str(data)
    this_pre_hash = last_block.hash
    block_hash, nonce = proof_of_work(this_index, this_timestamp, this_data, this_pre_hash)
    return Block(this_index, this_timestamp, this_data, this_pre_hash, nonce, block_hash)

def proof_of_work(index, timestamp, data, pre_hash):
    max_nonce = 2 ** 32
    target = 2 ** 240
    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(index)+
                                     str(timestamp)+
                                     str(data)+
                                     str(pre_hash)+
                                     str(nonce)).hexdigest()
        if long(hash_result, 16) < target:
            print("Success with nonce", nonce)
            print("Hash is", hash_result)
            return (hash_result, nonce)

blockchain = [create_genesis_block()]
latest_block = blockchain[0]

# num_of_blocks_to_add = 20

# for index in range(num_of_blocks_to_add):
#     new_block = next_block(latest_block)
#     blockchain.append(new_block)
#     latest_block = new_block
#     print("Block #{} has been added to the blockchain".format( new_block.index ))
#     print("Hash: {}\n".format( new_block.hash ))

tx1 = {
    "from": "Alex",
    "to": "Bob",
    "amount": 3
}

tx2 = {
    "from": "Bob",
    "to": "Alex",
    "amount": 7
}

data = [tx1, tx2]

new_block = next_block(latest_block, data)
blockchain.append(new_block)
latest_block = new_block
print("Block #{} has been added to the blockchain".format( new_block.index ))
print("Hash: {}\n".format( new_block.hash ))

print(blockchain[1].index, blockchain[1].timestamp, blockchain[1].data, blockchain[1].previous_hash, blockchain[1].nonce, blockchain[1].hash)