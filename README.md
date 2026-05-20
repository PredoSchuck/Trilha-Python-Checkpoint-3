# 🏦 Sistema Bancário — Padrão MVC

Um sistema de simulação bancária por terminal desenvolvido em Python, aplicando rigidamente o padrão arquitetural **MVC (Model-View-Controller)** e os conceitos de **Orientação a Objetos**. 

O projeto conta com validações em tempo real de integridade de dados, interface de usuário dinâmica no terminal e herança de classes.

---
## 🏗️ Estrutura do Projeto (MVC)

O sistema foi estruturado separando as responsabilidades de forma clara e escalável:

```text
meu_projeto/
│
├── controllers/          # Cérebro do sistema (Regras de fluxo)
│   ├── __init__.py       # Atalho de inicialização do pacote
│   └── conta_controller.py
│
├── models/               # Dados e Regras de Negócio (O "O que" o sistema faz)
│   ├── __init__.py
│   ├── cliente.py
│   ├── conta.py          # Classe pai das contas
│   ├── conta_corrente.py # Herança de Conta (com taxa de saque)
│   └── conta_poupanca.py # Herança de Conta (com rendimento de juros)
│
├── views/                # Interface com o usuário (O "Como se vê")
│   ├── __init__.py
│   ├── menus.py          # Telas de menus e inputs
│   └── utilidades.py     # Funções de console e animações
│
├── config.py             # Variáveis de configuração global do banco
├── main.py               # Arquivo raiz que inicia o loop do programa
└── README.md
```

## 🚀 Funcionalidades Atuais
### Cadastro de Cliente Blindado:
* Validação de campos obrigatórios (impede strings vazias).
* Validação de formato de CPF (aceita apenas números usando .isdigit()).
* Validação de integridade do banco (impede cadastrar o mesmo CPF duas vezes).
* Validação matemática exata de maioridade (18+ anos) comparando dia, mês e ano atuais.
* Loop de cadastro persistente (caso o usuário erre um dado, o sistema exibe o erro e reinicia o formulário até o sucesso).

### Interface Dinâmica via Console:
* Alinhamentos automáticos usando F-Strings (:<41 e :^41).
* Molduras de asteriscos autoajustáveis (as bordas nunca quebram ou entortam, independente do tamanho do texto ou nome digitado).
* Efeitos visuais de carregamento passo a passo (time.sleep) e limpeza universal de console.

### Modelagem de Contas via Orientação a Objetos:
* Estrutura de herança com Conta Corrente e Conta Poupança compartilhando atributos da classe base Conta.

## 🛠️ Tecnologias Utilizadas
Python 3.10+ (Uso extensivo de estruturas avançadas como match/case para navegação de menus).

Biblioteca Nativa datetime para processamento cronológico preciso.

Biblioteca Nativa os adaptada para compatibilidade multiplataforma (Windows, Linux e macOS).

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado no seu computador.
2. Clone ou faça o download das pastas deste repositório.
3. Abra o seu terminal e navegue até a pasta raiz do projeto.
4. Digite o seguinte comando e pressione ENTER:

```
python main.py
```

## 📝 Configurações Globais (config.py)
As regras financeiras do banco são centralizadas e podem ser alteradas a qualquer momento:

* TAXA_SAQUE: Valor fixo flutuante cobrado por cada saque efetuado na Conta Corrente.
* JUROS_POUPANCA: Taxa percentual de rendimento mensal aplicada ao saldo da Poupança.