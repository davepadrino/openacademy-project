# -*- coding: utf-8 -*-
from openerp import models, fields

class Session(models.Model):
	_name = 'openacademy.session'
	#para que aparezca un nombre por defecto, en la creacion de la sesion, en este caso aparecería un /
	# @api.model
	# def _get_default_name(self):
		#print ('self', self)
		#return "/"
	#name = fields.Char(required=True, default = _get_default_name)	
	name = fields.Char(required=True)
	start_date = fields.Date()
	duration = fields.Float(digits=(6, 2), help="Duration in days")
	seats = fields.Integer(string="Number of seats")
	instructor_id = fields.Many2one('res.partner', string="Instructor")
	course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True) #una sesion tiene un instructor
	attendee_ids = fields.Many2many('res.partner', string="Attendees")  #Muchos asistentes a muchas sesiones
