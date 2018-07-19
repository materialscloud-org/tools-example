import flask
from flask import Blueprint

blueprint = Blueprint('compute', __name__, url_prefix='/compute')

@blueprint.route('/register')
def register():
    return "register view"

# @bp.route('/process_data/', methods=['GET', 'POST'])
# def process_data():
#     """
#     Process data (uploaded from POST request)
#     """
#     if flask.request.method == 'POST':
#         try:
#             data_for_template = process_data_core(
#                 module_version="",
#                 call_source="process_data",
#                 logger=logger,
#                 flask_request=flask.request)
#             config_dict = get_config()
#             return flask.render_template(
#                 get_visualizer_template(flask.request), config=config_dict['config'], **data_for_template)
#         except FlaskRedirectException as e:
#             flask.flash(str(e))
#             return flask.redirect(flask.url_for('input_data'))
#         except Exception:
#             flask.flash("Unable to process the data, sorry...")
#             return flask.redirect(flask.url_for('input_data'))

#     else:  # GET Request
#         return flask.redirect(flask.url_for('input_data'))


# @pb.route('/process_example_data/', methods=['GET', 'POST'])
# def process_example_data():
#     """
#     Process an example data file (example name from POST request)
#     """
#     if flask.request.method == 'POST':
#         try:
#             data_for_template = process_data_core(
#                 module_version="",
#                 call_source="process_example_data",
#                 logger=logger,
#                 flask_request=flask.request)
#             return flask.render_template(
#                 get_visualizer_template(flask.request), config=config, **data_for_template)
#         except FlaskRedirectException as e:
#             flask.flash(str(e))
#             return flask.redirect(flask.url_for('input_data'))
#
#    else:  # GET Request
#        return flask.redirect(flask.url_for('input_data'))