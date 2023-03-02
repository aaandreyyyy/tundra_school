def make_hash(password: str):
    MOD = 1000000007
    POW = 73
    hash_pow = 1
    hash_ = 0
    for i in password:
        hash_ += (ord(i)) * hash_pow
        hash_ = hash_ % MOD
        hash_pow = (hash_pow * POW) % MOD
    return hash_


def compare(password: str, hash_):
    return make_hash(password) == hash_


if __name__ == '__main__':
    pass
