with open('input.txt', 'r') as f:
    input_text = f.read().splitlines()
tokens = []
emailpass = []
for entry in input_text:
    separated = entry.split(':')
    if separated != ['']:
        tokens.append(separated[2])
        _separated = entry.split(':')
        emailpass.append(f"{_separated[0]}:{_separated[1]}")
with open('tokens.txt', 'w+') as f:
    f.write("\n".join(tokens))
with open('emailpass.txt', 'w+') as f:
    f.write("\n".join(emailpass))
