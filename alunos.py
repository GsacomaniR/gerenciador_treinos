from dados import alunos, fila_atendimento, modalidades, status_aluno
from utils import titulo
from datetime import datetime

def cadastrar_aluno():
    titulo("Cadastrar Novo Aluno")
    
    nome = input("Nome do aluno: ")
    
    print("\nModalidades disponíveis:")
    for i, modalidade in enumerate(modalidades, 1):
        print(f"{i}. {modalidade}")
    
    try:
        opcao = int(input("Escolha a modalidade (1-{}): ".format(len(modalidades))))
        modalidade = modalidades[opcao - 1]
    except (ValueError, IndexError):
        print("Opção inválida. Usando Musculação como padrão.")
        modalidade = modalidades[0]
    
    dias_semana = input("Dias por semana (ex: 3, 5, 6): ")
    
    print("\nObjetivos disponíveis:")
    objetivos = ["Perda de peso", "Ganho de massa muscular", "Condicionamento físico", "Reabilitação"]
    for i, obj in enumerate(objetivos, 1):
        print(f"{i}. {obj}")
    
    try:
        opcao_obj = int(input("Escolha o objetivo (1-4): "))
        objetivo = objetivos[opcao_obj - 1]
    except (ValueError, IndexError):
        print("Opção inválida. Usando Condicionamento físico como padrão.")
        objetivo = objetivos[2]
    
    # CRIANDO O DICIONÁRIO COM TODOS OS CAMPOS
    aluno = {
        "id": len(alunos) + 1,
        "nome": nome,
        "modalidade": modalidade,
        "dias_semana": dias_semana,
        "objetivo": objetivo,
        "status": "Ativo",  # Status inicial
        "total_sessoes": 0,
        "sessoes": []  # Pilha de sessões
    }
    
    alunos.append(aluno)
    print(f"\n✅ Aluno {nome} cadastrado com sucesso!")
    print(f"Status: {aluno['status']}")  # Agora vai funcionar
    print(f"ID do aluno: {aluno['id']}")

def listar_alunos():
    titulo("Alunos Ativos")
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    ativos = [aluno for aluno in alunos if aluno.get("status") == "Ativo"]
    
    if not ativos:
        print("Nenhum aluno ativo encontrado.")
        return
    
    for i, aluno in enumerate(ativos, 1):
        print(f"ALUNO: {i}")
        print(f"ID: {aluno['id']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Modalidade: {aluno['modalidade']}")
        print(f"Dias/Semana: {aluno['dias_semana']}")
        print(f"Objetivo: {aluno['objetivo']}")
        print(f"Status: {aluno.get('status', 'Desconhecido')}")
        print(f"Total de Sessões: {aluno.get('total_sessoes', 0)}")
        print()

def atualizar_status_aluno():
    titulo("Atualizar Status do Aluno")
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("Alunos cadastrados:")
    for aluno in alunos:
        status_emoji = "✅" if aluno.get("status") == "Ativo" else "⚠️" if aluno.get("status") == "Suspenso" else "❌"
        print(f"ID: {aluno.get('id')} - {aluno.get('nome')} - Status: {status_emoji} {aluno.get('status', 'Desconhecido')}")
    
    try:
        id_aluno = int(input("\nDigite o ID do aluno: "))
    except ValueError:
        print("Digite um número válido.")
        return
    
    for aluno in alunos:
        if aluno.get("id") == id_aluno:
            status_atual = aluno.get("status", "Ativo")
            print(f"\nStatus atual: {status_atual}")
            
            # Definir opções baseadas no status atual
            if status_atual == "Ativo":
                print("\n1 - Suspender")
                print("2 - Cancelar")
                opcao = input("Escolha: ")
                
                if opcao == "1":
                    aluno["status"] = "Suspenso"
                    print(f"✅ Aluno {aluno['nome']} foi suspenso!")
                elif opcao == "2":
                    aluno["status"] = "Cancelado"
                    print(f"✅ Aluno {aluno['nome']} foi cancelado!")
                else:
                    print("Opção inválida!")
                    
            elif status_atual == "Suspenso":
                print("\n1 - Reativar (voltar para Ativo)")
                print("2 - Cancelar")
                opcao = input("Escolha: ")
                
                if opcao == "1":
                    aluno["status"] = "Ativo"
                    print(f"✅ Aluno {aluno['nome']} foi reativado!")
                elif opcao == "2":
                    aluno["status"] = "Cancelado"
                    print(f"✅ Aluno {aluno['nome']} foi cancelado!")
                else:
                    print("Opção inválida!")
                    
            else:  # Cancelado
                print("\n⚠️ Aluno já está cancelado.")
                reativar = input("Deseja reativar o aluno? (s/n): ")
                if reativar.lower() == 's':
                    aluno["status"] = "Ativo"
                    print(f"✅ Aluno {aluno['nome']} foi reativado!")
                else:
                    print("Operação cancelada.")
            
            return
    
    print("❌ Aluno não encontrado.")

def registrar_checkin():
    titulo("Registrar Check-in de Treino")
    
    ativos = [aluno for aluno in alunos if aluno.get("status") == "Ativo"]
    
    if not ativos:
        print("Nenhum aluno ativo disponível para check-in.")
        return
    
    print("Alunos ativos:")
    for aluno in ativos:
        print(f"ID: {aluno.get('id')} - {aluno.get('nome')} - Modalidade: {aluno.get('modalidade')}")
    
    try:
        id_aluno = int(input("\nDigite o ID do aluno: "))
    except ValueError:
        print("Digite um número válido.")
        return
    
    for aluno in alunos:
        if aluno.get("id") == id_aluno and aluno.get("status") == "Ativo":
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
            
            sessao = {
                "data": data_atual,
                "modalidade": aluno.get("modalidade"),
                "duracao": input("Duração do treino (minutos): ")
            }
            
            # Garantir que as chaves existem
            if "sessoes" not in aluno:
                aluno["sessoes"] = []
            if "total_sessoes" not in aluno:
                aluno["total_sessoes"] = 0
            
            aluno["sessoes"].append(sessao)
            aluno["total_sessoes"] += 1
            
            # Adicionar à fila de atendimento
            fila_atendimento.append(aluno)
            
            print(f"\n✅ Check-in registrado para {aluno['nome']} em {data_atual}!")
            print(f"Total de sessões: {aluno['total_sessoes']}")
            return
    
    print("Aluno não encontrado ou não está ativo.")

def ver_historico_sessoes():
    titulo("Histórico de Sessões por Aluno (Mais recentes primeiro)")
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("Alunos cadastrados:")
    for aluno in alunos:
        print(f"ID: {aluno.get('id')} - {aluno.get('nome')} - Total de sessões: {aluno.get('total_sessoes', 0)}")
    
    try:
        id_aluno = int(input("\nDigite o ID do aluno: "))
    except ValueError:
        print("Digite um número válido.")
        return
    
    for aluno in alunos:
        if aluno.get("id") == id_aluno:
            sessoes = aluno.get("sessoes", [])
            if not sessoes:
                print(f"\n{aluno.get('nome')} ainda não possui sessões registradas.")
                return
            
            print(f"\nHistórico de {aluno.get('nome')} (Total: {aluno.get('total_sessoes', 0)} sessões)")
            print("=" * 40)
            
            for i, sessao in enumerate(reversed(sessoes), 1):
                print(f"Sessão {i}:")
                print(f"  Data: {sessao.get('data')}")
                print(f"  Modalidade: {sessao.get('modalidade')}")
                print(f"  Duração: {sessao.get('duracao')} minutos")
                print()
            return
    
    print("Aluno não encontrado.")

def listar_por_modalidade():
    titulo("Alunos por Modalidade")
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    for modalidade in modalidades:
        print(f"\n{modalidade.upper()}:")
        print("-" * 40)
        
        alunos_modalidade = [aluno for aluno in alunos if aluno.get("modalidade") == modalidade]
        
        if not alunos_modalidade:
            print("Nenhum aluno nesta modalidade.")
        else:
            for aluno in alunos_modalidade:
                status_emoji = "✅" if aluno.get("status") == "Ativo" else "⚠️" if aluno.get("status") == "Suspenso" else "❌"
                print(f"{status_emoji} {aluno.get('nome')} - {aluno.get('status')} - Sessões: {aluno.get('total_sessoes', 0)}")

def deletar_aluno():
    titulo("Deletar Aluno")
    
    if not alunos:
        print("Nenhum aluno cadastrado para deletar.")
        return
    
    # Listar todos os alunos com seus status
    print("Alunos cadastrados:")
    print("-" * 40)
    for aluno in alunos:
        status_emoji = "✅" if aluno.get("status") == "Ativo" else "⚠️" if aluno.get("status") == "Suspenso" else "❌"
        print(f"ID: {aluno.get('id')} | Nome: {aluno.get('nome')} | Status: {status_emoji} {aluno.get('status')}")
        print(f"    Sessões: {aluno.get('total_sessoes', 0)} | Modalidade: {aluno.get('modalidade')}")
        print()
    
    try:
        id_aluno = int(input("Digite o ID do aluno que deseja deletar: "))
    except ValueError:
        print("❌ Digite um número válido.")
        return
    
    aluno_encontrado = None
    for aluno in alunos:
        if aluno.get("id") == id_aluno:
            aluno_encontrado = aluno
            break
    
    if not aluno_encontrado:
        print(f"❌ Aluno com ID {id_aluno} não encontrado.")
        return
    
    # Mostrar dados do aluno para confirmação
    print("\n" + "=" * 40)
    print("DADOS DO ALUNO A SER DELETADO:")
    print("=" * 40)
    print(f"ID: {aluno_encontrado.get('id')}")
    print(f"Nome: {aluno_encontrado.get('nome')}")
    print(f"Modalidade: {aluno_encontrado.get('modalidade')}")
    print(f"Status: {aluno_encontrado.get('status')}")
    print(f"Total de sessões: {aluno_encontrado.get('total_sessoes', 0)}")
    print(f"Data da última sessão: {aluno_encontrado.get('sessoes', [])[-1].get('data') if aluno_encontrado.get('sessoes') else 'Nenhuma sessão'}")
    print("=" * 40)
    
    # Confirmar deleção
    confirmar = input(f"\n⚠️ Tem certeza que deseja DELETAR permanentemente o aluno '{aluno_encontrado.get('nome')}'? (s/n): ")
    
    if confirmar.lower() == 's':
        if aluno_encontrado in fila_atendimento:
            fila_atendimento.remove(aluno_encontrado)
            print("✓ Aluno removido da fila de atendimento.")
        
        # Remover da lista principal
        alunos.remove(aluno_encontrado)
        
        print(f"\n✅ Aluno '{aluno_encontrado.get('nome')}' foi deletado com sucesso!")
        print(f"Total de alunos restantes: {len(alunos)}")
    else:
        print("\n❌ Operação cancelada. Aluno NÃO foi deletado.")