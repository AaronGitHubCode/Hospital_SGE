from odoo.models import Model
from odoo.fields import Char as String, Many2one

class Diagnostic(Model):
    _name = 'model.diagnostic'
    _description = 'Hospital diagnostic'

    description = String(
        string='Diagnostic'
    )

    patient_relation = Many2one(
        'model.patient',
        string='Patient'
    )

    doctor_relation = Many2one(
        'model.doctor',
        string='Doctor'
    )