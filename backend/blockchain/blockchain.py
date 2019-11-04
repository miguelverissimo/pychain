from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain is a list of blocks, representing a ledger of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def __repr__(self):
        return f"Blockchain: {self.chain}"

    def to_json(self):
        return list(map(lambda block: block.to_json(), self.chain))
        return serialized

    def add_block(self, data):
        self.chain.append(Block.mine(self.chain[-1], data))

    def replace_chain(self, chain):
        """
        Replace the current chain with the incoming one, if:
          - the incoming chain is longer than the current;
          - the incoming chain is valid.
        """
        if len(chain) <= len(self.chain):
            raise Exception("incoming chain is not longer than the current chain")

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f"chain is not valid: {e}")

        self.chain = chain

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
