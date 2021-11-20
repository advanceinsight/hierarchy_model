# -*- coding: utf-8 -*-

from odoo import models, fields, api


class objectives(models.Model):
    _name = 'objectives.objectives'
    _description = 'Strategic Objectives (level 1)'

    name = fields.Char(string="Strategic Objective")
    responsible = fields.Many2many('res.users',string="Department Lead(s)")
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

