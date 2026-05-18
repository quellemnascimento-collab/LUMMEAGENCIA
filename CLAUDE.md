# Lummé Agência Criativa — Contexto Operacional

## Empresa

- **Marca:** Lummé Agência Criativa
- **Razão social:** MADU Gestão Empresarial LTDA
- **CNPJ:** 65.723.134/0001-86
- **Fundadora:** Márcia Quellem Nascimento
- **Instagram:** @lummeagenciacriativa
- **Email:** contato@lummeagencia.com.br
- **Site:** www.lummeagencia.com.br
- **WhatsApp:** (27) 99884-5482
- **Segmento:** Branding premium, posicionamento estratégico, marketing com IA
- **ICP:** Profissional liberal com 5–20 anos de carreira (advogado, arquiteto, médico, consultor) — autoridade técnica com presença digital que não reflete o nível do trabalho
- **Ticket médio:** R$ 3.500 a R$ 8.000/mês
- **Tagline principal:** "A autoridade que não precisa gritar."
- **Tagline operacional:** Marketing estratégico com IA aplicada
- **Frase central:** "A Lummé não entrega posts. Entrega posicionamento."
- **Posicionamento:** Premium · Consultivo · Presença verificável

## Método Eixo

A metodologia central da Lummé, composta por 3 etapas sequenciais:

| Etapa | Nome | O que acontece |
|-------|------|----------------|
| 1 | **Diagnóstico** | Análise da presença atual, ICP, lacunas e oportunidades reais |
| 2 | **Construção** | Desenvolvimento de identidade, narrativa e estrutura de conteúdo |
| 3 | **Ativação** | Execução, publicação e mensuração com KPIs contratuais |

## Identidade Visual

### Paleta Digital (Web / Social Media)

| Nome | Hex | Uso |
|------|-----|-----|
| **Ameixa Escuro** | `#0d001f` | Fundo principal dark |
| **Ameixa Profundo** | `#1f003a` | Backgrounds secundários |
| **Ameixa Médio** | `#3f006d` | Elementos de destaque |
| **Champanhe** | `#dcc188` | Cor principal — títulos, CTAs, wordmark |
| **Lilás** | `#c86edc` | Acentos, taglines, tagline do logo |
| **Lavanda Clara** | `#f5effd` | Texto em fundo escuro |
| **Lavanda Média** | `#d4c6e8` | Texto secundário |

### Paleta de Documentos (PDF / Impresso)

| Nome | Hex | Uso |
|------|-----|-----|
| **Roxo Queimado** | `#7B3F6E` | Cor principal — headers, tabelas, CTAs |
| **Dourado Editorial** | `#C09850` | Acento — separadores, ícones, destaques |
| **Espresso** | `#2C1A14` | Wordmark, texto principal |
| **Areia Quente** | `#B5A898` | Fundo de logos, versões alternativas |
| **Champagne Claro** | `#F2E8D5` | Fundo de documentos, seções destacadas |

### Tipografia

| Uso | Fonte principal | Alternativa (offline) |
|-----|----------------|-----------------------|
| Títulos / Headings | Cormorant Garamond (peso 300–400) | Garamond Light |
| Corpo / Body | Inter (peso 300–500) | Calibri Regular |

### Logo

- **Símbolo:** Mandala de 9 retângulos arredondados girados, em champanhe (`#dcc188`)
- **Wordmark:** "lummé" minúsculas, Cormorant Garamond, champanhe
- **Tagline:** "AGÊNCIA CRIATIVA" em versalete, lilás (`#c86edc`)
- **Fundo:** Transparente ou sobre fundo escuro (ameixa)

## Padrões de Entrega

### Tom de voz
- Sofisticado, direto, sem clichês
- Presença antes do processo — o cliente vê o resultado, não a receita
- Frases curtas — máximo 25 palavras
- Voz ativa sempre
- Segunda pessoa direta: "você", "seu negócio", "sua marca"

### Vocabulário — Evitar vs. Preferir

| Evitar | Preferir |
|--------|----------|
| resultado (genérico) | percepção, reputação, presença verificável |
| engajamento | consistência, autoridade |
| viralizar, bombar | posicionamento, conversão |
| autêntico | criterioso, preciso |
| pacote | escopo, processo |
| estratégia digital (vago) | Método Eixo, diagnóstico |
| incrível, transformador | mensurável, específico |
| transforme, impulsione | construa, consolide, ative |

**Palavras da marca:** percepção, reputação, presença, posicionamento, autoridade, consistência, verificável, específico, escopo, processo, Método Eixo, diagnóstico, criterioso, preciso, curadoria, KPI, inteligência

### Formato de documentos
- Idioma: Português brasileiro
- Cabeçalho padrão em todo documento formal:
  ```
  ┌─────────────────────────────────────────┐
  │  [LOGO LUMMÉ]                           │
  │  Lummé Agência Criativa                 │
  │  [Nome do documento] · [Data] · v[X.X]  │
  └─────────────────────────────────────────┘
  ```
- Rodapé: `Lummé · MADU Gestão Empresarial LTDA · @lummeagenciacriativa · Cada detalhe importa.`
- Cores em tabelas: cabeçalho Roxo #7B3F6E / texto branco, alternância Champagne #F2E8D5
- Nunca usar preto puro — usar Espresso #2C1A14 ou Cinza Profundo #2C2C2C

## Comandos Disponíveis

| Comando | O que gera |
|---------|-----------|
| `/proposta` | Estrutura de proposta comercial personalizada |
| `/briefing` | Template de briefing de cliente |
| `/ata` | Template de ata de reunião |
| `/sop` | SOP para o processo descrito |
| `/relatorio` | Relatório executivo semanal |

## Estrutura do Repositório

```
LUMMEAGENCIA/
├── CLAUDE.md                    ← este arquivo
├── .claude/commands/            ← slash commands
├── docs/                        ← estratégia, manual de marca, personas
├── dossie/                      ← entregáveis padronizados, portfólio
├── servicos/                    ← catálogo de serviços
├── templates/                   ← contrato, proposta, briefing, relatório
├── processos/                   ← onboarding, fluxo, SLA, 4 setores
├── crm/                         ← sistema de gestão de clientes
├── financeiro/                  ← planilhas, dashboard, gestão fiscal
├── prospeccao/                  ← funil, scripts, CRM, campanhas
└── conteudo/                    ← pilares, calendário editorial
```

## Regras de Desenvolvimento

- Branch de trabalho: `claude/lumme-deliverables-docs-1cf9j`
- Todo arquivo novo deve seguir o padrão de cabeçalho com logo placeholder
- Documentos em `.md` para versionamento; arquivos gerados (`.xlsx`, `.html`) na pasta correspondente
- Commits descritivos em português
