import os 
from app import create_app, db 
from app.model import UserGroup, UserInfo, HospitalConstuct, HospitalClass, PatientInfo, DoctorTimetable, ImgDoctorTimetable, ExpertsTimetable, Medicine, CheckClass, CheckItem, ExamClass, ExamItem, InhospitalArea, BedInfo, Price, FamilyDoctorArea, FamilyDoctor, FamilyDoctorWorkArea, FamilyPatientInfo, FamilyPatientTestResult, SpecialConcern, LecturePlace, LectureTime, OpCheckin, OpExam, OpCheck, OpRecipe, OpCheckinAfford, OpExamAfford, OpCheckAfford, OpRecipeAfford, OpCost, InPatientDeposit, InPatientTableSet, InPatientTimeAndBed, InPatientCheck, InPatientInspect, InPatientPrescript, ImgpCheckin, ImgpRecipe, ImgpCheckinAfford, ImgpRecipeAfford, ImgpCost
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

# def make_shell_context():
manager.add_command('db', MigrateCommand)

# @manager.command
# def test():
#     """Run the unit tests"""
#     import unittest
#     test = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    #交互环境用
    manager.run()
    # app.run()
#运行程序用
