import hashlib

print(hashlib.sha256("Brian").hexdigest())
# 5714e04739071aabdf34a209fcec4c33976a969dd2ca1c5007b406b2d8642bc5

text = "Brian"
nonce = 0
textWithNonce = text + str(nonce)
print(textWithNonce)

for nonce in range(10):
    input = text + str(nonce)
    hash = hashlib.sha256(input).hexdigest()
    print(input, '=>', hash)