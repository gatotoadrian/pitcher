from flask import render_template
from . import main 

@main.errorhandler(404)
def foO4(error):
    '''
    Function that renders an error
    '''
    render_template('404.html'),404