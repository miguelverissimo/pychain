import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    "timestamp": 1,
    "prev_hash": "genesis_previous_hash",
    "hash": "genesis_hash",
    "data": [],
    "difficulty": 3,
    "nonce": "genesis_nonce",
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
            "Block("
            f"timestamp: {self.timestamp}, "
            f"prev_hash: {self.prev_hash}, "
            f"hash: {self.hash}, "
            f"data: {self.data}, "
            f"difficulty: {self.difficulty}, "
            f"nonce: {self.nonce})"
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

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

        while hex_to_binary(hash)[0:difficulty] != "0" * difficulty:
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

    @staticmethod
    def is_valid_block(previous_block, block):
        """
        Validate a block:
            - must have previous_hash equal to previous_block.hash
            - must meet proof of work
            - difficulty should be within 1 of the previous_block
            - hash must be a combination of the block's fields
        """
        if block.prev_hash != previous_block.hash:
            raise Exception("previous hash mismatch")

        if hex_to_binary(block.hash)[0 : block.difficulty] != "0" * block.difficulty:
            raise Exception("proof of work constraints not met")

        if abs(previous_block.difficulty - block.difficulty) > 1:
            raise Exception("difficulty expectation not met")

        rebuilt_hash = crypto_hash(
            block.timestamp, block.prev_hash, block.data, block.difficulty, block.nonce
        )

        if block.hash != rebuilt_hash:
            raise Exception(f"hash mismatch got: {block.hash} want: {rebuilt_hash}")


def main():
    genesis_block = Block.genesis()
    block = Block.mine(genesis_block, "foo")
    Block.is_valid_block(genesis_block, block)
    print(f"block: {block}")
    bad_block = Block.mine(block, "foo")
    # bad_block.prev_hash = 'totally-legit'
    bad_block.difficulty = 9000
    try:
        Block.is_valid_block(block, bad_block)
    except Exception as e:
        print(f"is_valid_block: {e}")


if __name__ == "__main__":
    main()
