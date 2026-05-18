# CRM — SISTEMA DE GESTÃO DE CLIENTES
## Lummé Agência Criativa

**Versão:** 1.0 | **Data:** Maio 2026 | **Uso:** Interno Lummé

---

## 1. VISÃO GERAL DO CRM

O CRM da Lummé é o sistema central de controle de toda a jornada do cliente — da prospecção ao pós-venda. Registra cada contato, proposta, contrato, entrega e resultado.

**Ferramenta recomendada:** Notion (gratuito/Plus) como base + planilha de controle em Excel/Google Sheets

---

## 2. PIPELINE DE VENDAS

### Estágios do Funil

| # | Estágio | Descrição | Prazo médio |
|---|---------|-----------|-------------|
| 1 | **Prospect** | Lead identificado, ainda sem contato. Foco em profissional liberal com 5–20 anos de carreira e presença digital inadequada (advogado, arquiteto, médico, consultor) | — |
| 2 | **Primeiro Contato** | Mensagem ou ligação inicial realizada | D+0 |
| 3 | **Qualificado** | Prospect respondeu e demonstrou interesse | D+3 |
| 4 | **Reunião Agendada** | Reunião de diagnóstico marcada | D+7 |
| 5 | **Diagnóstico Realizado** | Reunião feita, dor mapeada | D+10 |
| 6 | **Proposta Enviada** | Proposta comercial enviada | D+12 |
| 7 | **Negociação** | Cliente revisando, questionamentos | D+15 |
| 8 | **Contrato Assinado** | Fechado — entrar no onboarding | D+21 |
| 9 | **Perdido** | Não converteu — registrar motivo | — |

### Métricas do Pipeline

| Métrica | Meta mensal |
|---------|-------------|
| Prospects novos | ≥ 40 |
| Primeiros contatos | ≥ 30 |
| Reuniões realizadas | ≥ 15 |
| Propostas enviadas | ≥ 10 |
| Contratos fechados | 3–5 |
| Taxa de conversão geral | ≥ 10% |
| Ticket médio | R$ 3.500–8.000 |

---

## 3. FICHA DE PROSPECT / CLIENTE

```
======================================================
FICHA DE CONTATO — LUMMÉ CRM
======================================================
ID: [LP-001]
Data de entrada: [DD/MM/AAAA]
Status no pipeline: [Estágio]
Responsável: Quellem

---
DADOS DO CONTATO
Nome: _______________________________________________
Empresa: ____________________________________________
Segmento: ___________________________________________
Cargo: ______________________________________________
WhatsApp: ___________________________________________
E-mail: _____________________________________________
Instagram: __________________________________________
LinkedIn: ___________________________________________
Cidade/UF: __________________________________________
CNPJ: ______________________________________________

---
QUALIFICAÇÃO (BANT)
Budget — Orçamento disponível: [R$ ]
Authority — Quem decide: [Nome + cargo]
Need — Principal dor: ___________________________________
Timeline — Urgência: [Imediata / 30 dias / 60 dias / Indefinida]

---
HISTÓRICO DE INTERAÇÕES
[DD/MM] Canal: _____ Ação: _____ Resultado: _____________
[DD/MM] Canal: _____ Ação: _____ Resultado: _____________
[DD/MM] Canal: _____ Ação: _____ Resultado: _____________

---
PROPOSTA
Data de envio: _______________
Serviço proposto: _______________
Valor proposto: R$ _______________
Status: [Enviada / Em análise / Aprovada / Recusada]
Motivo da recusa (se aplicável): _______________

---
CONTRATO (quando fechado)
Data de assinatura: _______________
Valor mensal: R$ _______________
Vigência: _______________ a _______________
Renovação automática: [Sim / Não]
Vencimento: Dia ___ de cada mês

---
NOTAS E OBSERVAÇÕES
___________________________________________________
___________________________________________________
======================================================
```

---

## 4. DASHBOARD DE CLIENTES ATIVOS

### Tabela de Controle Mensal

| Cliente | Segmento | Pacote | Valor/mês | Início | Renovação | Status | NPS |
|---------|----------|--------|-----------|--------|-----------|--------|-----|
| [Nome] | [Seg.] | [Pacote] | R$ | [mês] | [mês] | Ativo | [nota] |

### Status Possíveis

| Status | Significado | Ação |
|--------|-------------|------|
| **Ativo** | Contrato vigente, entregas em dia | Manter SLA |
| **Em risco** | Atrasos, feedbacks negativos, pouco engajamento | Reunião urgente |
| **Inadimplente** | Pagamento em atraso > 5 dias | Notificação formal |
| **Renovando** | Contrato vencendo em até 30 dias | Proposta de renovação |
| **Encerrado** | Contrato finalizado | Off-boarding + pesquisa |
| **Pausado** | Serviço suspenso (mútuo acordo) | Protocolo de pausa |

---

## 5. CONTROLE DE PAGAMENTOS

### Calendário de Recebimentos

| Cliente | Vencimento | Valor | Forma | Status | Data recebido |
|---------|-----------|-------|-------|--------|---------------|
| [Nome] | Dia [X] | R$ | Pix | [Pago/Pendente/Atrasado] | [Data] |

### Régua de Cobrança

| Dia | Ação |
|-----|------|
| **D-2** | Lembrete automático por WhatsApp: "Amanhã vence sua mensalidade Lummé." |
| **D+0** | Vencimento — aguardar até às 18h |
| **D+1** | Follow-up WhatsApp informal: "Oi [Nome], passou alguma coisa com o pagamento?" |
| **D+3** | E-mail formal com dados bancários |
| **D+5** | Notificação de suspensão de entregas + multa contratual |
| **D+10** | Verificar rescisão ou acordo de parcelamento |
| **D+30** | Encaminhamento para cobrança formal (se necessário) |

### Mensagem WhatsApp D-2

```
Oi [Nome]! Quellem da Lummé aqui.
Passando pra lembrar que sua mensalidade vence em [data].
Valor: R$ [valor] | Pix: [chave]
Qualquer dúvida, me chama!
```

---

## 6. CONTROLE DE ENTREGAS

### Calendário de Entregas por Cliente

| Cliente | Entregável | Prazo | Status | Data entregue | Aprovação |
|---------|-----------|-------|--------|---------------|-----------|
| [Nome] | Relatório Mensal | Dia 5 | [Em prod./Pronto/Entregue] | [Data] | [Aprovado/Revisão] |
| [Nome] | Calendário maio | 25/04 | | | |

### Status de Entregável

| Status | Descrição |
|--------|-----------|
| **Planejado** | No calendário, ainda não iniciado |
| **Em produção** | Sendo criado pela Lummé |
| **Em revisão** | Checagem interna |
| **Aguardando aprovação** | Enviado ao cliente, pendente de OK |
| **Em ajuste** | Cliente solicitou alteração |
| **Entregue** | Aprovado e publicado/enviado |
| **Atrasado** | Passou do prazo sem entrega |

---

## 7. GESTÃO DE FOLLOW-UP

### Frequência de Contato por Estágio

| Estágio | Frequência | Canal | Template |
|---------|-----------|-------|---------|
| Prospect (sem resposta) | A cada 5 dias, até 3 tentativas | WhatsApp + e-mail | Script de prospecção |
| Qualificado (negociação) | A cada 3 dias | WhatsApp | Script de follow-up |
| Proposta enviada (sem resposta) | D+2, D+5, D+10 | WhatsApp + e-mail | Script de follow-up proposta |
| Cliente ativo | Mensal (reunião) + semanal (status) | Reunião + WhatsApp | Relatório mensal |
| Encerrado | 30 dias, 90 dias, 180 dias | E-mail | Script de reativação |

### Templates de Follow-up

**Follow-up pós-reunião (D+2)**
```
Oi [Nome]! Quellem aqui.

Que bom que conversamos [dia]! Fico pensando na oportunidade que identificamos
para [área da dor discutida].

Gostaria de saber se teve tempo de revisar a proposta. Tenho disponibilidade
para alinhar detalhes antes de você decidir.

Como prefere: por aqui mesmo ou agendar uma conversa rápida?
```

**Follow-up pós-proposta sem resposta (D+5)**
```
Oi [Nome]! Quellem da Lummé.

Deixa eu verificar se a proposta chegou sem problemas — às vezes o e-mail
cai no spam.

Se precisar de ajuste no formato, valor ou escopo, pode me falar com
tranquilidade.

Estou aqui para resolver.
```

**Reativação (cliente encerrado, 90 dias)**
```
Assunto: [Nome], uma novidade que pode ser relevante para você

Oi [Nome]!

Faz um tempo que não conversamos e pensei em você ao ver [insight do
segmento do cliente].

Estamos com novidades no [serviço] que podem fazer sentido para o momento
atual da [Empresa]. Vale uma conversa de 15 minutos?
```

---

## 8. RELATÓRIO SEMANAL DO CRM

Preencher toda sexta-feira:

```
SEMANA: [DD/MM a DD/MM]

PROSPECÇÃO
· Novos prospects: ___
· Primeiros contatos: ___
· Respostas recebidas: ___

PIPELINE
· Reuniões realizadas: ___
· Propostas enviadas: ___
· Contratos fechados: ___
· Perdas: ___ (motivo: ___)

CLIENTES ATIVOS
· Total de clientes: ___
· Em risco: ___
· Inadimplentes: ___
· Renovações próximas: ___

FINANCEIRO DA SEMANA
· Receita recebida: R$ ___
· Pagamentos pendentes: R$ ___
· Previsão próxima semana: R$ ___

AÇÕES PRIORITÁRIAS DA PRÓXIMA SEMANA
1. _______________
2. _______________
3. _______________
```

---

## 9. MÉTRICAS DO CRM — METAS MENSAIS

| Métrica | Meta | Como medir |
|---------|------|-----------|
| Novos prospects/mês | ≥ 40 | Fichas criadas no estágio 1 |
| Taxa de conversão prospect → reunião | ≥ 40% | Reuniões ÷ primeiros contatos |
| Taxa de conversão reunião → proposta | ≥ 80% | Propostas ÷ reuniões |
| Taxa de conversão proposta → contrato | ≥ 40% | Contratos ÷ propostas |
| Churn mensal | ≤ 5% | Clientes perdidos ÷ total ativo |
| NPS médio | ≥ 8,5/10 | Pesquisa mensal com clientes |
| MRR (Receita recorrente mensal) | Meta por fase | Ver Financeiro |
| Tempo médio de fechamento | ≤ 21 dias | Data 1º contato → assinatura |

---

## 10. PROCESSOS DE OFF-BOARDING

Quando um cliente encerra o contrato:

- [ ] Confirmar data de encerramento e última entrega
- [ ] Entregar todos os arquivos e acessos de volta
- [ ] Revogar acessos da Lummé às plataformas do cliente
- [ ] Enviar pesquisa de NPS e satisfação
- [ ] Registrar motivo do encerramento no CRM
- [ ] Agendar follow-up de reativação para 90 dias
- [ ] Solicitar depoimento (Google, Instagram, LinkedIn)

### E-mail de Encerramento

```
Assunto: Obrigada pela parceria, [Nome]

Olá, [Nome]!

É com respeito e gratidão que encerramos nossa parceria hoje.

Até o dia [data] você receberá:
· Todos os arquivos criados durante a parceria
· Relatório final com resultados do período

Devolvemos os acessos fornecidos até [data].

Adoraria saber sua opinião sobre o nosso trabalho. Se puder responder
3 perguntas rápidas: [link da pesquisa]

Quando precisar de presença digital com estratégia, estarei aqui.

Quellem | Lummé
```

---

---

*Lummé · MADU Gestão Empresarial LTDA · @lummeagenciacriativa · contato@lummeagencia.com.br · www.lummeagencia.com.br · (27) 99884-5482*
*Cada detalhe importa.*
