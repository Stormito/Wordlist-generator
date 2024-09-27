# Função para gerar padrões dinâmicos para standards
def generate_standards():
    standards = []
    
    # Padrões numéricos simples (crescentes e decrescentes)
    for i in range(6, 10):
        standards.append(''.join(['123456789'[:i]])) 
        standards.append(''.join(['987654321'[:i]]))  
    
    # Padrões com "mudar"
    mudar_variants = ['mudar@123', '123@mudar', 'mudar123', '123mudar', '@123mudar']
    standards.extend(mudar_variants) 
    
    return standards

def generate_recurrent():
    recurrent = []
    
    # Padrões de números simples
    for i in range(3, 10):
        recurrent.append(''.join(['123456789'[:i]]))  
    
    # Padrões com "@"
    for i in range(3, 10):
        recurrent.append(''.join(['123456789'[:i], '@']))  
    
    # Anos com "@"
    for year in range(2019, 2023):
        recurrent.append(f'@{year}')  
    
    # Padrões com "@123", "@1234", etc.
    for i in range(3, 6):
        recurrent.append(f'@{"123456"[:i]}')
    
    return recurrent
  
standards = generate_standards()
recurrent = generate_recurrent()

company = input('Insira o nome da empresa: ')

def generate_combinations(company, standards, recurrent):
    company_first_letter = company.capitalize()
    company_short = company[:3]

    # Gera combinações a partir das listas fornecidas
    combinations = []

    for standard in standards:
        combinations.append(standard)

    for rec in recurrent:
        combinations.extend([
            company + rec,
            rec + company,
            company_short + rec,
            rec + company_short,
            company_first_letter + rec,
            rec + company_first_letter,
            company_first_letter[:3] + rec,
            rec + company_first_letter[:3]
        ])

    return combinations

combinations = generate_combinations(company, standards, recurrent)
for combo in combinations:
    print(combo)
