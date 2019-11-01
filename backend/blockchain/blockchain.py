from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain is a list of blocks, representing a ledger of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine(self.chain[-1], data))

    def __repr__(self):
        return f"Blockchain: {self.chain}"

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate a chain:
          - must start with the genesis block
          - every block must be valid
        """
        if chain[0] != Block.genesis():
            raise Exception("genesis block is invalid")

        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i - 1]
            Block.is_valid_block(previous_block, current_block)


def main():
    blockchain = Blockchain()
    blockchain.add_block("foo")
    blockchain.add_block("bar")
    blockchain.add_block("baz")

    print(blockchain)


if __name__ == "__main__":
    main()
