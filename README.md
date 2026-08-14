<div align="center">

# 🧠 Bayesian Customer Intelligence (BCI)

  <p align="center">
    <strong>Modelo Probabilístico de Inferência de Intenção de Compra em E-Commerce</strong>
  </p>

  <!-- BADGES / SHIELDS -->
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.8%2B-3873A9?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge" alt="Status" />
    <img src="https://img.shields.io/badge/AI%20%26%20Data-Bayesian%20Inference-FF6F00?style=for-the-badge" alt="Bayesian" />
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
  </p>

</div>

---

> [!NOTE]
> **Contexto do Projeto:**  
> Projeto desenvolvido durante o programa **Tech Builder**, focado na aplicação prática de **Redes Bayesianas** para apoio à tomada de decisão em sistemas de e-commerce e análise de dados comportamentais.

---

## 📖 Contexto e Problema de Negócio

Em plataformas digitais de alto tráfego, estimar a **propensão de conversão** de um usuário em tempo real é fundamental para:
* 🎯 **Personalização de Ofertas:** Ativar banners ou cupom de desconto em tempo real para usuários com dúvida.
* ⚡ **Retenção Ativa:** Disparar gatilhos de engajamento antes que o usuário abandone a sessão.
* 📈 **Otimização de Marketing:** Direcionar campanhas para perfis com alta probabilidade de fechamento.

Este projeto consolida um **Modelo de Inferência Bayesiana** em Python que calcula de forma determinística a probabilidade condicional de um cliente finalizar uma compra ($P(\text{Compra})$) com base no seu histórico e comportamento de navegação instantâneo.

---

## 🕸️ Estrutura da Rede Bayesiana

A arquitetura da rede modela a dependência entre três variáveis observáveis (**Evidências**) e o evento de interesse (**Variável Alvo**):

```mermaid
graph TD
    A[📜 Histórico de Compras] -->|Impacto Condicional| D{🛒 Decisão de Compra}
    B[⏱️ Tempo no Site] -->|Impacto Condicional| D
    C[🏷️ Clicou em Promoção] -->|Impacto Condicional| D

    style A fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff
    style B fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff
    style C fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff
    style D fill:#0f172a,stroke:#22c55e,stroke-width:3px,color:#fff
