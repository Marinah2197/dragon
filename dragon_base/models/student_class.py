#-*- coding: utf-8 -*-

from odoo import models, fields


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Description module'

    name = fields.Char(string='Name')
    student_number = fields.Integer(string='Student number')
    stage= fields.Char(string='Stage')
   