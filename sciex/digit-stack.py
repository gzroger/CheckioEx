class Stack:

    def __init__(self):
        self.s = []
        self.sum = 0

    def command(self, command: str):
        cmdpar = command.split()
        if cmdpar[0] == "PUSH":
            self.s += [int(cmdpar[1])]
        elif cmdpar[0] == "POP":
            if self.s:
                self.sum += self.s.pop()
        elif cmdpar[0] == "PEEK":
            if self.s:
                self.sum += self.s[-1]


def digit_stack(commands: [str]):
    stack = Stack()
    for command in commands:
        stack.command(command)
    return stack.sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
#                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
