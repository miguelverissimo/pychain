from backend.blockchain.block import Block, GENESIS_DATA


def test_mine():
    previous_block = Block.genesis()
    data = 'test data'
    block = Block.mine(previous_block, data)

    assert isinstance(block, Block)
    assert block.data == data


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, val in GENESIS_DATA.items():
        getattr(genesis, key) == val
