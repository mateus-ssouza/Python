from models.cliente import Cliente
from models.conta import Conta


jorge: Cliente = Cliente('Jorge Sousa', 'jorge@gmail.com', '123.456.789-01', '02/09/1987')
angela: Cliente = Cliente('Angela Braga', 'angelbraga@gmail.com', '234.567.890-02', '08/07/1978')

print(jorge)
print(angela)


contaf: Conta = Conta(jorge)
contaa: Conta = Conta(angela)

print(contaf)
print(contaa)
