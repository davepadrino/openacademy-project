from openerp import models, fields, api

'''
Creacion del modelo del curso
'''

class Course(models.Model):
	'''
	Crea el modelo del curso
	'''
	_name = 'openacademy.course'  #nombre del modelo odoo, se usa '.', en BD se cambia por '_'
	name = fields.Char(string='Title', required=True)  #campo field reservado pra identificar el nombre del registro
	description = fields.Text(string='Description')  #asume required=False
