class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def check_brackets(text):
    error_pos = 0
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            b = Bracket(next, i+1)
            opening_brackets_stack.append(b)

        if next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack:
                error_pos = i + 1
                break
            top = opening_brackets_stack.pop()
            if not top.Match(next):
                error_pos = i + 1
                break

    if error_pos == 0 and not opening_brackets_stack:
        return "Success"
    else:
        if error_pos == 0:
            while len(opening_brackets_stack) > 1:
                opening_brackets_stack.pop()
            error_pos = opening_brackets_stack[-1].position
        return error_pos

if __name__ == "__main__":
    text = input("Enter a string with brackets: ")
    result = check_brackets(text)
    print(result)
