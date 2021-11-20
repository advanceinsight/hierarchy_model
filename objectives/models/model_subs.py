# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sub_activities(models.Model):
    _name = 'objectives.sub_activities'
    _description = 'Sub-Activities (level 3)'

    name = fields.Char(string="Sub-activity name")
    responsible = fields.Many2many('res.users',string="Department/Technical Lead")
    sub_activity_note = fields.Text(string="Note on sub-activity")
    sub_activity_start = fields.Date(string="Start date")
    sub_activity_end = fields.Date(string="End date")


    key_activity = fields.Many2one('objectives.activities',string="Activity")

    budget = fields.Float(string="Sub-activity Budget")

    # currency_id = fields.Many2one('res.currency',string="Currency",default="USD")