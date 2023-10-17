from odoo import models, fields, api
from odoo.exceptions import UserError

class customer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    related_patient_id= fields.Many2one(comodel_name="hms.patient")
    related_patient_email=fields.Char(related="related_patient_id.email")

    @api.onchange('related_patient_id')
    def check_patient_mail(self):
        if self.search_count([('email','=',self.related_patient_email)]):
            return {
                'warning': {
                    'title': 'Related Patient Email',
                    'message': 'The patient has the same email as an existing customer'
                }
            }
    
    _sql_constraints = [
        ('unique_related_patient' , 'UNIQUE(related_patient_id)' , 'The patient is already assigned')
    ]

    @api.ondelete(at_uninstall=False)
    def check_if_related_patient(self):
        if self.related_patient_id:
            raise UserError("Can't delete a customer with realted patients!")

