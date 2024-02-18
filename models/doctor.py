from odoo.models import Model
from odoo.fields import Char as String, Integer, Image, Many2many

class Doctor(Model):
    _name = 'model.doctor'
    _description = 'Hospital doctor'

    name = String(
        string='Doctor name'
    )

    last_name = String(
        string='Doctor last name'
    )

    doctor_number = Integer(
        string='Doctor number'
    )

    image = Image(
        string='Doctor image',
        max_width=100,
        max_height=100
    )

    patient_relation = Many2many(
        'model.patient',
        string='Patients'
    )