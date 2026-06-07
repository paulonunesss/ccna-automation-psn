"""
=====================================================================
 CCNA Automation - Script de Teste
=====================================================================

 Descricao:
   Este e apenas um script de TESTES, criado com o objetivo de
   praticar conceitos da prova CCNA voltados para automacao de redes.

   Importante: este e o meu PRIMEIRO script Python feito com o
   auxilio da Inteligencia Artificial do Claude (Anthropic), como
   parte do meu aprendizado e do meu primeiro repositorio no GitHub.

 Autor : Paulo Sergio
 Data  : 07/06/2026
=====================================================================
"""


# Lista simples de dispositivos de rede (simulacao de inventario)
dispositivos = [
    {"hostname": "R1", "tipo": "Roteador", "ip": "192.168.1.1"},
    {"hostname": "SW1", "tipo": "Switch", "ip": "192.168.1.2"},
    {"hostname": "SW2", "tipo": "Switch", "ip": "192.168.1.3"},
]


def listar_dispositivos(lista):
    """Exibe na tela todos os dispositivos do inventario."""
    print("=" * 45)
    print("INVENTARIO DE DISPOSITIVOS DE REDE")
    print("=" * 45)
    for i, dispositivo in enumerate(lista, start=1):
        print(f"{i}. {dispositivo['hostname']} "
              f"({dispositivo['tipo']}) - IP: {dispositivo['ip']}")
    print("=" * 45)


def gerar_comando_ping(ip):
    """Gera um comando de ping simples para testar conectividade."""
    return f"ping {ip}"


def main():
    print("Iniciando script de teste de automacao CCNA...\n")

    listar_dispositivos(dispositivos)

    print("\nComandos de teste de conectividade (ping):")
    for dispositivo in dispositivos:
        comando = gerar_comando_ping(dispositivo["ip"])
        print(f"  {dispositivo['hostname']}: {comando}")

    print("\nScript finalizado com sucesso! :)")


if __name__ == "__main__":
    main()
