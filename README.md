# Identifier – Validador de Identificadores

Um projeto simples para validar se uma string (identificador) segue um conjunto de regras de nomenclatura pré-definidas.

---

## 1. Descrição do Problema

O programa `Identifier` tem como objetivo verificar se um identificador é válido seguindo regras específicas de nomenclatura usadas em linguagens de programação.

Um identificador é considerado **válido** se atender a todos os seguintes critérios:

| Critério | Regra |
| :--- | :--- |
| **Início** | Deve começar com uma letra (A–Z ou a–z). |
| **Conteúdo** | Pode conter apenas letras (A–Z, a–z) ou dígitos (0–9). |
| **Comprimento** | Deve ter entre **1 e 6 caracteres** (inclusive). |

A função de validação retorna `True` (identificador válido) ou `False` (identificador inválido).

---

## 2. Análise e Definição de Testes (Passo a Passo)

A análise foi realizada identificando-se os três principais critérios de validação (Comprimento, Início e Conteúdo) e, em seguida, definindo-se classes de equivalência e valores limites para cada critério.

### Passo A: Classes de Equivalência

Definimos classes válidas e inválidas para cobrir todas as possibilidades de entrada, garantindo que o programa se comporte corretamente, inclusive nos casos de erro (CE4 a CE8).

| Categoria | ID | Descrição | Regra Coberta |
| :--- | :--- | :--- | :--- |
| **Válida** | **CE1** | 1 caractere (Apenas letra). | Limite mínimo de comprimento. |
| **Válida** | **CE2** | Entre 2 e 5 caracteres (Letra + letras/dígitos). | Intervalo válido de comprimento. |
| **Válida** | **CE3** | 6 caracteres (Limite máximo de comprimento). | Limite máximo de comprimento. |
| **Inválida** | CE4 | Identificador vazio (0 caracteres). | Comprimento abaixo do limite. |
| **Inválida** | CE5 | Mais de 6 caracteres. | Comprimento acima do limite. |
| **Inválida** | CE6 | Inicia com dígito. | Falha no critério de "Início". |
| **Inválida** | CE7 | Inicia com caractere especial (`@`, `_`, etc.). | Falha no critério de "Início". |
| **Inválida** | CE8 | Contém caractere especial no meio. | Falha no critério de "Conteúdo" (caracteres permitidos). |

### Passo B: Análise de Valores Limite

Os valores limites foram focados no critério de **Comprimento** (1 a 6), que é o mais quantificável. O teste garante que o sistema não falhe exatamente nos extremos:

| Valor | Comprimento | Resultado Esperado | Justificativa |
| :--- | :--- | :--- | :--- |
| **0** | **Vazio** | Inválido | Abaixo do limite inferior (CE4). |
| **1** | **Mínimo** | Válido | No limite inferior (CE1). |
| **6** | **Máximo** | Válido | No limite superior (CE3). |
| **7** | **Excedente** | Inválido | Acima do limite superior (CE5). |

---

## 3. Tabela de Casos de Teste

A tabela finaliza o processo de análise, mapeando uma entrada específica para cada classe de equivalência e valor limite definidos.

| ID | Entrada | Resultado Esperado | Classe de Equivalência |
| :--- | :--- | :--- | :--- |
| TC1 | `a123` | **True** | CE2 (Válido) |
| TC2 | `123` | **False** | CE6 (Inicia com dígito) |
| TC3 | `@abc` | **False** | CE7 (Inicia com especial) |
| TC4 | `a12345` | **True** | CE3 (Válido, limite superior) |
| TC5 | `a123456` | **False** | CE5 (Acima do limite) |
| TC6 | `a` | **True** | CE1 (Válido, limite inferior) |
| TC7 | `a@123` | **False** | CE8 (Contém especial) |

---

## 4. Instruções de Execução Local dos Testes

### Requisitos

* **Python 3** instalado (preferencialmente 3.6+).
* **`pytest`** instalado.

### Passo a Passo

1.  **Instalar dependências (se necessário):**
    ```bash
    pip install pytest
    ```

2.  **Executar os testes:**
    A partir do diretório raiz do projeto (`Identifier/`), execute o comando `pytest`:
    ```bash
    pytest
    ```
