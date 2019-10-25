import time
from backend.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS
from backend.util.hex_to_binary import hex_to_binary

def test_mine():
    previous_block = Block.genesis()
    data = 'test data'
    block = Block.mine(previous_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert hex_to_binary(block.hash)[0:block.difficulty] == '0' * block.difficulty


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, val in GENESIS_DATA.items():
        getattr(genesis, key) == val

def test_adjust_difficulty_slow_mining():
    last_block = Block.mine(Block.genesis(), 'foo')
    mined_block = Block.mine(last_block, 'bar')

    assert mined_block.difficulty == last_block.difficulty + 1

def test_adjust_difficulty_fast_mining():
    last_block = Block.mine(Block.genesis(), 'foo')
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine(last_block, 'bar')

    assert mined_block.difficulty == last_block.difficulty - 1

def test_adjust_difficulty_limits_at_1():
    last_block = Block(
        time.time_ns(),
        'test_previous_hash',
        'test_hash',
        'test_data',
        1,
        0
    )
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine(last_block, 'bar')

    assert mined_block.difficulty == 1