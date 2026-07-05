class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        mail_name, domain_part = email.split("@")
        domain_name, domain_extension = domain_part.split(".")
        return self.__is_name_valid(mail_name) and self.__is_mail_valid(domain_name) and self.__is_domain_valid(
            domain_extension)
