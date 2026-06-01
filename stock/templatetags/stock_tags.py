from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        return f"{float(value):,.2f} €"
    except (ValueError, TypeError):
        return value

@register.filter(name='multiply')
def multiply(value, multiplier):
    try:
        return float(value) * float(multiplier)
    except (ValueError, TypeError):
        return value

@register.simple_tag(takes_context=True)
def active_link(context, url_path):
    request = context.get('request')
    if not request:
        return ''
    current_path = request.path or ''
    if url_path == '/':
        return 'active-menu' if current_path == '/' else ''
    return 'active-menu' if current_path.startswith(url_path) else ''

@register.inclusion_tag('components/highlight_articles.html')
def highlight_articles(articles, count=3):
    return {'articles': articles[:count]}
