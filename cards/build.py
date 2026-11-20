"""Cartões SVG próprios do perfil do Kim, no visual 'deep-sky' do galaxy-profile (sem copiar código)."""
import random, html, os
BG="#0b1020"; TXT="#eef1f6"; DIM="#9ca0a9"; BLUE="#9fbcff"; WARM="#fff3dc"; ACC="#ffb020"
FONT="Spectral, Georgia, 'Times New Roman', serif"
import sys
LANG=(sys.argv[1] if len(sys.argv)>1 else "en")
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets","cards",LANG); os.makedirs(OUT,exist_ok=True)
PT=LANG=="pt"
T=lambda en,pt: pt if PT else en
e=html.escape
def dust(w,h,n,seed):
    r=random.Random(seed); s=[]
    for _ in range(n):
        x,y=r.uniform(0,w),r.uniform(0,h); o=r.uniform(.15,.6); rad=r.choice([.4,.5,.7,.9])
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="#fff" opacity="{o:.2f}"/>')
    return "".join(s)
def star(x,y,c=BLUE,big=False):
    g=9 if big else 6
    return (f'<circle cx="{x}" cy="{y}" r="{g}" fill="url(#h{c[1:]})"/>'
            f'<circle cx="{x}" cy="{y}" r="{2.2 if big else 1.6}" fill="#fff"/>')
def defs():
    out=""
    for c in (BLUE,WARM,ACC):
        out+=(f'<radialGradient id="h{c[1:]}"><stop offset="0" stop-color="{c}" stop-opacity=".75"/>'
              f'<stop offset=".35" stop-color="{c}" stop-opacity=".2"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>')
    return f"<defs>{out}</defs>"
def wrap(t,n):
    w,l=[], ""
    for p in t.split():
        if len(l)+len(p)+1>n: w.append(l); l=p
        else: l=(l+" "+p).strip()
    return w+[l]
def card(name,w,h,body,title,desc):
    svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">'
         f'<title id="t">{e(title)}</title><desc id="d">{e(desc)}</desc>{defs()}'
         f'<rect width="{w}" height="{h}" rx="14" fill="{BG}"/>{dust(w,h,int(w*h/2500),name)}{body}</svg>')
    open(os.path.join(OUT,name+".svg"),"w").write(svg)

# 1) Sistemas, agrupados por tema e em linguagem de quem não é da área
GROUPS=[
 (T("Getting paid for the care delivered","Receber pelo atendimento prestado"), ACC, [
   (T("SUS billing check","Conferência do faturamento SUS"),T("Catches errors in hospital and clinic billing before it goes to the Ministry of Health, so the city is not underpaid.","Encontra erros na produção dos hospitais e clínicas antes do envio ao Ministério da Saúde, para o município não receber a menos.")),
   (T("Procedure price table","Tabela de procedimentos e preços"),T("Keeps the national list of procedures and prices, month by month, as the basis for every calculation.","Mantém a tabela nacional de procedimentos e valores, mês a mês, como base de todos os cálculos."))]),
 (T("Patients waiting for care","Pacientes à espera de atendimento"), WARM, [
   (T("Waiting-list analytics","Análise das filas"),T("Shows who is waiting for which exam or surgery, for how long, and what it costs to clear the line.","Mostra quem espera por qual exame ou cirurgia, há quanto tempo, e quanto custa zerar a fila.")),
   (T("Live health-network panels","Painéis da rede em tempo real"),T("Real-time view of the city's clinics and emergency units for the management team.","Visão em tempo real das unidades de saúde e de urgência do município para a gestão."))]),
 (T("Contracts and public money","Contratos e dinheiro público"), BLUE, [
   (T("Hospital and clinic accountability","Prestação de contas dos prestadores"),T("Checks every month that contracted providers did what they billed, before payment is released.","Confere todo mês se os prestadores contratados fizeram o que cobraram, antes de liberar o pagamento.")),
   (T("Partnerships with nonprofits","Parcerias com entidades sem fins lucrativos"),T("Ready-made documents and review steps for hiring health nonprofits under the national partnership law.","Documentos prontos e etapas de revisão para firmar parcerias com entidades de saúde sem fins lucrativos.")),
   (T("Procurement and accreditation","Credenciamentos e compras"),T("Runs public calls to contract doctors and clinics, from planning to publication on the national portal.","Conduz os chamamentos para contratar médicos e clínicas, do planejamento à publicação no portal nacional.")),
   (T("Market price research","Banco de preços"),T("Finds what other public bodies paid for the same item, to set fair prices.","Encontra quanto outros órgãos públicos pagaram pelo mesmo item, para definir preços justos."))]),
 (T("Paperwork, people and training","Processos, pessoas e formação"), BLUE, [
   (T("Process and signature tracker","Acompanhamento de processos e assinaturas"),T("Follows official processes and signatures in the city's e-protocol and warns when something stalls.","Acompanha processos e assinaturas no protocolo eletrônico da Prefeitura e avisa quando algo para.")),
   (T("Health residency portal","Portal das residências em saúde"),T("Evaluations, grades and records for the city's residency programs in health.","Avaliações, notas e registros dos programas de residência em saúde do município.")),
   (T("Events and certificates","Eventos e certificados"),T("Sign-up and certificates for health-department courses and events.","Inscrições e certificados dos cursos e eventos da Secretaria de Saúde.")),
   (T("Medicine stock","Estoque de medicamentos"),T("Pharmacy supply and dispensing control (in testing).","Controle de estoque e dispensação da farmácia (em testes).")),
   (T("Electronic invoices","Notas fiscais eletrônicas"),T("Issues service invoices for small health businesses, checking them before they are sent.","Emite notas fiscais de serviço para pequenos negócios de saúde, conferindo antes do envio."))]),
]
W=850; H=96
for g,_,items in GROUPS: H+=34+sum(26+14*len(wrap(d,112)) for _,d in items)
H+=10
b=(f'<text x="44" y="46" font-family="{FONT}" font-size="22" fill="{TXT}">{T("What I have built","O que construí")}</text>'
   f'<text x="44" y="68" font-family="{FONT}" font-style="italic" font-size="13" fill="{DIM}">{T("Systems running in the Vilhena Municipal Health Department. The code is private because it handles patient data.","Sistemas em uso na Secretaria Municipal de Saúde de Vilhena. O código é privado porque lida com dados de pacientes.")}</text>')
y=100
for g,col,items in GROUPS:
    b+=star(51,y,col,big=True)+f'<text x="70" y="{y+5}" font-family="{FONT}" font-size="16.5" fill="{TXT}">{e(g)}</text>'
    y+=30
    for n,d in items:
        b+=(f'<text x="70" y="{y}" font-family="{FONT}" font-size="13.5" fill="{TXT}">{e(n)}</text>')
        ls=wrap(d,112)
        for k,l in enumerate(ls):
            b+=f'<text x="70" y="{y+16+k*14}" font-family="{FONT}" font-style="italic" font-size="11.5" fill="{DIM}">{e(l)}</text>'
        y+=26+14*len(ls)
    y+=4
card("systems",W,H,b,"What I have built","Thirteen systems for municipal public health, grouped by what they do.")

# 2) Como construo com LLMs
PR=[(T("Verification lives outside the model","A verificação fica fora do modelo"),T("An action closes on an external check, never on the agent's own report.","Uma ação só termina com uma conferência externa, nunca com o relato do próprio agente.")),
(T("Cross-model adversarial review","Revisão adversária entre modelos"),T("Legal and financial documents are attacked by another model family.","Documentos jurídicos e financeiros são atacados por um modelo de outra família.")),
(T("Human gates on the irreversible","Aprovação humana no irreversível"),T("Signing, sending, publishing and deploying stop for explicit approval.","Assinar, enviar, publicar e colocar no ar param à espera de aprovação explícita.")),
(T("Monitors measure progress","Vigias medem progresso"),T("Watchers track whether work advances, fail loudly and expire.","Vigias acompanham se o trabalho avança, avisam quando falham e se encerram sozinhos.")),
(T("Knowledge as versioned procedures","Conhecimento em procedimentos versionados"),T("Rules learned from incidents live in reviewed, versioned skills.","Regras aprendidas com incidentes viram procedimentos revisados e versionados."))]
H2=96+len(PR)*52+16
b=(f'<text x="44" y="46" font-family="{FONT}" font-size="22" fill="{TXT}">{T("How I build with LLMs","Como trabalho com IA")}</text>'
   f'<text x="44" y="68" font-family="{FONT}" font-style="italic" font-size="13" fill="{DIM}">{T("Model output is an untrusted proposal until something outside the model confirms it.","O que o modelo produz é uma proposta até que algo fora dele confirme.")}</text>')
for i,(t,d) in enumerate(PR):
    y=104+i*52
    b+=f'<line x1="51" y1="{y}" x2="51" y2="{y+52}" stroke="{BLUE}" stroke-opacity=".25"/>' if i<len(PR)-1 else ""
    b+=star(51,y,WARM,big=True)
    b+=(f'<text x="72" y="{y+5}" font-family="{FONT}" font-size="15.5" fill="{TXT}">{e(t)}</text>'
        f'<text x="72" y="{y+24}" font-family="{FONT}" font-style="italic" font-size="12" fill="{DIM}">{e(d)}</text>')
card("principles",W,H2,b,"How I build with LLMs","Five working principles for agents in public health.")

# 3) Stack declarada (não calculada)
ST=[(T("Health data & billing","Dados de saúde e faturamento"),"Python · PostgreSQL · SQL · DATASUS (SIA/SIH, SIGTAP)"),
(T("Web systems","Sistemas web"),"TypeScript · Node.js · FastAPI · Nginx · Docker"),
(T("Agents & automation","Agentes e automação"),T("Claude · multi-model review · MCP · cron watchers","Claude · revisão entre modelos · MCP · vigias agendados")),
(T("Desktop & tooling","Desktop e ferramentas"),"C# / .NET · PowerShell · Bash")]
H3=96+len(ST)*40+10
b=(f'<text x="44" y="46" font-family="{FONT}" font-size="22" fill="{TXT}">Stack</text>'
   f'<text x="44" y="68" font-family="{FONT}" font-style="italic" font-size="13" fill="{DIM}">{T("Declared, not measured: most of the code is private.","Declarada, não medida: quase todo o código é privado.")}</text>')
for i,(t,d) in enumerate(ST):
    y=104+i*40
    b+=star(51,y,BLUE)
    b+=(f'<text x="72" y="{y+5}" font-family="{FONT}" font-size="15" fill="{TXT}">{e(t)}</text>'
        f'<text x="300" y="{y+5}" font-family="{FONT}" font-style="italic" font-size="13" fill="{DIM}">{e(d)}</text>')
card("stack",W,H3,b,"Stack","Declared technology stack.")
print("ok", os.listdir(OUT))
