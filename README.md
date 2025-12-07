# Identifier - Validador de Identificadores

Projeto simples pra validar se uma string é um identificador válido seguindo as regras básicas de nomenclatura de variáveis.

## O que faz

Basicamente checa se o identificador segue essas regras:

- Tem que começar com letra (A-Z ou a-z)
- Só pode ter letras e números
- Tamanho entre 1 e 6 caracteres

Se passar em tudo, retorna `True`. Se falhar em qualquer coisa, retorna `False`.

## Como funciona a validação

### Casos Válidos
- `a` → válido (1 char, mínimo permitido)
- `a123` → válido (letra + números)
- `a12345` → válido (6 chars, máximo permitido)
- `Abc123` → válido (maiúsculas também funcionam)

### Casos Inválidos
- `` (vazio) → precisa ter pelo menos 1 caractere
- `a123456` → passou do limite de 6
- `123abc` → não pode começar com número
- `@abc` → não pode começar com caractere especial
- `a@123` → não pode ter caractere especial no meio
- `_test` → underscore não é permitido

## Testes

Criei 7 casos de teste pra cobrir todos os cenários importantes:

**TC1** - `a123` deve passar (caso normal)  
**TC2** - `123` deve falhar (começa com número)  
**TC3** - `@abc` deve falhar (começa com especial)  
**TC4** - `a12345` deve passar (limite máximo OK)  
**TC5** - `a123456` deve falhar (estourou o limite)  
**TC6** - `a` deve passar (limite mínimo OK)  
**TC7** - `a@123` deve falhar (caractere especial no meio)  

Os testes cobrem tanto os casos normais quanto os limites (boundaries) e as entradas inválidas.

## Rodando os testes

Precisa ter Python 3 e o pytest instalado:

```bash
pip install pytest coverage
```

Pra rodar:

```bash
pytest
```

Pra ver a cobertura:

```bash
coverage run -m pytest
coverage report
```

### Cobertura

Consegui 100% de cobertura nos testes - todas as linhas do código são executadas pelos casos de teste.

```
Name                       Stmts   Miss  Cover
----------------------------------------------
identifier\Identifier.py      14      0   100%
test\test_identifier.py       16      0   100%
----------------------------------------------
TOTAL                         30      0   100%
```

## Estrutura do projeto

```
.
├── identifier/
│   └── Identifier.py    # código principal
├── test/
│   └── test_identifier.py    # testes
└── README.md
```

---