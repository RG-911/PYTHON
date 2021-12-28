import emailapp
from emailapp import Email



class EmailApp:
    em1 = emailapp.Email.Email("John", "Smith")
    print(em1.show_info())
