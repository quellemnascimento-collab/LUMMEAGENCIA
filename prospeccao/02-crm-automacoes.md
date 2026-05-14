# CRM COMPLETO E AUTOMAÇÕES — LUMMÉ
## Sistema de Gestão de Relacionamento com Clientes e Leads

---

## PLATAFORMA RECOMENDADA

**Ferramenta principal:** RD Station CRM (versão gratuita → paga)
**Complemento:** Notion (gestão interna e documentação)
**Automações:** Make (ex-Integromat) ou Zapier

**Por que RD Station:**
- Interface em português
- Integração nativa com WhatsApp Business e e-mail
- Relatórios de funil em tempo real
- Automações de e-mail nativas
- Plano gratuito suficiente para os primeiros 6 meses

---

## ESTRUTURA DO CRM

### Campos obrigatórios por lead

**Dados básicos:**
```
Nome completo:
Profissão/cargo:
Empresa/escritório/clínica:
Segmento: [Advogado | Arquiteto | Design de Interiores | Estética | Outro]
Cidade/bairro:
Telefone (WhatsApp):
E-mail:
Instagram:
LinkedIn:
Site:
```

**Dados de qualificação:**
```
Faturamento estimado: [<15K | 15-30K | 30-60K | 60K+]
Já investe em marketing: [Sim | Não | Não sabe]
Valor investido/mês: [R$]
Decisor: [Sim | Não | Parcial]
Urgência: [Alta | Média | Baixa]
Score BANT+: [0-5]
```

**Dados de origem:**
```
Canal de origem: [Instagram | LinkedIn | WhatsApp | E-mail | Indicação | Evento | Google]
Fonte específica: [ex: hashtag #advogadoes / indicação de [nome]]
SDR responsável:
Data de entrada no CRM:
```

**Dados de processo:**
```
Estágio do funil: [Prospect | Lead | Qualificado | Reunião | Proposta | Negociação | Cliente | Perdido | Arquivado]
Próxima ação:
Data da próxima ação:
Observações:
```

---

## ESTÁGIOS DO PIPELINE

### Pipeline de Prospecção (SDR)

```
[PROSPECT]
Entrou na lista — ainda não abordado
        ↓
[PRIMEIRO CONTATO]
Abordagem enviada — aguardando resposta
        ↓
[EM QUALIFICAÇÃO]
Respondeu — em processo de BANT+
        ↓
[QUALIFICADO]
Passou no BANT+ — pronto para reunião
        ↓
[REUNIÃO AGENDADA]
Data confirmada — aguardando reunião
        ↓
[REUNIÃO REALIZADA]
Reunião ocorreu — proposta a ser enviada
```

### Pipeline de Fechamento (Closer/Quellem)

```
[PROPOSTA ENVIADA]
PDF enviado — aguardando feedback
        ↓
[EM NEGOCIAÇÃO]
Interesse confirmado — ajustes em andamento
        ↓
[GANHO — CLIENTE]
Contrato assinado e pago
        OU
[PERDIDO]
Motivo registrado — data de recontato definida
```

---

## TAGS DO CRM

### Tags de Segmento (obrigatório — escolher 1)
- `#advogado`
- `#arquiteto`
- `#design-interiores`
- `#estetica-premium`
- `#medico`
- `#consultor`
- `#coach-premium`
- `#outro-liberal`

### Tags de Status (obrigatório — atualizar sempre)
- `#quente` — Alta probabilidade de fechar (reunião realizada + interesse claro)
- `#morno` — Interesse médio, precisa de nutrição
- `#frio` — Pouco interesse, reabordar em 60+ dias
- `#vip` — Lead de altíssimo potencial (ticket acima de R$ 8.000)
- `#indicado` — Veio por indicação (tratamento diferenciado)

### Tags de Canal
- `#linkedin` `#instagram-dm` `#whatsapp` `#email` `#evento` `#google`

### Tags de Situação
- `#sem-resposta` — Não respondeu nenhuma tentativa
- `#concorrente-ativo` — Tem agência atualmente (reabordar em 60 dias)
- `#orcamento-baixo` — Orçamento abaixo do mínimo
- `#recontato-60d` `#recontato-90d` — Data de reabordagem programada

---

## AUTOMAÇÕES — LumméOS CONFIGURADOS

### Automação 1 — Captura de Lead (Site/Landing Page)

**Trigger:** Preenchimento de formulário na landing page da Lummé

**Sequência automática:**
```
Lead preenche formulário
        ↓ imediato
E-mail de boas-vindas automático enviado
        ↓ +2 horas
Notificação WhatsApp para SDR responsável
        ↓ +24 horas (se SDR não contatou)
Alerta automático para Coordenador
        ↓ D+3
E-mail automático #2 da sequência de nutrição
```

**Template do e-mail automático de boas-vindas:**
```
Assunto: [Nome], recebemos o seu contato — próximo passo

Olá, [Nome]!

Obrigada pelo interesse na Lummé.

Sou [nome do SDR/Quellem] e entrarei em contato nas próximas horas para 
entender melhor o contexto do seu negócio e verificar se podemos ajudar.

Enquanto isso, separei algo que pode te interessar:
→ [Link para conteúdo relevante para o nicho]

Até logo,
[Nome]
Lummé | (27) 99884-5482
```

---

### Automação 2 — Sequência de Nutrição (30 dias)

**Trigger:** Lead entra na tag `#morno` ou não qualificou imediatamente

| Dia | E-mail | Assunto |
|-----|--------|---------|
| D+3 | Educativo | "3 erros de marketing que [profissão] comete sem saber" |
| D+7 | Case | "Como um [profissional] do ES conseguiu [resultado] em 60 dias" |
| D+14 | Valor | "O sistema que os [profissionais] top usam para captar clientes" |
| D+21 | Diagnóstico | "Uma pergunta: qual é o maior desafio do seu marketing hoje?" |
| D+28 | CTA | "Conversa rápida esta semana?" |

---

### Automação 3 — Follow-up de Proposta

**Trigger:** Lead avança para estágio "Proposta Enviada"

| Horário | Ação | Responsável |
|---------|------|------------|
| D+0 (envio) | E-mail com proposta em PDF | Quellem/SDR |
| D+1 | Notificação para SDR: "Confirmar recebimento da proposta" | Sistema |
| D+3 | E-mail automático de follow-up leve | Sistema |
| D+5 | Alerta para SDR: "Ligar para [nome]" | Sistema |
| D+7 | E-mail de reforço de valor | Sistema |
| D+10 | Alerta: "Proposta em risco — ação necessária" | Sistema → Quellem |

---

### Automação 4 — Recontato Programado

**Trigger:** Lead marcado com `#recontato-60d` ou `#recontato-90d`

**Sequência:**
```
Tag aplicada
        ↓ 57 dias depois
Alerta: "Em 3 dias: recontatar [Nome] — motivo do adiamento: [registrado]"
        ↓ 60 dias depois
Tarefa criada automaticamente para o SDR: "Reabordagem de [Nome]"
        ↓ SDR faz o contato
Resultado registrado → novo estágio definido
```

---

### Automação 5 — Onboarding de Cliente (pós-fechamento)

**Trigger:** Lead muda para estágio "Ganho — Cliente"

**Sequência automática:**
```
Contrato assinado
        ↓ imediato
E-mail de boas-vindas Lummé enviado automaticamente
        ↓ +2h
Tarefa para SDR/Coord: "Enviar kit de onboarding"
        ↓ +24h
Tarefa para Quellem: "Agendar kickoff com [Nome]"
        ↓ +3 dias
Briefing enviado ao cliente (link automático)
```

---

### Automação 6 — NPS Mensal (pós-cliente)

**Trigger:** Todo dia 25 de cada mês, para todos os clientes ativos

**E-mail NPS:**
```
Assunto: Uma pergunta rápida, [Nome]

Olá, [Nome]!

Mês [X] da nossa parceria — passando para saber como está sendo a experiência.

Em uma escala de 0 a 10, o quanto você indicaria a Lummé para um colega?

[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]

Sua resposta nos ajuda a melhorar.

Quellem | Lummé
```

**Resposta automática por score:**
- Score 9–10 (Promotor): "Que ótimo! Você topa gravar um depoimento rápido?"
- Score 7–8 (Neutro): "Obrigada! O que poderíamos melhorar para chegar ao 10?"
- Score 0–6 (Detrator): Alerta imediato para Quellem → ligação em 24h

---

## RELATÓRIOS AUTOMÁTICOS DO CRM

### Relatório Diário (gerado automaticamente às 8h)
- Total de prospecções ativas por SDR
- Tarefas em atraso
- Leads sem contato há mais de 5 dias
- Reuniões do dia

### Relatório Semanal (gerado toda segunda, enviado ao coordenador)
- Novos leads por canal
- Leads qualificados
- Reuniões realizadas
- Propostas enviadas
- Taxa de conversão por estágio

### Relatório Mensal (enviado à Quellem todo dia 5)
- Pipeline completo com valores
- Contratos fechados e receita gerada
- Taxa de conversão geral
- Análise de canais (qual traz mais leads qualificados)
- Top 5 motivos de perda
- Previsão do próximo mês

---

## INTEGRAÇÃO DO CRM COM OUTRAS FERRAMENTAS

| Integração | Como | Objetivo |
|-----------|------|----------|
| **WhatsApp Business** | Make/Zapier | Registrar DMs no CRM automaticamente |
| **Instagram** | Make + Webhook | Capturar leads de DM e formulários |
| **Google Forms** | Nativo RD Station | Leads do formulário do site |
| **Hotmart** | Webhook | Comprador de produto → lead no CRM |
| **Google Analytics** | Integração nativa | Origem do tráfego por lead |
| **Calendly** | Integração RD | Agendamento automático → CRM |

---

## CONFIGURAÇÃO DO CALENDLY (AGENDAMENTO)

**Tipo de reunião:** "Diagnóstico Lummé — 45 minutos"
**Disponibilidade:** Seg–Sex, 9h–17h (horários configuráveis pela Quellem)
**Buffer entre reuniões:** 15 minutos
**Perguntas do formulário Calendly:**
1. Qual é a sua profissão/segmento?
2. Qual é o maior desafio da sua presença digital?
3. Você já investiu em marketing digital? Qual foi o resultado?
4. Aproximadamente quanto você pode investir em marketing por mês?

**Link do Calendly na proposta:** Para facilitar o fechamento, colocar o link de agendamento direto na proposta.

---

## GESTÃO DE DADOS (LGPD)

**Política de dados da Lummé:**
- Todos os leads que não fecham em 12 meses são arquivados e podem solicitar exclusão
- Opt-out de e-mail disponível em todos os e-mails
- Dados não são compartilhados com terceiros sem consentimento
- Equipe terceirizada assina NDA específico sobre dados de prospects

---

*Lummé — CRM e Automações v1.0 — Maio 2026*
