import hashlib

print(hashlib.sha256("1"+"31780"+"Brian").hexdigest())

index = "1"
text = "Brian"
max_nonce = 2 ** 32

def proof_of_work(index, data, difficulty_bits):
    target = 2 ** (256 - difficulty_bits)
    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(index)+str(nonce)+str(data)).hexdigest()
        if long(hash_result, 16) < target:
            print("Success with nonce", nonce)
            print("Hash is", hash_result)
            return (hash_result, nonce)

proof_of_work(index, text, 16)

