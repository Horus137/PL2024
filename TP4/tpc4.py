import ply.lex as lex
import sys

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'NUMBER',
    'OPERATOR',
    'COMMA',
)

def t_SELECT(t):
    r'(?i)\bSelect\b'
    return t

def t_FROM(t):
    r'(?i)\bFrom\b'
    return t

def t_WHERE(t):
    r'(?i)\bWhere\b'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OPERATOR(t):
    r'[><=]+'
    return t

def t_COMMA(t):
    r','
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

consulta = "Select id, nome, salario From empregados Where salario >= 820"

lexer.input(consulta)
while True:
    token = lexer.token()
    if not token:
        break
    print(token)