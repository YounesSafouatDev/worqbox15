# -*- coding: utf-8 -*-
{
    'name': "worqbox_crm_stage_multi_company",

    'summary': """CRM Stage Multi-company""",

    'description': """
        Adds support for multi-company on crm stages.
        - Stages with no company are available for all.
        - Stages with one or more company are only available for those.
    """,

    'author': "GIE",
    'website': "https://gie.ma",

    'category': 'Worqbox',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'base_multi_company',
        'crm',
    ],

    # always loaded
    'data': [
        'security/crm_security.xml',
        'views/crm_stage_views.xml',
    ],
}
