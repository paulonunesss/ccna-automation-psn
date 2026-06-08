"""
=====================================================================
 CCNA Automation - Inventario de Rede (versao melhorada)
=====================================================================

 Descricao:
   Evolucao do meu primeiro script de testes. Aqui transformei o
   inventario simples em um pequeno programa interativo com menu,
   validacao de IP e geracao de comandos de teste de conectividade.

   Continua sendo um projeto de APRENDIZADO, focado em praticar
   conceitos de automacao de redes (CCNA) com Python.

 Autor : Paulo Sergio Nunes da Silva
 Data  : 08/06/2026
 SO    : Linux Zorin OS 18
=====================================================================
"""

from dataclasses import dataclass, field


# ---------------------------------------------------------------------
# Modelo de dados
# ---------------------------------------------------------------------
@dataclass
class Dispositivo:
    """Representa um dispositivo de rede do inventario."""
    hostname: str
    tipo: str
    ip: str

    def comando_ping(self, repeticoes: int = 4) -> str:
        """Gera o comando de ping para testar a conectividade."""
        return f"ping -c {repeticoes} {self.ip}"

    def __str__(self) -> str:
        return f"{self.hostname} ({self.tipo}) - IP: {self.ip}"


@dataclass
class Inventario:
    """Colecao de dispositivos com operacoes basicas de gerenciamento."""
    dispositivos: list = field(default_factory=list)

    def adicionar(self, dispositivo: Dispositivo) -> None:
        self.dispositivos.append(dispositivo)

    def listar(self) -> None:
        linha = "=" * 50
        print(linha)
        print("INVENTARIO DE DISPOSITIVOS DE REDE".center(50))
        print(linha)
        if not self.dispositivos:
            print("Nenhum dispositivo cadastrado.")
        else:
            for i, dispositivo in enumerate(self.dispositivos, start=1):
                print(f"{i:>2}. {dispositivo}")
        print(linha)

    def total(self) -> int:
        return len(self.dispositivos)


# ---------------------------------------------------------------------
# Funcoes auxiliares
# ---------------------------------------------------------------------
def ip_valido(ip: str) -> bool:
    """Validacao simples de um endereco IPv4 (4 octetos de 0 a 255)."""
    octetos = ip.split(".")
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        if not octeto.isdigit():
            return False
        if not 0 <= int(octeto) <= 255:
            return False
    return True


def carregar_inventario_padrao() -> Inventario:
    """Cria um inventario de exemplo (simulacao de rede CCNA)."""
    inventario = Inventario()
    inventario.adicionar(Dispositivo("R1", "Roteador", "192.168.1.1"))
    inventario.adicionar(Dispositivo("SW1", "Switch", "192.168.1.2"))
    inventario.adicionar(Dispositivo("SW2", "Switch", "192.168.1.3"))
    return inventario


def gerar_testes_ping(inventario: Inventario) -> None:
    """Mostra os comandos de ping para todos os dispositivos."""
    print("\nComandos de teste de conectividade (ping):")
    if inventario.total() == 0:
        print("  Inventario vazio - nada a testar.")
        return
    for dispositivo in inventario.dispositivos:
        print(f"  {dispositivo.hostname:<6} -> {dispositivo.comando_ping()}")


def adicionar_dispositivo_interativo(inventario: Inventario) -> None:
    """Permite ao usuario cadastrar um novo dispositivo via terminal."""
    print("\n--- Novo dispositivo ---")
    hostname = input("Hostname: ").strip()
    tipo = input("Tipo (Roteador/Switch/etc): ").strip()
    ip = input("Endereco IP: ").strip()

    if not hostname or not tipo:
        print("Hostname e tipo nao podem ficar vazios. Operacao cancelada.")
        return
    if not ip_valido(ip):
        print(f"IP invalido: '{ip}'. Operacao cancelada.")
        return

    inventario.adicionar(Dispositivo(hostname, tipo, ip))
    print(f"Dispositivo '{hostname}' adicionado com sucesso!")


# ---------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------
def mostrar_menu() -> None:
    print("\n" + "-" * 50)
    print("MENU - AUTOMACAO CCNA")
    print("-" * 50)
    print("1 - Listar dispositivos")
    print("2 - Adicionar dispositivo")
    print("3 - Gerar comandos de ping")
    print("0 - Sair")


def main() -> None:
    print("Iniciando inventario de automacao CCNA...\n")
    inventario = carregar_inventario_padrao()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            inventario.listar()
        elif opcao == "2":
            adicionar_dispositivo_interativo(inventario)
        elif opcao == "3":
            gerar_testes_ping(inventario)
        elif opcao == "0":
            print("\nEncerrando... Script finalizado com sucesso! :)")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
print("Welcome to the world of CCNA Automation with Python! 🚀")