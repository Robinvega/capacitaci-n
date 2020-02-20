# -*- coding: utf-8 -*-

from odoo import models, fields


class hey!a(models.Model):
     _name = 'hey!a.hey!a'
     _description = 'hey!a.hey!a'

     nombre = fields.Char()
     apellido = fields.Integer()
     salario = fields.Float(compute="_value_pc", store=True)
     descripción = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
