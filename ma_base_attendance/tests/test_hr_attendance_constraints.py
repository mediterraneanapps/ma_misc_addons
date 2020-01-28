from odoo.tests.common import TransactionCase
import time


class TestHrAttendance(TransactionCase):
    """Tests for attendance date ranges validity"""

    def setUp(self):
        super(TestHrAttendance, self).setUp()
        self.attendance = self.env['res.partner.attendance']
        self.test_partner = self.env.ref('base.partner_demo')

    def test_attendance_in_before_out(self):
         
        with self.assertRaises(Exception):
            self.my_attend = self.attendance.create({
                'partner_id': self.test_partner.id,
                'check_in': time.strftime('%Y-%m-10 12:00'),
                'check_out': time.strftime('%Y-%m-10 11:00'),
            })

    def test_attendance_no_check_out(self):
         
        self.attendance.create({
            'partner_id': self.test_partner.id,
            'check_in': time.strftime('%Y-%m-10 10:00'),
        })
        with self.assertRaises(Exception):
            self.attendance.create({
                'partner_id': self.test_partner.id,
                'check_in': time.strftime('%Y-%m-10 11:00'),
            })

    def test_check_in_while_attendance(self):
         
        self.attendance.create({
            'partner_id': self.test_partner.id,
            'check_in': time.strftime('%Y-%m-10 08:00'),
            'check_out': time.strftime('%Y-%m-10 09:30'),
        })
        with self.assertRaises(Exception):
            self.attendance.create({
                'partner_id': self.test_partner.id,
                'check_in': time.strftime('%Y-%m-10 08:30'),
                'check_out': time.strftime('%Y-%m-10 09:30'),
            })

    def test_new_attendances(self):
         
        self.attendance.create({
            'partner_id': self.test_partner.id,
            'check_in': time.strftime('%Y-%m-10 11:00'),
            'check_out': time.strftime('%Y-%m-10 12:00'),
        })
        open_attendance = self.attendance.create({
            'partner_id': self.test_partner.id,
            'check_in': time.strftime('%Y-%m-10 10:00'),
        })
        with self.assertRaises(Exception):
            open_attendance.write({
                'check_out': time.strftime('%Y-%m-10 11:30'),
            })
