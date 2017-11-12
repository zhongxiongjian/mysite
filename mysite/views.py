from django.http import HttpResponse
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. nidaye</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

from reportlab.pdfgen import canvas
from django.http import HttpResponse
def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
