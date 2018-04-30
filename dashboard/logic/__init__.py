from .administrator.administrator_logic import AdministratorLogic
from .educator_logic import EducatorLogic
from .general_logic import GeneralLogic
from .student_logic import StudentLogic
from .user_logic import UserLogic

user_logic = UserLogic()
general = GeneralLogic()
student = StudentLogic()
educator = EducatorLogic()
administrator = AdministratorLogic(student=student)

__all__ = ['general', 'student', 'educator', 'administrator', 'user_logic']
