# know from the task that these bytes are only 5 bit long


def reverse_bits(inp):
    result = ""
    for i in inp:
        result += "0" if i == "1" else "1"
    return result


bits = [0] * 12
total_bytes = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        total_bytes += 1
        for i, bit in enumerate(line):
            if bit in ["0", "1"]:
                bits[i] += int(bit)


gamma_rate = "".join("1" if bit > total_bytes / 2 else "0" for bit in bits)
epsilon_rate = int(reverse_bits(gamma_rate), 2)
print(int(gamma_rate, 2) * epsilon_rate)

