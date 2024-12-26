import pandas as pd

# Sample DataFrame
data = {
    'vaccinated': [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    'contracted_chickenpox': [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    'sex': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female']
}

df = pd.DataFrame(data)

def chickenpox_by_sex(df):
    # Filter vaccinated children
    vaccinated = df[df['vaccinated'] == 1]

    # Count cases for males and females
    results = {}
    
    for sex in ['male', 'female']:
        # Filter by sex
        vaccinated_sex = vaccinated[vaccinated['sex'] == sex]
        
        # Count those who contracted chickenpox
        contracted = vaccinated_sex[vaccinated_sex['contracted_chickenpox'] == 1].shape[0]
        
        # Count those who did not contract chickenpox
        did_not_contract = vaccinated_sex[vaccinated_sex['contracted_chickenpox'] == 0].shape[0]
        
        # Calculate ratio
        if did_not_contract > 0:
            ratio = contracted / did_not_contract
        else:
            ratio = 0  # Avoid division by zero
        
        results[sex] = ratio
    
    return results

# Call the function and print results
result = chickenpox_by_sex(df)
print(result)