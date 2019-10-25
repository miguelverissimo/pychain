import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'prev_hash': 'genesis_previous_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}


class Block:
    """
    Block stores individual transactions
    """

    def __init__(self, timestamp, prev_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'prev_hash: {self.prev_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )

    @staticmethod
    def mine(previous_block, data):
        """
        Mine a block based on the previous_block and data, until a block hash is found
        that will satisfy the leading zeros requirement for proof of work.
        """

        timestamp = time.time_ns()
        previous_hash = previous_block.hash
        difficulty = Block.adjust_difficulty(previous_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, previous_hash, data, difficulty, nonce)
        
        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(previous_block, timestamp)
            hash = crypto_hash(timestamp, previous_hash, data, difficulty, nonce)

        return Block(timestamp, previous_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        Genesis generates the genesis (initial) block
        """
        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Calculate the adjusted difficulty according to the MINE_RATE, increasing it when
        the time to generate the previous block was below the threshold, and decresasing
        it when it was above the threshold.
        """

        time_to_mine = new_timestamp - last_block.timestamp

        if time_to_mine < MINE_RATE:
            return last_block.difficulty + 1

        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1

def main():
    genesis_block = Block.genesis()
    block = Block.mine(genesis_block, 'foo')
    print(block)


if __name__ == "__main__":
    main()
