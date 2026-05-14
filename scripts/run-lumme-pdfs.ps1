# Lummé — Gerador de PDFs completo (paleta champagne/dourado/roxo queimado/grafite)
$outDir   = "C:\Users\marci\Downloads\Lumme-PDFs"
$basePath = "C:\Users\marci\Downloads\agenciaflux_new\prospeccao"
$worker   = "C:\Users\marci\Downloads\make-lumme-pdf-bom.ps1"
if (-not (Test-Path $outDir)) { New-Item -Path $outDir -ItemType Directory -Force | Out-Null }

$docs = @(
    @{rel="00-playbook-operacional.md";                        title="Playbook Operacional Completo";         sub="Prospeccao e Vendas Lumme"},
    @{rel="01-funil-vendas.md";                                title="Funil de Vendas";                       sub="TOFU MOFU BOFU com Taxas de Conversao"},
    @{rel="02-crm-automacoes.md";                              title="CRM e Automacoes";                      sub="RD Station e Fluxos de Automacao"},
    @{rel="06-proposta-premium.md";                            title="Proposta Comercial Premium";            sub="Template com ROI Projetado"},
    @{rel="07-captura-leads.md";                               title="Sistema de Captura de Leads";           sub="Landing Pages e Automacoes"},
    @{rel="scripts\01-scripts-advogados.md";                   title="Scripts Advogados";                     sub="LinkedIn Instagram WhatsApp E-mail"},
    @{rel="scripts\02-scripts-arquitetos.md";                  title="Scripts Arquitetos";                    sub="LinkedIn Instagram E-mail"},
    @{rel="scripts\03-scripts-design-interiores.md";           title="Scripts Design de Interiores";          sub="Instagram LinkedIn E-mail"},
    @{rel="scripts\04-scripts-esteticistas-premium.md";        title="Scripts Estetica Premium";              sub="Instagram LinkedIn E-mail CFM ANVISA"},
    @{rel="scripts\05-scripts-outros-premium.md";              title="Scripts Outros Nichos Premium";         sub="Medicos Consultores Coaches Psicologos"},
    @{rel="campanhas\inbound.md";                              title="Campanhas Inbound";                     sub="Conteudo E-book Webinar SEO Trafego Pago"},
    @{rel="campanhas\outbound.md";                             title="Campanhas Outbound";                    sub="LinkedIn Instagram E-mail WhatsApp"},
    @{rel="sops\sop-prospeccao-ativa.md";                      title="SOP-PROSP-001 Prospeccao Ativa";        sub="Rotina Diaria do SDR"},
    @{rel="sops\sop-qualificacao-follow-up.md";                title="SOP-QUAL-002 Qualificacao e Follow-up"; sub="BANT+ e Cadencias de Follow-up"},
    @{rel="08-base-prospects.md";                              title="Base de Prospects";                     sub="Profissionais Liberais Premium Vitoria ES"},
    @{rel="..\servicos\catalogo-servicos.md";                  title="Catalogo de Servicos";                  sub="Estrategia e Presenca Visual para Marcas Premium"}
)

$ok = 0; $i = 0
foreach ($d in $docs) {
    $i++
    $mdPath  = Join-Path $basePath $d.rel
    $pdfFile = [System.IO.Path]::GetFileNameWithoutExtension([System.IO.Path]::GetFileName($d.rel)) + ".pdf"
    $pdfPath = Join-Path $outDir $pdfFile
    Write-Host ("[$i/" + $docs.Count + "] " + $d.title + "...")
    $result = powershell.exe -ExecutionPolicy Bypass -File $worker `
        -mdPath $mdPath -pdfPath $pdfPath `
        -title $d.title -sub $d.sub 2>&1
    if (Test-Path $pdfPath) {
        $sz = [math]::Round((Get-Item $pdfPath).Length/1KB, 0)
        Write-Host ("   OK  " + $pdfFile + " (" + $sz + " KB)")
        $ok++
    } else {
        Write-Host ("   FALHOU: " + $result)
    }
}
Write-Host ("`n" + $ok + "/" + $docs.Count + " PDFs gerados em: " + $outDir)
