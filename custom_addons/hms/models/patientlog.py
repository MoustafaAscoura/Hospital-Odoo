from odoo import models, fields

class hms_patientlog(models.Model):
    _name='hms.patientlog'

    patient_id=fields.Many2one(comodel_name='hms.patient')
    description=fields.Text(required=True)
