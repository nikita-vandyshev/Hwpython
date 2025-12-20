def build_freq(msg: str) -> dict[str, int]:
    freq: dict[str, int] = {}
    for ch in msg:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


def build_huffman_table(msg: str) -> dict[str, str]:
    freq = build_freq(msg)

    if len(freq) == 0:
        return {}

    if len(freq) == 1:
        only_char = next(iter(freq))
        return {only_char: "0"}

    nodes = []
    uid = 0
    for ch, f in freq.items():
        nodes.append((f, uid, ch, None, None))
        uid += 1

    while len(nodes) > 1:
        nodes.sort(key=lambda x: (x[0], x[1]))

        left = nodes.pop(0)
        right = nodes.pop(0)

        new_node = (left[0] + right[0], uid, None, left, right)
        uid += 1
        nodes.append(new_node)

    root = nodes[0]

    table: dict[str, str] = {}

    def dfs(node, code: str) -> None:
        ch = node[2]
        left = node[3]
        right = node[4]

        if ch is not None:
            table[ch] = code
            return

        dfs(left, code + "0")
        dfs(right, code + "1")

    dfs(root, "")
    return table


def encode(msg: str) -> tuple[str, dict[str, str]]:
    table = build_huffman_table(msg)

    encoded = ""
    for ch in msg:
        encoded += table[ch]

    return encoded, table


def decode(encoded: str, table: dict[str, str]) -> str:
    rev: dict[str, str] = {}
    for ch, code in table.items():
        rev[code] = ch

    result = ""
    cur = ""

    for bit in encoded:
        cur += bit
        if cur in rev:
            result += rev[cur]
            cur = ""

    return result


def encode_to_file(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        msg = f.read()

    encoded, table = encode(msg)

    with open(output_path, "w", encoding="utf-8") as f:
        for ch, code in table.items():
            f.write(f"{ord(ch)}:{code}\n")

        f.write("---\n")
        f.write(encoded)


def decode_from_file(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    table: dict[str, str] = {}
    i = 0

    while i < len(lines) and lines[i] != "---":
        line = lines[i]
        if line.strip() != "":
            left, code = line.split(":", 1)
            ch = chr(int(left))
            table[ch] = code
        i += 1

    i += 1
    encoded = "".join(lines[i:])

    msg = decode(encoded, table)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(msg)


if __name__ == "__main__":
    print("1 - encode text file to encoded.txt")
    print("2 - decode encoded.txt to decoded.txt")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        encode_to_file("input.txt", "encoded.txt")
        print("Done! Created encoded.txt")
    elif choice == "2":
        decode_from_file("encoded.txt", "decoded.txt")
        print("Done! Created decoded.txt")
    else:
        print("Unknown choice")
