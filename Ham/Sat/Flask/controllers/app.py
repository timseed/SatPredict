from werkzeug.utils import cached_property
from flask import Flask, Response
from  flask_restx import Api
import logging
import daiquiri
import yaml

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_DEBUG'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
ns_conf = api.namespace('sat/V1.1', description='Sat Tracking')



def create_logger(log_config_file):
    logging.basicConfig(level=logging.DEBUG)
    logger = daiquiri.getLogger(__name__)
    logger.info("only to rotating file logger")

