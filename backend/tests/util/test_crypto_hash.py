from backend.util.crypto_hash import crypto_hash


def test_crypto_hash():
    # it should produce the same hash independent of the params' order
    assert crypto_hash(1, [2], 'tres') == crypto_hash('tres', 1, [2])

    # it always produces the same output for the same input
    assert crypto_hash(
        1, [2], 'tres') == '91dee9cb59dc4cb8b571a4b8c594000a402030a28f80d7299a872074f65fe479'
