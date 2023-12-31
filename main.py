from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template2.html')
'''
caps = [
{
        "title": "Красная кепка",
        "price": "$ 100.00",
        "image": "https://dvmn.org/filer/canonical/1569333143/329/"
    },
    {
        "title": "Чёрная кепка",
        "price": "$ 120.00",
        "image": "https://dvmn.org/filer/canonical/1569333143/330/"
    },
    {
        "title": "Ещё одна чёрная кепка",
        "price": "$ 90.00",
        "image": "https://dvmn.org/filer/canonical/1569333144/331/"
    },
    {
        "title": "Камуфляжная кепка",
        "price": "$ 100.00",
        "image": "https://dvmn.org/filer/canonical/1569943835/350/"
    },
    {
        "title": "Джинсовая кепка",
        "price": "$ 100.00",
        "image": "https://dvmn.org/filer/canonical/1569943835/351/"
    },
    {
        "title": "Плоская кепка",
        "price": "$ 100.00",
        "image": "https://dvmn.org/filer/canonical/1569943836/352/"
    }
]
'''
time_range = (datetime.datetime.now() - datetime.datetime(year=1920, month=1,day=1)).days//365

rendered_page = template.render(time_range=time_range)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
