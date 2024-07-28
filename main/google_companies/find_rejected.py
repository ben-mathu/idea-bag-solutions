import os

f = open(f'{os.path.dirname(os.path.realpath(__file__))}/companies_found.txt', 'r')
companies_found = f.readlines()

f = open(f'{os.path.dirname(os.path.realpath(__file__))}/rejects.txt', 'r')
rejects = f.readlines()

f = open(f'{os.path.dirname(os.path.realpath(__file__))}/companies.txt', 'r')
companies = f.readlines()

found_mapping = []
with open(f'{os.path.dirname(os.path.realpath(__file__))}/rejects.txt', 'a') as f:
  for company in companies:
    company = company.strip()
    index = company.split('-')[0].split('.')[0].strip()
    
    for rejected in rejects:
      rejected = rejected.strip()
      if rejected == '':
        continue
      
      rejected_index = rejected.split('-')[0].split('.')[0].strip()

      if rejected_index == index:
        found_mapping.append(index)
        break

    if index in found_mapping:
      continue
    
    for company_found in companies_found:
      company_found = company_found.strip()
      
      if company_found == '':
        continue
      
      index_company_found = company_found.split('-')[0].split('.')[0].split(' ')[-1].strip()
      
      if index == index_company_found:
        found_mapping.append(index)
        break
    
    if index in found_mapping:
      continue
    
    f.write(f'{company}\n')
        