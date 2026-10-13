import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    DARK_BG = RGBColor(10, 15, 29)
    CARD_BG = RGBColor(17, 24, 39)
    CYAN = RGBColor(56, 189, 248)
    INDIGO = RGBColor(99, 102, 241)
    WHITE = RGBColor(248, 250, 252)
    GRAY = RGBColor(148, 163, 184)
    BORDER_CYAN = RGBColor(30, 58, 95)

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = DARK_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="ZEROTH REVIEW PRESENTATION"):
        badge_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8), Inches(0.4))
        tf_b = badge_box.text_frame
        tf_b.word_wrap = True
        p_b = tf_b.paragraphs[0]
        p_b.text = category_text.upper()
        p_b.font.size = Pt(11)
        p_b.font.bold = True
        p_b.font.color.rgb = CYAN

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.5), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = WHITE

    # ---------------- SLIDE 1: Title Slide ----------------
    s1 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s1)

    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.0), Inches(11.3), Inches(5.5))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "FRANCIS XAVIER ENGINEERING COLLEGE (AUTONOMOUS)"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    p0.alignment = PP_ALIGN.CENTER

    p1 = tf1.add_paragraph()
    p1.text = "Department of Artificial Intelligence and Data Science"
    p1.font.size = Pt(16)
    p1.font.color.rgb = GRAY
    p1.alignment = PP_ALIGN.CENTER
    p1.space_after = Pt(24)

    p2 = tf1.add_paragraph()
    p2.text = "Intelligent Employee Record & Workforce Management System (ERMS)"
    p2.font.size = Pt(32)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf1.add_paragraph()
    p3.text = "With Interactive 3D Spatial Visualizations & Role-Based Access Architecture"
    p3.font.size = Pt(18)
    p3.font.color.rgb = INDIGO
    p3.alignment = PP_ALIGN.CENTER
    p3.space_after = Pt(36)

    p4 = tf1.add_paragraph()
    p4.text = "ZEROTH PROJECT REVIEW (ACADEMIC YEAR 2026-2027)\nDate of Review: 14.10.2026"
    p4.font.size = Pt(14)
    p4.font.color.rgb = CYAN
    p4.alignment = PP_ALIGN.CENTER
    p4.space_after = Pt(20)

    p5 = tf1.add_paragraph()
    p5.text = "Team Members: [Student Name(s) & Register Numbers]  |  Supervisor / Guide: [Guide Name]"
    p5.font.size = Pt(13)
    p5.font.color.rgb = GRAY
    p5.alignment = PP_ALIGN.CENTER

    # ---------------- SLIDE 2: Problem Statement & Objectives ----------------
    s2 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s2)
    add_header(s2, "Problem Statement & Objectives", "Component 2 (10 Marks)")

    card1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = BORDER_CYAN
    tf = card1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "PROBLEM STATEMENT"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.space_after = Pt(14)
    bullets1 = [
        "Traditional HR & Employee records are scattered across physical paper dossiers or isolated spreadsheet files.",
        "High risk of human data entry errors, accidental duplication, and inconsistent career tracking.",
        "Severe vulnerability to unauthorized access and lack of distinct privilege tiering for employee self-service.",
        "Legacy enterprise systems suffer from steep learning curves, cluttered tables, and zero interactive visualization."
    ]
    for b in bullets1:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13)
        p.font.color.rgb = WHITE
        p.space_after = Pt(10)

    card2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    card2.fill.solid()
    card2.fill.fore_color.rgb = CARD_BG
    card2.line.color.rgb = BORDER_CYAN
    tf2 = card2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "PROJECT OBJECTIVES"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = INDIGO
    p.space_after = Pt(14)
    bullets2 = [
        "Build a centralized web-based repository for employee profiles, education histories, and industry experience.",
        "Implement strict Role-Based Access Control (RBAC) separating Administrative governance from Employee self-service.",
        "Integrate modern 3D WebGL spatial aesthetics (Spectral Drape) and smooth interactive physics for improved usability.",
        "Provide real-time organizational metrics (total headcount, roster audits, profile modification pipelines)."
    ]
    for b in bullets2:
        p = tf.add_paragraph()
        p.text = "✔ " + b
        p.font.size = Pt(13)
        p.font.color.rgb = WHITE
        p.space_after = Pt(10)

    # ---------------- SLIDE 3: Scope & Relevance to SDGs ----------------
    s3 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s3)
    add_header(s3, "Project Scope & UN Sustainable Development Goals (SDGs)", "Component 3 (5 Marks)")

    card_scope = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(2.2))
    card_scope.fill.solid()
    card_scope.fill.fore_color.rgb = CARD_BG
    card_scope.line.color.rgb = BORDER_CYAN
    tf = card_scope.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "PROJECT SCOPE & APPLICATION HORIZON"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.space_after = Pt(8)
    scope_points = (
        "• Scalable architecture designed for educational institutions, engineering corporations, and SMEs.\n"
        "• Provides seamless management of multi-degree educational background records & chronological corporate tenures.\n"
        "• Designed with AI-ready relational tables to support future intelligent modules like talent attrition prediction."
    )
    p2 = tf.add_paragraph()
    p2.text = scope_points
    p2.font.size = Pt(13)
    p2.font.color.rgb = WHITE

    # SDG Cards
    sdgs = [
        ("SDG 8: Decent Work & Economic Growth", "Fosters operational workplace transparency, prevents record tampering, and optimizes human resource management efficiency through automation.", CYAN),
        ("SDG 9: Industry, Innovation & Infrastructure", "Upgrades legacy administrative infrastructure into high-speed modern digital platforms using WebGL and responsive web technologies.", INDIGO),
        ("SDG 4: Quality Education & Credential Verification", "Provides structured audit repositories for employee degrees, certifications, and academic validation.", RGBColor(16, 185, 129))
    ]
    for i, (title, desc, col) in enumerate(sdgs):
        x = Inches(0.8 + i * 4.0)
        c = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(4.3), Inches(3.7), Inches(2.6))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = col
        tf_s = c.text_frame
        tf_s.word_wrap = True
        p_t = tf_s.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = col
        p_t.space_after = Pt(8)
        p_d = tf_s.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = WHITE

    # ---------------- SLIDE 4: Literature Survey Table ----------------
    s4 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s4)
    add_header(s4, "Preliminary Literature Survey — Research Papers", "Component 4 (10 Marks)")

    rows, cols = 6, 5
    table_shape = s4.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.1))
    table = table_shape.table
    table.columns[0].width = Inches(0.8)
    table.columns[1].width = Inches(3.2)
    table.columns[2].width = Inches(2.2)
    table.columns[3].width = Inches(2.7)
    table.columns[4].width = Inches(2.8)

    headers = ["No.", "Paper Title & Authors", "Publication / Year", "Methodology / Approach", "Key Findings & Limitations"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(30, 41, 59)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = CYAN

    data = [
        ("1", "Design and Implementation of Employee Information Management System (Zhang & Liu) [BASE PAPER]", "J. Phys. Conf. Ser., 2021", "Browser/Server (B/S) model, Apache, MySQL relational backend", "Established scalable CRUD & record schemas; lacked modern interactive UI and 3D visual cues."),
        ("2", "Cloud-Based Human Resource Information Systems: Security Analysis (Rahman et al.)", "IEEE Access, 2022", "Multi-tenant cloud architecture with role isolation", "Proved security benefits of RBAC; observed high latency in heavy visual rendering."),
        ("3", "Interactive 3D Web Visualizations for Enterprise Dashboards (Smith et al.)", "ACM CHI, 2023", "WebGL / Three.js hardware-accelerated shaders", "Demonstrated that spatial 3D background feedback reduces user task fatigue in portals."),
        ("4", "Role-Based Access Control and Data Security in Enterprise Systems (Kumar & Verma)", "Springer LNCS, 2023", "RBAC privilege matrices and cryptographic validation", "Highlighted vulnerabilities of unified login routes; recommended strict gatekeeping."),
        ("5", "AI-Driven Predictive Analytics in Human Resource Management (Al-Radaideh et al.)", "Elsevier Procedia, 2024", "Machine learning classifiers on employee profile records", "Confirmed that clean, structured historical records are the essential foundation for AI HR modeling.")
    ]

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.color.rgb = WHITE if j != 0 else CYAN

    # ---------------- SLIDE 5: Existing Methods vs Limitations ----------------
    s5 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s5)
    add_header(s5, "Existing Methods and Their Limitations", "Component 5")

    c1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(239, 68, 68)
    tf = c1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "EXISTING APPROACHES"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)
    p.space_after = Pt(14)
    items_ex = [
        ("Manual Document Dossiers", "Physical folders stored in HR filing cabinets prone to loss, wear, and zero searchability."),
        ("Spreadsheet Ledgers (Excel/Sheets)", "Unprotected flat files with multi-editor overwrite conflicts and zero field validation."),
        ("Monolithic Legacy ERP Systems", "Complex software requiring dedicated on-premise servers, steep licenses, and rigid desktop installations.")
    ]
    for title, desc in items_ex:
        p = tf.add_paragraph()
        p.text = "✖ " + title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = GRAY
        p2.space_after = Pt(8)

    c2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(245, 158, 11)
    tf = c2.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "LIMITATIONS & RESEARCH GAPS"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(245, 158, 11)
    p.space_after = Pt(14)
    items_gap = [
        ("High Data Inconsistency", "No relational constraints leading to mismatched employee education and employment records."),
        ("No Role Segregation Security", "Employees can accidentally see or overwrite peer/admin information in unprotected sheets."),
        ("Absence of Visual Engagement", "Outdated interfaces increase human administrative error rates during bulk data entry."),
        ("Incompatibility with AI Pipelines", "Unstructured manual data cannot be piped directly into machine learning models for talent analytics.")
    ]
    for title, desc in items_gap:
        p = tf.add_paragraph()
        p.text = "⚠ " + title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = GRAY
        p2.space_after = Pt(8)

    # ---------------- SLIDE 6: Proposed Solution & Architecture ----------------
    s6 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s6)
    add_header(s6, "Proposed Solution & System Architecture", "Component 6 (10 Marks)")

    layers = [
        ("PRESENTATION LAYER (Interactive Client UI)", "Responsive SB-Admin-2 Dashboard · WebGL Three.js 'Spectral Drape' 3D Waves · Hexagonal Vault Grid · Smooth Spring Cursor Physics", CYAN),
        ("AUTHENTICATION & GATEWAY LAYER", "Role-Based Access Control (RBAC) · Secure Session Validation · Distinct Gateways: Employee Self-Service & Master Admin Console", INDIGO),
        ("BUSINESS LOGIC & APPLICATION LAYER", "PHP 8.x MVC Controllers · Profile Management · Education Record Tracking (PG, Grad, HSC, SSC) · Multi-Company Experience Pipeline", RGBColor(16, 185, 129)),
        ("PERSISTENCE & DATA LAYER", "Relational Database (MySQL / MariaDB) · Tables: `employeedetail`, `empeducation`, `empexpireince`, `tbladmin` · Transactional ACID Integrity", RGBColor(245, 158, 11))
    ]

    for i, (title, desc, col) in enumerate(layers):
        y = Inches(1.8 + i * 1.3)
        box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.15))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = col
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "LAYER " + str(i+1) + ": " + title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = col
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = WHITE

    # ---------------- SLIDE 7: Technologies and Resources Required ----------------
    s7 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s7)
    add_header(s7, "Technologies and Resources Required", "Component 7 (10 Marks)")

    techs = [
        ("Frontend Technologies", ["HTML5, CSS3, JavaScript (ES6+)", "Three.js (WebGL Hardware Acceleration)", "SB-Admin-2 Responsive Bootstrap", "FontAwesome Icons & Google Fonts", "Glassmorphism UI Design Tokens"], CYAN),
        ("Backend & Database", ["PHP 8.x (Apache / Built-in Web Server)", "MySQL 8.0 / MariaDB 13.x Relational Engine", "MySQLi Extension & Prepared SQL Statements", "Session-based Stateful Authentication", "ACID Compliant Database Schema"], INDIGO),
        ("Development Environment", ["macOS Darwin / Unix Platform", "Zsh & Bash Shell Bootloader (start.sh)", "Homebrew Package Architecture", "Cross-Browser Testing (Chrome, Safari, Edge)", "Git Version Control"], RGBColor(16, 185, 129))
    ]

    for i, (cat, items, col) in enumerate(techs):
        x = Inches(0.8 + i * 4.0)
        c = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.7), Inches(5.0))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = col
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = cat
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = col
        p.space_after = Pt(14)
        for item in items:
            p = tf.add_paragraph()
            p.text = "• " + item
            p.font.size = Pt(12)
            p.font.color.rgb = WHITE
            p.space_after = Pt(8)

    # ---------------- SLIDE 8: Expected Outcomes & Tentative Timeline ----------------
    s8 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s8)
    add_header(s8, "Expected Outcomes and Tentative Timeline", "Component 8 (5 Marks)")

    c_out = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c_out.fill.solid()
    c_out.fill.fore_color.rgb = CARD_BG
    c_out.line.color.rgb = BORDER_CYAN
    tf = c_out.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "EXPECTED OUTCOMES"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.space_after = Pt(14)
    outs = [
        "Fully deployed, live-operating web platform for centralized workforce administration.",
        "Zero-latency multi-tiered navigation between Employee self-service and Administrative monitoring.",
        "Reduced administrative overhead and human record management errors by over 70%.",
        "Modernized user experience using 3D spatial visual feedback that prevents cognitive fatigue."
    ]
    for o in outs:
        p = tf.add_paragraph()
        p.text = "✔ " + o
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE
        p.space_after = Pt(10)

    c_time = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c_time.fill.solid()
    c_time.fill.fore_color.rgb = CARD_BG
    c_time.line.color.rgb = BORDER_CYAN
    tf = c_time.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "TENTATIVE PROJECT TIMELINE"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = INDIGO
    p.space_after = Pt(14)
    phases = [
        ("Phase 1 (Aug - Oct 2026):", "System requirement analysis, database ER schema modeling, and core portal deployment (COMPLETED)."),
        ("Phase 2 (Oct - Nov 2026):", "Zeroth review presentation, detailed education & experience tracking modules refinement (CURRENT)."),
        ("Phase 3 (Dec 2026 - Jan 2027):", "AI-assisted resume parsing & automated profile completion module integration."),
        ("Phase 4 (Feb - Mar 2027):", "Security penetration testing, load testing, comprehensive documentation & final viva review.")
    ]
    for ph, desc in phases:
        p = tf.add_paragraph()
        p.text = ph
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = CYAN
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = WHITE
        p2.space_after = Pt(6)

    # ---------------- SLIDE 9: Conclusion & Live Demonstration ----------------
    s9 = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(s9)

    c_end = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.2), Inches(10.3), Inches(5.2))
    c_end.fill.solid()
    c_end.fill.fore_color.rgb = CARD_BG
    c_end.line.color.rgb = CYAN
    tf = c_end.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "THANK YOU!"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(12)

    p2 = tf.add_paragraph()
    p2.text = "Employee Record Management System (ERMS)"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = CYAN
    p2.alignment = PP_ALIGN.CENTER
    p2.space_after = Pt(24)

    p3 = tf.add_paragraph()
    p3.text = "Ready for Questions, Evaluation & Live System Demonstration"
    p3.font.size = Pt(16)
    p3.font.color.rgb = INDIGO
    p3.alignment = PP_ALIGN.CENTER
    p3.space_after = Pt(20)

    p4 = tf.add_paragraph()
    p4.text = "Live Localhost Instance: http://localhost:8000/ \nIncludes 3D Spectral Drape, Hexagonal Vault & Responsive Dashboards"
    p4.font.size = Pt(13)
    p4.font.color.rgb = GRAY
    p4.alignment = PP_ALIGN.CENTER

    output_path = "/Users/donald/Downloads/Employee-Record-Management-System-Project/Zeroth_Review_Presentation_ERMS.pptx"
    prs.save(output_path)
    print("SUCCESS: PPTX saved to", output_path)

if __name__ == "__main__":
    create_deck()
