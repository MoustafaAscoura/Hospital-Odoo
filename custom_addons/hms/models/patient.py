from odoo import models, fields, api
from odoo.exceptions import  ValidationError
from datetime import date
import re

class hms_patient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'fname'

    fname=fields.Char(required=True)
    lname=fields.Char(required=True)
    birthdate=fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float()
    blood_type=fields.Selection([('A','Blood Group A'),\
        ('B','Blood Group B'),('O','Blood Group O'),\
            ('AB','Blood Group AB')])
    pcr=fields.Boolean('PCR')
    image=fields.Image("Image")
    address=fields.Text()
    age=fields.Integer(compute='compute_age')
    email=fields.Char()

    status=fields.Selection([('0' ,'Undetermined' ),\
    ('1', 'Good') , ('2', 'Fair'),\
    ('3', 'Serious')] , default = '0')

    dept_id=fields.Many2one(comodel_name='hms.department')
    dept_capacity=fields.Integer(related='dept_id.capacity')
    logs = fields.One2many('hms.patientlog','patient_id')
    doctors=fields.Many2many(comodel_name='hms.doctor')
    
    _sql_constraints=[('Duplicate_Email', 'UNIQUE(email)', 'This email already exists')]

    @api.onchange('age')
    def check_pcr(self):
        if 0 < self.age < 30:
            self.pcr=True
            return {
                'warning': {
                    'title': ('PCR is automatically checked'),
                    'message': 'PCR is checked as age is less than 30'
                }
            }
        
    @api.onchange('status')
    def log_change(self):
        log = {
            'patient_id': self.id, #Doesn't get added!
            'description': f"status changed to {self.status}"
        }
        self.env['hms.patientlog'].create(log)
    
    @api.constrains('email')
    def check_valid_mail(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        for rec in self:
            if not (re.fullmatch(regex, rec.email)):
                raise ValidationError("Invalid Email")
    
    @api.depends('birthdate')
    def compute_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = date.today().year - rec.birthdate.year
            else:
                rec.age=0

