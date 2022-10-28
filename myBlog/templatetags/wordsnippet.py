from django import template
register=template.Library()

@register.filter
def wordsnippet(content, count=30):
    words=content.split(' ')
    if len(words)>count:
        return ' '.join(words[:count])+"..."
    return ' '.join(words)