# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings mismos""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Dave",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'view/openacademy_course_view.xml',
        'view/openacademy_session_view.xml',
        'view/partner_view.xml',
        'workflow/openacademy_session_workflow.xml',
        'security/security.xml', #ojo con el orden de declaracion de archivos
        'security/ir.model.access.csv',
        'view/openacademy_wizard_view.xml',
        'report/openacademy_session_report.xml',
        'view/openacademy_session_board.xml',

        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        # para que odoo reconozca el .xml
        'demo/openacademy_course_demo.xml',
    ],
    'installable': True,
    'auto_install':False,
    'active': False,
}