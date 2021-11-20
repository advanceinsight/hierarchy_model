# -*- coding: utf-8 -*-
{
    'name':                     "Objective Management",

    'summary':                  """
                                This model enables the management and assessment of company/project objectives, broken down into activities and sub-activities.
                                """,

    'description':              """
                                This model enables the management and assessment of company objectives, broken down into activities and sub-activities.
                                """,

    'author':                   "Douwe van Loenen / Advance Insight BV",
    'website':                  "http://www.advanceinsight.dev",

    'category':                 'Uncategorized',
    'version':                  '0.01',

    'depends':                  [
                                'base'
                                ],

    'data':                     [
                                'security/ir.model.access.csv',
                                'views/tree_views.xml',
                                'views/form_views.xml',
                                'views/actions.xml',
                                'views/menu.xml',
                                ],
