'''
To generate the unique url, we could:

Take the MD5 hash of the user's ip_address + timestamp
MD5 is a widely used hashing function that produces a 128-bit hash value
MD5 is uniformly distributed
Alternatively, we could also take the MD5 hash of randomly-generated data
Base 62 encode the MD5 hash
Base 62 encodes to [a-zA-Z0-9] which works well for urls, eliminating the need for escaping special characters
There is only one hash result for the original input and Base 62 is deterministic (no randomness involved)
Base 64 is another popular encoding but provides issues for urls because of the additional + and / characters
The following Base 62 pseudocode runs in O(k) time where k is the number of digits = 7:
'''
def base_encode(num, base=62):
    digits = []
    while num > 0
      remainder = modulo(num, base)
      digits.push(remainder)
      num = divide(num, base)
    digits = digits.reverse

# url = base_encode(md5(ip_address+timestamp))[:URL_LENGTH]    