from faker import Faker
fake = Faker()

def create_contacts(amount):
    for i in range(0,amount):
        name = fake.first_name()
        surname = fake.last_name()
        company = f'{fake.first_name()}&partners'
        position = fake.job()
        number = fake.phone_number()
        email = f'{name}@{company}.com'
        company_phone = fake.phone_number()
        print(name, surname, company, position, number, email, company_phone)

create_contacts(3)
