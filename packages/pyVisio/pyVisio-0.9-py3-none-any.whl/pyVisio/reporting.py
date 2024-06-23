from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from jinja2 import Template

def generate_report(report_data, format='pdf', output_path='report.pdf'):
    """
    Generates a report with the given data.

    Parameters:
        report_data (dict): The data for the report.
        format (str, optional): The format of the report. Default is 'pdf'.
        output_path (str, optional): The output path for the report. Default is 'report.pdf'.

    Returns:
        None
    """
    if format != 'pdf':
        raise ValueError("Currently only 'pdf' format is supported")

    template = Template("""
    Title: {{ title }}
    Author: {{ author }}
    Date: {{ date }}
    {% for item in content %}
    - {{ item.title }} ({{ item.type }}): {{ item.data }}
    {% endfor %}
    """)

    content = template.render(
        title=report_data['title'],
        author=report_data['author'],
        date=report_data['date'],
        content=report_data['content']
    )

    pdf = canvas.Canvas(output_path, pagesize=letter)
    pdf.drawString(100, 750, report_data['title'])
    pdf.drawString(100, 735, f"Author: {report_data['author']}")
    pdf.drawString(100, 720, f"Date: {report_data['date']}")

    y = 700
    for item in report_data['content']:
        pdf.drawString(100, y, f"{item['title']} ({item['type']}): {item['data']}")
        y -= 15

    pdf.save()
