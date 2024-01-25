from odoo import models, fields

class PersonalDataEducation(models.Model):
    _name = 'personal.data.education'

    personal_data_id = fields.Many2one('personal.data', string="Personal Data")
    school_name = fields.Char(string="School Name")
    degree = fields.Char(string="Degree")
    major = fields.Char(string="Major")
    graduation_year = fields.Date(string="Graduation Year")