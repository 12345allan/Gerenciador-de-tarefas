# 🧠 Gerenciador de Tarefas em Python

Este é um projeto simples de gerenciador de tarefas feito em Python, com interface de texto no terminal. Ele permite adicionar, visualizar, atualizar, completar e deletar tarefas de forma prática e intuitiva.

## 🚀 Funcionalidades

- ✅ Adicionar novas tarefas  
- 📋 Visualizar lista de tarefas com status  
- ✏️ Atualizar o nome de uma tarefa  
- ✔️ Marcar tarefas como completadas  
- 🗑️ Deletar tarefas que já foram concluídas  
- 🔁 Menu interativo para navegação  

## 💻 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/AllanDevX/gerenciador-tarefas.git
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd gerenciador-tarefas
   ```

3. Execute o script:
   ```bash
   python gerenciador.py
   ```

## 📂 Estrutura do Projeto

```
gerenciador-tarefas/
│
├── gerenciador.py        # Código principal com menu e funções
└── README.md             # Documentação do projeto
```

## 🧠 Lógica do Código

O projeto é dividido em funções que cuidam de cada ação:

- `adicionar_tarefa()`: adiciona uma nova tarefa à lista  
- `ver_tarefas()`: exibe todas as tarefas com status  
- `atualizar_tarefa()`: altera o nome de uma tarefa existente  
- `completar_tarefa()`: marca uma tarefa como concluída  
- `deletar_completadas()`: remove tarefas que já foram concluídas  
- `menu()`: interface interativa que conecta todas as funções  

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- Terminal / Console  

## 📌 Próximos Passos

- [ ] Salvar tarefas em arquivo `.json` ou `.txt`  
- [ ] Criar interface gráfica com Tkinter  
- [ ] Transformar em API com Flask (versão futura)  

## 📣 Autor

Desenvolvido por Allan — apaixonado por código limpo e soluções práticas.  
🔗 GitHub: [AllanDevX](https://github.com/AllanDevX)

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.