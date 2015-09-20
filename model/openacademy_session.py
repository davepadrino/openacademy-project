# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Session(models.Model):
	_name = 'openacademy.session'
	#para que aparezca un nombre por defecto, en la creacion de la sesion, en este caso aparecería un /
	# @api.model
	# def _get_default_name(self):
		#print ('self', self)
		#print ('_get_default_name::self', self)
		#print ('_get_default_name::self.cr', self.cr)
		#return "/"
	#name = fields.Char(required=True, default = _get_default_name)	
	name = fields.Char(required=True)
	start_date = fields.Date(default=fields.Date.today)
	duration = fields.Float(digits=(6, 2), help="Duracion en dias")
	seats = fields.Integer(string="Numero de Asientos")
	instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|', ('instructor', '=', True),('category_id.name', 'ilike', "Teacher")])
	'''
	el primer campo es el nombre del campo al cual se hace referencia (nombre a referenciar en partner.py)
	
	El domain anterior permite que en las sesiones se agreguen solo los partner que sean seleccionados como instructores
	manualmente directo desde el perfil de cada partner, es IMPORTANTE, ya que sirve como un filtro dentro del mismo elemento
	en este caso, un fields.Many2one	
	'''
	course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True) #una sesion tiene un instructor
	attendee_ids = fields.Many2many('res.partner', string="Attendees")  #Muchos sesiones a muchos asistentes (partners)
	taken_seats = fields.Float(string="Asientos Ocupados", compute='_taken_seats') 
	active = fields.Boolean(default=True)  # Active sirve para eliminado lógico, desaparece de la pantalla de activos, 
											#se puede buscar con una busqueda avanzada por los campos activos = False

	''' 
	# _taken_seats: es el compute field

	@api.one -> Este Decorador solo genera una Instancia de una Clase en Odoo, itera en registros de un conjunto de registros
				Decorador de registros que espera recibir self para crear una instancia singular de una clase Odoo. Adicionalmente
				iterará entre regitros y creara una lista con los resultados.
				Si hay un decorador @returns, se concatena con las instancias resultantes  	


	@api.depends() -> Este Decorador es utilizado para campos Calculados, o campos que requieran obtener un listado de valores
	'''

	@api.one
	@api.depends('seats', 'attendee_ids')
	def _taken_seats(self):
		if not self.seats:
			self.taken_seats = 0.0
		else:
			self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats

