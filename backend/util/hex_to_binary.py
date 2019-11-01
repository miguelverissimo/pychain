from backend.util.crypto_hash import crypto_hash

HEX_TO_BINARY_CONVERSION_TABLE = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}


def hex_to_binary(hex_str):
    binary_str = ""

    for char in hex_str:
        binary_str += HEX_TO_BINARY_CONVERSION_TABLE[char]

    return binary_str


def main():
    num = 4562
    hex_num = hex(num)[2:]
    bin_num = hex_to_binary(hex_num)
    decoded_num = int(bin_num, 2)

    print(f"hex_num:      {hex_num}")
    print(f"bin_num:      {bin_num}")
    print(f"decoded_num:  {decoded_num}\n")
    print(f"original_num: {num}\n")

    hex_to_binary_crypto_hash = hex_to_binary(crypto_hash("foo bar baz quux"))
    print(f"binary from hash: {hex_to_binary_crypto_hash}")


if __name__ == "__main__":
    main()
