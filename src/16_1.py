version_sum = 0
# Receives hex string, returns binary string.
# Binary output length will always be a multiple of 4, with leading zeroes if needed.
# Input should not begin with '0x', output does not begin with '0b'.
# >>> hex_to_binary('D2FE28')
# >>> '110100101111111000101000'
# >>> hex_to_binary('38006F45291200')
# >>> '00111000000000000110111101000101001010010001001000000000'
def hex_to_binary(hex: str) -> str:
    return bin(int('1'+hex, 16))[3:]

# print(hex_to_binary('D2FE28'))
# print('110100101111111000101000')

# print(hex_to_binary('38006F45291200'))
# print('00111000000000000110111101000101001010010001001000000000')

# print(hex_to_binary('EE00D40C823060'))
# print('11101110000000001101010000001100100000100011000001100000')

def parse_packet(packet: str):
    binary = packet
    version = int(binary[:3], 2)
    global version_sum
    version_sum += version
    type_id = int(binary[3:6], 2)

    if type_id == 4:  # literal value
        literal = ""
        prefix_index = 6
        while True:
            prefix_bit = binary[prefix_index]
            group = binary[prefix_index + 1 : prefix_index + 5]
            literal += group
            prefix_index += 5
            if prefix_bit == "0":
                break
        literal_value = int(literal, 2)
        packet_len = prefix_index
        return packet_len

    else:
        length_type = binary[6]
        print("Operator packet ", end="")
        if length_type == "0":
            subpackets_len = int(binary[7 : 7 + 15], 2)
            print(f"with {subpackets_len} bits of subpackets.")
            subpackets_pos = 7 + 15
            subpackets_end = 7 + 15 + subpackets_len
            while subpackets_pos < subpackets_end:
                subpackets_pos += parse_packet(binary[subpackets_pos:])
            return subpackets_pos
        elif length_type == "1":
            subpackets_count = int(binary[7 : 7 + 11], 2)
            i = 0
            subpackets_pos = 7 + 11
            print(f"with {subpackets_count} subpackets")
            while i < subpackets_count:
                subpackets_pos += parse_packet(binary[subpackets_pos:])
                i += 1
            return subpackets_pos

        else:
            raise Exception(f"Unexpected length_type: {length_type}")


def solve(hex_packet: str):
    binary = hex_to_binary(hex_packet)
    global version_sum
    version_sum = 0
    parse_packet(binary)
    print(version_sum)

packet1 = "D2FE28"
packet2 = "38006F45291200"
packet3 = "EE00D40C823060"
packet4 = '8A004A801A8002F478'
packet5 = '620080001611562C8802118E34'
packet6 = 'C0015000016115A2E0802F182340'
packet7 = 'A0016C880162017C3686B18A3D4780'
packet8 = '005473C9244483004B001F79A9CE75FF9065446725685F1223600542661B7A9F4D001428C01D8C30C61210021F0663043A20042616C75868800BAC9CB59F4BC3A40232680220008542D89B114401886F1EA2DCF16CFE3BE6281060104B00C9994B83C13200AD3C0169B85FA7D3BE0A91356004824A32E6C94803A1D005E6701B2B49D76A1257EC7310C2015E7C0151006E0843F8D000086C4284910A47518CF7DD04380553C2F2D4BFEE67350DE2C9331FEFAFAD24CB282004F328C73F4E8B49C34AF094802B2B004E76762F9D9D8BA500653EEA4016CD802126B72D8F004C5F9975200C924B5065C00686467E58919F960C017F00466BB3B6B4B135D9DB5A5A93C2210050B32A9400A9497D524BEA660084EEA8EF600849E21EFB7C9F07E5C34C014C009067794BCC527794BCC424F12A67DCBC905C01B97BF8DE5ED9F7C865A4051F50024F9B9EAFA93ECE1A49A2C2E20128E4CA30037100042612C6F8B600084C1C8850BC400B8DAA01547197D6370BC8422C4A72051291E2A0803B0E2094D4BB5FDBEF6A0094F3CCC9A0002FD38E1350E7500C01A1006E3CC24884200C46389312C401F8551C63D4CC9D08035293FD6FCAFF1468B0056780A45D0C01498FBED0039925B82CCDCA7F4E20021A692CC012B00440010B8691761E0002190E21244C98EE0B0C0139297660B401A80002150E20A43C1006A0E44582A400C04A81CD994B9A1004BB1625D0648CE440E49DC402D8612BB6C9F5E97A5AC193F589A100505800ABCF5205138BD2EB527EA130008611167331AEA9B8BDCC4752B78165B39DAA1004C906740139EB0148D3CEC80662B801E60041015EE6006801364E007B801C003F1A801880350100BEC002A3000920E0079801CA00500046A800C0A001A73DFE9830059D29B5E8A51865777DCA1A2820040E4C7A49F88028B9F92DF80292E592B6B840'

solve(packet8)
