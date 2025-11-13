def encode_ceaser(decode, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encode = ''
    decode = decode.lower()
    for i in decode:
        if i in alphabet:
            encode += alphabet[alphabet.index(i) + offset]
        else:
            encode += i
    return encode.upper()
print(encode_ceaser("AbZ",2)) #CDB


def decode_ceaser(encode, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    decode = ''
    encode = encode.lower()
    for i in encode:
        if i in alphabet:
            decode += alphabet[alphabet.index(i) - offset]
        else:
            decode += i
    return decode.upper()
print(decode_ceaser("CdB",2)) #ABZ

