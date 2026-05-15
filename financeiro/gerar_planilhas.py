"""
Gerador de planilhas financeiras — Lummé Agência Criativa
MADU Gestão Empresarial LTDA | CNPJ 65.723.134/0001-86
"""

import xlsxwriter
from datetime import datetime, date
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Paleta Lummé ──────────────────────────────────────────────────────────────
ROXO       = "#7B3F6E"   # primária
DOURADO    = "#C09850"   # acento
CHAMPAGNE  = "#F2E8D5"   # fundo neutro
ROXO_CLARO = "#E8D6E4"   # tabelas alternadas
CINZA_ESC  = "#2C2C2C"   # texto principal
CINZA_MED  = "#6B6B6B"   # texto secundário
BRANCO     = "#FFFFFF"
VERDE      = "#2E7D32"
VERMELHO   = "#C62828"
AMARELO    = "#F57F17"


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


# ── Helpers de formato ────────────────────────────────────────────────────────

def fmt(wb, bold=False, italic=False, size=11, color=CINZA_ESC,
        bg=None, align="left", valign="vcenter", border=0,
        num_format=None, wrap=False, indent=0):
    f = wb.add_format({
        "bold": bold,
        "italic": italic,
        "font_size": size,
        "font_color": color,
        "font_name": "Calibri",
        "align": align,
        "valign": valign,
        "border": border,
        "text_wrap": wrap,
        "indent": indent,
    })
    if bg:
        f.set_bg_color(bg)
    if num_format:
        f.set_num_format(num_format)
    return f


def title_row(ws, row, col, text, wb, merge_to=None, bg=ROXO, fg=BRANCO, size=13):
    f = wb.add_format({
        "bold": True, "font_size": size, "font_color": fg,
        "font_name": "Calibri", "align": "left", "valign": "vcenter",
        "bg_color": bg, "border": 0, "indent": 1,
    })
    if merge_to is not None:
        ws.merge_range(row, col, row, merge_to, text, f)
    else:
        ws.write(row, col, text, f)
    ws.set_row(row, 22)


def sub_header(ws, row, col, text, wb, merge_to=None):
    f = wb.add_format({
        "bold": True, "font_size": 11, "font_color": BRANCO,
        "font_name": "Calibri", "align": "left", "valign": "vcenter",
        "bg_color": DOURADO, "border": 0, "indent": 1,
    })
    if merge_to is not None:
        ws.merge_range(row, col, row, merge_to, text, f)
    else:
        ws.write(row, col, text, f)
    ws.set_row(row, 18)


def write_table_headers(ws, row, col, headers, widths, wb):
    fh = wb.add_format({
        "bold": True, "font_size": 10, "font_color": BRANCO,
        "font_name": "Calibri", "align": "center", "valign": "vcenter",
        "bg_color": ROXO, "border": 1, "border_color": ROXO_CLARO,
    })
    for i, (h, w) in enumerate(zip(headers, widths)):
        ws.write(row, col + i, h, fh)
        ws.set_column(col + i, col + i, w)
    ws.set_row(row, 20)


def write_table_row(ws, row, col, values, formats, alt=False):
    bg = CHAMPAGNE if alt else BRANCO
    for i, (v, f) in enumerate(zip(values, formats)):
        ws.write(row, col + i, v, f)


# ══════════════════════════════════════════════════════════════════════════════
# ABA 1 — DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════

def sheet_dashboard(wb):
    ws = wb.add_worksheet("📊 Dashboard")
    ws.set_tab_color(ROXO)
    ws.hide_gridlines(2)
    ws.set_zoom(90)

    # Coluna decorativa esquerda
    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 22)
    ws.set_column(2, 2, 18)
    ws.set_column(3, 3, 18)
    ws.set_column(4, 4, 18)
    ws.set_column(5, 5, 18)
    ws.set_column(6, 6, 18)
    ws.set_column(7, 7, 2)

    # ── Cabeçalho ──
    ws.set_row(0, 6)
    header_bg = wb.add_format({"bg_color": ROXO})
    for c in range(8):
        ws.write(0, c, "", header_bg)

    logo_fmt = wb.add_format({
        "bold": True, "font_size": 22, "font_color": BRANCO,
        "font_name": "Calibri", "align": "left", "valign": "vcenter",
        "bg_color": ROXO, "border": 0, "indent": 1,
    })
    sub_fmt = wb.add_format({
        "font_size": 10, "font_color": DOURADO,
        "font_name": "Calibri", "align": "left", "valign": "vcenter",
        "bg_color": ROXO, "border": 0, "indent": 1,
    })
    ws.merge_range(1, 1, 1, 6, "LUMMÉ · DASHBOARD FINANCEIRO", logo_fmt)
    ws.merge_range(2, 1, 2, 4, "MADU Gestão Empresarial LTDA · CNPJ 65.723.134/0001-86", sub_fmt)
    ws.set_row(1, 36)
    ws.set_row(2, 18)

    date_fmt = wb.add_format({
        "font_size": 9, "font_color": CINZA_MED,
        "font_name": "Calibri", "align": "right", "valign": "vcenter",
        "bg_color": ROXO, "border": 0,
    })
    ws.merge_range(2, 5, 2, 6, f"Atualizado: {date.today().strftime('%d/%m/%Y')}", date_fmt)

    ws.set_row(3, 10)

    # ── Bloco: RECEITAS ──
    title_row(ws, 4, 1, "💰  RECEITAS DO MÊS", wb, merge_to=6)
    ws.set_row(5, 6)

    labels_rec = [
        ("MRR — Mensalidades recorrentes", "mrr"),
        ("Serviços pontuais", "pontual"),
        ("Produtos digitais (Lummé Starter/Pro/Club)", "digital"),
        ("Outros", "outros"),
    ]
    lbl = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                         "align": "left", "valign": "vcenter", "bg_color": CHAMPAGNE, "indent": 2})
    val = wb.add_format({"font_size": 10, "bold": True, "font_color": CINZA_ESC,
                         "font_name": "Calibri", "align": "right", "valign": "vcenter",
                         "bg_color": CHAMPAGNE, "num_format": 'R$ #,##0.00'})
    empty = wb.add_format({"bg_color": CHAMPAGNE})

    for i, (label, _) in enumerate(labels_rec):
        r = 6 + i
        ws.merge_range(r, 1, r, 4, label, lbl)
        ws.write(r, 5, 0.00, val)
        ws.write(r, 6, "", empty)
        ws.set_row(r, 18)

    # Total receita
    tot_lbl = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO,
                              "font_name": "Calibri", "align": "left", "valign": "vcenter",
                              "bg_color": ROXO, "indent": 2})
    tot_val = wb.add_format({"bold": True, "font_size": 11, "font_color": DOURADO,
                              "font_name": "Calibri", "align": "right", "valign": "vcenter",
                              "bg_color": ROXO, "num_format": 'R$ #,##0.00'})
    tot_empty = wb.add_format({"bg_color": ROXO})
    ws.merge_range(10, 1, 10, 4, "RECEITA TOTAL BRUTA", tot_lbl)
    ws.write_formula(10, 5, "=SUM(G7:G10)", tot_val, 0.00)
    ws.write(10, 6, "", tot_empty)
    ws.set_row(10, 22)

    ws.set_row(11, 10)

    # ── Bloco: DESPESAS ──
    title_row(ws, 12, 1, "📤  DESPESAS DO MÊS", wb, merge_to=6, bg=CINZA_ESC)
    ws.set_row(13, 6)

    labels_desp = [
        "Ferramentas e assinaturas",
        "Impostos (Simples Nacional)",
        "Marketing da agência (tráfego próprio)",
        "Freelancers / colaboradores",
        "Telefone e internet",
        "Educação e cursos",
        "Pró-labore",
        "Reserva (10% faturamento)",
        "Outras despesas",
    ]
    lbl2 = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                           "align": "left", "valign": "vcenter", "bg_color": BRANCO, "indent": 2})
    val2 = wb.add_format({"font_size": 10, "bold": True, "font_color": VERMELHO,
                           "font_name": "Calibri", "align": "right", "valign": "vcenter",
                           "bg_color": BRANCO, "num_format": 'R$ #,##0.00'})
    lbl2b = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                            "align": "left", "valign": "vcenter", "bg_color": CHAMPAGNE, "indent": 2})
    val2b = wb.add_format({"font_size": 10, "bold": True, "font_color": VERMELHO,
                            "font_name": "Calibri", "align": "right", "valign": "vcenter",
                            "bg_color": CHAMPAGNE, "num_format": 'R$ #,##0.00'})

    for i, label in enumerate(labels_desp):
        r = 14 + i
        alt = i % 2 == 0
        lf = lbl2b if alt else lbl2
        vf = val2b if alt else val2
        empty_f = wb.add_format({"bg_color": CHAMPAGNE if alt else BRANCO})
        ws.merge_range(r, 1, r, 4, label, lf)
        ws.write(r, 5, 0.00, vf)
        ws.write(r, 6, "", empty_f)
        ws.set_row(r, 18)

    tot2_lbl = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO,
                               "font_name": "Calibri", "align": "left", "valign": "vcenter",
                               "bg_color": CINZA_ESC, "indent": 2})
    tot2_val = wb.add_format({"bold": True, "font_size": 11, "font_color": VERMELHO,
                               "font_name": "Calibri", "align": "right", "valign": "vcenter",
                               "bg_color": CINZA_ESC, "num_format": 'R$ #,##0.00'})
    tot2_empty = wb.add_format({"bg_color": CINZA_ESC})
    ws.merge_range(23, 1, 23, 4, "DESPESA TOTAL", tot2_lbl)
    ws.write_formula(23, 5, "=SUM(G15:G23)", tot2_val, 0.00)
    ws.write(23, 6, "", tot2_empty)
    ws.set_row(23, 22)

    ws.set_row(24, 10)

    # ── Bloco: RESULTADO ──
    title_row(ws, 25, 1, "📈  RESULTADO", wb, merge_to=6, bg=DOURADO, fg=CINZA_ESC)
    ws.set_row(26, 6)

    res_labels = [
        ("LUCRO LÍQUIDO", "=G11-G24", VERDE),
        ("MARGEM LÍQUIDA (%)", "=IF(G11>0,(G11-G24)/G11*100,0)", CINZA_ESC),
        ("META DO MÊS", 0.00, CINZA_ESC),
        ("VARIAÇÃO DA META", "=G27-G29", CINZA_ESC),
    ]
    for i, (label, formula, fc) in enumerate(res_labels):
        r = 27 + i
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        rlf = wb.add_format({"bold": True if i == 0 else False, "font_size": 10,
                              "font_color": CINZA_ESC, "font_name": "Calibri",
                              "align": "left", "valign": "vcenter", "bg_color": bg, "indent": 2})
        rvf_fmt = 'R$ #,##0.00' if i != 1 else '0.00"%"'
        rvf = wb.add_format({"bold": True if i == 0 else False, "font_size": 10 if i != 0 else 12,
                              "font_color": fc, "font_name": "Calibri",
                              "align": "right", "valign": "vcenter", "bg_color": bg,
                              "num_format": rvf_fmt})
        re = wb.add_format({"bg_color": bg})
        ws.merge_range(r, 1, r, 4, label, rlf)
        if isinstance(formula, str):
            ws.write_formula(r, 5, formula, rvf, 0.00)
        else:
            ws.write(r, 5, formula, rvf)
        ws.write(r, 6, "", re)
        ws.set_row(r, 20 if i == 0 else 18)

    ws.set_row(31, 10)

    # ── Bloco: CLIENTES ──
    title_row(ws, 32, 1, "👥  CLIENTES & MRR", wb, merge_to=6)
    ws.set_row(33, 6)

    cli_labels = [
        "Total de clientes ativos",
        "Novos clientes no mês",
        "Clientes perdidos (churn)",
        "MRR total",
        "Ticket médio",
    ]
    cli_fmts = ["#,##0", "#,##0", "#,##0", "R$ #,##0.00", "R$ #,##0.00"]
    for i, (label, nf) in enumerate(zip(cli_labels, cli_fmts)):
        r = 34 + i
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        clf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                              "align": "left", "valign": "vcenter", "bg_color": bg, "indent": 2})
        cvf = wb.add_format({"bold": True, "font_size": 10, "font_color": CINZA_ESC,
                              "font_name": "Calibri", "align": "right", "valign": "vcenter",
                              "bg_color": bg, "num_format": nf})
        ce = wb.add_format({"bg_color": bg})
        ws.merge_range(r, 1, r, 4, label, clf)
        ws.write(r, 5, 0, cvf)
        ws.write(r, 6, "", ce)
        ws.set_row(r, 18)

    # ── Rodapé ──
    ws.set_row(40, 20)
    rod = wb.add_format({"font_size": 9, "font_color": CINZA_MED, "font_name": "Calibri",
                          "align": "center", "valign": "vcenter", "italic": True})
    ws.merge_range(40, 1, 40, 6, "Lummé · Dashboard Financeiro · @lumme.agencia · Cada detalhe importa.", rod)


# ══════════════════════════════════════════════════════════════════════════════
# ABA 2 — CONTROLE DE RECEITAS
# ══════════════════════════════════════════════════════════════════════════════

def sheet_receitas(wb):
    ws = wb.add_worksheet("💰 Receitas")
    ws.set_tab_color(VERDE)
    ws.hide_gridlines(2)
    ws.set_zoom(90)

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 12)   # Data
    ws.set_column(2, 2, 22)   # Cliente
    ws.set_column(3, 3, 24)   # Tipo
    ws.set_column(4, 4, 16)   # Valor bruto
    ws.set_column(5, 5, 14)   # Imposto %
    ws.set_column(6, 6, 16)   # Valor líq
    ws.set_column(7, 7, 14)   # Forma pgto
    ws.set_column(8, 8, 14)   # Competência
    ws.set_column(9, 9, 2)

    title_row(ws, 1, 1, "💰  CONTROLE DE RECEITAS", wb, merge_to=8, size=14)
    ws.set_row(2, 8)

    headers = ["Data", "Cliente", "Tipo de Receita", "Valor Bruto", "Imposto (%)", "Valor Líquido", "Forma Pgto", "Competência"]
    widths   = [12,    22,         24,                  16,            14,             16,              14,           14]
    write_table_headers(ws, 3, 1, headers, widths, wb)

    tipos = [
        ("01/06/2026", "Ex: Advogada Renata", "MRR — Gestão Mídias Sociais", 2500.00, 6.0),
        ("05/06/2026", "Ex: Clínica Estética", "MRR — Branding + Conteúdo", 4000.00, 6.0),
        ("10/06/2026", "Ex: Arquiteto Carlos", "Pontual — Diagnóstico Digital", 1000.00, 6.0),
        ("15/06/2026", "—", "Digital — Lummé Starter", 37.00, 6.0),
        ("20/06/2026", "—", "Digital — Lummé Club (assinatura)", 47.00, 6.0),
    ]

    d_fmt = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                            "align": "center", "valign": "vcenter", "bg_color": CHAMPAGNE, "border": 1,
                            "border_color": "#E0D0D8"})
    t_fmt = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                            "align": "left", "valign": "vcenter", "bg_color": CHAMPAGNE, "border": 1,
                            "border_color": "#E0D0D8", "indent": 1})
    n_fmt = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                            "align": "right", "valign": "vcenter", "bg_color": CHAMPAGNE, "border": 1,
                            "border_color": "#E0D0D8", "num_format": "R$ #,##0.00"})
    p_fmt = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                            "align": "right", "valign": "vcenter", "bg_color": CHAMPAGNE, "border": 1,
                            "border_color": "#E0D0D8", "num_format": "0.00%"})

    for i, (dt, cli, tipo, bruto, imp_pct) in enumerate(tipos):
        r = 4 + i
        alt_bg = BRANCO if i % 2 == 0 else CHAMPAGNE
        for f in [d_fmt, t_fmt, n_fmt, p_fmt]:
            f.set_bg_color(alt_bg)

        ws.write(r, 1, dt, d_fmt)
        ws.write(r, 2, cli, t_fmt)
        ws.write(r, 3, tipo, t_fmt)
        ws.write(r, 4, bruto, n_fmt)
        ws.write(r, 5, imp_pct / 100, p_fmt)
        liq_f = wb.add_format({"font_size": 10, "bold": True, "font_color": VERDE,
                                "font_name": "Calibri", "align": "right", "valign": "vcenter",
                                "bg_color": alt_bg, "border": 1, "border_color": "#E0D0D8",
                                "num_format": "R$ #,##0.00"})
        ws.write_formula(r, 6, f"=E{r+1}*(1-F{r+1})", liq_f)
        ws.write(r, 7, "Pix", d_fmt)
        ws.write(r, 8, "06/2026", d_fmt)
        ws.set_row(r, 18)

    # Adicionar 25 linhas em branco para preenchimento
    blank_d = wb.add_format({"font_size": 10, "font_color": CINZA_MED, "font_name": "Calibri",
                              "align": "center", "border": 1, "border_color": "#E0D0D8"})
    blank_t = wb.add_format({"font_size": 10, "font_color": CINZA_MED, "font_name": "Calibri",
                              "align": "left", "border": 1, "border_color": "#E0D0D8", "indent": 1})
    blank_n = wb.add_format({"font_size": 10, "font_color": CINZA_MED, "font_name": "Calibri",
                              "align": "right", "border": 1, "border_color": "#E0D0D8",
                              "num_format": "R$ #,##0.00"})
    blank_p = wb.add_format({"font_size": 10, "font_color": CINZA_MED, "font_name": "Calibri",
                              "align": "right", "border": 1, "border_color": "#E0D0D8",
                              "num_format": "0.00%"})
    blank_liq = wb.add_format({"font_size": 10, "font_color": VERDE, "font_name": "Calibri",
                                "align": "right", "border": 1, "border_color": "#E0D0D8",
                                "num_format": "R$ #,##0.00"})

    for i in range(25):
        r = 9 + i
        ws.write(r, 1, "", blank_d)
        ws.write(r, 2, "", blank_t)
        ws.write(r, 3, "", blank_t)
        ws.write(r, 4, 0.00, blank_n)
        ws.write(r, 5, 0.06, blank_p)
        ws.write_formula(r, 6, f"=IF(E{r+1}>0,E{r+1}*(1-F{r+1}),\"\")", blank_liq)
        ws.write(r, 7, "", blank_d)
        ws.write(r, 8, "", blank_d)
        ws.set_row(r, 18)

    last_data = 9 + 25 - 1
    # Totais
    tot_r = last_data + 2
    tl = wb.add_format({"bold": True, "font_size": 11, "font_color": BRANCO, "font_name": "Calibri",
                         "align": "left", "valign": "vcenter", "bg_color": ROXO, "indent": 2})
    tv = wb.add_format({"bold": True, "font_size": 11, "font_color": DOURADO, "font_name": "Calibri",
                         "align": "right", "valign": "vcenter", "bg_color": ROXO,
                         "num_format": "R$ #,##0.00"})
    ws.merge_range(tot_r, 1, tot_r, 3, "TOTAL RECEITA BRUTA", tl)
    ws.write_formula(tot_r, 4, f"=SUM(E5:E{last_data+1})", tv)
    ws.merge_range(tot_r, 5, tot_r, 5, "", wb.add_format({"bg_color": ROXO}))
    ws.write_formula(tot_r, 6, f"=SUM(G5:G{last_data+1})", tv)
    ws.merge_range(tot_r, 7, tot_r, 8, "TOTAL RECEITA LÍQUIDA →", tl)
    ws.set_row(tot_r, 24)


# ══════════════════════════════════════════════════════════════════════════════
# ABA 3 — CONTROLE DE DESPESAS
# ══════════════════════════════════════════════════════════════════════════════

def sheet_despesas(wb):
    ws = wb.add_worksheet("📤 Despesas")
    ws.set_tab_color(VERMELHO)
    ws.hide_gridlines(2)
    ws.set_zoom(90)

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 12)
    ws.set_column(2, 2, 24)
    ws.set_column(3, 3, 20)
    ws.set_column(4, 4, 16)
    ws.set_column(5, 5, 14)
    ws.set_column(6, 6, 12)
    ws.set_column(7, 7, 2)

    title_row(ws, 1, 1, "📤  CONTROLE DE DESPESAS", wb, merge_to=6, bg=CINZA_ESC, size=14)
    ws.set_row(2, 8)

    headers = ["Data", "Categoria", "Descrição", "Valor", "Forma Pgto", "Recorrente?"]
    widths   = [12,    20,          24,           16,      14,           12]
    write_table_headers(ws, 3, 1, headers, widths, wb)

    despesas_fixas = [
        ("01/06", "Ferramenta", "Canva Pro", 35.00, "Cartão", "Sim"),
        ("01/06", "Ferramenta", "Claude Pro (Anthropic)", 110.00, "Cartão", "Sim"),
        ("01/06", "Ferramenta", "Adobe Creative Cloud", 115.00, "Cartão", "Sim"),
        ("01/06", "Ferramenta", "RD Station Starter", 75.00, "Cartão", "Sim"),
        ("01/06", "Infra", "Domínio lumme.com.br + hospedagem", 50.00, "Cartão", "Sim"),
        ("01/06", "Infra", "Google Workspace (e-mail corporativo)", 30.00, "Cartão", "Sim"),
        ("01/06", "Infra", "Notion Plus", 20.00, "Cartão", "Sim"),
        ("01/06", "Ferramenta", "Buffer (agendamento social)", 35.00, "Cartão", "Sim"),
        ("05/06", "Imposto", "DAS — Simples Nacional", 0.00, "Débito", "Sim"),
        ("10/06", "Marketing", "Tráfego pago — @lumme.agencia", 0.00, "Cartão", "Não"),
        ("15/06", "Colaborador", "Freelancer (se aplicável)", 0.00, "Pix", "Não"),
        ("20/06", "Comunicação", "Telefone + Internet", 150.00, "Débito", "Sim"),
        ("25/06", "Educação", "Cursos / Certificações", 0.00, "Pix", "Não"),
        ("30/06", "Pró-labore", "Retirada fundadora", 0.00, "Pix", "Sim"),
        ("30/06", "Reserva", "Fundo de emergência (10% MRR)", 0.00, "Pix", "Sim"),
    ]

    for i, (dt, cat, desc, val, forma, rec) in enumerate(despesas_fixas):
        r = 4 + i
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        df = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        tf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "indent": 1})
        vf = wb.add_format({"font_size": 10, "bold": True, "font_color": VERMELHO,
                             "font_name": "Calibri", "align": "right", "bg_color": bg,
                             "border": 1, "border_color": "#E0D0D8", "num_format": "R$ #,##0.00"})
        rf = wb.add_format({"font_size": 10, "font_color": VERDE if rec == "Sim" else CINZA_MED,
                             "font_name": "Calibri", "align": "center", "bold": rec == "Sim",
                             "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        ws.write(r, 1, dt, df)
        ws.write(r, 2, cat, tf)
        ws.write(r, 3, desc, tf)
        ws.write(r, 4, val, vf)
        ws.write(r, 5, forma, df)
        ws.write(r, 6, rec, rf)
        ws.set_row(r, 18)

    # Linhas em branco
    for i in range(10):
        r = 4 + len(despesas_fixas) + i
        bg = CHAMPAGNE if i % 2 == 0 else BRANCO
        for c in range(1, 7):
            bf = wb.add_format({"font_size": 10, "bg_color": bg, "border": 1,
                                 "border_color": "#E0D0D8",
                                 "num_format": "R$ #,##0.00" if c == 4 else ""})
            ws.write(r, c, 0.00 if c == 4 else "", bf)
        ws.set_row(r, 18)

    last_r = 4 + len(despesas_fixas) + 10 - 1
    tot_r = last_r + 2
    tl = wb.add_format({"bold": True, "font_size": 11, "font_color": BRANCO, "font_name": "Calibri",
                         "align": "left", "valign": "vcenter", "bg_color": CINZA_ESC, "indent": 2})
    tv = wb.add_format({"bold": True, "font_size": 11, "font_color": VERMELHO, "font_name": "Calibri",
                         "align": "right", "valign": "vcenter", "bg_color": CINZA_ESC,
                         "num_format": "R$ #,##0.00"})
    ws.merge_range(tot_r, 1, tot_r, 3, "TOTAL DESPESAS", tl)
    ws.write_formula(tot_r, 4, f"=SUM(E5:E{last_r+1})", tv)
    ws.merge_range(tot_r, 5, tot_r, 6, "", wb.add_format({"bg_color": CINZA_ESC}))
    ws.set_row(tot_r, 24)


# ══════════════════════════════════════════════════════════════════════════════
# ABA 4 — FLUXO DE CAIXA (6 meses)
# ══════════════════════════════════════════════════════════════════════════════

def sheet_fluxo(wb):
    ws = wb.add_worksheet("📅 Fluxo de Caixa")
    ws.set_tab_color(DOURADO)
    ws.hide_gridlines(2)
    ws.set_zoom(85)

    meses = ["Mai/26", "Jun/26", "Jul/26", "Ago/26", "Set/26", "Out/26"]

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 30)
    for c in range(2, 8):
        ws.set_column(c, c, 14)
    ws.set_column(8, 8, 2)

    title_row(ws, 1, 1, "📅  FLUXO DE CAIXA PROJETADO — 6 MESES", wb, merge_to=7, bg=DOURADO, fg=CINZA_ESC, size=14)
    ws.set_row(2, 8)

    # Header colunas
    hf = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                         "align": "center", "bg_color": ROXO, "border": 1, "border_color": ROXO_CLARO})
    hl = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                         "align": "left", "bg_color": ROXO, "border": 1, "border_color": ROXO_CLARO,
                         "indent": 1})
    ws.write(3, 1, "Item", hl)
    for i, m in enumerate(meses):
        ws.write(3, 2 + i, m, hf)
    ws.set_row(3, 20)

    # Dados
    entradas = [
        ("MRR — Mensalidades", [0, 3500, 7000, 12000, 18000, 25000]),
        ("Serviços pontuais", [2000, 3000, 4000, 5000, 6000, 8000]),
        ("Produtos digitais", [0, 200, 400, 800, 1200, 2000]),
    ]
    despesas = [
        ("Ferramentas (stack fixo)", [470, 470, 470, 470, 470, 470]),
        ("Impostos (Simples Nacional)", [120, 400, 700, 1100, 1600, 2200]),
        ("Marketing — tráfego próprio", [0, 300, 300, 500, 500, 800]),
        ("Freelancers / colaboradores", [0, 0, 500, 1000, 1500, 2500]),
        ("Telefone e internet", [150, 150, 150, 150, 150, 150]),
        ("Educação e cursos", [200, 100, 100, 100, 200, 200]),
        ("Pró-labore", [0, 0, 2000, 4000, 6000, 8000]),
        ("Reserva (10%)", [200, 670, 1140, 1780, 2520, 3500]),
    ]

    row = 4
    def section_lbl(label, bg=CHAMPAGNE, color=CINZA_ESC, bold=False):
        return wb.add_format({"bold": bold, "font_size": 10, "font_color": color,
                               "font_name": "Calibri", "align": "left", "valign": "vcenter",
                               "bg_color": bg, "border": 1, "border_color": "#E0D0D8", "indent": 1})
    def num_cell(bg=CHAMPAGNE, color=CINZA_ESC, bold=False):
        return wb.add_format({"bold": bold, "font_size": 10, "font_color": color,
                               "font_name": "Calibri", "align": "right", "valign": "vcenter",
                               "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                               "num_format": "R$ #,##0"})

    # Entradas header
    sub_header(ws, row, 1, "ENTRADAS", wb, merge_to=7)
    row += 1

    entrada_rows = []
    for i, (label, vals) in enumerate(entradas):
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        ws.write(row, 1, label, section_lbl(bg))
        for c, v in enumerate(vals):
            ws.write(row, 2 + c, v, num_cell(bg))
        ws.set_row(row, 18)
        entrada_rows.append(row)
        row += 1

    # Total entradas
    tef = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                          "align": "left", "bg_color": VERDE, "border": 1, "border_color": BRANCO,
                          "indent": 1})
    tvf = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                          "align": "right", "bg_color": VERDE, "border": 1, "border_color": BRANCO,
                          "num_format": "R$ #,##0"})
    ws.write(row, 1, "TOTAL ENTRADAS", tef)
    for c in range(6):
        col_letter = chr(ord('C') + c)
        ws.write_formula(row, 2 + c,
                         f"=SUM({col_letter}{entrada_rows[0]+1}:{col_letter}{entrada_rows[-1]+1})",
                         tvf, sum(e[1][c] for e in entradas))
    total_entrada_row = row
    ws.set_row(row, 20)
    row += 1

    ws.set_row(row, 8)
    row += 1

    # Despesas header
    sub_header(ws, row, 1, "SAÍDAS", wb, merge_to=7)
    row += 1

    saida_rows = []
    for i, (label, vals) in enumerate(despesas):
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        vf = wb.add_format({"font_size": 10, "font_color": VERMELHO, "font_name": "Calibri",
                              "align": "right", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                              "num_format": "R$ #,##0"})
        ws.write(row, 1, label, section_lbl(bg))
        for c, v in enumerate(vals):
            ws.write(row, 2 + c, v, vf)
        ws.set_row(row, 18)
        saida_rows.append(row)
        row += 1

    tdf = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                          "align": "left", "bg_color": VERMELHO, "border": 1, "border_color": BRANCO,
                          "indent": 1})
    tdv = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                          "align": "right", "bg_color": VERMELHO, "border": 1, "border_color": BRANCO,
                          "num_format": "R$ #,##0"})
    ws.write(row, 1, "TOTAL SAÍDAS", tdf)
    for c in range(6):
        col_letter = chr(ord('C') + c)
        ws.write_formula(row, 2 + c,
                         f"=SUM({col_letter}{saida_rows[0]+1}:{col_letter}{saida_rows[-1]+1})",
                         tdv, sum(d[1][c] for d in despesas))
    total_saida_row = row
    ws.set_row(row, 20)
    row += 2

    # Saldo do mês
    saldo_f = wb.add_format({"bold": True, "font_size": 11, "font_color": CINZA_ESC,
                              "font_name": "Calibri", "align": "left", "bg_color": CHAMPAGNE,
                              "border": 1, "border_color": DOURADO, "indent": 1})
    saldo_v = wb.add_format({"bold": True, "font_size": 11, "font_color": VERDE,
                              "font_name": "Calibri", "align": "right", "bg_color": CHAMPAGNE,
                              "border": 1, "border_color": DOURADO, "num_format": "R$ #,##0"})
    ws.write(row, 1, "SALDO DO MÊS", saldo_f)
    saldo_mes = [0, 2530, 3830, 6200, 9060, 14150]
    for c in range(6):
        col_letter = chr(ord('C') + c)
        ws.write_formula(row, 2 + c,
                         f"={col_letter}{total_entrada_row+1}-{col_letter}{total_saida_row+1}",
                         saldo_v, saldo_mes[c])
    saldo_mes_row = row
    ws.set_row(row, 22)
    row += 1

    acum_f = wb.add_format({"bold": True, "font_size": 11, "font_color": BRANCO,
                             "font_name": "Calibri", "align": "left", "bg_color": ROXO,
                             "border": 1, "border_color": DOURADO, "indent": 1})
    acum_v = wb.add_format({"bold": True, "font_size": 11, "font_color": DOURADO,
                             "font_name": "Calibri", "align": "right", "bg_color": ROXO,
                             "border": 1, "border_color": DOURADO, "num_format": "R$ #,##0"})
    ws.write(row, 1, "SALDO ACUMULADO", acum_f)
    acum = 0
    for c in range(6):
        acum += saldo_mes[c]
        col_letter = chr(ord('C') + c)
        if c == 0:
            ws.write_formula(row, 2, f"={col_letter}{saldo_mes_row+1}", acum_v, saldo_mes[0])
        else:
            prev = chr(ord('C') + c - 1)
            ws.write_formula(row, 2 + c, f"={prev}{row+1}+{col_letter}{saldo_mes_row+1}", acum_v, acum)
    ws.set_row(row, 22)

    # Gráfico de barras
    chart = wb.add_chart({"type": "column"})
    chart.add_series({
        "name": "Saldo do Mês",
        "categories": ["📅 Fluxo de Caixa", 3, 2, 3, 7],
        "values":     ["📅 Fluxo de Caixa", saldo_mes_row, 2, saldo_mes_row, 7],
        "fill":       {"color": ROXO},
        "gap":        80,
    })
    chart.set_title({"name": "Saldo Mensal — Lummé", "name_font": {"color": CINZA_ESC, "size": 12}})
    chart.set_x_axis({"name": "Mês", "line": {"none": True}})
    chart.set_y_axis({"name": "R$", "num_format": "R$ #,##0"})
    chart.set_legend({"none": True})
    chart.set_size({"width": 480, "height": 250})
    chart.set_chartarea({"border": {"none": True}, "fill": {"color": CHAMPAGNE}})
    ws.insert_chart(row + 3, 1, chart)


# ══════════════════════════════════════════════════════════════════════════════
# ABA 5 — DRE
# ══════════════════════════════════════════════════════════════════════════════

def sheet_dre(wb):
    ws = wb.add_worksheet("📋 DRE")
    ws.set_tab_color(CINZA_ESC)
    ws.hide_gridlines(2)
    ws.set_zoom(90)

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 32)
    ws.set_column(2, 2, 18)
    ws.set_column(3, 3, 16)
    ws.set_column(4, 4, 2)

    title_row(ws, 1, 1, "📋  DRE — DEMONSTRATIVO DE RESULTADO", wb, merge_to=3, bg=CINZA_ESC, size=14)
    ws.set_row(2, 8)

    hf = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                         "align": "center", "bg_color": ROXO, "border": 1, "border_color": ROXO_CLARO})
    hl = wb.add_format({"bold": True, "font_size": 10, "font_color": BRANCO, "font_name": "Calibri",
                         "align": "left", "bg_color": ROXO, "border": 1, "border_color": ROXO_CLARO,
                         "indent": 1})
    ws.write(3, 1, "Item", hl)
    ws.write(3, 2, "Valor (R$)", hf)
    ws.write(3, 3, "% Receita", hf)
    ws.set_row(3, 20)

    secoes = [
        ("(+) RECEITA BRUTA", None, True, VERDE, False),
        ("(-) Deduções — impostos sobre NF (6%)", "=-B5*0.06", False, VERMELHO, True),
        ("(=) RECEITA LÍQUIDA", "=B5+B6", True, VERDE, False),
        (None, None, False, None, False),  # separador
        ("(-) CUSTOS DIRETOS DE PRODUÇÃO", None, True, CINZA_ESC, False),
        ("    · Freelancers e colaboradores", None, False, CINZA_ESC, True),
        ("    · Ferramentas por cliente", None, False, CINZA_ESC, True),
        ("(=) LUCRO BRUTO", "=B7-(B10+B11)", True, VERDE, False),
        (None, None, False, None, False),
        ("(-) DESPESAS OPERACIONAIS", None, True, CINZA_ESC, False),
        ("    · Stack de ferramentas fixas", 470, False, CINZA_ESC, True),
        ("    · Marketing da agência", None, False, CINZA_ESC, True),
        ("    · Educação e cursos", None, False, CINZA_ESC, True),
        ("    · Comunicação (tel + internet)", 150, False, CINZA_ESC, True),
        ("(=) EBITDA", "=B12-(B15+B16+B17+B18)", True, VERDE, False),
        (None, None, False, None, False),
        ("(-) Pró-labore", None, False, CINZA_ESC, True),
        ("(-) Reserva emergência (10%)", "=B5*0.1", False, CINZA_ESC, True),
        (None, None, False, None, False),
        ("(=) RESULTADO LÍQUIDO FINAL", "=B19-B21-B22", True, VERDE, False),
    ]

    row = 4
    for i, item in enumerate(secoes):
        if item[0] is None:
            ws.set_row(row, 8)
            row += 1
            continue
        label, formula, bold, color, indent = item
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        lf = wb.add_format({"bold": bold, "font_size": 10, "font_color": color or CINZA_ESC,
                             "font_name": "Calibri", "align": "left", "bg_color": bg,
                             "border": 1, "border_color": "#E0D0D8", "indent": 2 if indent else 1})
        vf = wb.add_format({"bold": bold, "font_size": 10,
                             "font_color": color if bold else CINZA_ESC,
                             "font_name": "Calibri", "align": "right", "bg_color": bg,
                             "border": 1, "border_color": "#E0D0D8", "num_format": "R$ #,##0.00"})
        pf = wb.add_format({"bold": bold, "font_size": 10, "font_color": CINZA_MED,
                             "font_name": "Calibri", "align": "right", "bg_color": bg,
                             "border": 1, "border_color": "#E0D0D8", "num_format": "0.0%"})
        ws.write(row, 1, label, lf)
        if formula is None:
            ws.write(row, 2, 0.00, vf)
        elif isinstance(formula, (int, float)):
            ws.write(row, 2, formula, vf)
        else:
            ws.write_formula(row, 2, formula, vf, 0.00)
        # % da receita
        if row != 4:
            ws.write_formula(row, 3, f"=IF(B5>0,B{row+1}/B5,0)", pf, 0.0)
        else:
            ws.write(row, 3, 1.0, pf)
        ws.set_row(row, 20 if bold else 18)
        row += 1


# ══════════════════════════════════════════════════════════════════════════════
# ABA 6 — PRECIFICAÇÃO
# ══════════════════════════════════════════════════════════════════════════════

def sheet_precificacao(wb):
    ws = wb.add_worksheet("💎 Precificação")
    ws.set_tab_color(DOURADO)
    ws.hide_gridlines(2)
    ws.set_zoom(88)

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 32)
    ws.set_column(2, 2, 14)
    ws.set_column(3, 3, 12)
    ws.set_column(4, 4, 16)
    ws.set_column(5, 5, 16)
    ws.set_column(6, 6, 12)
    ws.set_column(7, 7, 2)

    title_row(ws, 1, 1, "💎  TABELA DE PRECIFICAÇÃO — LUMMÉ", wb, merge_to=6, bg=DOURADO, fg=CINZA_ESC, size=14)
    ws.set_row(2, 8)

    headers = ["Serviço", "Custo Direto", "Horas Lummé", "Preço de Venda", "Preço Máximo", "Margem %"]
    widths   = [32,        14,              12,             16,               16,              12]
    write_table_headers(ws, 3, 1, headers, widths, wb)

    tiers = [
        ("TIER 1 — SERVIÇOS DE ENTRADA", None),
        ("Diagnóstico de Presença Digital",        50, 8,  800,  1200),
        ("Consultoria Avulsa (2h)",                30, 2,  500,  800),
        ("Identidade Visual Estratégica",          200, 20, 1500, 2000),
        ("TIER 2 — RECORRENTES / MÊS", None),
        ("Pacote Essencial — Presença Estratégica", 350, 30, 1800, 2200),
        ("Pacote Posicionamento — Autoridade",      500, 45, 2800, 3500),
        ("Pacote Premium — Full Presence",          800, 70, 4500, 5000),
        ("Gestão de Tráfego Pago",                 200, 20, 1500, 2000),
        ("TIER 3 — PREMIUM / PROJETO", None),
        ("Consultoria Estratégica Trimestral",     1000, 40, 8000, 12000),
        ("Mentoria Método G.O.F. (8 encontros)",   500, 16, 3500, 5000),
        ("Pacote Full-Service Lummé",              2000, 120, 10000, 15000),
        ("TIER 4 — PRODUTOS DIGITAIS", None),
        ("Lummé Starter (60 templates)",           500, 0,  37,   37),
        ("Lummé Pro (200 templates)",              1000, 0,  97,   97),
        ("Lummé Club (30 templates/mês)",          200, 0,  47,   47),
        ("Lummé Academy (curso — por aluno)",      2000, 0,  497,  497),
    ]

    row = 4
    for item in tiers:
        label = item[0]
        if item[1] is None:
            sub_header(ws, row, 1, label, wb, merge_to=6)
            row += 1
            continue
        _, custo, horas, preco_min, preco_max = item
        alt = row % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        lf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "indent": 1})
        nf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "right", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "num_format": "R$ #,##0"})
        hf2 = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                              "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        mf = wb.add_format({"bold": True, "font_size": 10, "font_color": VERDE, "font_name": "Calibri",
                             "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "num_format": "0%"})
        ws.write(row, 1, label, lf)
        ws.write(row, 2, custo, nf)
        ws.write(row, 3, horas if horas else "—", hf2)
        ws.write(row, 4, preco_min, nf)
        ws.write(row, 5, preco_max, nf)
        # Margem calculada com preço médio
        preco_medio = (preco_min + preco_max) / 2
        margem = (preco_medio - custo) / preco_medio if preco_medio > 0 else 0
        ws.write(row, 6, margem, mf)
        ws.set_row(row, 18)
        row += 1

    # Política de desconto
    row += 1
    title_row(ws, row, 1, "📌  POLÍTICA DE DESCONTO", wb, merge_to=6)
    row += 1

    descontos = [
        ("Pagamento trimestral antecipado", "10%", "Pagamento integral em D+0"),
        ("Pagamento semestral antecipado", "15%", "Pagamento integral em D+0"),
        ("Indicação de novo cliente", "R$ 300 crédito", "Após fechamento do indicado"),
        ("Combo de 2+ serviços contratados", "10%", "Contrato mínimo de 3 meses"),
    ]
    dh = ["Situação", "Desconto Máximo", "Condição"]
    dw = [32, 18, 30]
    write_table_headers(ws, row, 1, dh, dw, wb)
    row += 1
    for i, (sit, desc, cond) in enumerate(descontos):
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        df2 = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                              "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                              "indent": 1})
        df3 = wb.add_format({"bold": True, "font_size": 10, "font_color": DOURADO,
                              "font_name": "Calibri", "align": "center", "bg_color": bg,
                              "border": 1, "border_color": "#E0D0D8"})
        ws.write(row, 1, sit, df2)
        ws.write(row, 2, desc, df3)
        ws.write(row, 3, cond, df2)
        ws.set_row(row, 18)
        row += 1

    # Aviso
    row += 1
    aviso = wb.add_format({"bold": True, "italic": True, "font_size": 10, "font_color": VERMELHO,
                            "font_name": "Calibri", "align": "left", "bg_color": "#FFF3F3",
                            "indent": 2})
    ws.merge_range(row, 1, row, 6,
                   "⚠  Regra: Nunca dar desconto sem contrapartida. Desconto sem motivo = desvalorização da marca Lummé.", aviso)
    ws.set_row(row, 22)


# ══════════════════════════════════════════════════════════════════════════════
# ABA 7 — METAS POR FASE
# ══════════════════════════════════════════════════════════════════════════════

def sheet_metas(wb):
    ws = wb.add_worksheet("🎯 Metas por Fase")
    ws.set_tab_color(ROXO)
    ws.hide_gridlines(2)
    ws.set_zoom(90)

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 22)
    ws.set_column(2, 2, 22)
    ws.set_column(3, 3, 16)
    ws.set_column(4, 4, 18)
    ws.set_column(5, 5, 16)
    ws.set_column(6, 6, 16)
    ws.set_column(7, 7, 2)

    title_row(ws, 1, 1, "🎯  METAS POR FASE — MAI/2026 → JAN/2027", wb, merge_to=6, size=14)
    ws.set_row(2, 8)

    headers = ["Fase", "Período", "Clientes Ativos", "MRR Alvo", "Receita Mensal", "Pró-labore"]
    widths   = [22,    22,         16,                  18,          18,               16]
    write_table_headers(ws, 3, 1, headers, widths, wb)

    fases = [
        ("1 — Fundação",       "Mai–Jun/2026", "0–2",  "R$ 0–5K",   "R$ 0–7K",    "R$ 0"),
        ("2 — Posicionamento", "Jun–Jul/2026", "2–4",  "R$ 5–12K",  "R$ 5–15K",   "R$ 2.000"),
        ("3 — Prova Social",   "Ago–Set/2026", "4–6",  "R$ 12–20K", "R$ 15–25K",  "R$ 4.000"),
        ("4 — Sistematização", "Out–Nov/2026", "6–10", "R$ 20–35K", "R$ 25–40K",  "R$ 8.000"),
        ("5 — Escala",         "Dez/26–Jan/27","10–15","R$ 35–55K", "R$ 40–60K",  "R$ 15.000"),
    ]

    fase_colors = [CINZA_ESC, "#5B2D52", "#7B3F6E", "#9B5F8E", DOURADO]

    row = 4
    for i, (fase, periodo, cli, mrr, receita, pro) in enumerate(fases):
        ws.set_row(row, 30)
        fg_color = fase_colors[i]
        lf = wb.add_format({"bold": True, "font_size": 11, "font_color": BRANCO,
                             "font_name": "Calibri", "align": "left", "valign": "vcenter",
                             "bg_color": fg_color, "border": 1, "border_color": BRANCO, "indent": 1})
        cf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "center", "valign": "vcenter",
                             "bg_color": CHAMPAGNE if i % 2 == 0 else BRANCO,
                             "border": 1, "border_color": "#E0D0D8"})
        vf2 = wb.add_format({"bold": True, "font_size": 10, "font_color": VERDE, "font_name": "Calibri",
                              "align": "center", "valign": "vcenter",
                              "bg_color": CHAMPAGNE if i % 2 == 0 else BRANCO,
                              "border": 1, "border_color": "#E0D0D8"})
        ws.write(row, 1, fase, lf)
        ws.write(row, 2, periodo, cf)
        ws.write(row, 3, cli, cf)
        ws.write(row, 4, mrr, vf2)
        ws.write(row, 5, receita, vf2)
        ws.write(row, 6, pro, cf)
        row += 1

    # Composição de receita
    row += 1
    title_row(ws, row, 1, "📊  COMPOSIÇÃO DA RECEITA ALVO (Fase 4+)", wb, merge_to=6)
    row += 1

    comps = [
        ("MRR — mensalidades recorrentes", "65%", "Base estável e previsível"),
        ("Serviços pontuais (diagnóstico, branding)", "20%", "Entrada de novos clientes"),
        ("Produtos digitais (Lummé Starter/Pro/Club/Academy)", "15%", "Receita escalável"),
    ]
    ch = ["Fonte de Receita", "% alvo", "Estratégia"]
    cw = [36, 12, 30]
    write_table_headers(ws, row, 1, ch, cw, wb)
    row += 1
    for i, (fonte, pct, est) in enumerate(comps):
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        lf2 = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                              "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                              "indent": 1})
        pf2 = wb.add_format({"bold": True, "font_size": 10, "font_color": ROXO, "font_name": "Calibri",
                              "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        ws.write(row, 1, fonte, lf2)
        ws.write(row, 2, pct, pf2)
        ws.write(row, 3, est, lf2)
        ws.set_row(row, 18)
        row += 1

    # Gráfico de meta MRR
    chart = wb.add_chart({"type": "line"})
    # Gráfico simples sem referência de planilha para metas
    pass


# ══════════════════════════════════════════════════════════════════════════════
# ABA 8 — STACK DE FERRAMENTAS
# ══════════════════════════════════════════════════════════════════════════════

def sheet_stack(wb):
    ws = wb.add_worksheet("🛠 Stack de Ferramentas")
    ws.set_tab_color(CINZA_MED)
    ws.hide_gridlines(2)
    ws.set_zoom(90)

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 26)
    ws.set_column(2, 2, 30)
    ws.set_column(3, 3, 14)
    ws.set_column(4, 4, 14)
    ws.set_column(5, 5, 12)
    ws.set_column(6, 6, 2)

    title_row(ws, 1, 1, "🛠  STACK DE FERRAMENTAS — LUMMÉ", wb, merge_to=5, size=14)
    ws.set_row(2, 8)

    headers = ["Ferramenta", "Função", "Custo/mês", "Prioridade", "Status"]
    widths   = [26,          30,        14,           14,           12]
    write_table_headers(ws, 3, 1, headers, widths, wb)

    ferramentas = [
        ("PRODUÇÃO E DESIGN", None, None, None, None),
        ("Canva Pro", "Templates e design de conteúdo", 35, "Imediata", "Ativo"),
        ("Adobe Creative Cloud", "Illustrator, Photoshop, InDesign", 115, "Imediata", "Ativo"),
        ("CapCut (Reels)", "Edição de vídeo para redes sociais", 0, "Imediata", "Ativo"),
        ("INTELIGÊNCIA ARTIFICIAL", None, None, None, None),
        ("Claude Pro (Anthropic)", "Produção de conteúdo e copy com IA", 110, "Imediata", "Ativo"),
        ("ChatGPT Plus (OpenAI)", "Apoio na criação e pesquisa", 100, "Fase 2", "Avaliar"),
        ("CRM E AUTOMAÇÃO", None, None, None, None),
        ("RD Station Starter", "CRM e e-mail marketing", 75, "Imediata", "Ativo"),
        ("Notion Plus", "Documentação, CRM, calendário", 20, "Imediata", "Ativo"),
        ("Asaas", "Cobranças, Pix recorrente, boleto", "% por tx", "Fase 2", "Avaliar"),
        ("AGENDAMENTO E PUBLICAÇÃO", None, None, None, None),
        ("Buffer", "Agendamento Instagram, LinkedIn, FB", 35, "Imediata", "Ativo"),
        ("Meta Business Suite", "Agendamento e análise Meta", 0, "Imediata", "Ativo"),
        ("INFRAESTRUTURA", None, None, None, None),
        ("Google Workspace", "E-mail corporativo, Drive, Meet", 30, "Imediata", "Ativo"),
        ("Domínio lumme.com.br", "Identidade digital", "20/ano", "Imediata", "Ativo"),
        ("Hospedagem (Hostgator/Locaweb)", "Site Lummé", 30, "Imediata", "Ativo"),
        ("BANCO E FINANCEIRO", None, None, None, None),
        ("Nubank PJ / Inter PJ", "Conta corrente MADU LTDA — gratuita", 0, "Imediata", "Ativo"),
        ("ContaAzul ou Nibo", "ERP financeiro completo, DRE automático", 150, "Fase 2", "Avaliar"),
        ("ANÁLISE E PERFORMANCE", None, None, None, None),
        ("Google Analytics 4", "Análise de tráfego do site", 0, "Fase 2", "Ativo"),
        ("Meta Ads Manager", "Tráfego pago Instagram + Facebook", 0, "Conforme contrato", "Ativo"),
        ("Google Ads", "Tráfego pago Google", 0, "Conforme contrato", "Avaliar"),
    ]

    row = 4
    total = 0
    for item in ferramentas:
        nome, func, custo, prio, status = item
        if func is None:
            sub_header(ws, row, 1, nome, wb, merge_to=5)
            row += 1
            continue
        alt = row % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        lf = wb.add_format({"bold": True, "font_size": 10, "font_color": CINZA_ESC,
                             "font_name": "Calibri", "align": "left", "bg_color": bg,
                             "border": 1, "border_color": "#E0D0D8", "indent": 1})
        tf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "indent": 1})
        cf2 = wb.add_format({"bold": isinstance(custo, (int, float)), "font_size": 10,
                              "font_color": VERDE if isinstance(custo, (int, float)) and custo > 0 else CINZA_MED,
                              "font_name": "Calibri", "align": "right", "bg_color": bg,
                              "border": 1, "border_color": "#E0D0D8",
                              "num_format": "R$ #,##0" if isinstance(custo, (int, float)) else ""})
        pf2 = wb.add_format({"font_size": 10, "font_color": ROXO if prio == "Imediata" else CINZA_MED,
                              "font_name": "Calibri", "bold": prio == "Imediata",
                              "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        sf = wb.add_format({"bold": True, "font_size": 10,
                             "font_color": VERDE if status == "Ativo" else AMARELO,
                             "font_name": "Calibri", "align": "center", "bg_color": bg,
                             "border": 1, "border_color": "#E0D0D8"})
        ws.write(row, 1, nome, lf)
        ws.write(row, 2, func, tf)
        if isinstance(custo, (int, float)):
            ws.write(row, 3, custo, cf2)
            if prio == "Imediata" and status == "Ativo" and custo > 0:
                total += custo
        else:
            ws.write(row, 3, custo, cf2)
        ws.write(row, 4, prio, pf2)
        ws.write(row, 5, status, sf)
        ws.set_row(row, 18)
        row += 1

    # Total
    row += 1
    tl = wb.add_format({"bold": True, "font_size": 12, "font_color": BRANCO, "font_name": "Calibri",
                         "align": "left", "valign": "vcenter", "bg_color": ROXO, "indent": 2})
    tv2 = wb.add_format({"bold": True, "font_size": 12, "font_color": DOURADO, "font_name": "Calibri",
                          "align": "right", "valign": "vcenter", "bg_color": ROXO,
                          "num_format": "R$ #,##0"})
    ws.merge_range(row, 1, row, 3, "STACK FIXO MENSAL (ferramentas ativas imediatas)", tl)
    ws.write(row, 4, total, tv2)
    ws.merge_range(row, 5, row, 5, "", wb.add_format({"bg_color": ROXO}))
    ws.set_row(row, 26)

    row += 2
    obs = wb.add_format({"font_size": 9, "italic": True, "font_color": CINZA_MED,
                          "font_name": "Calibri", "align": "left", "indent": 1})
    ws.merge_range(row, 1, row, 5, "* Ferramentas 'Avaliar' são recomendadas para Fase 2+ dependendo do faturamento.", obs)


# ══════════════════════════════════════════════════════════════════════════════
# ABA 9 — GESTÃO FISCAL
# ══════════════════════════════════════════════════════════════════════════════

def sheet_fiscal(wb):
    ws = wb.add_worksheet("🏛 Gestão Fiscal")
    ws.set_tab_color(CINZA_ESC)
    ws.hide_gridlines(2)
    ws.set_zoom(90)

    ws.set_column(0, 0, 2)
    ws.set_column(1, 1, 30)
    ws.set_column(2, 2, 18)
    ws.set_column(3, 3, 18)
    ws.set_column(4, 4, 18)
    ws.set_column(5, 5, 2)

    title_row(ws, 1, 1, "🏛  GESTÃO FISCAL — SIMPLES NACIONAL", wb, merge_to=4, bg=CINZA_ESC, size=14)
    ws.set_row(2, 8)

    # Alíquotas
    sub_header(ws, 3, 1, "Alíquotas do Simples Nacional — Serviços (Anexo III/V)", wb, merge_to=4)
    ws.set_row(3, 20)

    headers = ["Faturamento 12 meses", "Alíquota Nominal", "Alíquota Efetiva", "Obs."]
    widths   = [30, 18, 18, 20]
    write_table_headers(ws, 4, 1, headers, widths, wb)

    aliq = [
        ("Até R$ 180.000", "6,00%", "~4,5%", "Faixa inicial — Lummé agora"),
        ("R$ 180.001 a R$ 360.000", "11,20%", "~7,0%", "Meta Fase 3–4"),
        ("R$ 360.001 a R$ 720.000", "13,50%", "~9,0%", "Meta Fase 5"),
        ("R$ 720.001 a R$ 1.800.000", "16,00%", "~11,0%", "Longo prazo"),
    ]
    for i, (fat, nom, efe, obs) in enumerate(aliq):
        r = 5 + i
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        lf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "indent": 1})
        af = wb.add_format({"bold": True, "font_size": 10, "font_color": VERMELHO, "font_name": "Calibri",
                             "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        ws.write(r, 1, fat, lf)
        ws.write(r, 2, nom, af)
        ws.write(r, 3, efe, af)
        ws.write(r, 4, obs, lf)
        ws.set_row(r, 18)

    row = 10
    ws.set_row(row, 10)
    row += 1

    # Obrigações mensais
    sub_header(ws, row, 1, "Obrigações Fiscais Mensais", wb, merge_to=4)
    row += 1

    obr_h = ["Obrigação", "Vencimento", "Responsável", "Status"]
    obr_w = [30, 18, 18, 12]
    write_table_headers(ws, row, 1, obr_h, obr_w, wb)
    row += 1

    obrigacoes = [
        ("DAS — Simples Nacional", "Dia 20 de cada mês", "Contador", "Mensal"),
        ("NFS-e (Nota Fiscal de Serviço Eletrônica)", "A cada recebimento (até 5 dias)", "Quellem", "Por venda"),
        ("INSS Pró-labore (11%)", "Dia 20 de cada mês", "Contador", "Mensal"),
        ("FGTS (se houver CLT)", "Dia 7 do mês seguinte", "Contador", "Mensal"),
        ("DEFIS (Declaração simplificada)", "Até 31/03 do ano seguinte", "Contador", "Anual"),
        ("IRPF — Declaração de IR Fundadora", "Até 30/04 do ano seguinte", "Contador", "Anual"),
    ]
    for i, (obr, venc, resp, freq) in enumerate(obrigacoes):
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        lf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "indent": 1})
        cf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        ff = wb.add_format({"bold": True, "font_size": 10, "font_color": ROXO, "font_name": "Calibri",
                             "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        ws.write(row, 1, obr, lf)
        ws.write(row, 2, venc, cf)
        ws.write(row, 3, resp, cf)
        ws.write(row, 4, freq, ff)
        ws.set_row(row, 18)
        row += 1

    row += 1
    # Pró-labore por fase
    sub_header(ws, row, 1, "Pró-labore por Fase de Crescimento", wb, merge_to=4)
    row += 1
    ph = ["Fase", "Pró-labore", "Estratégia"]
    pw = [20, 14, 28]
    write_table_headers(ws, row, 1, ph, pw, wb)
    row += 1
    prolabores = [
        ("Fase 1 — Fundação",       "R$ 0",        "Reinvestimento total — construir o ativo"),
        ("Fase 2 — Posicionamento", "R$ 2.000",    "Retirada mínima — INSS ativo"),
        ("Fase 3 — Prova Social",   "R$ 4.000",    "Equivale a analista sênior"),
        ("Fase 4 — Sistematização", "R$ 8.000",    "Pró-labore + distribuição trimestral"),
        ("Fase 5 — Escala",         "R$ 15.000",   "Pró-labore + bônus por resultado"),
    ]
    for i, (fase, valor, est) in enumerate(prolabores):
        alt = i % 2 == 0
        bg = CHAMPAGNE if alt else BRANCO
        lf = wb.add_format({"font_size": 10, "font_color": CINZA_ESC, "font_name": "Calibri",
                             "align": "left", "bg_color": bg, "border": 1, "border_color": "#E0D0D8",
                             "indent": 1})
        vf3 = wb.add_format({"bold": True, "font_size": 10, "font_color": VERDE, "font_name": "Calibri",
                              "align": "center", "bg_color": bg, "border": 1, "border_color": "#E0D0D8"})
        ws.write(row, 1, fase, lf)
        ws.write(row, 2, valor, vf3)
        ws.write(row, 3, est, lf)
        ws.set_row(row, 18)
        row += 1

    row += 1
    nota = wb.add_format({"italic": True, "font_size": 9, "font_color": CINZA_MED,
                           "font_name": "Calibri", "align": "left", "indent": 1})
    ws.merge_range(row, 1, row, 4,
                   "Nota: Pró-labore incide INSS (11%). Distribuição de lucros é isenta de IR no Simples Nacional.", nota)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN — gerar arquivo
# ══════════════════════════════════════════════════════════════════════════════

def main():
    path = os.path.join(OUTPUT_DIR, "lumme-financeiro-completo.xlsx")
    wb = xlsxwriter.Workbook(path, {"default_date_format": "dd/mm/yyyy"})

    sheet_dashboard(wb)
    sheet_receitas(wb)
    sheet_despesas(wb)
    sheet_fluxo(wb)
    sheet_dre(wb)
    sheet_precificacao(wb)
    sheet_metas(wb)
    sheet_stack(wb)
    sheet_fiscal(wb)

    wb.close()
    print(f"✅ Planilha gerada: {path}")
    return path


if __name__ == "__main__":
    main()
