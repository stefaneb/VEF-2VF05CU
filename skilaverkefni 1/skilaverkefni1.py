from bottle import route, run

@route('/')
def index():
    return "<h2><a style='text-decoration: none;' href='/about'>About</a> <a style='text-decoration: none;' href='/biography'>Biograpy</a> <a style='text-decoration: none;' href='/pictures'>Pictures</a></h2> "
@route('/about')
def about():
    return "<p>This is a website about Steve Jobs.</p>"

@route('/biography')
def biography():
    return "<u>Steve Jobs</u> co-founded Apple Computers with Steve Wozniak.<br> Under Jobs' guidance, the company pioneered a series of revolutionary technologies,<br> including the iPhone and iPad."

@route('/pictures')
def pictures():
    return "Hérna væru myndir af Steve Jobs"
run()