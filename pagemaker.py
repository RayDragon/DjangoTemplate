from django import views
from django.template import loader

LOREAM = "The quick brown fox jumps over the laxy dog. The quick brown fox jumps over the laxy dog. The quick brown fox jumps over the laxy dog. The quick brown fox jumps over the laxy dog. The quick brown fox jumps over the laxy dog. The quick brown fox jumps over the laxy dog."

def load(file_name, request, data):
    temp = loader.get_template(file_name)
    render = data
    return temp.render(render, request)


class PageMaker:
    head = ''
    nav = ''
    body = ''
    foot = ''
    request = None
    forms=0

    def get_card(self, head, body, color=""):
        return load("card.html", self.request, {'head': head, 'body': body, 'color':color})


    def get_nav(self, data, selected=None, color="blue"):
        '''
        :param data:[['name', 'link'],['d','Name',[[name, link][][]]],[r, name, link]]
        :param selected: 'name'
        :return:html of nav
        '''
        return load("navbar.html",
                        None,
                        {
                            'selected': selected, 'items': data, 'color':color
                        })

    def get_form(self, action, head=None, submit_text='Submit', elements=None):
        '''
            :param elements: element, type, name, id, placeholder, validation
            validation = 'rena'
                r-required
                e-email
                n-number
                a-alphabates(A-Z, a-z,  )
                for required email 're'/'er' (order not mandatory)


        '''
        self.forms += 1
        return load("form_create.html", self.request, {
            'elements': elements,
            'head': head,
            'sbtn_text': submit_text,
            'action': action,
            'formno': self.forms
        })

    def get_duel(self, left, right):
        return "<div class='w3-row'><div class='w3-half'>" + left + "</div><div class='w3-half'>" + right + "</div></div>"

    def add_to_body(self, append_to_body=""):
        self.body += append_to_body

    def get_page(self, title=""):
        return load("head.html", None, {'page_title': title}) + self.head + self.nav + self.body

    def get_row(self, data, add = "-padding"):
        return load("row.html", None,
                    {'type': 'beign',
                     'data': load("row.html", None, {'type': 'row', 'elements': data}),
                     'add': add
                    })

    def __int__(self, head, navigation, body):
        self.head = head
        return 'done'

