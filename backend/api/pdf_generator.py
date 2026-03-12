"""
Professional PDF itinerary generator using ReportLab.
"""
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def generate_itinerary_pdf(city_data, itinerary_data):
    """
    Generate a professional travel guide PDF.

    city_data: dict with city info (name, description, best_time_to_visit, travel_tips, places, foods)
    itinerary_data: dict with itinerary (days, budget info)

    Returns: BytesIO buffer containing the PDF
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
    )

    # Define colors
    saffron = colors.HexColor('#FF6B35')
    deep_blue = colors.HexColor('#1B3A5C')
    gold = colors.HexColor('#D4A843')
    light_bg = colors.HexColor('#FFF8F0')

    # Styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontSize=28,
        textColor=deep_blue,
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    ))
    styles.add(ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=saffron,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica',
    ))
    styles.add(ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=deep_blue,
        spaceBefore=16,
        spaceAfter=8,
        fontName='Helvetica-Bold',
        borderColor=saffron,
        borderWidth=2,
        borderPadding=(0, 0, 4, 0),
    ))
    styles.add(ParagraphStyle(
        'BodyText2',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        spaceAfter=6,
        leading=14,
    ))
    styles.add(ParagraphStyle(
        'DayTitle',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=saffron,
        spaceBefore=12,
        spaceAfter=6,
        fontName='Helvetica-Bold',
    ))
    styles.add(ParagraphStyle(
        'TimeSlot',
        parent=styles['Normal'],
        fontSize=10,
        textColor=deep_blue,
        fontName='Helvetica-Bold',
        spaceAfter=2,
    ))

    elements = []
    city_name = city_data.get('name', 'City')

    # ── Title Page ──
    elements.append(Spacer(1, 40))
    elements.append(Paragraph('🇮🇳 India Travel Guide', styles['TitleStyle']))
    elements.append(Paragraph(city_name, styles['TitleStyle']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        f"Your personalized travel itinerary",
        styles['SubtitleStyle']
    ))
    elements.append(HRFlowable(
        width="80%", thickness=2, color=gold, spaceAfter=20, spaceBefore=10
    ))

    # ── City Overview ──
    elements.append(Paragraph('City Overview', styles['SectionTitle']))
    description = city_data.get('description', '')
    if description:
        elements.append(Paragraph(description, styles['BodyText2']))

    best_time = city_data.get('best_time_to_visit', '')
    if best_time:
        elements.append(Spacer(1, 6))
        elements.append(Paragraph(
            f"<b>Best Time to Visit:</b> {best_time}",
            styles['BodyText2']
        ))

    # ── Budget Summary ──
    budget_type = itinerary_data.get('budget_type', 'medium')
    daily_budget = itinerary_data.get('estimated_daily_budget', 0)
    total_budget = itinerary_data.get('estimated_total_budget', 0)
    currency = itinerary_data.get('currency', 'INR')

    elements.append(Spacer(1, 10))
    elements.append(Paragraph('Budget Estimation', styles['SectionTitle']))

    budget_data = [
        ['Category', 'Details'],
        ['Budget Type', budget_type.capitalize()],
        ['Daily Estimate', f'{currency} {daily_budget:,}'],
        ['Total Estimate', f'{currency} {total_budget:,}'],
        ['Duration', f"{itinerary_data.get('num_days', 0)} days"],
    ]
    budget_table = Table(budget_data, colWidths=[150, 300])
    budget_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), deep_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BACKGROUND', (0, 1), (-1, -1), light_bg),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#DDDDDD')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, light_bg]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    elements.append(budget_table)

    # ── Day-wise Itinerary ──
    elements.append(Spacer(1, 10))
    elements.append(Paragraph('Day-wise Itinerary', styles['SectionTitle']))
    elements.append(HRFlowable(
        width="100%", thickness=1, color=gold, spaceAfter=10
    ))

    days = itinerary_data.get('days', [])
    for day_info in days:
        day_num = day_info.get('day', 0)
        activities = day_info.get('activities', [])

        day_elements = []
        day_elements.append(Paragraph(f'Day {day_num}', styles['DayTitle']))

        for act in activities:
            time = act.get('time', '')
            activity = act.get('activity', '')
            desc = act.get('description', '')

            day_elements.append(Paragraph(
                f"<b>{time}:</b> {activity}",
                styles['BodyText2']
            ))
            if desc:
                day_elements.append(Paragraph(
                    f"<i>{desc}</i>",
                    styles['BodyText2']
                ))

        day_elements.append(Spacer(1, 8))
        elements.append(KeepTogether(day_elements))

    # ── Famous Tourist Places ──
    places = city_data.get('places', [])
    if places:
        elements.append(Spacer(1, 10))
        elements.append(Paragraph('Famous Tourist Places', styles['SectionTitle']))

        place_data = [['Place', 'Category', 'Timings', 'Entry Fee']]
        for p in places:
            name = p.get('name', '') if isinstance(p, dict) else str(p)
            cat = p.get('category', '') if isinstance(p, dict) else ''
            timing = p.get('timing', '') if isinstance(p, dict) else ''
            fee = p.get('entry_fee', 'Free') if isinstance(p, dict) else 'Free'
            place_data.append([name, cat.capitalize(), timing, fee])

        place_table = Table(place_data, colWidths=[150, 90, 120, 90])
        place_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), deep_blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#DDDDDD')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, light_bg]),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ]))
        elements.append(place_table)

    # ── Famous Foods ──
    foods = city_data.get('foods', [])
    if foods:
        elements.append(Spacer(1, 10))
        elements.append(Paragraph('Famous Foods', styles['SectionTitle']))

        for f in foods:
            name = f.get('name', '') if isinstance(f, dict) else str(f)
            desc = f.get('description', '') if isinstance(f, dict) else ''
            elements.append(Paragraph(
                f"• <b>{name}</b> — {desc}" if desc else f"• <b>{name}</b>",
                styles['BodyText2']
            ))

    # ── Travel Tips ──
    tips = city_data.get('travel_tips', '')
    if tips:
        elements.append(Spacer(1, 10))
        elements.append(Paragraph('Travel Tips', styles['SectionTitle']))
        for tip in tips.split('\n'):
            tip = tip.strip()
            if tip:
                elements.append(Paragraph(f"✓ {tip}", styles['BodyText2']))

    # ── Footer ──
    elements.append(Spacer(1, 30))
    elements.append(HRFlowable(
        width="100%", thickness=1, color=gold, spaceAfter=10
    ))
    elements.append(Paragraph(
        'Generated by India Travel Planner • Plan Your Perfect Trip Across India',
        ParagraphStyle('Footer', parent=styles['Normal'],
                       fontSize=8, textColor=colors.gray, alignment=TA_CENTER)
    ))

    doc.build(elements)
    buffer.seek(0)
    return buffer
