<div align="center">

# 🧠 Bayesian Customer Intelligence (BCI)

  <p align="center">
    <strong>Modelo Probabilístico de Inferência de Intenção de Compra em E-Commerce</strong>
  </p>

  <!-- BADGES / SHIELDS -->
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3873A9?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge" alt="Status" />
    <img src="https://img.shields.io/badge/AI%20%26%20Data-Bayesian-FF6F00?style=for-the-badge" alt="Bayesian" />
  </p>

</div>

---

> [!NOTE]
> **Contexto do Projeto:**  
> Projeto desenvolvido durante o programa **Tech Builder**, focado na implementação prática de **Redes Bayesianas** para tomada de decisão em sistemas de e-commerce.

---

## 📖 Contexto e Problema de Negócio

Em plataformas de e-commerce, identificar a **propensão de compra** de um usuário em tempo real permite personalizar ofertas, ativar gatilhos de retenção e otimizar campanhas de marketing. 

Este projeto constrói um **Modelo de Inferência Bayesiana** simples que calcula a probabilidade de um cliente finalizar uma compra ($P(\text{Compra})$) com base em seu comportamento imediato de navegação no site.

---

## 🕸️ Estrutura da Rede Bayesiana

A rede avalia como três variáveis de entrada (**Evidências**) influenciam a variável dependente alvo (**Compra**):

```mermaid
graph TD
    A[📜 Histórico de Compras] -->|Impacto| D{🛒 Decisão de Compra}
    B[⏱️ Tempo no Site] -->|Impacto| D
    C[🏷️ Clicou em Promoção] -->|Impacto| D

    style A fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff
    style B fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff
    style C fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff
    style D fill:#0f172a,stroke:#22c55e,stroke-width:3px,color:#fff
