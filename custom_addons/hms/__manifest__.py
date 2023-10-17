{
    'name': "HMS Module",
    'summary': 'A module to manage a hospital system',
    'author': 'Moustafa Ascoura',
    'depends': ['crm'],

    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/patients_data.xml',
        'views/departments_data.xml',
        'views/doctors_data.xml',
        'views/patients_logs.xml',
        'views/related_patient.xml',
        'reports/hms_patient_template.xml',
        'reports/reports.xml'
    ],
}