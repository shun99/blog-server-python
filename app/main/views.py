from . import main


@main.route('/')
def home():
    return main.send_static_file('index.html')
