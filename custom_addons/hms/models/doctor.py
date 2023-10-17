from odoo import models, fields

class hms_doctor(models.Model):
    _name='hms.doctor'

    fname=fields.Char(required=True)
    lname=fields.Char(required=True)
    image=fields.Image()

    patients=fields.Many2many(comodel_name='hms.patient')
    dept_id=fields.Many2one(comodel_name='hms.department')
