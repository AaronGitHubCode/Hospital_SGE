from odoo.models import Model
from odoo.fields import Char as String, Many2many

class Patient(Model):
    _name = 'model.patient'
    _description = 'Hospital patient'

    name = String(
        string="Patient name"
    )

    last_name = String(
        string="Patient last name"
    )

    syntoms = String(
        string="Patient syntoms"
    )

    diagnostic_relation = Many2many(
        'model.diagnostic',
        string='Diagnostic'
    )