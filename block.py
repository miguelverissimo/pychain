import time
from crypto_hash import crypto_hash


class Block:
    """
    Block stores individual transactions
    """

    def __init__(self, timestamp, prev_hash, hash, data):
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'prev_hash: {self.prev_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data})'
        )

    @staticmethod
    def mine(previous_block, data):

        timestamp = time.time_ns()
        previous_hash = previous_block.hash
        hash = crypto_hash(timestamp, previous_hash, data)

        return Block(timestamp, previous_hash, hash, data)

    @staticmethod
    def genesis():
        """
        Genesis generates the genesis (initial) block
        """
        return Block(1, 'genesis_previous_hash', 'genesis_hash', [])


def main():
    genesis_block = Block.genesis()
    block = Block.mine(genesis_block, 'foo')
    print(block)


if __name__ == "__main__":
    main()
