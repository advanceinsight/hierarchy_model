# -*- coding: utf-8 -*-

from odoo import models, fields, api

class activities(models.Model):
    _name = 'objectives.activities'
    _description = 'Activities (level 2)'

    name = fields.Char(string="Activity name")
    responsible = fields.Many2many('res.users',string="Department/Technical Lead")
    activity_note = fields.Text(string="Note on activity")
    activity_start = fields.Date(string="Start date")
    activity_end = fields.Date(string="End date")

    key_objective = fields.Many2one('objectives.objectives',string="Key Objective")

    # Count (and reference to) the activities on the Objective

    sub_activities_count = fields.Integer(compute="compute_subs")

    def compute_subs(self):
        for activity in self:
            activity.sub_activities_count = self.env['objectives.sub_activities'].search_count([('key_activity', '=', self.name)])

    def get_subs(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sub-Activities',
            'view_mode': 'tree,form',
            'res_model': 'objectives.sub_activities',
            'domain': [('key_activity', '=', self.name)],
            'context': "{'create': True}"
        }

    # Calculate sum of total budget coming from the sub-activities

    budget = fields.Float(compute='_get_sub_total', string='Sub-Total Budget')

    @api.depends('activity_sub_budgets')
    def _get_sub_total(self):
        for activity in self:
            activity.budget = sum(sub_activity.budget for sub_activity in activity.activity_sub_budgets)
  
    activity_sub_budgets = fields.One2many( comodel_name='objectives.sub_activities',
                                        inverse_name='key_activity',
                                        string='Sub-Activity Budgets')