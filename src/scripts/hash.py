from hashlib import pbkdf2_hmac


key = b"locker"


async def hash_converter(password):
    bpassword = bytes(password)
    iters = 500_000
    output = pbkdf2_hmac('md5', key, bpassword, iters)
    return output.hex()

