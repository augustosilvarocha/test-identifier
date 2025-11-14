from identifier.Identifier import Identifier

identifier = Identifier()

def test_identificador_valido():
    assert identifier.validate_identifier("a123") == True

def test_identificador_inicia_com_digito():
    assert identifier.validate_identifier("123") == False

def test_identificador_inicia_com_caractere_especial():
    assert identifier.validate_identifier("@abc") == False

def test_identificador_limite_superior():
    assert identifier.validate_identifier("a12345") == True

def test_identificador_acima_limite():
    assert identifier.validate_identifier("a123456") == False

def test_identificador_limite_inferior():
    assert identifier.validate_identifier("a") == True

def test_identificador_contem_caractere_especial():
    assert identifier.validate_identifier("a@123") == False
