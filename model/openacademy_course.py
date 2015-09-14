# -*- coding: utf-8 -*-
from openerp import models, fields, api

'''
Creacion del modelo del curso
'''

class Course(models.Model):
	'''
	Crea el modelo del curso

	Aparecerá un campo search y unas opciones de filtrado y busqueda avanzada que son heredadas de "models" como parametro (models.Model)
	'''
	_name = 'openacademy.course'  #nombre del modelo odoo, se usa '.', en BD se cambia por '_'
	name = fields.Char(string='Title', required=True)  #campo field reservado pra identificar el nombre del registro, el string es lo que se vera en el formulario
	description = fields.Text(string='Description')  #asume required=False, el string es lo que se vera en el formulario
	responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)  #un curso tiene un responsable

