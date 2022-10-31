# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _

class PatientBase(models.Model):
	_name = 'patient.base'
	_description = 'Patient management'
	_inherit = 'mail.thread'

	name = fields.Char(compute='compute_name', string='Name', default=" ")
	lastname = fields.Char(string='lastname')
	firstname = fields.Char(string='Firstname')
	age = fields.Integer(string='age', tracking=True)
	state = fields.Selection([('new', 'New'), ('consulted', 'Consulted'),
                              ('treaty', 'Treaty'), ('cancelled', 'Cancelled'), 
                              ('renews', 'Renews')], default='new')

	def set_consulted(self):
		self.state ='consulted'


	def set_treaty(self):
		self.state ='treaty'


	def set_cancelled(self):
		self.state ='cancelled'


	def set_renews(self):
		self.state ='renews'


	def open_wizard(self):
		return {
			'name': _('Test Window Action'),
			'view_mode': 'form',
			'res_model': 'patient.wizard',
			'type': 'ir.actions.act_window',
			'target': 'new',
			'context': {'Birth_date_value':'Date'},
		}

	@api.depends("firstname","lastname")
	def compute_name(self):
		for record in self:
			record.name = "%s %s"%(record.firstname, record.lastname)