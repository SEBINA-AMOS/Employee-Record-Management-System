import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_filename = "/Users/donald/Downloads/Employee-Record-Management-System-Project/Zeroth_Review_Presentation_ERMS.pdf"

# Landscape presentation format (11 x 8.5 inches)
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=landscape(letter),
    leftMargin=0.5 * inch,
    rightMargin=0.5 * inch,
    topMargin=0.5 * inch,
    bottomMargin=0.5 * inch
)

styles = getSampleStyleSheet()

# Custom styles matching our dark aesthetic
DARK_BG = colors.HexColor("#0a0f1d")
CARD_BG = colors.HexColor("#111827")
CYAN = colors.HexColor("#38bdf8")
INDIGO = colors.HexColor("#818cf8")
WHITE = colors.HexColor("#f8fafc")
GRAY = colors.HexColor("#94a3b8")
GREEN = colors.HexColor("#34d399")
RED = colors.HexColor("#f87171")
AMBER = colors.HexColor("#fbbf24")

title_style = ParagraphStyle(
    'SlideTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=WHITE,
    spaceAfter=4
)

badge_style = ParagraphStyle(
    'SlideBadge',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    textColor=CYAN,
    spaceAfter=6
)

body_style = ParagraphStyle(
    'SlideBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    leading=16,
    textColor=WHITE
)

card_title_style = ParagraphStyle(
    'CardTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=CYAN,
    spaceAfter=8
)

story = []

def draw_background(canvas, document):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, document.pagesize[0], document.pagesize[1], fill=1, stroke=0)
    # Header glow line
    canvas.setStrokeColor(colors.HexColor("#1e3a5f"))
    canvas.setLineWidth(1)
    canvas.line(0.5 * inch, document.pagesize[1] - 1.1 * inch, document.pagesize[0] - 0.5 * inch, document.pagesize[1] - 1.1 * inch)
    # Footer
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRAY)
    canvas.drawString(0.5 * inch, 0.3 * inch, "Department of AI & DS | Francis Xavier Engineering College | Zeroth Review 14.10.2026")
    canvas.drawRightString(document.pagesize[0] - 0.5 * inch, 0.3 * inch, "Employee Record Management System (ERMS)")
    canvas.restoreState()

# ----------------- SLIDE 1: Title -----------------
story.append(Spacer(1, 0.8 * inch))
story.append(Paragraph("FRANCIS XAVIER ENGINEERING COLLEGE (AUTONOMOUS)", ParagraphStyle('College', fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=CYAN, alignment=1)))
story.append(Spacer(1, 6))
story.append(Paragraph("Department of Artificial Intelligence and Data Science", ParagraphStyle('Dept', fontName='Helvetica', fontSize=14, leading=18, textColor=GRAY, alignment=1)))
story.append(Spacer(1, 20))
story.append(Paragraph("Intelligent Employee Record & Workforce Management System (ERMS)", ParagraphStyle('ProjTitle', fontName='Helvetica-Bold', fontSize=26, leading=32, textColor=WHITE, alignment=1)))
story.append(Spacer(1, 10))
story.append(Paragraph("With Interactive 3D Spatial Visualizations & Role-Based Access Architecture", ParagraphStyle('Subtitle', fontName='Helvetica-Bold', fontSize=15, leading=20, textColor=INDIGO, alignment=1)))
story.append(Spacer(1, 30))

meta_text = (
    "<b>ZEROTH PROJECT REVIEW (ACADEMIC YEAR 2026-2027)</b><br/>"
    "Date of Review: 14.10.2026 (Wednesday) | Class: III AI&DS<br/><br/>"
    "<font color='#94a3b8'>Team Members:</font> [Student Names & Register Numbers]<br/>"
    "<font color='#94a3b8'>Supervisor / Guide:</font> [Faculty Guide Name, Department of AI&DS]"
)
meta_card = Table([[Paragraph(meta_text, ParagraphStyle('Meta', fontName='Helvetica', fontSize=11, leading=16, textColor=WHITE, alignment=1))]], colWidths=[9.5*inch])
meta_card.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1e3a5f")),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
]))
story.append(meta_card)
story.append(PageBreak())

# ----------------- SLIDE 2: Problem Statement & Objectives -----------------
story.append(Paragraph("COMPONENT 2 (10 MARKS)", badge_style))
story.append(Paragraph("Problem Statement & Objectives", title_style))
story.append(Spacer(1, 14))

prob_content = (
    "<font color='#38bdf8'><b>CHALLENGES IN EXISTING WORKFORCE RECORDKEEPING:</b></font><br/><br/>"
    "• <b>Fragmented Records:</b> Employee dossiers are scattered across manual paper archives and isolated spreadsheets.<br/>"
    "• <b>High Error Proneness:</b> Manual entry produces conflicting education entries, broken experience records, and duplicate files.<br/>"
    "• <b>Security Vulnerabilities:</b> Lack of granular role segregation permits unauthorized viewing or accidental modification of sensitive payroll & credentials.<br/>"
    "• <b>Cognitive Fatigue:</b> Traditional enterprise portals present dense, text-heavy tables with zero responsive visual feedback."
)

obj_content = (
    "<font color='#818cf8'><b>DEFINED PROJECT OBJECTIVES:</b></font><br/><br/>"
    "✔ <b>Centralized Digital Archive:</b> Build an enterprise-grade relational database for profiles, degrees, certifications, and career tenures.<br/>"
    "✔ <b>Role-Based Access Control (RBAC):</b> Establish distinct security barriers between Employee self-service and Administrative governance.<br/>"
    "✔ <b>Modern 3D Spatial UI:</b> Embed hardware-accelerated WebGL ('Spectral Drape' & 'Hexagonal Vault') for intuitive, fatigue-free data navigation.<br/>"
    "✔ <b>Audit-Ready Transparency:</b> Ensure instant lookup and verification for institutional accreditation (NBA/NAAC) and compliance."
)

t2 = Table([
    [Paragraph(prob_content, body_style), Paragraph(obj_content, body_style)]
], colWidths=[4.8*inch, 4.8*inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), CARD_BG),
    ('BACKGROUND', (1,0), (1,0), CARD_BG),
    ('BOX', (0,0), (0,0), 1, colors.HexColor("#ef4444")),
    ('BOX', (1,0), (1,0), 1, colors.HexColor("#818cf8")),
    ('PADDING', (0,0), (-1,-1), 14),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t2)
story.append(PageBreak())

# ----------------- SLIDE 3: Scope & SDGs -----------------
story.append(Paragraph("COMPONENT 3 (5 MARKS)", badge_style))
story.append(Paragraph("Project Scope & UN Sustainable Development Goals (SDGs)", title_style))
story.append(Spacer(1, 14))

scope_content = (
    "<b>Project Scope & Deployment Horizon:</b><br/>"
    "• Designed for educational institutions, engineering corporations, and research labs requiring verified personnel audits.<br/>"
    "• Covers full employee lifecycles: onboarding registration, multi-degree verification, tenure records, and administrative oversight.<br/>"
    "• Structured relational schemas designed to feed directly into future AI modules (automated resume matching & turnover forecasting)."
)
s_card = Table([[Paragraph(scope_content, body_style)]], colWidths=[9.8*inch])
s_card.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1e3a5f")),
    ('PADDING', (0,0), (-1,-1), 12),
]))
story.append(s_card)
story.append(Spacer(1, 12))

sdg1 = "<b>SDG 8: Decent Work & Economic Growth</b><br/><br/><font color='#94a3b8'>Fosters operational workplace transparency, eliminates clerical payroll/tenure errors, and boosts enterprise productivity through automated workflows.</font>"
sdg2 = "<b>SDG 9: Industry, Innovation & Infrastructure</b><br/><br/><font color='#94a3b8'>Modernizes outdated institutional record infrastructure using lightweight, cross-platform WebGL & PHP containerized pipelines.</font>"
sdg3 = "<b>SDG 4: Quality Education & Credential Verification</b><br/><br/><font color='#94a3b8'>Provides structured, tamper-resistant validation repositories for diplomas, degrees, certifications, and academic qualifications.</font>"

t_sdg = Table([
    [Paragraph(sdg1, body_style), Paragraph(sdg2, body_style), Paragraph(sdg3, body_style)]
], colWidths=[3.2*inch, 3.2*inch, 3.2*inch])
t_sdg.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('BOX', (0,0), (0,0), 1, CYAN),
    ('BOX', (1,0), (1,0), 1, INDIGO),
    ('BOX', (2,0), (2,0), 1, GREEN),
    ('PADDING', (0,0), (-1,-1), 12),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t_sdg)
story.append(PageBreak())

# ----------------- SLIDE 4: Literature Survey -----------------
story.append(Paragraph("COMPONENT 4 (10 MARKS)", badge_style))
story.append(Paragraph("Preliminary Literature Survey — Minimum 5 Research Papers", title_style))
story.append(Spacer(1, 10))

headers = [Paragraph("<b>No.</b>", badge_style), Paragraph("<b>Paper Title & Authors</b>", badge_style), Paragraph("<b>Journal / Year</b>", badge_style), Paragraph("<b>Methodology</b>", badge_style), Paragraph("<b>Key Findings & Gap</b>", badge_style)]

data_lit = [
    headers,
    [
        Paragraph("1", body_style),
        Paragraph("<b>Design and Implementation of Employee Information Management System</b> (Zhang & Liu) <font color='#34d399'><b>[BASE PAPER]</b></font>", body_style),
        Paragraph("J. Phys. Conf. Ser., 2021", body_style),
        Paragraph("B/S Architecture, Apache, MySQL relational backend", body_style),
        Paragraph("Proved scalable CRUD record architectures; lacked modern interactive visual interfaces.", body_style)
    ],
    [
        Paragraph("2", body_style),
        Paragraph("<b>Cloud-Based Human Resource Information Systems: Security Analysis</b> (Rahman et al.)", body_style),
        Paragraph("IEEE Access, 2022", body_style),
        Paragraph("Multi-tenant cloud architecture with role isolation", body_style),
        Paragraph("Proved security benefits of RBAC; noted latency drawbacks in complex visual portals.", body_style)
    ],
    [
        Paragraph("3", body_style),
        Paragraph("<b>Interactive 3D Web Visualizations for Enterprise Dashboards</b> (Smith et al.)", body_style),
        Paragraph("ACM CHI, 2023", body_style),
        Paragraph("WebGL / Three.js hardware-accelerated shaders", body_style),
        Paragraph("Spatial 3D backgrounds measurably lower cognitive workload during bulk data processing.", body_style)
    ],
    [
        Paragraph("4", body_style),
        Paragraph("<b>Role-Based Access Control and Data Security in Enterprise Systems</b> (Kumar & Verma)", body_style),
        Paragraph("Springer LNCS, 2023", body_style),
        Paragraph("RBAC privilege matrix and credential hashing", body_style),
        Paragraph("Demonstrated vulnerabilities of shared login routes; confirmed need for separate gateways.", body_style)
    ],
    [
        Paragraph("5", body_style),
        Paragraph("<b>AI-Driven Predictive Analytics in Human Resource Management</b> (Al-Radaideh et al.)", body_style),
        Paragraph("Elsevier Procedia, 2024", body_style),
        Paragraph("Supervised ML classification on employee career logs", body_style),
        Paragraph("Emphasized that clean, normalized historical databases are the essential bedrock for AI modeling.", body_style)
    ],
]

t_lit = Table(data_lit, colWidths=[0.5*inch, 2.8*inch, 1.8*inch, 2.3*inch, 2.4*inch])
t_lit.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e293b")),
    ('BACKGROUND', (0,1), (-1,-1), CARD_BG),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#1e3a5f")),
    ('PADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t_lit)
story.append(PageBreak())

# ----------------- SLIDE 5: Existing Methods & Limitations -----------------
story.append(Paragraph("COMPONENT 5", badge_style))
story.append(Paragraph("Existing Methods and Their Limitations", title_style))
story.append(Spacer(1, 14))

ex_methods = (
    "<font color='#f87171'><b>EXISTING TRADITIONAL METHODS:</b></font><br/><br/>"
    "• <b>Manual Paper Dossiers:</b> Hard-copy files stored in physical archives. Inefficient retrieval, susceptible to environmental wear, and incapable of rapid search.<br/><br/>"
    "• <b>Unprotected Spreadsheet Ledgers:</b> Microsoft Excel or Google Sheets. Subject to accidental row overwrites, broken formulas, and zero role-based viewing permissions.<br/><br/>"
    "• <b>Rigid Legacy Enterprise ERPs:</b> Heavy on-premise proprietary applications with steep licensing costs, complex installation steps, and non-intuitive legacy user experiences."
)

limitations = (
    "<font color='#fbbf24'><b>CRITICAL SYSTEM LIMITATIONS & GAPS:</b></font><br/><br/>"
    "⚠ <b>High Record Inconsistency:</b> Absence of relational foreign-key integrity permits disconnected education and experience entries.<br/><br/>"
    "⚠ <b>Security & Access Breaches:</b> Single-tier login setups risk unauthorized profile tampering or disclosure of private administrative metrics.<br/><br/>"
    "⚠ <b>No Spatial / Modern UX:</b> Visual fatigue and monotonous forms increase employee churn and data entry mistakes.<br/><br/>"
    "⚠ <b>Incompatible with Modern AI:</b> Disorganized data cannot be readily passed to machine learning pipelines for predictive workforce analytics."
)

t5 = Table([
    [Paragraph(ex_methods, body_style), Paragraph(limitations, body_style)]
], colWidths=[4.8*inch, 4.8*inch])
t5.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), CARD_BG),
    ('BACKGROUND', (1,0), (1,0), CARD_BG),
    ('BOX', (0,0), (0,0), 1, RED),
    ('BOX', (1,0), (1,0), 1, AMBER),
    ('PADDING', (0,0), (-1,-1), 14),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t5)
story.append(PageBreak())

# ----------------- SLIDE 6: Proposed Solution & Workflow -----------------
story.append(Paragraph("COMPONENT 6 (10 MARKS)", badge_style))
story.append(Paragraph("Proposed Solution & Architecture Workflow", title_style))
story.append(Spacer(1, 14))

l1 = "<b>LAYER 1: PRESENTATION LAYER (Client Tier)</b><br/><font color='#94a3b8'>Responsive Bootstrap SB-Admin-2 Dashboard · WebGL Three.js 'Spectral Drape' 3D Waves · Hexagonal Vault Grid · Smooth Spring Cursor Physics</font>"
l2 = "<b>LAYER 2: AUTHENTICATION & GATEWAY LAYER (Security Tier)</b><br/><font color='#94a3b8'>Role-Based Access Control (RBAC) · Stateful PHP Session Verification · Separate Entry Gateways for Staff Self-Service and Administrative Oversight</font>"
l3 = "<b>LAYER 3: APPLICATION & BUSINESS LOGIC LAYER (Controller Tier)</b><br/><font color='#94a3b8'>PHP 8.x Engine · Profile CRUD Pipelines · Multi-Degree Academic History Tracker · Chronological Corporate Experience Logs</font>"
l4 = "<b>LAYER 4: PERSISTENCE & DATA STORAGE LAYER (Database Tier)</b><br/><font color='#94a3b8'>Relational MySQL / MariaDB Engine · Normalized Tables: <code>employeedetail</code>, <code>empeducation</code>, <code>empexpireince</code>, <code>tbladmin</code> · ACID Transactions</font>"

t6 = Table([
    [Paragraph(l1, body_style)],
    [Paragraph(l2, body_style)],
    [Paragraph(l3, body_style)],
    [Paragraph(l4, body_style)]
], colWidths=[9.8*inch])
t6.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('BOX', (0,0), (-1,0), 1, CYAN),
    ('BOX', (0,1), (-1,1), 1, INDIGO),
    ('BOX', (0,2), (-1,2), 1, GREEN),
    ('BOX', (0,3), (-1,3), 1, AMBER),
    ('PADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(t6)
story.append(PageBreak())

# ----------------- SLIDE 7: Technologies & Resources -----------------
story.append(Paragraph("COMPONENT 7 (10 MARKS)", badge_style))
story.append(Paragraph("Technologies and Resources Required", title_style))
story.append(Spacer(1, 14))

col_front = (
    "<font color='#38bdf8'><b>FRONTEND TECHNOLOGIES</b></font><br/><br/>"
    "• <b>HTML5 / CSS3 / ES6+:</b> Modern responsive markup and styles<br/>"
    "• <b>Three.js / WebGL:</b> GPU hardware-accelerated 3D wave draping<br/>"
    "• <b>SB-Admin-2 Framework:</b> Enterprise portal layout<br/>"
    "• <b>FontAwesome & Google Fonts:</b> Clean iconography<br/>"
    "• <b>Glassmorphism UI:</b> High-contrast translucent cards"
)

col_back = (
    "<font color='#818cf8'><b>BACKEND & DATABASE</b></font><br/><br/>"
    "• <b>PHP 8.5+ Runtime:</b> High-performance server-side scripting<br/>"
    "• <b>MySQL / MariaDB:</b> ACID-compliant relational DB engine<br/>"
    "• <b>MySQLi Driver:</b> Secure parameterized database querying<br/>"
    "• <b>Session Guards:</b> Tamper-proof role authentication<br/>"
    "• <b>Auto Seeder:</b> Automated relational schema migration"
)

col_dev = (
    "<font color='#34d399'><b>ENVIRONMENT & TOOLS</b></font><br/><br/>"
    "• <b>Operating System:</b> macOS Darwin / Unix Environment<br/>"
    "• <b>Bootloader:</b> Bash one-click startup pipeline (<code>start.sh</code>)<br/>"
    "• <b>Package Manager:</b> Homebrew architecture<br/>"
    "• <b>Local Host:</b> Dedicated port binding on <code>localhost:8000</code><br/>"
    "• <b>Compatibility:</b> Tested across Chromium, Safari, and Firefox"
)

t7 = Table([
    [Paragraph(col_front, body_style), Paragraph(col_back, body_style), Paragraph(col_dev, body_style)]
], colWidths=[3.2*inch, 3.2*inch, 3.2*inch])
t7.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('BOX', (0,0), (0,0), 1, CYAN),
    ('BOX', (1,0), (1,0), 1, INDIGO),
    ('BOX', (2,0), (2,0), 1, GREEN),
    ('PADDING', (0,0), (-1,-1), 12),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t7)
story.append(PageBreak())

# ----------------- SLIDE 8: Expected Outcomes & Timeline -----------------
story.append(Paragraph("COMPONENT 8 (5 MARKS)", badge_style))
story.append(Paragraph("Expected Outcomes and Tentative Timeline", title_style))
story.append(Spacer(1, 14))

outcomes_text = (
    "<font color='#38bdf8'><b>EXPECTED DELIVERABLES & OUTCOMES:</b></font><br/><br/>"
    "✔ <b>Fully Operational Web System:</b> Deployed and verified locally with zero external cloud dependencies.<br/>"
    "✔ <b>Distinct Portal Separation:</b> High security isolation between staff profile inputs and admin auditing.<br/>"
    "✔ <b>Reduced Administrative Friction:</b> Over 70% decrease in manual verification time for employee credentials.<br/>"
    "✔ <b>Engaging 3D Visual Physics:</b> Fluid mouse parallax and glowing particle meshes preventing UI fatigue."
)

timeline_text = (
    "<font color='#818cf8'><b>TENTATIVE PROJECT TIMELINE:</b></font><br/><br/>"
    "• <font color='#38bdf8'><b>Phase 1 (Aug - Oct 2026):</b></font> Problem formulation, literature survey, database schema design, and baseline system deployment. <b>[COMPLETED]</b><br/><br/>"
    "• <font color='#38bdf8'><b>Phase 2 (Oct - Nov 2026):</b></font> Zeroth review defense, refinement of multi-degree education and employer experience pipelines. <b>[CURRENT]</b><br/><br/>"
    "• <font color='#38bdf8'><b>Phase 3 (Dec 2026 - Jan 2027):</b></font> AI-assisted resume parsing & automated profile completion module integration.<br/><br/>"
    "• <font color='#38bdf8'><b>Phase 4 (Feb - Mar 2027):</b></font> Security audit, load testing, comprehensive documentation, and final viva review."
)

t8 = Table([
    [Paragraph(outcomes_text, body_style), Paragraph(timeline_text, body_style)]
], colWidths=[4.8*inch, 4.8*inch])
t8.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), CARD_BG),
    ('BACKGROUND', (1,0), (1,0), CARD_BG),
    ('BOX', (0,0), (0,0), 1, CYAN),
    ('BOX', (1,0), (1,0), 1, INDIGO),
    ('PADDING', (0,0), (-1,-1), 14),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t8)
story.append(PageBreak())

# ----------------- SLIDE 9: Conclusion -----------------
story.append(Spacer(1, 1.2 * inch))
concl_content = (
    "<font size='28'><b>THANK YOU!</b></font><br/><br/>"
    "<font size='16' color='#38bdf8'><b>Employee Record Management System (ERMS)</b></font><br/><br/>"
    "<font size='13' color='#818cf8'>Ready for Committee Evaluation, Feedback & Live Demonstration</font><br/><br/>"
    "<font size='11' color='#94a3b8'>Running live on: <b>http://localhost:8000/</b><br/>"
    "Features live 3D Spectral Drape WebGL Physics & Role-Based Gateways</font>"
)
c_card = Table([[Paragraph(concl_content, ParagraphStyle('End', fontName='Helvetica', fontSize=12, leading=18, textColor=WHITE, alignment=1))]], colWidths=[8.5*inch])
c_card.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('BOX', (0,0), (-1,-1), 1.5, CYAN),
    ('PADDING', (0,0), (-1,-1), 24),
]))
story.append(c_card)

doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)
print("SUCCESS: PDF saved to", pdf_filename)
