# Sistema de Nutrição em Python

Aplicação em linha de comando desenvolvida em Python para cadastro de pacientes, cálculo de IMC e estimativa de gasto energético diário com base na equação de Harris-Benedict.

## Sobre o projeto

Este sistema foi desenvolvido com o objetivo de aplicar conceitos de programação à área da nutrição, permitindo realizar avaliações básicas de pacientes de forma simples, rápida e organizada.

O projeto integra lógica de programação, validação de dados e cálculos nutricionais, simulando um pequeno sistema utilizado em contextos clínicos ou acadêmicos.

## Funcionalidades

- Cadastro de pacientes com validação de dados
- Armazenamento das informações utilizando listas e dicionários
- Cálculo do IMC (Índice de Massa Corporal)
- Classificação do IMC conforme parâmetros padrão
- Cálculo de gasto energético basal (Harris-Benedict)
- Ajuste calórico diário com base no nível de atividade física
- Interface interativa via terminal
- Uso de cores para melhor experiência do usuário
- Limpeza automática de tela

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão `os`

## Fórmulas utilizadas

### IMC (Índice de Massa Corporal)

IMC = peso (kg) / altura² (m)

### Equação de Harris-Benedict (Taxa metabólica basal)

**Mulheres:**

TMB = 655 + (9.6 × peso) + (1.8 × altura_cm) - (4.7 × idade)

**Homens:**

TMB = 66 + (13.7 × peso) + (5 × altura_cm) - (6.8 × idade)

### Fatores de atividade física

| Nível      | Fator |
| ---------- | ----- |
| Sedentário | 1.12  |
| Leve       | 1.2   |
| Moderado   | 1.3   |
| Intenso    | 1.55  |

## Como executar o projeto

1. Clone o repositório
2. Acesse a pasta do projeto
3. Execute o arquivo no terminal
python app_nutrition.py

## Objetivo do projeto

Este projeto foi desenvolvido a fins de estudo e prática, visando:
- Praticar lógica de programação e uso de funções em Python
- Aplicar conceitos de validação de dados
- Integrar conhecimentos da área da nutrição com tecnologia
- Criar um projeto funcional para portfólio

## Autora

Desenvolvido por **Alyssa Moutinho**

