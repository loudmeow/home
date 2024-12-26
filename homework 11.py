import pandas as pd

data = {
    'vaccinated': [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    'contracted_chickenpox': [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    'sex': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female']
}

df = pd.DataFrame(data)

def chickenpox_by_sex(df):
    vaccinated = df[df['vaccinated'] == 1]
    results = {}
    
    for sex in ['male', 'female']:
        vaccinated_sex = vaccinated[vaccinated['sex'] == sex]
        contracted = vaccinated_sex[vaccinated_sex['contracted_chickenpox'] == 1].shape[0]
        did_not_contract = vaccinated_sex[vaccinated_sex['contracted_chickenpox'] == 0].shape[0]
        if did_not_contract > 0:
            ratio = contracted / did_not_contract
        else:
            ratio = 0 
        
        results[sex] = ratio
    
    return results
result = chickenpox_by_sex(df)
print(result)