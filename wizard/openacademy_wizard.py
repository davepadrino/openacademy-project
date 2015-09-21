# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
	_name = 'openacademy.wizard'

	def _default_session(self):
		#return self.env['openacademy.session'].browse(self._context.get('active_id'))
		#lo que venga de active_ids, conviertelo en openacademy.session
		return self.env['openacademy.session'].browse(self._context.get('active_ids'))

	#session_wiz_id = fields.Many2one('openacademy.session', string="Sesion", required=True, default=_default_session)
	session_wiz_ids = fields.Many2many('openacademy.session', string="Sesiones", required=True, default=_default_session)	
	attendee_wiz_ids = fields.Many2many('res.partner', string="Asistentes")

	@api.multi
	def subscribe(self):
		for session_wiz in self.session_wiz_ids:	
			session_wiz.attendee_ids |= self.attendee_wiz_ids #|= es como el += pero con objetos, es decir, concatena asistentes a los ya existentes 
		return {}	
