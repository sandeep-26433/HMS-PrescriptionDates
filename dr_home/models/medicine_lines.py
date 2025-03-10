from odoo import models, fields

class DoctorMedicineLines(models.Model):
    _name = 'doctor.medicine.lines'
    _description = 'Medicine Lines'

    appointment_id = fields.Many2one('doctor.appointments', string="Appointment", ondelete='cascade')
    medicine_id = fields.Many2one('doctor.medicines', string="Medicine")
    dosage_id = fields.Many2one('doctor.dosages', string="Dosage")
    usage = fields.Text(string="Usage")
    days = fields.Integer(string="Days")
    course = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ], string="Course")
    quantity = fields.Integer(string="Quantity")
    prescription_date = fields.Date(string="Prescription Date")  # Add prescription_date field

