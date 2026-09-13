#!/usr/bin/env python3
"""Generate a PDF pitch deck for OmniTender LLC."""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import os

# Colors
PRIMARY = HexColor("#1a365d")
ACCENT = HexColor("#2b6cb0")
LIGHT = HexColor("#ebf4ff")
DARK = HexColor("#1a202c")
GRAY = HexColor("#718096")

def add_footer(c, page_num, total=10):
    """Add page footer with page number."""
    c.setFont("Helvetica", 8)
    c.setFillColor(GRAY)
    c.drawRightString(LETTER[0] - 0.75*inch, 0.5*inch, f"OmniTender LLC | Confidential | Page {page_num} of {total}")
    c.drawString(0.75*inch, 0.5*inch, "September 2026")
    c.setFillColor(DARK)

def draw_header(c, title, subtitle=None):
    """Draw page header with title."""
    c.setFillColor(PRIMARY)
    c.rect(0, LETTER[1] - 1.2*inch, LETTER[0], 1.2*inch, fill=1, stroke=0)
    c.setFillColor(HexColor("#ffffff"))
    c.setFont("Helvetica-Bold", 20)
    c.drawString(0.75*inch, LETTER[1] - 0.85*inch, title)
    if subtitle:
        c.setFont("Helvetica", 12)
        c.drawString(0.75*inch, LETTER[1] - 1.05*inch, subtitle)
    c.setFillColor(DARK)

def draw_text_block(c, x, y, text, font="Helvetica", size=11, color=DARK, spacing=14):
    """Draw text with line wrapping."""
    c.setFont(font, size)
    c.setFillColor(color)
    lines = []
    for line in text.split('\n'):
        while line and c.stringWidth(line, font, size) > 6.5*inch:
            idx = len(line) // 2
            while idx > 0 and line[idx] != ' ':
                idx -= 1
            if idx == 0:
                idx = len(line) // 2
            lines.append(line[:idx])
            line = line[idx:].strip()
        lines.append(line)
    
    current_y = y
    for line in lines:
        c.drawString(x, current_y, line)
        current_y -= spacing
    return current_y

def slide_cover(c):
    """Cover slide."""
    c.setFillColor(PRIMARY)
    c.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    
    # Logo area
    c.setFillColor(HexColor("#ffffff"))
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 + 1.5*inch, "OmniTender LLC")
    
    c.setFont("Helvetica", 16)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 + 1.0*inch, "Working Capital Pitch Deck")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 + 0.5*inch, "$100K – $200K")
    
    c.setFont("Helvetica", 11)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 - 1.0*inch, "Daniel Read, Founder")
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 - 1.3*inch, "Raleigh-Durham, NC")
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 - 1.6*inch, "September 2026")

def slide_overview(c):
    """Company overview."""
    draw_header(c, "Company Overview", "OmniTender LLC at a Glance")
    
    y = LETTER[1] - 1.8*inch
    
    facts = [
        ("Entity", "North Carolina LLC"),
        ("Location", "Raleigh-Durham, NC (remote-first)"),
        ("Industry", "Payment Processing + E-Commerce"),
        ("Founded", "Active & Revenue-Generating"),
        ("Owner", "Daniel Read (sole member)"),
        ("Ask", "$100K–$200K working capital"),
        ("Use", "Inventory expansion, merchant growth, equipment"),
    ]
    
    for label, value in facts:
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(PRIMARY)
        c.drawString(0.75*inch, y, f"{label}:")
        c.setFont("Helvetica", 11)
        c.setFillColor(DARK)
        c.drawString(1.75*inch, y, value)
        y -= 0.3*inch

def slide_business_model(c):
    """Business model."""
    draw_header(c, "Business Model", "Dual Revenue Streams")
    
    y = LETTER[1] - 1.8*inch
    
    # Left box
    c.setFillColor(LIGHT)
    c.roundRect(0.75*inch, y - 2.0*inch, 3.0*inch, 2.0*inch, 8, fill=1, stroke=0)
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.9*inch, y - 0.3*inch, "OmniTender")
    c.setFont("Helvetica", 10)
    text = "• Card-present & card-not-present processing\n• POS integration for local businesses\n• Interchange-plus pricing model\n• Monthly SaaS fees + setup fees"
    draw_text_block(c, 0.9*inch, y - 0.6*inch, text, size=10, color=DARK)
    
    # Right box
    c.setFillColor(LIGHT)
    c.roundRect(4.0*inch, y - 2.0*inch, 3.0*inch, 2.0*inch, 8, fill=1, stroke=0)
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(4.15*inch, y - 0.3*inch, "OmniBay")
    c.setFont("Helvetica", 10)
    text = "• Multi-channel e-commerce (eBay, Shopify)\n• Sourced inventory (liquidation, wholesale)\n• 30-50% margins after COGS\n• Scalable, data-driven selection"
    draw_text_block(c, 4.15*inch, y - 0.6*inch, text, size=10, color=DARK)
    
    y -= 2.8*inch
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(PRIMARY)
    c.drawCentredString(LETTER[0]/2, y, "Combined: Active revenue stream with clear path to profitability at scale")

def slide_market(c):
    """Market opportunity."""
    draw_header(c, "Market Opportunity", "Triangle Ecosystem & Beyond")
    
    y = LETTER[1] - 1.8*inch
    
    stats = [
        ("$1.5T+", "U.S. annual payment processing volume"),
        ("$30B+", "E-commerce resale market (growing)"),
        ("2.1M", "Triangle metro population (+2% annually)"),
        ("70%", "Small businesses dissatisfied with current processors"),
    ]
    
    for stat, desc in stats:
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(ACCENT)
        c.drawString(0.75*inch, y, stat)
        c.setFont("Helvetica", 11)
        c.setFillColor(DARK)
        c.drawString(2.5*inch, y - 2, desc)
        y -= 0.7*inch

def slide_use_of_funds(c):
    """Use of funds."""
    draw_header(c, "Use of Funds", "$100,000 Allocation")
    
    y = LETTER[1] - 1.8*inch
    
    categories = [
        ("OmniBay Inventory", "$50,000", "50%"),
        ("Marketing & Acquisition", "$15,000", "15%"),
        ("Equipment & Software", "$10,000", "10%"),
        ("Working Capital / Runway", "$20,000", "20%"),
        ("Contingency Buffer", "$5,000", "5%"),
    ]
    
    for name, amount, pct in categories:
        bar_width = float(pct.replace('%','')) / 100 * 5.0 * inch
        c.setFillColor(LIGHT)
        c.roundRect(2.0*inch, y - 0.15*inch, 5.0*inch, 0.3*inch, 4, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.roundRect(2.0*inch, y - 0.15*inch, bar_width, 0.3*inch, 4, fill=1, stroke=0)
        
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(DARK)
        c.drawString(0.75*inch, y, name)
        c.setFillColor(ACCENT)
        c.drawRightString(1.95*inch, y, amount)
        y -= 0.5*inch
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(PRIMARY)
    c.drawString(0.75*inch, y - 0.3*inch, "Total: $100,000")

def slide_projections(c):
    """Financial projections."""
    draw_header(c, "12-Month Projections", "Path to Profitability")
    
    y = LETTER[1] - 1.8*inch
    
    # Simple table
    headers = ["Month", "Revenue", "COGS", "Gross Profit", "OpEx", "Net"]
    col_widths = [0.8, 1.1, 0.9, 1.1, 0.9, 0.9]
    
    x = 0.75*inch
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(PRIMARY)
    for i, h in enumerate(headers):
        c.drawString(x, y, h)
        x += col_widths[i] * inch
    
    y -= 0.25*inch
    c.setLineWidth(0.5)
    c.setStrokeColor(PRIMARY)
    c.line(0.75*inch, y + 0.15*inch, 7.25*inch, y + 0.15*inch)
    
    data = [
        ("Month 1", "$8,000", "$3,500", "$4,500", "$3,000", "$1,500"),
        ("Month 3", "$11,000", "$4,500", "$6,500", "$3,200", "$3,300"),
        ("Month 6", "$14,000", "$6,000", "$8,000", "$3,500", "$4,500"),
        ("Month 9", "$17,000", "$7,500", "$9,500", "$3,800", "$5,700"),
        ("Month 12", "$20,000", "$8,500", "$11,500", "$4,000", "$7,500"),
    ]
    
    c.setFont("Helvetica", 9)
    c.setFillColor(DARK)
    for row in data:
        x = 0.75*inch
        for i, val in enumerate(row):
            c.drawString(x, y, val)
            x += col_widths[i] * inch
        y -= 0.3*inch
    
    y -= 0.2*inch
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(PRIMARY)
    c.drawString(0.75*inch, y, "Key Insight: By Month 12, monthly net profit covers loan payment 3-4x over")

def slide_repayment(c):
    """Repayment scenarios."""
    draw_header(c, "Repayment Capacity", "Conservative Scenarios")
    
    y = LETTER[1] - 1.8*inch
    
    scenarios = [
        ("$100K @ 10% / 5yr", "$2,125/mo", "$27,500 total interest"),
        ("$150K @ 12% / 5yr", "$3,337/mo", "$50,200 total interest"),
        ("$200K @ 14% / 5yr", "$4,650/mo", "$79,000 total interest"),
    ]
    
    x = 0.75*inch
    for label, payment, interest in scenarios:
        c.setFillColor(LIGHT)
        c.roundRect(x, y - 1.2*inch, 2.0*inch, 1.2*inch, 8, fill=1, stroke=0)
        c.setFillColor(PRIMARY)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(x + 1.0*inch, y - 0.3*inch, label)
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(ACCENT)
        c.drawCentredString(x + 1.0*inch, y - 0.7*inch, payment)
        c.setFont("Helvetica", 9)
        c.setFillColor(GRAY)
        c.drawCentredString(x + 1.0*inch, y - 1.0*inch, interest)
        x += 2.5*inch
    
    y -= 2.0*inch
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(PRIMARY)
    c.drawString(0.75*inch, y, "Recommendation: Start at $100K, prove performance, expand facility later")

def slide_team(c):
    """Owner background."""
    draw_header(c, "Owner Background", "Daniel Read — Founder & Sole Member")
    
    y = LETTER[1] - 1.8*inch
    
    points = [
        "Full-stack software developer & technology entrepreneur",
        "Built neural-network connectome hub (agent ecosystem registry)",
        "Active in e-commerce (OmniBay) and payment systems (OmniTender)",
        "Manages multiple ventures simultaneously",
        "Credit score ~550: recovering from divorce-related debt settlement",
        "Zero bankruptcies, zero foreclosures, zero recent late payments",
    ]
    
    for point in points:
        c.setFont("Helvetica", 11)
        c.setFillColor(DARK)
        c.drawString(0.9*inch, y, "•")
        c.drawString(1.1*inch, y, point)
        y -= 0.3*inch

def slide_risk(c):
    """Risk mitigation."""
    draw_header(c, "Risk Factors & Mitigation", "Honest Assessment")
    
    y = LETTER[1] - 1.8*inch
    
    risks = [
        ("Credit score at 550", "CDFI/SBA focus; strong business fundamentals"),
        ("Inventory risk", "Proven resale channels; diversified sourcing"),
        ("Customer concentration", "Multiple merchants; marketplace diversification"),
        ("Economic downturn", "Payment processing is counter-cyclical"),
        ("Owner dependency", "Build team as revenue scales"),
    ]
    
    for risk, mitigation in risks:
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(PRIMARY)
        c.drawString(0.75*inch, y, risk)
        c.setFont("Helvetica", 10)
        c.setFillColor(DARK)
        c.drawString(0.75*inch, y - 0.2*inch, f"  → {mitigation}")
        y -= 0.5*inch

def slide_contact(c):
    """Contact / closing slide."""
    c.setFillColor(PRIMARY)
    c.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    
    c.setFillColor(HexColor("#ffffff"))
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 + 1.5*inch, "Let's Build Something")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 + 0.8*inch, "Daniel Read | Founder, OmniTender LLC")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 + 0.3*inch, "subtilior.ars@gmail.com")
    
    c.setFont("Helvetica", 11)
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 - 0.5*inch, "Raleigh-Durham, NC")
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 - 0.8*inch, "September 2026")
    c.drawCentredString(LETTER[0]/2, LETTER[1]/2 - 1.8*inch, "\"We're not asking for a rescue — we're asking for a partner in growth.\"")

def main():
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pitch-deck.pdf")
    c = canvas.Canvas(output_path, pagesize=LETTER)
    
    slides = [
        slide_cover,
        slide_overview,
        slide_business_model,
        slide_market,
        slide_use_of_funds,
        slide_projections,
        slide_repayment,
        slide_team,
        slide_risk,
        slide_contact,
    ]
    
    total = len(slides)
    for i, slide_fn in enumerate(slides):
        slide_fn(c)
        add_footer(c, i + 1, total)
        c.showPage()
    
    c.save()
    print(f"PDF generated: {output_path}")
    print(f"Slides: {total}")

if __name__ == "__main__":
    main()
