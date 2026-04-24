# HackBio Stage Zero: Python Script
# Requirement: Write a simple Python script for printing the names, affiliation, and the name of the genes you love most, and the name of the organism bearing the gene. The final output should be something like, “Hi, my name is Adewale Ogunleye, a researcher at the University of Tübingen. My favorite gene is lexA in Escherichia coli.”

# HackBio Stage Zero: Team Aspartic Acid Introduction Script

# We use a list of dictionaries to store the details of each team member.
team_aspartic_acid = [
    {
        "name": "Pritish Doshi",
        "affiliation": "a Senior Data Architect from University of Mumbai",
        "favorite_gene": "BRCA2",
        "organism": "Homo sapiens"
    },
    {
        "name": "Gauri Jagtap",
        "affiliation": "a Data Engineer Lead from University of Mumbai",
        "favorite_gene": "HER2",
        "organism": "Homo sapiens"
    }
]

print("--- Team Aspartic Acid Introductions ---\n")
# A 'for' loop iterates through the list and prints the f-string for each team member
for member in team_aspartic_acid:
    output_message = f"Hi, my name is {member['name']}, {member['affiliation']}. My favorite gene is {member['favorite_gene']} in {member['organism']}.\n"
    print(output_message)