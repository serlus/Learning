import calendar

def calendario_texto():
    """criando um calendario no formato texto
    """
    calendario_texto = calendar.TextCalendar(calendar.SUNDAY)
    txt_calendario = calendario_texto.formatmonth(2020, 8)
    print(txt_calendario)

calendario_texto()

def calendario_HTML():
    """criando um calendario no formato texto
    """
    calendario_HTML = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendario = calendario_HTML.formatmonth(2020, 8)
    print(html_calendario)

calendario_HTML()