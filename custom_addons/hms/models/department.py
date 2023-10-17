from odoo import models, fields

class hms_department(models.Model):
    _name = "hms.department"

    name=fields.Char(required=True)
    capacity=fields.Integer(required=True)
    is_open=fields.Boolean(default=False)

    patients=fields.One2many(comodel_name='hms.patient',inverse_name='dept_id')
    doctors=fields.One2many(comodel_name='hms.doctor',inverse_name='dept_id')
    