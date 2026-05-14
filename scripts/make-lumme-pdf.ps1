# Lummé — Gerador de PDF (tipografia Fraunces/Inter, paleta champagne/dourado/roxo/café)
param(
    [string]$mdPath,
    [string]$pdfPath,
    [string]$title,
    [string]$sub,
    [string]$logoPath = "C:\Users\marci\Downloads\flux-logo-transparent.png"
)

function wRGB($r,$g,$b){ [int]($r + $g*256 + $b*65536) }

# Paleta Lumme — identidade visual da landing page lummeagencia.lovable.app
$CHAMPAGNE = wRGB 242 232 213   # #F2E8D5 — fundo claro, capa
$OURO      = wRGB 192 152  80   # #C09850 — dourado editorial, acentos, H3, bordas
$ROXO      = wRGB 123  63 110   # #7B3F6E — roxo queimado suave, H1, H2, header, tabela
$CAFE      = wRGB  74  44  23   # #4A2C17 — cafe profundo, body text, H4
$MARFIM    = wRGB 239 229 212   # #EFE5D4 — marfim/areia, tabelas, code blocks
$TAUPE     = wRGB 196 181 160   # #C4B5A0 — nude/taupe, texto secundario, rodape
$NUDE      = wRGB 217 205 184   # #D9CDB8 — perola, tabela linhas impares
$GRAFITE   = wRGB  46  40  38   # #2E2826 — grafite (reservado para contraste forte)
$BRANCO    = wRGB 255 255 255

$wdLeft=0; $wdCenter=1; $wdRight=2

# Tipografia — detecta Fraunces (landing page) ou usa Garamond; Inter ou Calibri
Add-Type -AssemblyName System.Drawing -ErrorAction SilentlyContinue
$_installedFonts = @()
try { $_installedFonts = (New-Object System.Drawing.Text.InstalledFontCollection).Families | ForEach-Object { $_.Name } } catch {}
$hFont = if ($_installedFonts -contains "Fraunces") { "Fraunces" } elseif ($_installedFonts -contains "Cormorant Garamond") { "Cormorant Garamond" } else { "Garamond" }
$bFont = if ($_installedFonts -contains "Inter") { "Inter" } else { "Calibri" }

function SF($sel,$nm,$sz,$bd,$col,$it=$false){
    $sel.Font.Name=$nm; $sel.Font.Size=$sz
    $sel.Font.Bold=if($bd){-1}else{0}; $sel.Font.Color=$col
    $sel.Font.Italic=if($it){-1}else{0}; $sel.Font.Underline=0
}
function PA($sel,$al,$sb=0,$sa=5,$li=0){
    $sel.ParagraphFormat.Alignment=$al
    $sel.ParagraphFormat.SpaceBefore=$sb; $sel.ParagraphFormat.SpaceAfter=$sa
    $sel.ParagraphFormat.LeftIndent=$word.CentimetersToPoints($li)
    $sel.ParagraphFormat.LineSpacingRule=0
    try { $sel.ParagraphFormat.Borders.Item(3).LineStyle=0 } catch {}
}

# H1: Roxo queimado, borda dourada embaixo — 18pt (Fraunces light, landing page style)
function RH1($t,$sel){
    PA $sel $wdLeft 16 4; SF $sel $hFont 18 $false $ROXO
    try{ $sel.TypeText($t.Trim()) }catch{}
    try{ $sel.ParagraphFormat.Borders.Item(3).LineStyle=1 }catch{}
    try{ $sel.ParagraphFormat.Borders.Item(3).Color=$OURO }catch{}
    try{ $sel.ParagraphFormat.Borders.Item(3).LineWidth=12 }catch{}
    $sel.TypeParagraph(); SF $sel $bFont 11 $false $CAFE; PA $sel $wdLeft 0 5
}
# H2: Roxo queimado — 13pt
function RH2($t,$sel){
    PA $sel $wdLeft 8 3; SF $sel $hFont 13 $false $ROXO
    try{ $sel.TypeText($t.Trim()) }catch{}
    $sel.TypeParagraph(); SF $sel $bFont 11 $false $CAFE; PA $sel $wdLeft 0 5
}
# H3: Dourado editorial — 11pt bold
function RH3($t,$sel){
    PA $sel $wdLeft 6 2; SF $sel $hFont 11 $true $OURO
    try{ $sel.TypeText($t.Trim()) }catch{}
    $sel.TypeParagraph(); SF $sel $bFont 11 $false $CAFE; PA $sel $wdLeft 0 5
}
# H4: Cafe profundo bold
function RH4($t,$sel){
    PA $sel $wdLeft 4 2; SF $sel $bFont 11 $true $CAFE
    try{ $sel.TypeText($t.Trim()) }catch{}
    $sel.TypeParagraph(); SF $sel $bFont 11 $false $CAFE; PA $sel $wdLeft 0 5
}
# Bullet: cafe com recuo
function RBullet($t,$ind,$sel){
    SF $sel $bFont 10 $false $CAFE
    PA $sel $wdLeft 0 2 (0.4+[math]::Min($ind,3)*0.4)
    try{ $sel.TypeText("  "+$t) }catch{}
    $sel.TypeParagraph(); $sel.ParagraphFormat.LeftIndent=0
}
# Body: cafe profundo 11pt
function RBody($t,$sel){
    SF $sel $bFont 11 $false $CAFE; PA $sel $wdLeft 0 4
    try{ $sel.TypeText($t) }catch{}; $sel.TypeParagraph()
}
# Blockquote: roxo italico, borda dourada esquerda
function RQuote($t,$sel){
    SF $sel $hFont 10 $false $ROXO $true; PA $sel $wdLeft 2 2 0.5
    try{ $sel.ParagraphFormat.Borders.Item(1).LineStyle=1
         $sel.ParagraphFormat.Borders.Item(1).Color=$OURO
         $sel.ParagraphFormat.Borders.Item(1).LineWidth=18 }catch{}
    try{ $sel.TypeText($t) }catch{}
    $sel.TypeParagraph()
    try{ $sel.ParagraphFormat.Borders.Item(1).LineStyle=0 }catch{}
    $sel.ParagraphFormat.LeftIndent=0; SF $sel $bFont 11 $false $CAFE
}
# Code block: Consolas sobre marfim, borda taupe esquerda
function RCode($ls,$sel){
    if ($ls.Count -eq 0) { return }
    foreach ($cl in $ls) {
        SF $sel "Consolas" 8 $false $GRAFITE; PA $sel $wdLeft 0 0 0.4
        try { $sel.ParagraphFormat.Shading.BackgroundPatternColor=$MARFIM } catch {}
        try { $sel.ParagraphFormat.Borders.Item(1).LineStyle=1
              $sel.ParagraphFormat.Borders.Item(1).Color=$TAUPE
              $sel.ParagraphFormat.Borders.Item(1).LineWidth=12 } catch {}
        $d = if ([string]::IsNullOrEmpty($cl)) { " " } else { $cl }
        try { $sel.TypeText($d) } catch {}
        $sel.TypeParagraph()
        try { $sel.ParagraphFormat.Borders.Item(1).LineStyle=0
              $sel.ParagraphFormat.Shading.BackgroundPatternColor=-1 } catch {}
        $sel.ParagraphFormat.LeftIndent=0
    }
    SF $sel $bFont 11 $false $CAFE; PA $sel $wdLeft 0 5
}
# Tabela: header roxo/branco, alternando marfim/nude
function RTable($rows,$doc,$sel){
    if ($rows.Count -eq 0) { return }
    $parsed = $rows | ForEach-Object { ,($_.Trim().TrimStart('|').TrimEnd('|') -split '\|' | ForEach-Object { $_.Trim() }) }
    $nC = ($parsed | ForEach-Object { $_.Count } | Measure-Object -Max).Maximum
    $nR = $parsed.Count
    if ($nC -lt 1 -or $nR -lt 1) { return }
    try {
        $tbl = $doc.Tables.Add($sel.Range, $nR, $nC)
        $tbl.PreferredWidthType=2; $tbl.PreferredWidth=100; $tbl.Borders.Enable=$true
        for ($ri=0; $ri -lt $nR; $ri++) {
            $row=$parsed[$ri]; $hdr=($ri -eq 0)
            for ($ci=0; $ci -lt $nC; $ci++) {
                $ct = if($ci -lt $row.Count){$row[$ci]}else{""}
                $cell=$tbl.Cell($ri+1,$ci+1); $cell.VerticalAlignment=1
                try {
                    if ($hdr)            { $cell.Shading.BackgroundPatternColor=$ROXO }
                    elseif ($ri%2 -eq 1) { $cell.Shading.BackgroundPatternColor=$NUDE }
                    else                 { $cell.Shading.BackgroundPatternColor=$MARFIM }
                } catch {}
                $rng=$cell.Range; $rng.MoveEnd(1,-1)|Out-Null
                $rng.Font.Name=if($hdr){$hFont}else{$bFont}; $rng.Font.Size=9
                $rng.Font.Bold=if($hdr){-1}else{0}
                $rng.Font.Color=if($hdr){$CHAMPAGNE}else{$CAFE}
                $rng.ParagraphFormat.SpaceBefore=2; $rng.ParagraphFormat.SpaceAfter=2
                $ct2=$ct -replace '\*\*([^*]+)\*\*','$1' -replace '\*([^*]+)\*','$1' -replace '`([^`]+)`','$1'
                try { $rng.Text=$ct2 } catch {}
            }
        }
        try {
            $er=$doc.Range($tbl.Range.End,$tbl.Range.End)
            $er.InsertParagraphAfter()
            $sel.SetRange($er.End,$er.End)
        } catch { $sel.EndKey(6)|Out-Null }
    } catch {}
    SF $sel $bFont 11 $false $CAFE; PA $sel $wdLeft 0 5
}

# ===== MAIN =====
$word = New-Object -ComObject Word.Application
$word.Visible = $false; $word.DisplayAlerts = 0
$doc = $word.Documents.Add()
$sel = $word.Selection

# Margens (ref. DOCX): top=1.75cm, bottom=2cm, left/right=2.5cm
$doc.PageSetup.PageWidth    = $word.CentimetersToPoints(21)
$doc.PageSetup.PageHeight   = $word.CentimetersToPoints(29.7)
$doc.PageSetup.TopMargin    = $word.CentimetersToPoints(1.75)
$doc.PageSetup.BottomMargin = $word.CentimetersToPoints(2)
$doc.PageSetup.LeftMargin   = $word.CentimetersToPoints(2.5)
$doc.PageSetup.RightMargin  = $word.CentimetersToPoints(2.5)

# ===== CAPA — minimalista, sem fundo =====
# Usa Fraunces (landing page) ou Player Display ou Garamond como fallback
$displayFont = if ($_installedFonts -contains "Player Display") { "Player Display" } elseif ($_installedFonts -contains "Fraunces") { "Fraunces" } else { $hFont }

# Tabela invisivel (sem fundo, sem borda) para centralizar verticalmente
$cvT = $doc.Tables.Add($sel.Range, 1, 1)
$cvT.PreferredWidthType=2; $cvT.PreferredWidth=100; $cvT.Borders.Enable=$false
$cvT.Rows.Item(1).HeightRule=1
$cvT.Rows.Item(1).Height=$word.CentimetersToPoints(25)
$cvT.Cell(1,1).VerticalAlignment=1  # wdCellAlignVerticalCenter
for ($bi=1; $bi -le 6; $bi++) {
    try { $cvT.Cell(1,1).Borders.Item($bi).LineStyle=0 } catch {}
}

$c1 = $cvT.Cell(1,1)
$sel.SetRange($c1.Range.Start, $c1.Range.Start)

# LUMMÉ — grande, centralizado, dourado leve
$sel.Font.Name=$displayFont; $sel.Font.Size=72; $sel.Font.Bold=$false
$sel.Font.Color=$OURO; $sel.Font.Italic=$false; $sel.Font.Underline=0
$sel.ParagraphFormat.Alignment=$wdCenter
$sel.ParagraphFormat.SpaceBefore=0; $sel.ParagraphFormat.SpaceAfter=18
$sel.ParagraphFormat.LineSpacingRule=0
try { $sel.ParagraphFormat.Borders.Item(3).LineStyle=0 } catch {}
try { $sel.TypeText("LUMME") } catch {}
$sel.TypeParagraph()

# AGENCIA DE MARKETING — pequeno, espaçado, bege
$sel.Font.Name="Garamond"; $sel.Font.Size=10; $sel.Font.Bold=$false
$sel.Font.Color=$TAUPE; $sel.Font.Italic=$false; $sel.Font.Underline=0
$sel.ParagraphFormat.Alignment=$wdCenter
$sel.ParagraphFormat.SpaceBefore=0; $sel.ParagraphFormat.SpaceAfter=0
try { $sel.TypeText("AGENCIA DE MARKETING") } catch {}

$sel.EndKey(6) | Out-Null
try { $sel.InsertBreak(7) } catch {}
$sel = $word.Selection

# ===== CABECALHO E RODAPE =====
try {
    $sec = $doc.Sections.Item(1)
    $sec.PageSetup.DifferentFirstPageHeaderFooter = -1

    $h = $sec.Headers.Item(1); $hr = $h.Range
    $hr.Delete() | Out-Null
    $hr.Font.Name=$bFont; $hr.Font.Size=8; $hr.Font.Bold=-1; $hr.Font.Color=$ROXO
    $hr.ParagraphFormat.Alignment=$wdLeft
    try { $hr.Text = ("Lummé  |  " + $title) } catch { $hr.Text = "Lummé" }
    try {
        $hr.ParagraphFormat.Borders.Item(3).LineStyle=1
        $hr.ParagraphFormat.Borders.Item(3).Color=$OURO
        $hr.ParagraphFormat.Borders.Item(3).LineWidth=6
    } catch {}

    $f = $sec.Footers.Item(1); $fr = $f.Range
    $fr.Delete() | Out-Null
    $fr.Font.Name=$bFont; $fr.Font.Size=8; $fr.Font.Color=$TAUPE; $fr.Font.Bold=0
    $fr.ParagraphFormat.Alignment=$wdCenter
    try { $fr.Text = "lumme.com.br" } catch {}
} catch {}

$doc.ActiveWindow.ActivePane.View.SeekView = 0
$sel = $word.Selection

# ===== PARSING MARKDOWN =====
$lines = [System.IO.File]::ReadAllLines($mdPath, [System.Text.Encoding]::UTF8)
$inCode=0; $inTable=0
$codeL = [System.Collections.Generic.List[string]]::new()
$tabL  = [System.Collections.Generic.List[string]]::new()

foreach ($ln in $lines) {
    try {
        if ($ln -match '^\s*```') {
            if ($inCode) {
                if ($inTable) { RTable $tabL $doc $sel; $tabL.Clear(); $inTable=0 }
                RCode $codeL $sel; $codeL.Clear(); $inCode=0
            } else {
                if ($inTable) { RTable $tabL $doc $sel; $tabL.Clear(); $inTable=0 }
                $inCode=1
            }
            continue
        }
        if ($inCode) { $codeL.Add($ln); continue }
        if ($ln -match '^\s*\|') {
            if ($ln -match '^\s*\|[-: |]+\|') { continue }
            $tabL.Add($ln); $inTable=1; continue
        } elseif ($inTable) { RTable $tabL $doc $sel; $tabL.Clear(); $inTable=0 }
        if ($ln -match '^# (.+)')    { RH1 $Matches[1] $sel; continue }
        if ($ln -match '^## (.+)')   { RH2 $Matches[1] $sel; continue }
        if ($ln -match '^### (.+)')  { RH3 $Matches[1] $sel; continue }
        if ($ln -match '^#### (.+)') { RH4 $Matches[1] $sel; continue }
        if ($ln -match '^-{3,}\s*$') { continue }
        if ($ln -match '^(\s*)[-*+] (.+)') { RBullet $Matches[2] ([math]::Floor($Matches[1].Length/2)) $sel; continue }
        if ($ln -match '^\s*\d+\. (.+)') { RBullet $Matches[1] 0 $sel; continue }
        if ($ln -match '^\s*> ?(.*)') { RQuote $Matches[1] $sel; continue }
        if ($ln -match '^\s*$') { continue }
        RBody $ln $sel
    } catch {}
}
if ($tabL.Count -gt 0) { RTable $tabL $doc $sel }
if ($codeL.Count -gt 0) { RCode $codeL $sel }

$doc.ExportAsFixedFormat($pdfPath, 17)
$doc.Close($false)
$word.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
Write-Host ("OK " + [math]::Round((Get-Item $pdfPath).Length/1KB,0) + "KB")
