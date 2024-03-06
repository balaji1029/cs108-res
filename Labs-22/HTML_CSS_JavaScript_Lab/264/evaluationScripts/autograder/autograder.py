'''Import required modules'''
import json
from bs4 import BeautifulSoup

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

marks = {
    'Nav':  {
        'bar': 0,
        'titles': 0,
        'links': 0
    },
    'Home': {
        'desc': 0,
        'image': 0
    },
    'Projects': {
        'list': 0,
        'desc': 0
    },
    'Education': {
        'table': 0,
        'data': 0
    },
    'Hobbies': {
        'checkboxes': 0,
        'button': 0
    },
    'Contact': {
        'links': 0,
        'form': 0
    },
    'inline-css': {
        'desc': 0
    },
    'internal-css': {
        'navbar': 0,
        'projects': 0
    },
    'external-css': {
        'table': 0
    },
    'learn-more': {
        'function': 0,
        'desc': 0,
    },
    'submit': {
        'function': 0,
        'popup': 0
    }
}

feedback = {
    'Nav':  {
        'bar': '',
        'titles': '',
        'links': ''
    },
    'Home': {
        'desc': '',
        'image': ''
    },
    'Projects': {
        'list': '',
        'desc': ''
    },
    'Education': {
        'table': '',
        'data': ''
    },
    'Hobbies': {
        'checkboxes': '',
        'button': ''
    },
    'Contact': {
        'links': '',
        'form': ''
    },
    'inline-css': {
        'desc': ''
    },
    'internal-css': {
        'navbar': '',
        'projects': ''
    },
    'external-css': {
        'table': ''
    },
    'learn-more': {
        'function': '',
        'desc': '',
    },
    'submit': {
        'function': '',
        'popup': ''
    }
}

# -------------------------- Navigation ---------------------------

# default
mks1 = {
    'bar': 0,
    'titles': 0,
    'links': 0
}
fb1 = {
    'bar': '',
    'titles': '',
    'links': ''
}

# autograding
mapper = {
    'Home': 'index.html',
    'Projects': 'projects.html',
    'Education': 'education.html',
    'Hobbies': 'hobbies.html',
    'Contact': 'contact.html'
}
page = open('public_html/index.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
if soup.style is not None:
    sty = soup.style.text
    if '.topnav' in sty:
        marks['internal-css']['navbar'] = 1
    else:
        feedback['internal-css']['navbar'] = 'NavBar not styled'
try:
    navbar = soup.find('div', class_='topnav')
    if navbar is not None:
        mks1['bar'] += 1
        try:
            links = navbar.find_all('a')
            if links is not None:
                if len(links) == 5:
                    mks1['bar'] += 1
                else:
                    fb1['bar'] = 'All links not present'
                valid = list(
                    filter(lambda x: mapper[x.text] in x.get('href'), links))
                if len(valid) == 5:
                    mks1['titles'] = 1
                else:
                    fb1['titles'] = 'All links not present'
                lnks = BeautifulSoup(''.join(map(str, links)), 'html.parser')
                if lnks is not None:
                    lnks = list(filter(lambda x: x.get(
                        'target') is not None and 'blank' in x.get('target'), lnks))
                    if len(lnks) == len(links):
                        mks1['links'] += 1
                    else:
                        fb1['links'] = 'All links do not redirect to new tab'
                else:
                    fb1['links'] = 'All links not present'
            else:
                fb1['bar'] = 'All links not present'
        except AttributeError:
            fb1['titles'] = 'Error encountered (check navbar links)'
    else:
        fb1['bar'] = 'Navigation bar missing'
except AttributeError:
    fb1['bar'] = 'Error encountered (check navbar)'

# record
marks['Nav'] = mks1
feedback['Nav'] = fb1

# --------------------------- Home ------------------------------

# default
mks2 = {
    'desc': 0,
    'image': 0
}
fb2 = {
    'desc': '',
    'image': ''
}

# autograding
page = open('./public_html/index.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
try:
    intro = soup.find('p', id='desc')
    if intro is not None:
        if len(intro.text) >= 150:
            mks2['desc'] = 1
        else:
            fb2['desc'] = 'Intro too short'
        if intro.get('font-size') == '11pt':
            marks['inline-css']['desc'] = 1
        elif 'font-size:11pt' in intro.get('style').replace(' ', ''):
            marks['inline-css']['desc'] = 1
        else:
            feedback['inline-css']['desc'] = 'Font size incorrect'
    else:
        fb2['desc'] = 'Intro missing'
except AttributeError:
    fb2['desc'] = 'Error encountered (check intro)'
try:
    image = soup.find('img', id='myimage')
    if image is not None:
        source = image.get('src')
        if source is not None:
            title = image.get('title')
            if title is not None:
                mks2['image'] = 1
            else:
                fb2['image'] = 'Image title missing'
        else:
            fb2['image'] = 'Image source missing'
    else:
        fb2['image'] = 'Image missing'
except AttributeError:
    fb2['image'] = 'Error encountered (check image)'

# record
marks['Home'] = mks2
feedback['Home'] = fb2

# --------------------------- Projects ------------------------------

# default
mks3 = {
    'list': 0,
    'desc': 0
}
fb3 = {
    'list': '',
    'desc': ''
}

# autograding
page = open('./public_html/projects.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
if soup.style is not None:
    sty = soup.style.text
    if 'ol' in sty:
        marks['internal-css']['projects'] = 1
    else:
        feedback['internal-css']['projects'] = 'Projects not styled'
try:
    oli = soup.find('ol', id='projects')
    if oli is not None:
        mks3['list'] += 1
        try:
            projs = oli.find_all('li')
            if projs is not None:
                if len(projs) >= 2:
                    mks3['list'] += 1
                else:
                    fb3['list'] = 'Not enough projects'
                projs = BeautifulSoup(''.join(map(str, projs)), 'html.parser')
                if projs is not None:
                    try:
                        descs = projs.find_all('p')
                        if descs is not None:
                            if len(descs) == len(projs):
                                mks3['desc'] += min(len(descs), 2)
                            else:
                                fb3['desc'] = 'Not enough descriptions'
                        else:
                            fb3['desc'] = 'Project descriptions missing'
                    except AttributeError:
                        fb3['desc'] = 'Error encountered (check proj desc)'
                else:
                    fb3['desc'] = 'Projects missing'
            else:
                fb3['desc'] = 'Projects missing'
        except AttributeError:
            fb3['list'] = 'Error encountered (check proj entries)'
    else:
        fb3['list'] = 'Projects missing'
except AttributeError:
    fb3['list'] = 'Error encountered (check proj list)'

# record
marks['Projects'] = mks3
feedback['Projects'] = fb3

# -------------------------- Education ------------------------

# default
mks4 = {
    'table': 0,
    'data': 0
}
fb4 = {
    'table': '',
    'data': ''
}

# autograding
page = open('./public_html/education.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
eds = False
if soup.link is not None:
    if 'style.css' in soup.link.get('href'):
        eds = True
    else:
        feedback['external-css']['table'] = 'Style sheet not linked'
else:
    feedback['external-css']['table'] = 'Style sheet not linked'
try:
    tbl = soup.find('table', id='education')
    if tbl is not None:
        mks4['table'] += 1
        try:
            cols = tbl.find('thead')
            if cols is not None:
                cols = BeautifulSoup(str(cols), 'html.parser')
                coldata = cols.find_all('td')
                if len(coldata) >= 3:
                    mks4['table'] += 1
                else:
                    fb4['table'] = 'Not enough columns'
            else:
                fb4['table'] = 'Education columns missing'
        except AttributeError:
            fb4['table'] = 'Error encountered (check table header)'
        try:
            bod = tbl.find('tbody')
            if bod is not None:
                mks4['table'] += 1
                bod = BeautifulSoup(str(bod), 'html.parser')
                try:
                    data = bod.find_all('td')
                    if len(data) % len(coldata) == 0:
                        mks4['data'] += len(data) // len(coldata)
                        if len(data) // len(coldata) < 1:
                            fb4['data'] = 'Insufficient data'
                    else:
                        fb4['data'] = 'Incorrect data filling'
                except AttributeError:
                    fb4['table'] = 'Error encountered (check table entries)'
            else:
                fb4['table'] = 'Education data missing'
        except AttributeError:
            fb4['table'] = 'Error encountered (check table body)'
    else:
        fb4['table'] = 'Education missing'
except AttributeError:
    fb4['table'] = 'Error encountered (check table)'

# record
marks['Education'] = mks4
feedback['Education'] = fb4

# ----------------------------- Hobbies --------------------------

# default
mks5 = {
    'checkboxes': 0,
    'button': 0
}
fb5 = {
    'checkboxes': '',
    'button': ''
}

# autograding
page = open('./public_html/hobbies.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
if soup.script is not None:
    if soup.script.text is not None:
        script = soup.script.text.replace(' ', '')
        toggles = 0
        if 'showHobbies' in script:
            marks['learn-more']['function'] += 1
            if 'checked==true' in script:
                marks['learn-more']['desc'] += 1
                toggles = script.count('checked==true')
            else:
                feedback['learn-more']['function'] = 'showHobbies not handled in expected way'
        else:
            feedback['learn-more']['function'] = 'showHobbies function missing'
    else:
        feedback['learn-more']['function'] = 'Script not added'
else:
    feedback['learn-more']['function'] = 'Script not added'
try:
    div = soup.find('div', id='hobbies')
    if div is not None:
        try:
            checks = list(filter(lambda x: 'checkbox' in x,
                          map(str, div.find_all('input'))))
            if len(checks) > 0:
                mks5['checkboxes'] += 1
            else:
                fb5['checkboxes'] = 'Checkboxes missing'
        except AttributeError:
            fb5['checkboxes'] = 'Error encountered (check input checkboxes)'
        try:
            descs = list(filter(lambda x: x is not None and
                                'display:none' in x.replace(' ', ''), map(str, div.find_all('p'))))
            if len(descs) == len(checks):
                mks5['checkboxes'] += 1
            else:
                fb5['checkboxes'] = 'Descriptions not hidden'
            if len(descs) == toggles:
                marks['learn-more']['desc'] += 1
            else:
                feedback['learn-more']['desc'] = 'Incomplete handling of checkboxes'
        except AttributeError:
            fb5['checkboxes'] = 'Error encountered (check descriptions)'
    else:
        fb5['checkboxes'] = 'Hobbies missing'
except AttributeError:
    fb5['checkboxes'] = 'Error encountered (check hobbies div)'
try:
    but = soup.find('button')
    func = but.get('onclick')
    if func == 'showHobbies()':
        mks5['button'] += 1
    else:
        fb5['button'] = 'Wrong button function'
except AttributeError:
    fb5['button'] = 'Error encountered (check hobbies button)'

# record
marks['Hobbies'] = mks5
feedback['Hobbies'] = fb5

# ------------------------------ Contact ------------------------------

# default
mks6 = {
    'links': 0,
    'form': 0
}
fb6 = {
    'links': '',
    'form': ''
}

# autograding
page = open('./public_html/contact.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
scr = False
if soup.script is not None:
    if 'script.js' in soup.script.get('src'):
        scr = True
    else:
        feedback['submit']['function'] = 'JavaScript not linked'
else:
    feedback['submit']['function'] = 'JavaScript not linked'
try:
    links = soup.find('div', id='links')
    if links is not None:
        try:
            links = links.find_all('a')
            if links is not None:
                mks6['links'] += 1
            else:
                fb6['links'] = 'Links not present'
        except AttributeError:
            fb6['links'] = 'Error encountered (check links)'
    else:
        fb6['links'] = 'Links missing'
except AttributeError:
    fb6['links'] = 'Error encountered (check contact div)'
try:
    form = soup.find('form')
    if form is not None:
        func = form.get('onsubmit')
        if func == 'submitMessage()':
            mks6['form'] += 1
        else:
            fb6['form'] = 'Wrong form function'
        try:
            labels = form.find_all('label')
            if ['Email', 'Message', 'Name'] == sorted(map(lambda x: x.string, labels)):
                mks6['form'] += 1
            else:
                fb6['form'] = 'Incorrect form fields'
        except AttributeError:
            fb6['form'] = 'Error encountered (check input labels)'
        butt = form.find('button')
        typ = butt.get('type')
        if typ == 'submit':
            mks6['form'] += 1
        else:
            fb6['form'] = 'Incorrect form button'
    else:
        fb6['form'] = 'Form missing'
except AttributeError:
    fb6['form'] = 'Error encountered (check contact form)'

# record
marks['Contact'] = mks6
feedback['Contact'] = fb6

# -------------------------- External CSS -------------------------

sheet = ''.join(open('./public_html/style.css',
                'r', encoding='utf-8').readlines())
if 'table' in sheet and eds:
    marks['external-css']['table'] = 1
else:
    feedback['external-css']['table'] = 'Education table not styled'

# -------------------------- JavaScript ----------------------

script = ''.join(open('./public_html/script.js', 'r',
                 encoding='utf-8').readlines()).replace(' ', '')
if 'submitMessage' in script and scr:
    marks['submit']['function'] += 1
else:
    feedback['submit']['function'] = 'Contact form function missing'
if 'alert' in script and 'Thankyou' in script:
    marks['submit']['popup'] += 1
else:
    feedback['submit']['popup'] = 'Contact form popup incorrect'

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(sum(compo.values()) for compo in marks.values())
overall['feedback'] = feedback
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('----------------------- FEEDBACK -----------------------------')
print(json.dumps(feedback, indent=4))
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
