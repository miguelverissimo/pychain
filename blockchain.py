from block import Block


class Blockchain:
    """
    Blockchain is a list of blocks, representing a ledger of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'


def main():
    blockchain = Blockchain()
    blockchain.add_block('foo')
    blockchain.add_block('bar')
    blockchain.add_block('baz')

    print(blockchain)


if __name__ == "__main__":
    main()
