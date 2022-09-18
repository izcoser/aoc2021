# Receives hex string, returns binary string.
# Binary output length will always be a multiple of 4, with leading zeroes if needed.
# Input should not begin with '0x', output does not begin with '0b'.
# >>> hex_to_binary('D2FE28')
# >>> '110100101111111000101000'
# >>> hex_to_binary('38006F45291200')
# >>> '00111000000000000110111101000101001010010001001000000000'
def hex_to_binary(hex: str) -> str:
    res = bin(int(hex, 16))[2:]
    return '0' * (len(res) % 4) + res

#print(hex_to_binary('D2FE28'))
#print('110100101111111000101000')


#print(hex_to_binary('38006F45291200'))
#print('00111000000000000110111101000101001010010001001000000000')

#print(hex_to_binary('EE00D40C823060'))
#print('11101110000000001101010000001100100000100011000001100000')