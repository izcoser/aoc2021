# Packet id to operation dict.
id_to_operation = {
    0: "+",
    1: "*",
    2: "min",
    3: "max",
    5: ">",
    6: "<",
    7: "==",
}

# Store all operations on this stack.
# Example, if you read a sum packet, with two literals x and y,
# the stack will be [+, x, y].
stack = []

# Receives hex string, returns binary string.
# Binary output length will always be a multiple of 4, with leading zeroes if needed.
# Input should not begin with '0x', output does not begin with '0b'.
# >>> hex_to_binary('D2FE28')
# >>> '110100101111111000101000'
# >>> hex_to_binary('38006F45291200')
# >>> '00111000000000000110111101000101001010010001001000000000'
def hex_to_binary(hex: str) -> str:
    return bin(int("1" + hex, 16))[3:]


# Parses a packet and its subpackets recursively.
def parse_packet(packet: str):
    binary = packet
    version = int(binary[:3], 2)
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
        stack.append(literal_value)
        packet_len = prefix_index
        return packet_len

    else:
        stack.append(id_to_operation[type_id])
        length_type = binary[6]
        print(f"Operator packet {id_to_operation[type_id]} ", end="")
        if length_type == "0":
            subpackets_len = int(binary[7 : 7 + 15], 2)
            print(f"with {subpackets_len} bits of subpackets.")
            subpackets_pos = 7 + 15
            subpackets_end = 7 + 15 + subpackets_len
            while subpackets_pos < subpackets_end:
                subpackets_pos += parse_packet(binary[subpackets_pos:])
            stack.append(")")  # marks the end of a packet.
            return subpackets_pos
        elif length_type == "1":
            subpackets_count = int(binary[7 : 7 + 11], 2)
            i = 0
            subpackets_pos = 7 + 11
            print(f"with {subpackets_count} subpackets")
            while i < subpackets_count:
                subpackets_pos += parse_packet(binary[subpackets_pos:])
                i += 1
            stack.append(")")
            return subpackets_pos

        else:
            raise Exception(f"Unexpected length_type: {length_type}")


def evaluate_stack(stack):
    # Evaluation stack. Will pop from {stack} to compute the final value.
    eval_stack = []
    while len(stack) > 0:
        element = stack.pop()
        print("Stack: ", end="")
        print(*stack, sep=" ")
        print(f"Current element: {element}")
        if element == "+":
            ret = 0
            while True:
                p = eval_stack.pop()
                if p == ")":
                    break
                ret += p
            eval_stack.append(ret)
        elif element == "*":
            ret = 1
            while True:
                p = eval_stack.pop()
                if p == ")":
                    break
                ret *= p
            eval_stack.append(ret)
        elif element == "min":
            ret = float("INF")
            while True:
                p = eval_stack.pop()
                if p == ")":
                    break
                ret = min(p, ret)
            eval_stack.append(ret)
        elif element == "max":
            ret = float("-INF")
            while True:
                p = eval_stack.pop()
                if p == ")":
                    break
                ret = max(p, ret)
            eval_stack.append(ret)
        elif element == ">":
            a = eval_stack.pop()
            b = eval_stack.pop()
            eval_stack.pop()  # )
            eval_stack.append(1 if a > b else 0)
        elif element == "<":
            a = eval_stack.pop()
            b = eval_stack.pop()
            eval_stack.pop()  # )
            eval_stack.append(1 if a < b else 0)
        elif element == "==":
            a = eval_stack.pop()
            b = eval_stack.pop()
            eval_stack.pop()  # )
            eval_stack.append(1 if a == b else 0)
        elif type(element) == int or element == ")":
            eval_stack.append(element)
        else:
            raise Exception(f"Unexpected element type: {element}")

        print("Eval stack: ", sep="")
        print(*eval_stack, sep=" ")
    print(eval_stack)


def solve(hex_packet: str):
    binary = hex_to_binary(hex_packet)
    parse_packet(binary)
    evaluate_stack(stack)


puzzle = input()
solve(puzzle)
