from array import array


var={
    
}

class main():
    def __init__(self, array:list, current_letter_with_index:tuple) -> None:
        self.current_letter_with_index = current_letter_with_index
        self.array                     = array


def error(type):
    return

# Lexer
def tokenize(sc):
    tokens = []
    for i, c in enumerate(sc):
        m=main(sc, (i, c))

        if sc[i:5].strip() == "print":
            new_i, new_c=(i+5, sc[i+5])
            tokens.append(("PRINT", "print"))
            end           = sc.find('\n')
            strings       = sc[new_i:end]
            if strings != '':
                strings=strings.split()
                new_string=[]
                for string in strings:
                    if string.startswith("-") and string.endswith("-"): 
                        try:    string=var[string]
                        except: return error("NO VAR IN PRINT")
                    new_string.append(string)
                tokens.append(("STRING", new_string))
                i = end
        

        elif sc[i:4].strip() == "mvar":
            new_i, new_c=(i+4, sc[i+4])
            tokens.append(("MVAR", "mvar"))
            end           = sc.find('\n')
            var_args      = sc[new_i:end].strip()
            if var_args != '':
                split_var_args=var_args.split()
                if len(split_var_args) < 2: return error("VAR ARGS SHORT")
                if len(split_var_args) > 2: return error("VAR ARGS LARGE")
                tokens.append(("MVAR_ARG1", "-"+split_var_args[0]+ "-"))
                tokens.append(("MVAR_ARG2", split_var_args[1]))
                i = end
        
        elif c == "\n":
            tokens.append(("NL", "\n"))

    return tokens

# Parser
def parse(tokens):
    def parse_expression():
        index = 0
        if tokens[index][0] == "PRINT":
            index += 1
            string = " ".join(tokens[index][1])
            index += 1
            if tokens[index][0] == "NL":
                index += 1
                return ("PRINT", string)
        elif tokens[index][0] == "MVAR":
            index += 1
            variable = tokens[index][1]
            index += 1
            value = tokens[index][1]
            index += 1
            return ("MVAR", variable, value)
        
        return None
    return parse_expression()     

# Interpreter
def interpret(ast):
    if ast[0] == "PRINT":
        print(ast[1])
    elif ast[0] == "MVAR":
        variable = ast[1]
        value = ast[2]
        # Add the variable and value to a dictionary of variables
        var[variable] = value
        
def format_code(code):
    code=code.strip() + " \n"
    return code

# Test the language
with open("main.lunar") as source_code: 
    for code in source_code:
        source=format_code(code)
        tokens=tokenize   (source)
        if tokens is not None:
            #print            (tokens)
            ast   =parse      (tokens)
            #print            (ast)
            interpret         (ast)
