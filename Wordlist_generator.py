company = input('Insira o nome da empresa:')
company_first_letter = (company[0].upper() + company[1:])
standards = ['123456', '1234567', '12345678', '123456789', '987654321', '87654321', '7654321', '654321', 'mudar@123', '123@mudar', 'mudar123', '123mudar', '@123mudar']
recurrent = ['123', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789', '123@', '1234@', '12345@', '123456@', '1234567@', '12345678@', '123456789@', '@2019', '@2020', '@2021', '@2022', '123', '1234', '12345', '@123', '@1234', '@12345']

for i in range(len(standards)):
  print(standards[i])

for i in  range(len(recurrent)):
  print(company + recurrent[i])
  print(recurrent[i] + company)
  print(company[0:3] + recurrent[i])
  print(recurrent[i] + company[0:3])
  print(company_first_letter + recurrent[i])
  print(recurrent[i] + company_first_letter)
  print(company_first_letter[0:3] + recurrent[i])
  print(recurrent[i] + company_first_letter[0:3])