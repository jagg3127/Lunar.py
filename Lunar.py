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
        elif c == '\n':
            tokens.append(("NL", "\n"))
            

            
    return tokens

# Parser
def parse(tokens):
    def parse_expression():
        index = 0        
        if tokens[index][0] == "ECHO":
            string = tokens[index+1][1]
            if tokens[index+2][0] == "NL":
                index += 1
                return ("ECHO", string)
        return index
    return parse_expression()

# Interpreter
def interpret(ast):
    #print("AST:", ast)
    if ast[0] == "ECHO":
        print(ast[1])


def format_code(code):
    code=code.strip() + "\n"
    return code

# Test the language
with open("languege.py/luna.AS") as source_code: 
    for code in source_code:
        source=format_code(code)
        tokens = tokenize(source)
        #print("TOKENS:", tokens)
        ast = parse(tokens)
        #print("AST:", ast)
        interpret(ast)

