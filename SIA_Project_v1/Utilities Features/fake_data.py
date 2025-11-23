from faker import Faker

fake = Faker()

fake_name = fake.name()
fake_email = fake.email()
fake_address = fake.address()
fake_text = fake.text()
fake_date = fake.date_of_birth()

print(f"Name: {fake_name}")
print(f"Email: {fake_email}")
print(f"Address: {fake_address}")
print(f"Birthdate: {fake_date}")