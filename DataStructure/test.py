def accept(a, w):
    if len(w) % 6 != 0:
        return "reject"

    #split the input into chunks of 6 digits
    chunks = [w[i:i+6] for i in range(0, len(w), 6)]

    currentState = a.start
    fullPath = []

    for chunk in chunks:
        stack = [(currentState, chunk, [])]
        validChunk = False
        chunkPath = []

        while stack:
            state, remainingInput, path = stack.pop()
            if not remainingInput:
                if state in a.accepts:
                    validChunk = True
                    chunkPath = path
                    break
                for symbol, nextStates in a.transitions.get(state, {}).items():
                    if symbol.isalpha() and 'q0' in nextStates: #treat letter as lambda
                        path.append((state, symbol, 'q0'))
                        validChunk = True
                        chunkPath = path
                        break
                continue

            symbol = remainingInput[0]
            if state not in a.transitions or symbol not in a.transitions[state]:
                continue
            for nextState in a.transitions[state][symbol]:
                newPath = path + [(state, symbol, nextState)]
                stack.append((nextState, remainingInput[1:], newPath))

        if not validChunk:
            return "reject"

        currentState = chunkPath[-1][2] if chunkPath else currentState
        fullPath.extend(chunkPath)

    result = "accept\n"
    for step in fullPath:
        result += f"{step[0]} {step[1]} {step[2]}\n"
    return result.strip()