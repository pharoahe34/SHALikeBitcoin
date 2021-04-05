"""
App that help you to encode your data in a sha256 way
"""

# importing libraries
from hashlib import sha256
import time

# settings
MAX_NONCE = 100000000000

# reading information as unicode string from the file
def SHA256(text):
    """
    * text:-> string that will be hash
    """

    return sha256(text.encode("ascii")).hexdigest()

# constructing new hash key and finding nonce number  
def mine(block_number, transactions, previous_hash, prefix_zeros):
    """
    * block_number:-> int of the block number
    * transactions:-> string that contains all transactions of this block number
    * previous_hash:-> previous hash encoding
    * prefix_zeros:-> number of zero at the beginning of the sha string
    """

    prefix_str = '0' * prefix_zeros

    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        # new hash started with '0'
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__=='__main__':
    
    # settings
    transactions = "Marc/Jules->20, Mike/Cara->45"
    difficulty = 4 # higher number will take more time for mining as difficulty increases
    
    # initialized counter
    start = time.time()
    print("Start mining")
    new_hash = mine(5, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"End of mining.\nMining took: {total_time} seconds")
    print(new_hash)