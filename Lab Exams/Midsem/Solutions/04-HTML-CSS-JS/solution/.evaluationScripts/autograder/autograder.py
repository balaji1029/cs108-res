'''Import required modules'''
import json
import math
from bs4 import BeautifulSoup
import js2py

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

marks = {
    'Nav':  {
        'bar': 0,
        'titles': 0
    },
    'Home': {
        'desc': 0,
        'image': 0
    },
    'Prime': {
        'form': 0,
        'button': 0
    },
    'inline-css': {
        'desc': 0
    },
    'internal-css': {
        'navbar': 0,
    },
    'external-css': {
        'input': 0
    },
    'runFunc': {
        'num': 0,
        'popup': 0,
    },
    'isPrime': {
        'linking': 0,
        'testcases': 0
    }
}

feedback = {
    'Nav':  {
        'bar': '',
        'titles': ''
    },
    'Home': {
        'desc': '',
        'image': ''
    },
    'Prime': {
        'form': '',
        'button': ''
    },
    'inline-css': {
        'desc': ''
    },
    'internal-css': {
        'navbar': ''
    },
    'external-css': {
        'input': ''
    },
    'runFunc': {
        'num': '',
        'popup': ''
    },
    'isPrime': {
        'linking': '',
        'testcases': ''
    }
}

# # -------------------------- Navigation ---------------------------

# default
mks1 = {
    'bar': 0,
    'titles': 0
}
fb1 = {
    'bar': '',
    'titles': ''
}
barCount = 0

# autograding
mapper = {
    'home': 'index.html',
    'prime': 'prime.html'
}
page = open('public_html/index.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
if soup.style is not None:
    sty = soup.style.text
    if sty is not None and '.topnav' in sty:
        marks['internal-css']['navbar'] = 1
    else:
        feedback['internal-css']['navbar'] = 'NavBar not styled'
else:
    feedback['internal-css']['navbar'] = 'NavBar not styled'
try:
    navbar = soup.find('div', class_='topnav')
    if navbar is not None:
        try:
            links = navbar.find_all('a')
            if links is not None:
                if len(links) == 2:
                    barCount += 1
                else:
                    fb1['bar'] = 'All links not present'
                valid = list(
                    filter(lambda x: x.text is not None and
                           mapper[x.text.lower().replace(
                               ' ', '')] in x.get('href'), links
                           )
                )
                if len(valid) == 2:
                    mks1['titles'] = 1
                else:
                    fb1['titles'] = 'All links not present'
            else:
                fb1['bar'] = 'All links not present'
        except AttributeError:
            fb1['titles'] = 'Error encountered (check navbar links)'
    else:
        fb1['bar'] = 'Navigation bar missing somewhere'
except AttributeError:
    fb1['bar'] = 'Error encountered (check navbar)'

# record
marks['Nav'] = mks1
feedback['Nav'] = fb1

# # --------------------------- Home ------------------------------

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
        if intro.text is not None and len(intro.text) >= 20:
            mks2['desc'] = 1
        else:
            fb2['desc'] = 'Intro too short'
        if intro.get('font-size') == '11pt':
            marks['inline-css']['desc'] = 1
        elif intro.get('style') is not None and \
                'font-size:11pt' in intro.get('style').replace(' ', ''):
            marks['inline-css']['desc'] = 1
        else:
            feedback['inline-css']['desc'] = 'Font size incorrect'
    else:
        fb2['desc'] = 'Intro missing'
        feedback['inline-css']['desc'] = 'Intro missing'
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

# -------------------------- Prime ------------------------

# default
mks6 = {
    'form': 0,
    'button': 0
}
fb6 = {
    'form': '',
    'button': ''
}

# autograding
page = open('./public_html/prime.html', 'r', encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
eds = False
if soup.link is not None:
    if soup.link.get('href') is not None and 'style.css' in soup.link.get('href'):
        eds = True
    else:
        feedback['external-css']['input'] = 'Style sheet not linked'
else:
    feedback['external-css']['input'] = 'Style sheet not linked'
scripts = soup.find_all('script')
if len(scripts) > 1 and scripts[1] is not None:
    if scripts[1].text is not None:
        script = scripts[1].text.replace(' ', '')
        if 'runFunc' in script:
            if '.value' in script and 'isPrime' in script:
                marks['runFunc']['num'] += 1
            else:
                feedback['runFunc'] = 'runFunc not handled in expected way'
            if 'alert' in script:
                marks['runFunc']['popup'] += 1
            else:
                feedback['runFunc'] = 'runFunc not handled in expected way'
        else:
            feedback['runFunc'] = 'runFunc function missing'
    else:
        feedback['runFunc'] = 'Script not added'
else:
    feedback['runFunc'] = 'Script not added'
if scripts[0] is not None:
    if scripts[0].get('src') is not None and 'script.js' in scripts[0].get('src'):
        marks['isPrime']['linking'] = 1
    else:
        feedback['isPrime']['linking'] = 'JavaScript not linked'
else:
    feedback['isPrime']['linking'] = 'JavaScript not linked'
try:
    navbar = soup.find('div', class_='topnav')
    if navbar is not None:
        barCount += 1
        if barCount == 2:
            mks1['bar'] += 1
        else:
            fb1['bar'] = 'All nav-bars not present'
        # record
        marks['Nav'] = mks1
        feedback['Nav'] = fb1
    else:
        fb1['bar'] = 'Navigation bar missing somewhere'
except AttributeError:
    fb1['bar'] = 'Error encountered (check navbar)'
try:
    form = soup.find('form')
    if form is not None:
        try:
            func = form.get('onsubmit')
            if func is not None and 'runFunc' in func:
                mks6['form'] += 1
            else:
                fb6['form'] = 'Wrong form function'
            try:
                label = form.find('label')
                if label is not None and label.text is not None and \
                        'enteranumber' in label.text.lower().replace(' ', ''):
                    mks6['form'] += 1
                else:
                    fb6['form'] = 'Incorrect form field label'
            except AttributeError:
                fb6['form'] = 'Error encountered (check input label)'
            butt = form.find('button')
            if butt is not None:
                typ = butt.get('type')
                if typ == 'submit':
                    mks6['button'] += 1
            else:
                fb6['button'] = 'Incorrect form button'
        except AttributeError:
            fb6['form'] = 'Form missing submit handler'
    else:
        fb6['form'] = 'Form missing'
except AttributeError:
    fb6['form'] = 'Error encountered (check contact form)'

# record
marks['Prime'] = mks6
feedback['Prime'] = fb6

# # -------------------------- External CSS -------------------------

sheet = ''.join(open('./public_html/style.css',
                'r', encoding='utf-8').readlines())
if 'input' in sheet and 'red' in sheet and eds:
    marks['external-css']['input'] = 1
else:
    feedback['external-css']['input'] = 'Input field not styled correctly'

# -------------------------- JavaScript ----------------------

def isPrime(num):
    if num < 0:
        return isPrime(-num)
    if num == 1:
        return 0
    if num == 2:
        return 1
    for i in range(2,int(math.sqrt(num) + 1)):
        if num % i == 0:
            return 0
    return 1

file = ''.join(open('./public_html/script.js',
                  'r', encoding='utf-8').readlines())
func = js2py.eval_js(file)

tc = list(map(int,open('./hidden/easy.txt','r',encoding='utf-8').readlines()))
correct = 0
for i in range(len(tc)):
    if func(i) == isPrime(i):
        correct += 1
marks['isPrime']['testcases'] += correct / len(tc)

tc = list(map(int,open('./hidden/medium.txt','r',encoding='utf-8').readlines()))
correct = 0
for i in range(len(tc)):
    if func(i) == isPrime(i):
        correct += 1
marks['isPrime']['testcases'] += correct / len(tc)

# --------------------------- Record ---------------------------

overall = {
    "data": []
}

total_marks = sum(sum(compo.values()) for compo in marks.values())

result = {
    "testid": "1",
    "status": "success",
    "score": total_marks,
    "maximum marks": 15,
    "message": [marks, feedback]
}

data = []
data.append(result)
overall['data'] = data

print(overall)
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
