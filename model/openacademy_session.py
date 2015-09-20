# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions

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
				Al utilizar un api.one decorator los parametros 'cr' (cursor de la BD), 'uid'(usuario de la BD), 
				'id' (identificador del registro) y 'context'(es un diccionario de python usado para cierta data a un metodo), se desaparecen de los parametros de una funcion nueva o heredada


	@api.depends() -> Este Decorador es utilizado para campos Calculados, o campos que requieran obtener un listado de valores

	tambien puediera escribirse como

	@api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
	'''

	@api.one
	@api.depends('seats', 'attendee_ids')
	def _taken_seats(self):
		if not self.seats:
			self.taken_seats = 0.0
		else:
			self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats

	''' 
	El onchange permite que al momento de modificar un campo y se retire el cursor de el, se active la funcion y se compruebe 
	si hay  no errores
	'''
	@api.onchange('seats', 'attendee_ids')
	def _verify_valid_seats(self):
		if self.seats < 0:
			return {
				'warning': {
					'title': "Valores incorrectos de asientos",
					'message': "El numero de asientos no puede ser negativo",
				},
			}
		if self.seats < len(self.attendee_ids):
			return {
                'warning': {
                    'title': "MUCHOS ASISTENTES!",
                    'message': "Aumenta el numero de Asientos o elimina algunos asistentes",
                },
            }

	''' 
	El constrains permite hacer validaciones a nivel de API de python, otra forma de hacer la que está below es:

	@api.one
	@api.constrains('instructor_id', 'attendee_ids')
	def _check_instructor_not_in_attendees(self):
			if self.instructor_id and self.instructor_id in self.attendee_ids:
				raise exceptions.ValidationError("A session's instructor can't be an attendee") 


	'''
	@api.constrains('instructor_id', 'attendee_ids')
	def _check_instructor_not_in_attendees(self):
			for r in self:
				if r.instructor_id and r.instructor_id in r.attendee_ids:   #atendee_ids es un listado
					raise exceptions.ValidationError("Un instructor no puede ser su mismo asistente")            