import hashlib
import json


def crypto_hash(*args):
    """
    crypto_hash encrypts the provided data into a sha256 hash
    """

    args_string = sorted(map(lambda data: json.dumps(data), args))
    concatenated = "".join(args_string)

    return hashlib.sha256(concatenated.encode("utf-8")).hexdigest()


def main():
    print(f"crypto_hash('foo', 233223, [4]): {crypto_hash('foo', 233223, [4])}")
    print(f"crypto_hash(233223, 'foo', [4]): {crypto_hash(233223, 'foo', [4])}")


if __name__ == "__main__":
    main()
