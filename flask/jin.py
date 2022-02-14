from jinja2 import Template 
template = Template('hello world from {{ programming_world }}!')
template.render(programming_world='Jinja2 template engine')