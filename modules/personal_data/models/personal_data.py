from odoo import models, fields

class PersonalData(models.Model):
    _name = 'personal.data'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone Number")
    website = fields.Char(string="Website")
    address = fields.Text(string="Address", required=True)
    summary = fields.Text(string="Summary", required=True)

    # Experience
    experience_ids = fields.One2many(
        'personal.data.experience', 'personal_data_id', string="Experience", required=True
    )

    # Education
    education_ids = fields.One2many(
        'personal.data.education', 'personal_data_id', string="Education", required=True
    )

    # Skills
    skills = fields.Text(string="Skills", required=True)

    # Optional fields
    awards = fields.One2many(
        'personal.data.certificate', 'personal_data_id', string="Awards and Certifications"
    )

    references = fields.Text(string="References")
    languages = fields.Text(string="Languages", required=True)
    volunteer_experience = fields.Text(string="Volunteer Experience")