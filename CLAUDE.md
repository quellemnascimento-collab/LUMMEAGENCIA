# Lummé Agência Criativa — Contexto Operacional

## Empresa

- **Marca:** Lummé Agência Criativa
- **Razão social:** MADU Gestão Empresarial LTDA
- **CNPJ:** 65.723.134/0001-86
- **Fundadora:** Márcia Quellem Nascimento
- **Contato:** contato@lumme.com.br · (27) 99884-5482 · @lumme.agencia
- **Segmento:** Branding premium, posicionamento estratégico, marketing com IA
- **Público:** Profissionais liberais e PMEs de alto padrão
- **Posicionamento:** Premium · Consultivo · Resultado-Orientado

## Identidade Visual

| Elemento | Valor |
|---------|-------|
| Roxo Queimado | `#7B3F6E` — cor principal |
| Dourado Editorial | `#C09850` — acento |
| Espresso | `#2C1A14` — wordmark original |
| Areia Quente | `#B5A898` — fundo logos |
| Champagne | `#F2E8D5` — fundo documentos |
| Fonte headings | Garamond Light |
| Fonte body | Calibri |

**Logo:** Mandala geométrica (símbolo) + wordmark "lummé" lowercase + tagline "Agencia criativa" (versão horizontal)

## Padrões de Entrega

### Tom de voz
- Sofisticado, direto, sem clichês
- Resultado antes do processo
- Frases curtas — máximo 25 palavras
- Voz ativa sempre
- Segunda pessoa direta: "você", "seu negócio", "sua marca"

### Palavras proibidas
Nunca use: "transforme", "impulsione", "eleve seu negócio", "incrível", "sensacional", "revolucionário", "bombar", "viral", "fofo", "corre!", "não perca!"

### Palavras da marca
Use: estratégia, posicionamento, resultado, conversão, método, layer, presença, autoridade, curadoria, mensurável, KPI, diagnóstico, inteligência

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
- Rodapé: `Lummé · MADU Gestão Empresarial LTDA · @lumme.agencia · Cada detalhe importa.`
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
