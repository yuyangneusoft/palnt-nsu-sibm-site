from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("C:/Users/余阳/.codex/skills/guizang-ppt-skill")
OUT = ROOT / "PALNT-pdf"
HTML_OUT = OUT / "index.html"
PDF_OUT = OUT / "信息与商务管理学院-AI新商科.pdf"
TEMPLATE = SKILL / "assets" / "template-swiss.html"

TITLE = "信息与商务管理学院 · AI时代的新商科"
TOTAL = 8


def chrome(page, label):
    return f"""
    <div class="chrome-min">
      <div class="l">{TITLE}</div>
      <div class="r">{label} · {page:02d} / {TOTAL:02d}</div>
    </div>
    """


slides = f"""
<section class="slide accent" data-layout="SWISS-COVER-ASCII" data-animate="hero">
  <div class="canvas-card">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    {chrome(1, "COVER")}
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.6vh">
      <div data-anim="kicker" class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em">BUSINESS FIRST · AI AMPLIFIES</div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(8.8vw,15.4vh);line-height:.96;letter-spacing:-.025em;color:#fff">AI 越强<br/>越需要真正<span style="font-style:italic;font-weight:300">懂业务</span>的人</h1>
      <div data-anim="bottom" style="display:grid;grid-template-rows:auto auto;gap:1.6vh;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh">
        <div class="lead" style="max-width:58ch;color:rgba(255,255,255,.86);font-weight:300">技术会越来越普及，业务判断会越来越稀缺。懂客户、懂组织、懂财务、懂供应链的人，才能把 AI 变成真实生产力。</div>
        <div style="display:flex;justify-content:space-between;align-items:end">
          <div class="t-meta" style="color:rgba(255,255,255,.6)">成都东软学院 · 信息与商务管理学院</div>
          <div class="t-meta" style="color:rgba(255,255,255,.6)">SWISS STYLE DECK</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="slide split" data-layout="S03" data-animate="split-statement">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-ink" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        {chrome(2, "THESIS")}
        <div data-anim="manifesto">
          <div class="t-meta" style="color:rgba(255,255,255,.62);letter-spacing:.22em;margin-bottom:2vh">CORE JUDGEMENT</div>
          <h2 style="font-family:var(--sans),var(--sans-zh);font-size:min(7.6vw,13.2vh);line-height:.96;letter-spacing:-.025em;font-weight:200;color:#fff">技术是工具<br/>业务是方向</h2>
        </div>
        <div class="t-meta" style="color:rgba(255,255,255,.62)">BUSINESS DEFINES VALUE</div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:0">
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:3vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,8.2vh);line-height:.9;color:var(--text-primary)">01</div>
            <div><h3 style="font-size:max(18px,1.8vw);font-weight:400;margin-bottom:1vh">AI 负责生成答案</h3><p class="t-body">但它不知道什么问题真正值得解决。</p></div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:3vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,8.2vh);line-height:.9;color:var(--text-primary)">02</div>
            <div><h3 style="font-size:max(18px,1.8vw);font-weight:400;margin-bottom:1vh">业务决定问题价值</h3><p class="t-body">懂业务的人知道目标、风险、机会和取舍。</p></div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:3vh 0;border-top:1px solid var(--border-subtle);border-bottom:2px solid var(--accent)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,8.2vh);line-height:.9;color:var(--accent)">03</div>
            <div><h3 style="font-size:max(18px,1.8vw);font-weight:400;margin-bottom:1vh;color:var(--accent)">AI 放大业务能力</h3><p class="t-body">会用 AI 的业务人才，比只会工具的人更受欢迎。</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="slide grey" data-layout="S18" data-animate="why-now">
  <div class="canvas-card">
    {chrome(3, "WHY NOW")}
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:4vh">
      <div data-anim="line" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">WHY NOW</div>
        <h2 class="h-xl-zh" style="font-size:min(5.2vw,9.2vh)">为什么现在必须重估商科价值</h2>
      </div>
      <div data-anim="up" class="why-now-grid">
        <div class="card-fill"><div class="t-cat">技术平权</div><h3 class="h-md">AI 工具人人可用</h3><p class="t-body">真正拉开差距的，不再是会不会点按钮，而是知不知道按钮该为谁、为何、何时按下去。</p></div>
        <div class="card-fill"><div class="t-cat">场景稀缺</div><h3 class="h-md">业务问题越来越复杂</h3><p class="t-body">客户、成本、现金流、组织、供应风险交织在一起，需要能看懂真实场景的人。</p></div>
        <div class="card-accent"><div class="t-cat">组织需要</div><h3 class="h-md">能落地的人更值钱</h3><p class="t-body">企业最终需要的是结果，不是炫技。业务理解让 AI 输出变成可执行方案。</p></div>
      </div>
      <div class="num-mega" style="font-size:min(8.4vw,14vh);line-height:.85;color:var(--accent)">BUSINESS &gt; TOOL</div>
    </div>
  </div>
</section>

<section class="slide" data-layout="S19" data-animate="four-cards">
  <div class="canvas-card">
    {chrome(4, "MEMORY")}
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:5vh">
      <div data-anim="line" style="display:flex;flex-direction:column;gap:1.4vh">
        <div style="height:2px;background:var(--accent);width:100%"></div>
        <div class="t-meta">FOUR WORDS</div>
        <h2 class="h-xl-zh" style="font-size:min(5.6vw,9.8vh)">请记住这四个词</h2>
      </div>
      <div data-anim="up" class="four-cards">
        <div class="card-ink"><h3>懂业务</h3><p>知道真实目标在哪里。</p></div>
        <div class="card-fill"><h3>会用 AI</h3><p>把工具变成生产力。</p></div>
        <div class="card-fill"><h3>能落地</h3><p>把方案做成结果。</p></div>
        <div class="card-accent"><h3>更稀缺</h3><p>成为组织真正需要的人。</p></div>
      </div>
    </div>
  </div>
</section>

<section class="slide grey" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    {chrome(5, "MAJORS")}
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:4vh">
      <div data-anim="line" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">AI-NATIVE MAJORS</div>
        <h2 class="h-xl-zh" style="font-size:min(5.1vw,9vh)">五个专业，五种业务能力</h2>
      </div>
      <div data-anim="up" class="brief-grid">
        <div class="brief-card"><span>01</span><h3>电子商务</h3><p>懂用户，才能让 AI 内容变成真实订单。</p></div>
        <div class="brief-card"><span>02</span><h3>信息管理与信息系统</h3><p>懂流程，才能让系统真正服务企业。</p></div>
        <div class="brief-card"><span>03</span><h3>财务管理</h3><p>懂经营，才能把报表变成决策。</p></div>
        <div class="brief-card"><span>04</span><h3>供应链管理</h3><p>懂链条，才能让企业跑得更稳。</p></div>
        <div class="brief-card"><span>05</span><h3>人力资源管理</h3><p>懂组织，才能让 AI 更懂人。</p></div>
        <div class="brief-card card-accent"><span>KEY</span><h3>共同底层</h3><p>业务理解 + AI 工具 + 结果交付。</p></div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-layout="S11" data-animate="timeline-walk">
  <div class="canvas-card">
    {chrome(6, "PATH")}
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:4vh">
      <div data-anim="line" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">LEARNING PATH</div>
        <h2 class="h-xl-zh" style="font-size:min(5.2vw,9.2vh)">从“学工具”到“解决业务问题”</h2>
      </div>
      <div data-anim="timeline" class="timeline-h">
        <div class="tl-h-axis"></div>
        <div class="th-node"><div class="dot"></div><h3>理解场景</h3><p>客户、岗位、流程、风险。</p></div>
        <div class="th-node"><div class="dot"></div><h3>提出问题</h3><p>目标是什么，价值在哪里。</p></div>
        <div class="th-node"><div class="dot"></div><h3>调用 AI</h3><p>调研、生成、分析、校验。</p></div>
        <div class="th-node"><div class="dot"></div><h3>交付结果</h3><p>方案、看板、模型、复盘。</p></div>
      </div>
      <div class="t-meta">TOPCARES · PROJECT BASED LEARNING · BUSINESS FIRST</div>
    </div>
  </div>
</section>

<section class="slide" data-layout="S08" data-animate="duo-mirror">
  <div class="canvas-card">
    {chrome(7, "COMPARE")}
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:4vh">
      <div data-anim="line" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">BEFORE / AFTER</div>
        <h2 class="h-xl-zh" style="font-size:min(5.2vw,9.2vh)">只懂技术 vs 懂业务又会 AI</h2>
      </div>
      <div class="duo-compare" data-anim="up">
        <div class="col"><div class="t-cat">ONLY TOOL</div><h3>等待任务的人</h3><p>会操作工具，但不知道业务要什么；会生成内容，但不知道内容是否有价值；会做报表，但解释不了经营。</p></div>
        <div class="vrule"></div>
        <div class="col"><div class="t-cat">BUSINESS + AI</div><h3>定义问题的人</h3><p>先看懂目标，再选择工具；先判断价值，再生成方案；先理解业务，再让 AI 放大自己的判断。</p></div>
      </div>
    </div>
  </div>
</section>

<section class="slide split" data-layout="SWISS-CLOSING-ASCII" data-animate="split-statement">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1"><div class="l">08 / 08</div><div class="r">CLOSING</div></div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em;margin-bottom:1.6vh">FINAL WORD</div>
          <h2 style="font-family:var(--sans),var(--sans-zh);font-size:min(7.5vw,13.2vh);line-height:.96;letter-spacing:-.025em;font-weight:200;color:#fff">别只学工具<br/>要学会<span style="font-style:italic;font-weight:300">解决问题</span></h2>
          <div style="font-size:max(13px,1vw);line-height:1.6;color:rgba(255,255,255,.82);font-weight:300;max-width:36ch;margin-top:1.4vh">懂业务的人，才有资格把 AI 变成战斗力。</div>
        </div>
        <div class="t-meta" style="color:rgba(255,255,255,.62);position:relative;z-index:1">成都东软学院 · 信息与商务管理学院</div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min"><div class="l">TAKEAWAYS</div><div class="r">03 RULES</div></div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:0">
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle)"><div style="font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9">01</div><div><h3 style="font-weight:400;font-size:max(18px,1.8vw);margin-bottom:1vh">业务是方向</h3><p class="t-body">决定目标、价值、风险和取舍。</p></div></div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle)"><div style="font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9">02</div><div><h3 style="font-weight:400;font-size:max(18px,1.8vw);margin-bottom:1vh">AI 是放大器</h3><p class="t-body">加速调研、分析、生成和验证。</p></div></div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle);border-bottom:2px solid var(--accent)"><div style="font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9;color:var(--accent)">03</div><div><h3 style="font-weight:400;font-size:max(18px,1.8vw);margin-bottom:1vh;color:var(--accent)">结果才是答案</h3><p class="t-body">企业欢迎的不是工具人，而是业务解决者。</p></div></div>
        </div>
        <div class="t-meta" style="color:var(--text-helper);text-align:right">END · AI-NATIVE BUSINESS EDUCATION</div>
      </div>
    </div>
  </div>
</section>
"""


def build_html():
    template = TEMPLATE.read_text(encoding="utf-8")
    template = template.replace("[必填] 替换为 PPT 标题 · Deck Title", TITLE)
    template = re.sub(
        r'(<div id="deck">)[\s\S]*?(</div>\s*<div id="nav">)',
        r"\1\n" + slides + r"\n\2",
        template,
        count=1,
    )
    HTML_OUT.write_text(template, encoding="utf-8")


pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))


PAGE_W, PAGE_H = 13.333 * inch, 7.5 * inch
BLUE = colors.HexColor("#002FA7")
INK = colors.HexColor("#0A0A0A")
PAPER = colors.HexColor("#FAFAF8")
GREY = colors.HexColor("#F0F0EE")
MUTED = colors.HexColor("#525252")


def wrap_text(text, max_chars):
    lines = []
    for para in text.split("\n"):
        buf = ""
        for ch in para:
            if len(buf) >= max_chars:
                lines.append(buf)
                buf = ""
            buf += ch
        if buf:
            lines.append(buf)
    return lines


def draw_text(c, text, x, y, size=18, color=INK, max_chars=22, leading=None):
    c.setFont("STSong-Light", size)
    c.setFillColor(color)
    leading = leading or size * 1.45
    for line in wrap_text(text, max_chars):
        c.drawString(x, y, line)
        y -= leading
    return y


def header(c, page, label, dark=False):
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.white if dark else MUTED)
    c.drawString(0.65 * inch, PAGE_H - 0.45 * inch, TITLE)
    c.drawRightString(PAGE_W - 0.65 * inch, PAGE_H - 0.45 * inch, f"{label} · {page:02d}/{TOTAL:02d}")


def new_page(c, bg=PAPER, dark=False, page=1, label=""):
    c.setFillColor(bg)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    header(c, page, label, dark=dark)


def pdf_cover(c):
    new_page(c, BLUE, True, 1, "COVER")
    c.setFillColor(colors.white)
    c.setFont("STSong-Light", 42)
    c.drawString(0.85 * inch, 4.75 * inch, "AI 越强")
    c.drawString(0.85 * inch, 4.05 * inch, "越需要真正懂业务的人")
    c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.35))
    c.line(0.85 * inch, 2.25 * inch, PAGE_W - 0.85 * inch, 2.25 * inch)
    draw_text(c, "技术会越来越普及，业务判断会越来越稀缺。懂客户、懂组织、懂财务、懂供应链的人，才能把 AI 变成真实生产力。", 0.85 * inch, 1.85 * inch, 16, colors.white, 36)


def pdf_simple(c, page, title, subtitle, bullets, bg=PAPER, accent=False):
    new_page(c, bg, False, page, "FIELD NOTE")
    c.setFillColor(BLUE)
    c.rect(0.65 * inch, PAGE_H - 1.15 * inch, 1.0 * inch, 0.08 * inch, fill=1, stroke=0)
    draw_text(c, title, 0.65 * inch, PAGE_H - 1.65 * inch, 34, INK, 17, 42)
    draw_text(c, subtitle, 0.65 * inch, PAGE_H - 3.0 * inch, 15, MUTED, 45, 23)
    y = PAGE_H - 4.0 * inch
    for i, (head, body) in enumerate(bullets, 1):
        c.setFillColor(BLUE if accent and i == len(bullets) else INK)
        c.setFont("Helvetica", 28)
        c.drawString(0.75 * inch, y, f"{i:02d}")
        draw_text(c, head, 1.55 * inch, y + 0.05 * inch, 18, BLUE if accent and i == len(bullets) else INK, 20)
        y = draw_text(c, body, 1.55 * inch, y - 0.32 * inch, 12.5, MUTED, 48, 18) - 0.28 * inch


def pdf_majors(c):
    new_page(c, GREY, False, 5, "MAJORS")
    draw_text(c, "五个专业，五种业务能力", 0.65 * inch, PAGE_H - 1.35 * inch, 31, INK, 18)
    majors = [
        ("电子商务", "懂用户，才能让 AI 内容变成真实订单。"),
        ("信息管理与信息系统", "懂流程，才能让系统真正服务企业。"),
        ("财务管理", "懂经营，才能把报表变成决策。"),
        ("供应链管理", "懂链条，才能让企业跑得更稳。"),
        ("人力资源管理", "懂组织，才能让 AI 更懂人。"),
    ]
    x0, y0 = 0.65 * inch, PAGE_H - 2.25 * inch
    w, h = 3.95 * inch, 1.42 * inch
    for idx, (name, body) in enumerate(majors):
        col, row = idx % 3, idx // 3
        x, y = x0 + col * (w + 0.25 * inch), y0 - row * (h + 0.25 * inch)
        c.setFillColor(PAPER)
        c.rect(x, y - h, w, h, fill=1, stroke=0)
        c.setFillColor(BLUE)
        c.setFont("Helvetica", 18)
        c.drawString(x + 0.22 * inch, y - 0.38 * inch, f"{idx + 1:02d}")
        draw_text(c, name, x + 0.22 * inch, y - 0.74 * inch, 15, INK, 14)
        draw_text(c, body, x + 0.22 * inch, y - 1.08 * inch, 11.5, MUTED, 18, 16)
    c.setFillColor(BLUE)
    c.rect(x0 + 2 * (w + 0.25 * inch), y0 - (h + 0.25 * inch) - h, w, h, fill=1, stroke=0)
    draw_text(c, "共同底层", x0 + 2 * (w + 0.25 * inch) + 0.22 * inch, y0 - (h + 0.25 * inch) - 0.52 * inch, 16, colors.white, 14)
    draw_text(c, "业务理解 + AI 工具 + 结果交付。", x0 + 2 * (w + 0.25 * inch) + 0.22 * inch, y0 - (h + 0.25 * inch) - 0.92 * inch, 12, colors.white, 18)


def build_pdf():
    c = canvas.Canvas(str(PDF_OUT), pagesize=(PAGE_W, PAGE_H))
    pdf_cover(c)
    c.showPage()
    pdf_simple(c, 2, "技术是工具\n业务是方向", "AI 负责生成答案，但业务决定问题价值。", [
        ("AI 负责生成答案", "但它不知道什么问题真正值得解决。"),
        ("业务决定问题价值", "懂业务的人知道目标、风险、机会和取舍。"),
        ("AI 放大业务能力", "会用 AI 的业务人才，比只会工具的人更受欢迎。"),
    ], accent=True)
    c.showPage()
    pdf_simple(c, 3, "为什么现在必须重估商科价值", "工具正在平权，场景正在变复杂，组织更需要能把工具落到业务结果的人。", [
        ("技术平权", "AI 工具人人可用，会点技术不再稀缺。"),
        ("场景稀缺", "客户、成本、现金流、组织、供应风险交织在一起。"),
        ("组织需要", "企业最终需要的是结果，不是炫技。"),
    ], bg=GREY, accent=True)
    c.showPage()
    pdf_simple(c, 4, "请记住这四个词", "懂业务、会用 AI、能落地、更稀缺。", [
        ("懂业务", "知道真实目标在哪里。"),
        ("会用 AI", "把工具变成生产力。"),
        ("能落地", "把方案做成结果。"),
        ("更稀缺", "成为组织真正需要的人。"),
    ], accent=True)
    c.showPage()
    pdf_majors(c)
    c.showPage()
    pdf_simple(c, 6, "从学工具到解决业务问题", "学习路径不是工具清单，而是业务能力逐层放大。", [
        ("理解场景", "客户、岗位、流程、风险。"),
        ("提出问题", "目标是什么，价值在哪里。"),
        ("调用 AI", "调研、生成、分析、校验。"),
        ("交付结果", "方案、看板、模型、复盘。"),
    ])
    c.showPage()
    pdf_simple(c, 7, "只懂技术 vs 懂业务又会 AI", "未来岗位欢迎的不是工具人，而是业务解决者。", [
        ("只懂技术", "会操作工具，但不知道业务要什么；会生成内容，但不知道内容是否有价值。"),
        ("懂业务又会 AI", "先看懂目标，再选择工具；先判断价值，再生成方案。"),
    ], accent=True)
    c.showPage()
    new_page(c, BLUE, True, 8, "CLOSING")
    c.setFillColor(colors.white)
    c.setFont("STSong-Light", 36)
    c.drawString(0.85 * inch, 4.95 * inch, "别只学工具")
    c.drawString(0.85 * inch, 4.25 * inch, "要学会解决问题")
    c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.35))
    c.line(0.85 * inch, 2.7 * inch, PAGE_W - 0.85 * inch, 2.7 * inch)
    draw_text(c, "业务是方向。AI 是放大器。结果才是答案。企业欢迎的不是工具人，而是业务解决者。", 0.85 * inch, 2.28 * inch, 16, colors.white, 34)
    c.save()


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    build_html()
    build_pdf()
    print(HTML_OUT)
    print(PDF_OUT)
