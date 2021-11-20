# -*- coding: utf-8 -*-

from odoo import models, fields, api


class objectives(models.Model):
    _name = 'objectives.objectives'
    _description = 'Strategic Objectives (level 1)'

    name = fields.Char(string="Strategic Objective")
    responsible = fields.Many2one('res.users',string="Lead")
    support = fields.Many2many('res.users',string="Support")
    objective_note = fields.Text(string="Note on objective")
    objective_start = fields.Date(string="Start date")
    objective_end = fields.Date(string="End date")

    # Count (and reference to) the activities on the Objective

    activities_count_on_obj = fields.Integer(compute="compute_activities")

    def compute_activities(self):
        for record in self:
            record.activities_count_on_obj = self.env['objectives.activities'].search_count([('key_objective', '=', self.name)])

    def get_activities(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Activities',
            'view_mode': 'tree,form',
            'res_model': 'objectives.activities',
            'domain': [('key_objective', '=', self.name)],
            'context': "{'create': True}"
        }

    # Calculate sum of total budget coming from the activities

    budget_total = fields.Float(compute='_get_total', string='Total Budget')

    @api.depends('activity_budgets')
    def _get_total(self):
        for objective in self:
            objective.budget_total = sum(activity.budget for activity in objective.activity_budgets)
    
    activity_budgets = fields.One2many( comodel_name='objectives.activities',
                                        inverse_name='key_objective',
                                        string='Activity Budgets')  