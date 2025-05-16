from django import template
register = template.Library()

@register.filter
def replace_comma(value):
    return str(value).replace(",", ".")

MONTHS_IS = {
    1: "janúar", 2: "febrúar", 3: "mars", 4: "apríl",
    5: "maí", 6: "júní", 7: "júlí", 8: "ágúst",
    9: "september", 10: "október", 11: "nóvember", 12: "desember"
}

@register.filter
def format_open_house_time_is(value):
    if not value:
        return ""
    day = value.day
    month = MONTHS_IS.get(value.month, "")
    time_str = value.strftime("%H:%M")
    return f"{day}. {month}, kl. {time_str}"