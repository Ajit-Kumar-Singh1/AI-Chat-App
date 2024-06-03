patterns = {
    'select_employee_by_ohrid': {
        'pattern': r"select employee with ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {}"
    },
    'select_employee_by_name': {
        'pattern': r"select employee with name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%'"
    },
    'select_employee_by_email': {
        'pattern': r"select employee with email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpEmailID = '{}'"
    },
    'select_employee_by_band': {
        'pattern': r"select employee with band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}'"
    },
    'select_employee_by_tower': {
        'pattern': r"select employee in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%'"
    },
    'select_employee_by_process_id': {
        'pattern': r"select employee with process id (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {}"
    },
    'select_employee_by_process_name': {
        'pattern': r"select employee in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%'"
    },
    'select_employee_by_doj': {
        'pattern': r"select employee with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ = '{}'"
    },
    'select_employee_by_dol': {
        'pattern': r"select employee with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL = '{}'"
    },
    'select_employee_by_mgr_ohrid': {
        'pattern': r"select employee with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {}"
    },
    'select_employee_by_mgr_email': {
        'pattern': r"select employee with manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}'"
    },
    'select_employee_by_mgr_band': {
        'pattern': r"select employee with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}'"
    },
    'select_employee_by_oneoone_mgr_ohrid': {
        'pattern': r"select employee with one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {}"
    },
    'select_employee_by_oneoone_mgr_email': {
        'pattern': r"select employee with one-o-one manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}'"
    },
    'select_employee_by_inserted_on': {
        'pattern': r"select employee inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}'"
    },
    'select_employee_by_modified_by': {
        'pattern': r"select employee modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}'"
    },
    'select_employee_by_modified_on': {
        'pattern': r"select employee modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}'"
    },
    'all_employees': {
        'pattern': r"show all employees",
        'query_template': "SELECT * FROM EmployeeMaster"
    },
    'employees_with_band': {
        'pattern': r"show employees with band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}'"
    },
    'employees_in_tower': {
        'pattern': r"show employees in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%'"
    },
    'employees_in_process': {
        'pattern': r"show employees in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%'"
    },
    'employees_with_mgr_ohrid': {
        'pattern': r"show employees with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {}"
    },
    'employees_with_mgr_email': {
        'pattern': r"show employees with manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}'"
    },
    'employees_with_mgr_band': {
        'pattern': r"show employees with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}'"
    },
    'employees_with_oneoone_mgr_ohrid': {
        'pattern': r"show employees with one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {}"
    },
    'employees_with_oneoone_mgr_email': {
        'pattern': r"show employees with one-o-one manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}'"
    },
    'employees_inserted_on': {
        'pattern': r"show employees inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}'"
    },
    'employees_modified_by': {
        'pattern': r"show employees modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}'"
    },
    'employees_modified_on': {
        'pattern': r"show employees modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}'"
    },
    'select_employees_name_email': {
        'pattern': r"select employee with name (.+) and email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%' AND EmpEmailID = '{}'"
    },
    'select_employees_band_tower': {
        'pattern': r"select employee with band (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employees_process_doj': {
        'pattern': r"select employee in process (.+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND DOJ = '{}'"
    },
    'select_employees_mgr_ohrid_email': {
        'pattern': r"select employee with manager ohrid (\d+) and email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {} AND EmpEmailID = '{}'"
    },
    'select_employees_mgr_band_name': {
        'pattern': r"select employee with manager band (.+) and name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}' AND EmpName LIKE '%{}%'"
    },
    'select_employees_oneoone_mgr_ohrid_dol': {
        'pattern': r"select employee with one-o-one manager ohrid (\d+) and dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {} AND DOL = '{}'"
    },
    'select_employees_inserted_modified': {
        'pattern': r"select employee inserted on (.+) and modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}' AND ModifiedOn = '{}'"
    },
    'show_employees_with_doj_before': {
        'pattern': r"show employees with doj before (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ < '{}'"
    },
    'show_employees_with_doj_after': {
        'pattern': r"show employees with doj after (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ > '{}'"
    },
    'show_employees_with_dol_before': {
        'pattern': r"show employees with dol before (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL < '{}'"
    },
    'show_employees_with_dol_after': {
        'pattern': r"show employees with dol after (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL > '{}'"
    },
    'show_employees_with_doj_between': {
        'pattern': r"show employees with doj between (.+) and (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ BETWEEN '{}' AND '{}'"
    },
    'show_employees_with_dol_between': {
        'pattern': r"show employees with dol between (.+) and (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL BETWEEN '{}' AND '{}'"
    },
    'select_employee_with_mgr_name': {
        'pattern': r"select employee with manager name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID IN (SELECT OHRID FROM EmployeeMaster WHERE EmpName LIKE '%{}%')"
    },
    'select_employee_with_mgr_band': {
        'pattern': r"select employee with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID IN (SELECT OHRID FROM EmployeeMaster WHERE EmpBand = '{}')"
    },
    'show_employees_in_process_and_tower': {
        'pattern': r"show employees in process (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND TowerName LIKE '%{}%'"
    },
    'show_employees_with_doj_dol_between': {
        'pattern': r"show employees with doj between (.+) and (.+) and dol between (.+) and (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ BETWEEN '{}' AND '{}' AND DOL BETWEEN '{}' AND '{}'"
    },
    'select_employee_with_process_id_and_name': {
        'pattern': r"select employee with process id (\d+) and name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {} AND EmpName LIKE '%{}%'"
    },
    'select_employee_with_process_id_and_doj': {
        'pattern': r"select employee with process id (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {} AND DOJ = '{}'"
    },
    'select_employee_with_mgr_ohrid_and_process': {
        'pattern': r"select employee with manager ohrid (\d+) and in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {} AND ProcessName LIKE '%{}%'"
    },
    'select_employee_with_mgr_ohrid_and_doj': {
        'pattern': r"select employee with manager ohrid (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {} AND DOJ = '{}'"
    },
    'select_employee_with_mgr_band_and_tower': {
        'pattern': r"select employee with manager band (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employee_with_mgr_email_and_process': {
        'pattern': r"select employee with manager email (.+) and in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}' AND ProcessName LIKE '%{}%'"
    },
    'select_employee_with_oneoone_mgr_ohrid_and_doj': {
        'pattern': r"select employee with one-o-one manager ohrid (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {} AND DOJ = '{}'"
    },
    'select_employee_with_oneoone_mgr_email_and_tower': {
        'pattern': r"select employee with one-o-one manager email (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employee_with_inserted_on_and_mgr_band': {
        'pattern': r"select employee inserted on (.+) with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}' AND MgrBand = '{}'"
    },
    'select_employee_with_modified_by_and_doj': {
        'pattern': r"select employee modified by (.+) with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}' AND DOJ = '{}'"
    },
    'select_employee_with_modified_on_and_process': {
        'pattern': r"select employee modified on (.+) in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}' AND ProcessName LIKE '%{}%'"
    },
    'show_employees_with_name_and_email': {
        'pattern': r"show employees with name (.+) and email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%' AND EmpEmailID = '{}'"
    },
    'show_employees_with_band_and_doj': {
        'pattern': r"show employees with band (.+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND DOJ = '{}'"
    },
    'show_employees_with_tower_and_dol': {
        'pattern': r"show employees in tower (.+) with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND DOL = '{}'"
    },
    'show_employees_with_process_and_mgr_ohrid': {
        'pattern': r"show employees in process (.+) with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND MgrOhrID = {}"
    },
    'show_employees_with_mgr_band_and_process': {
        'pattern': r"show employees with manager band (.+) in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}' AND ProcessName LIKE '%{}%'"
    },
    'show_employees_with_oneoone_mgr_ohrid_and_doj': {
        'pattern': r"show employees with one-o-one manager ohrid (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {} AND DOJ = '{}'"
    },
    'show_employees_with_oneoone_mgr_email_and_dol': {
        'pattern': r"show employees with one-o-one manager email (.+) and dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}' AND DOL = '{}'"
    },
    'show_employees_with_inserted_on_and_doj': {
        'pattern': r"show employees inserted on (.+) with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}' AND DOJ = '{}'"
    },
    'show_employees_with_modified_by_and_dol': {
        'pattern': r"show employees modified by (.+) with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}' AND DOL = '{}'"
    },
    'show_employees_with_modified_on_and_tower': {
        'pattern': r"show employees modified on (.+) in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employee_with_ohrid_and_band': {
        'pattern': r"select employee with ohrid (\d+) and band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {} AND EmpBand = '{}'"
    },
    'select_employee_with_ohrid_and_tower': {
        'pattern': r"select employee with ohrid (\d+) in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {} AND TowerName LIKE '%{}%'"
    },
    'select_employee_with_ohrid_and_process': {
        'pattern': r"select employee with ohrid (\d+) in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {} AND ProcessName LIKE '%{}%'"
    },
    'select_employee_with_ohrid_and_mgr_ohrid': {
        'pattern': r"select employee with ohrid (\d+) and manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {} AND MgrOhrID = {}"
    },
    'select_employee_with_ohrid_and_doj': {
        'pattern': r"select employee with ohrid (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {} AND DOJ = '{}'"
    },
    'select_employee_with_ohrid_and_dol': {
        'pattern': r"select employee with ohrid (\d+) and dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {} AND DOL = '{}'"
    },
    'select_employee_with_band_and_doj': {
        'pattern': r"select employee with band (.+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND DOJ = '{}'"
    },
    'select_employee_with_band_and_dol': {
        'pattern': r"select employee with band (.+) and dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND DOL = '{}'"
    },
    'select_employee_with_band_and_tower': {
        'pattern': r"select employee with band (.+) in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employee_with_band_and_process': {
        'pattern': r"select employee with band (.+) in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND ProcessName LIKE '%{}%'"
    },
    'select_employee_with_band_and_mgr_ohrid': {
        'pattern': r"select employee with band (.+) and manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND MgrOhrID = {}"
    },
    'select_employee_with_band_and_oneoone_mgr_ohrid': {
        'pattern': r"select employee with band (.+) and one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND OneOOneMgrOhrID = {}"
    },
    'select_employee_with_band_and_inserted_on': {
        'pattern': r"select employee with band (.+) inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND InsertedOn = '{}'"
    },
    'select_employee_with_band_and_modified_by': {
        'pattern': r"select employee with band (.+) modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND ModifiedBy = '{}'"
    },
    'select_employee_with_band_and_modified_on': {
        'pattern': r"select employee with band (.+) modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND ModifiedOn = '{}'"
    },
    'select_employee_with_tower_and_doj': {
        'pattern': r"select employee in tower (.+) with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND DOJ = '{}'"
    },
    'select_employee_with_tower_and_dol': {
        'pattern': r"select employee in tower (.+) with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND DOL = '{}'"
    },
    'select_employee_with_tower_and_mgr_ohrid': {
        'pattern': r"select employee in tower (.+) with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND MgrOhrID = {}"
    },
    'select_employee_with_tower_and_oneoone_mgr_ohrid': {
        'pattern': r"select employee in tower (.+) with one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND OneOOneMgrOhrID = {}"
    },
    'select_employee_with_tower_and_inserted_on': {
        'pattern': r"select employee in tower (.+) inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND InsertedOn = '{}'"
    },
    'select_employee_with_tower_and_modified_by': {
        'pattern': r"select employee in tower (.+) modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND ModifiedBy = '{}'"
    },
    'select_employee_with_tower_and_modified_on': {
        'pattern': r"select employee in tower (.+) modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%' AND ModifiedOn = '{}'"
    },
    'select_employee_with_process_and_doj': {
        'pattern': r"select employee in process (.+) with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND DOJ = '{}'"
    },
    'select_employee_with_process_and_dol': {
        'pattern': r"select employee in process (.+) with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND DOL = '{}'"
    },
    'select_employee_with_process_and_mgr_ohrid': {
        'pattern': r"select employee in process (.+) with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND MgrOhrID = {}"
    },
    'select_employee_with_process_and_oneoone_mgr_ohrid': {
        'pattern': r"select employee in process (.+) with one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND OneOOneMgrOhrID = {}"
    },
    'select_employee_with_process_and_inserted_on': {
        'pattern': r"select employee in process (.+) inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND InsertedOn = '{}'"
    },
    'select_employee_with_process_and_modified_by': {
        'pattern': r"select employee in process (.+) modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND ModifiedBy = '{}'"
    },
    'select_employee_with_process_and_modified_on': {
        'pattern': r"select employee in process (.+) modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND ModifiedOn = '{}'"
    },
    # Patterns including 'What', 'Who', and 'Whose'
    'what_is_employee_email': {
        'pattern': r"what is the email of employee with ohrid (\d+)",
        'query_template': "SELECT EmpEmailID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_name': {
        'pattern': r"what is the name of employee with ohrid (\d+)",
        'query_template': "SELECT EmpName FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_band': {
        'pattern': r"what is the band of employee with ohrid (\d+)",
        'query_template': "SELECT EmpBand FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_tower': {
        'pattern': r"what is the tower of employee with ohrid (\d+)",
        'query_template': "SELECT TowerName FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_process_name': {
        'pattern': r"what is the process name of employee with ohrid (\d+)",
        'query_template': "SELECT ProcessName FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_doj': {
        'pattern': r"what is the doj of employee with ohrid (\d+)",
        'query_template': "SELECT DOJ FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_dol': {
        'pattern': r"what is the dol of employee with ohrid (\d+)",
        'query_template': "SELECT DOL FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_mgr_ohrid': {
        'pattern': r"what is the manager ohrid of employee with ohrid (\d+)",
        'query_template': "SELECT MgrOhrID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_mgr_email': {
        'pattern': r"what is the manager email of employee with ohrid (\d+)",
        'query_template': "SELECT MgrEmailID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_mgr_band': {
        'pattern': r"what is the manager band of employee with ohrid (\d+)",
        'query_template': "SELECT MgrBand FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_oneoone_mgr_ohrid': {
        'pattern': r"what is the one-o-one manager ohrid of employee with ohrid (\d+)",
        'query_template': "SELECT OneOOneMgrOhrID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_oneoone_mgr_email': {
        'pattern': r"what is the one-o-one manager email of employee with ohrid (\d+)",
        'query_template': "SELECT OneOOneMgrEmailID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_inserted_on': {
        'pattern': r"what is the inserted on date of employee with ohrid (\d+)",
        'query_template': "SELECT InsertedOn FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_modified_by': {
        'pattern': r"what is the modified by of employee with ohrid (\d+)",
        'query_template': "SELECT ModifiedBy FROM EmployeeMaster WHERE OHRID = {}"
    },
    'what_is_employee_modified_on': {
        'pattern': r"what is the modified on date of employee with ohrid (\d+)",
        'query_template': "SELECT ModifiedOn FROM EmployeeMaster WHERE OHRID = {}"
    },
    'who_is_employee_with_ohrid': {
        'pattern': r"who is the employee with ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {}"
    },
    'who_is_employee_with_email': {
        'pattern': r"who is the employee with email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpEmailID = '{}'"
    },
    'who_is_employee_with_name': {
        'pattern': r"who is the employee with name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%'"
    },
    'who_is_employee_with_band': {
        'pattern': r"who is the employee with band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}'"
    },
    'who_is_employee_in_tower': {
        'pattern': r"who is the employee in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%'"
    },
    'who_is_employee_in_process': {
        'pattern': r"who is the employee in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%'"
    },
    'who_is_employee_with_doj': {
        'pattern': r"who is the employee with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ = '{}'"
    },
    'who_is_employee_with_dol': {
        'pattern': r"who is the employee with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL = '{}'"
    },
    'who_is_employee_with_mgr_ohrid': {
        'pattern': r"who is the employee with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {}"
    },
    'who_is_employee_with_mgr_email': {
        'pattern': r"who is the employee with manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}'"
    },
    'who_is_employee_with_mgr_band': {
        'pattern': r"who is the employee with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}'"
    },
    'who_is_employee_with_oneoone_mgr_ohrid': {
        'pattern': r"who is the employee with one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {}"
    },
    'who_is_employee_with_oneoone_mgr_email': {
        'pattern': r"who is the employee with one-o-one manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}'"
    },
    'who_is_employee_inserted_on': {
        'pattern': r"who is the employee inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}'"
    },
    'who_is_employee_modified_by': {
        'pattern': r"who is the employee modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}'"
    },
    'who_is_employee_modified_on': {
        'pattern': r"who is the employee modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}'"
    },
    'whose_mgr_ohrid_is': {
        'pattern': r"whose manager ohrid is (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {}"
    },
    'whose_mgr_email_is': {
        'pattern': r"whose manager email is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}'"
    },
    'whose_mgr_band_is': {
        'pattern': r"whose manager band is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}'"
    },
    'whose_oneoone_mgr_ohrid_is': {
        'pattern': r"whose one-o-one manager ohrid is (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {}"
    },
    'whose_oneoone_mgr_email_is': {
        'pattern': r"whose one-o-one manager email is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}'"
    },
    'whose_inserted_on_is': {
        'pattern': r"whose inserted on date is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}'"
    },
    'whose_modified_by_is': {
        'pattern': r"whose modified by is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}'"
    },
    'whose_modified_on_is': {
        'pattern': r"whose modified on date is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}'"
    },
    'whose_name_is': {
        'pattern': r"whose name is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%'"
    },
    'whose_email_is': {
        'pattern': r"whose email is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpEmailID = '{}'"
    },
    'whose_band_is': {
        'pattern': r"whose band is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}'"
    },
    'whose_tower_is': {
        'pattern': r"whose tower is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%'"
    },
    'whose_process_id_is': {
        'pattern': r"whose process id is (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {}"
    },
    'whose_process_name_is': {
        'pattern': r"whose process name is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%'"
    },
    'whose_doj_is': {
        'pattern': r"whose doj is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ = '{}'"
    },
    'whose_dol_is': {
        'pattern': r"whose dol is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL = '{}'"
    },
    'select_employee_by_ohrid': {
        'pattern': r"select employee with ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {}"
    },
    'select_employee_by_name': {
        'pattern': r"select employee with name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%'"
    },
    'select_employee_by_email': {
        'pattern': r"select employee with email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpEmailID = '{}'"
    },
    'select_employee_by_band': {
        'pattern': r"select employee with band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}'"
    },
    'select_employee_by_tower': {
        'pattern': r"select employee in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%'"
    },
    'select_employee_by_process_id': {
        'pattern': r"select employee with process id (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {}"
    },
    'select_employee_by_process_name': {
        'pattern': r"select employee in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%'"
    },
    'select_employee_by_doj': {
        'pattern': r"select employee with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ = '{}'"
    },
    'select_employee_by_dol': {
        'pattern': r"select employee with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL = '{}'"
    },
    'select_employee_by_mgr_ohrid': {
        'pattern': r"select employee with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {}"
    },
    'select_employee_by_mgr_email': {
        'pattern': r"select employee with manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}'"
    },
    'select_employee_by_mgr_band': {
        'pattern': r"select employee with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}'"
    },
    'select_employee_by_oneoone_mgr_ohrid': {
        'pattern': r"select employee with one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {}"
    },
    'select_employee_by_oneoone_mgr_email': {
        'pattern': r"select employee with one-o-one manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}'"
    },
    'select_employee_by_inserted_on': {
        'pattern': r"select employee inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}'"
    },
    'select_employee_by_modified_by': {
        'pattern': r"select employee modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}'"
    },
    'select_employee_by_modified_on': {
        'pattern': r"select employee modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}'"
    },
    'all_employees': {
        'pattern': r"show all employees",
        'query_template': "SELECT * FROM EmployeeMaster"
    },
    # Complex Queries with combinations
    'select_employee_by_name_and_email': {
        'pattern': r"select employee with name (.+) and email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%' AND EmpEmailID = '{}'"
    },
    'select_employee_by_band_and_tower': {
        'pattern': r"select employee with band (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employee_by_process_and_doj': {
        'pattern': r"select employee in process (.+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND DOJ = '{}'"
    },
    'select_employee_by_mgr_ohrid_and_email': {
        'pattern': r"select employee with manager ohrid (\d+) and email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {} AND EmpEmailID = '{}'"
    },
    'select_employee_by_mgr_band_and_name': {
        'pattern': r"select employee with manager band (.+) and name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}' AND EmpName LIKE '%{}%'"
    },
    'select_employee_by_oneoone_mgr_ohrid_and_dol': {
        'pattern': r"select employee with one-o-one manager ohrid (\d+) and dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {} AND DOL = '{}'"
    },
    'select_employee_by_inserted_and_modified': {
        'pattern': r"select employee inserted on (.+) and modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}' AND ModifiedOn = '{}'"
    },
    # Date-based Queries
    'show_employees_with_doj_before': {
        'pattern': r"show employees with doj before (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ < '{}'"
    },
    'show_employees_with_doj_after': {
        'pattern': r"show employees with doj after (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ > '{}'"
    },
    'show_employees_with_dol_before': {
        'pattern': r"show employees with dol before (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL < '{}'"
    },
    'show_employees_with_dol_after': {
        'pattern': r"show employees with dol after (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL > '{}'"
    },
    'show_employees_with_doj_between': {
        'pattern': r"show employees with doj between (.+) and (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ BETWEEN '{}' AND '{}'"
    },
    'show_employees_with_dol_between': {
        'pattern': r"show employees with dol between (.+) and (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL BETWEEN '{}' AND '{}'"
    },
    # Queries with Manager Details
    'select_employee_with_mgr_name': {
        'pattern': r"select employee with manager name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID IN (SELECT OHRID FROM EmployeeMaster WHERE EmpName LIKE '%{}%')"
    },
    'select_employee_with_mgr_band': {
        'pattern': r"select employee with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID IN (SELECT OHRID FROM EmployeeMaster WHERE EmpBand = '{}')"
    },
    'show_employees_in_process_and_tower': {
        'pattern': r"show employees in process (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%' AND TowerName LIKE '%{}%'"
    },
    'show_employees_with_doj_dol_between': {
        'pattern': r"show employees with doj between (.+) and (.+) and dol between (.+) and (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ BETWEEN '{}' AND '{}' AND DOL BETWEEN '{}' AND '{}'"
    },
    'select_employee_with_process_id_and_name': {
        'pattern': r"select employee with process id (\d+) and name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {} AND EmpName LIKE '%{}%'"
    },
    'select_employee_with_process_id_and_doj': {
        'pattern': r"select employee with process id (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {} AND DOJ = '{}'"
    },
    'select_employee_with_mgr_ohrid_and_process': {
        'pattern': r"select employee with manager ohrid (\d+) and in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {} AND ProcessName LIKE '%{}%'"
    },
    'select_employee_with_mgr_ohrid_and_doj': {
        'pattern': r"select employee with manager ohrid (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {} AND DOJ = '{}'"
    },
    'select_employee_with_mgr_band_and_tower': {
        'pattern': r"select employee with manager band (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employee_with_mgr_email_and_process': {
        'pattern': r"select employee with manager email (.+) and in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}' AND ProcessName LIKE '%{}%'"
    },
    'select_employee_with_oneoone_mgr_ohrid_and_doj': {
        'pattern': r"select employee with one-o-one manager ohrid (\d+) and doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {} AND DOJ = '{}'"
    },
    'select_employee_with_oneoone_mgr_email_and_tower': {
        'pattern': r"select employee with one-o-one manager email (.+) and in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}' AND TowerName LIKE '%{}%'"
    },
    'select_employee_with_inserted_on_and_mgr_band': {
        'pattern': r"select employee inserted on (.+) with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}' AND MgrBand = '{}'"
    },
    'select_employee_with_modified_by_and_doj': {
        'pattern': r"select employee modified by (.+) with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}' AND DOJ = '{}'"
    },
    'select_employee_with_modified_on_and_process': {
        'pattern': r"select employee modified on (.+) in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}' AND ProcessName LIKE '%{}%'"
    },
    # Queries with Greetings and Natural Language
    'greet_and_ask_employee_name': {
        'pattern': r"(hi|hello|hey),? what is the name of employee with ohrid (\d+)",
        'query_template': "SELECT EmpName FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_email': {
        'pattern': r"(hi|hello|hey),? what is the email of employee with ohrid (\d+)",
        'query_template': "SELECT EmpEmailID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_band': {
        'pattern': r"(hi|hello|hey),? what is the band of employee with ohrid (\d+)",
        'query_template': "SELECT EmpBand FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_tower': {
        'pattern': r"(hi|hello|hey),? what is the tower of employee with ohrid (\d+)",
        'query_template': "SELECT TowerName FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_process': {
        'pattern': r"(hi|hello|hey),? what is the process of employee with ohrid (\d+)",
        'query_template': "SELECT ProcessName FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_doj': {
        'pattern': r"(hi|hello|hey),? when did employee with ohrid (\d+) join",
        'query_template': "SELECT DOJ FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_dol': {
        'pattern': r"(hi|hello|hey),? when did employee with ohrid (\d+) leave",
        'query_template': "SELECT DOL FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_mgr_ohrid': {
        'pattern': r"(hi|hello|hey),? who is the manager of employee with ohrid (\d+)",
        'query_template': "SELECT MgrOhrID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_mgr_email': {
        'pattern': r"(hi|hello|hey),? what is the email of manager of employee with ohrid (\d+)",
        'query_template': "SELECT MgrEmailID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_mgr_band': {
        'pattern': r"(hi|hello|hey),? what is the band of manager of employee with ohrid (\d+)",
        'query_template': "SELECT MgrBand FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_oneoone_mgr_ohrid': {
        'pattern': r"(hi|hello|hey),? who is the one-o-one manager of employee with ohrid (\d+)",
        'query_template': "SELECT OneOOneMgrOhrID FROM EmployeeMaster WHERE OHRID = {}"
    },
    'greet_and_ask_employee_oneoone_mgr_email': {
        'pattern': r"(hi|hello|hey),? what is the email of one-o-one manager of employee with ohrid (\d+)",
        'query_template': "SELECT OneOOneMgrEmailID FROM EmployeeMaster WHERE OHRID = {}"
    },
    # Combining Queries and Natural Language
    'who_is_employee_with_ohrid': {
        'pattern': r"who is the employee with ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OHRID = {}"
    },
    'who_is_employee_with_email': {
        'pattern': r"who is the employee with email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpEmailID = '{}'"
    },
    'who_is_employee_with_name': {
        'pattern': r"who is the employee with name (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%'"
    },
    'who_is_employee_with_band': {
        'pattern': r"who is the employee with band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}'"
    },
    'who_is_employee_in_tower': {
        'pattern': r"who is the employee in tower (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%'"
    },
    'who_is_employee_in_process': {
        'pattern': r"who is the employee in process (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%'"
    },
    'who_is_employee_with_doj': {
        'pattern': r"who is the employee with doj (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ = '{}'"
    },
    'who_is_employee_with_dol': {
        'pattern': r"who is the employee with dol (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL = '{}'"
    },
    'who_is_employee_with_mgr_ohrid': {
        'pattern': r"who is the employee with manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {}"
    },
    'who_is_employee_with_mgr_email': {
        'pattern': r"who is the employee with manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}'"
    },
    'who_is_employee_with_mgr_band': {
        'pattern': r"who is the employee with manager band (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}'"
    },
    'who_is_employee_with_oneoone_mgr_ohrid': {
        'pattern': r"who is the employee with one-o-one manager ohrid (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {}"
    },
    'who_is_employee_with_oneoone_mgr_email': {
        'pattern': r"who is the employee with one-o-one manager email (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}'"
    },
    'who_is_employee_inserted_on': {
        'pattern': r"who is the employee inserted on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}'"
    },
    'who_is_employee_modified_by': {
        'pattern': r"who is the employee modified by (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}'"
    },
    'who_is_employee_modified_on': {
        'pattern': r"who is the employee modified on (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}'"
    },
    # Using "Whose"
    'whose_mgr_ohrid_is': {
        'pattern': r"whose manager ohrid is (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrOhrID = {}"
    },
    'whose_mgr_email_is': {
        'pattern': r"whose manager email is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrEmailID = '{}'"
    },
    'whose_mgr_band_is': {
        'pattern': r"whose manager band is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE MgrBand = '{}'"
    },
    'whose_oneoone_mgr_ohrid_is': {
        'pattern': r"whose one-o-one manager ohrid is (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrOhrID = {}"
    },
    'whose_oneoone_mgr_email_is': {
        'pattern': r"whose one-o-one manager email is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE OneOOneMgrEmailID = '{}'"
    },
    'whose_inserted_on_is': {
        'pattern': r"whose inserted on date is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE InsertedOn = '{}'"
    },
    'whose_modified_by_is': {
        'pattern': r"whose modified by is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedBy = '{}'"
    },
    'whose_modified_on_is': {
        'pattern': r"whose modified on date is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ModifiedOn = '{}'"
    },
    'whose_name_is': {
        'pattern': r"whose name is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpName LIKE '%{}%'"
    },
    'whose_email_is': {
        'pattern': r"whose email is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpEmailID = '{}'"
    },
    'whose_band_is': {
        'pattern': r"whose band is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE EmpBand = '{}'"
    },
    'whose_tower_is': {
        'pattern': r"whose tower is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE TowerName LIKE '%{}%'"
    },
    'whose_process_id_is': {
        'pattern': r"whose process id is (\d+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessID = {}"
    },
    'whose_process_name_is': {
        'pattern': r"whose process name is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE ProcessName LIKE '%{}%'"
    },
    'whose_doj_is': {
        'pattern': r"whose doj is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOJ = '{}'"
    },
    'whose_dol_is': {
        'pattern': r"whose dol is (.+)",
        'query_template': "SELECT * FROM EmployeeMaster WHERE DOL = '{}'"
    },

       # Contextual Responses
    'greeting': {
        'pattern': r"(hi|hello|hey|good morning|good afternoon|good evening)",
        'response': "Hello! How can I assist you today with the CMDB Tracker?"
    },
    'about_cmdb_tracker': {
        'pattern': r"(what is|tell me about|describe) CMDB Tracker",
        'response': "CMDB Tracker is a system designed to manage and track the configuration items in your IT environment. It includes comprehensive details about each employee, including their OHRID, name, email, band, tower, process information, and managerial relationships."
    },
    'employee_master_details': {
        'pattern': r"(describe|what is) EmployeeMaster",
        'response': "The EmployeeMaster table contains detailed information about each employee, including their OHRID, name, email, band, tower, process ID, process name, date of joining (DOJ), date of leaving (DOL), manager OHRID, manager email, manager band, one-on-one manager OHRID, one-on-one manager email, insertion date, and modification details."
    },
    'how_to_use': {
        'pattern': r"(how to use|guide me|help) CMDB Tracker",
        'response': "You can use CMDB Tracker by querying for specific employee details using their OHRID, name, email, or other attributes. For example, you can ask 'select employee with ohrid 12345' to get details about a specific employee. You can also inquire about the entire employee list by saying 'show all employees'."
    },
    'thanks': {
        'pattern': r"(thank you|thanks)",
        'response': "You're welcome! If you have any more questions, feel free to ask."
    }
}
