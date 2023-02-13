variables={}

# Lexer
def tokenize(source_code):
    tokens = []
    for i, c in enumerate(source_code):
        if c == "e" and source_code[i:i+4] == "echo":
            tokens.append(("ECHO", "echo"))
            end = source_code.find('\n', i + 1)
            string=source_code[i+4:end].strip()
            if string != '':
                tokens.append(("STRING", string))
                i = end
            continue
        elif c == "(":
            tokens.append(("LPAREN", "("))
            continue
        elif c == ")":
            tokens.append(("RPAREN", ")"))
            continue
        elif c == "=":
            tokens.append(("EQUALS", "="))
            continue
        elif c.isalpha():
            name = c
            while i + 1 < len(source_code) and source_code[i + 1].isalnum():
                i += 1
                name += source_code[i]
            tokens.append(("VARIABLE", name))
            continue
        elif c == '\n':
            tokens.append(("NL", "\n"))
    return tokens

# Parser
def parse(tokens):
    index = 0
    def parse_expression():
        nonlocal index
        if tokens[index][0] == "ECHO":
            index += 1
            string = tokens[index][1]
            index += 1
            if tokens[index][0] == "NL":
                index += 1
                return ("ECHO", string)
        elif tokens[index][0] == "VARIABLE":
            variable = tokens[index][1]
            index += 1
            if tokens[index][0] == "EQUALS":
                index += 1
                value = tokens[index][1]
                index += 1
                return ("ASSIGN", variable, value)
        return None
    return parse_expression()

# Interpreter
def interpret(ast):
    if ast[0] == "ECHO":
        print(ast[1])
    elif ast[0] == "ASSIGN":
        variable = ast[1]
        value = ast[2]
        # Add the variable and value to a dictionary of variables
        variables[variable] = value


def format_code(code):
    code=code.strip() + " \n"
    return code

# Test the language
with open("main.lunar") as source_code: 
    for code in source_code:
        try:
            source=format_code(code)
            tokens = tokenize(source)
            ast = parse(tokens)
            #print("AST:", ast)
            interpret(ast)
        except:
            pass
       

