import os
import django
from datetime import datetime
import random

# Ensure the Django environment is set up correctly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BioLine.settings')
django.setup()

from timeline.models import MoleculeDisc


discoveries = [
    {'name': 'Quinine', 'description': 'Antimalarial drug from cinchona bark', 'date': '1820-01-01'},
    {'name': 'Smallpox Vaccine', 'description': 'First successful vaccine, developed by Edward Jenner', 'date': '1796-01-01'},
    {'name': 'Morphine', 'description': 'Pain medication isolated from opium', 'date': '1804-01-01'},
    {'name': 'Penicillin', 'description': 'First antibiotic discovered by Alexander Fleming', 'date': '1928-09-28'},
    {'name': 'Vitamin C', 'description': 'Essential nutrient, ascorbic acid isolated by Albert Szent-Györgyi', 'date': '1932-01-01'},
    {'name': 'Aspirin', 'description': 'Pain reliever and anti-inflammatory drug, marketed by Bayer', 'date': '1899-01-01'},
    {'name': 'Insulin', 'description': 'Hormone for diabetes treatment, discovered by Frederick Banting and Charles Best', 'date': '1921-01-01'},
    {'name': 'Cisplatin', 'description': 'Chemotherapy drug', 'date': '1965-01-01'},
    {'name': 'Monoclonal Antibodies', 'description': 'Antibodies from a single clone of cells, developed by César Milstein and Georges Köhler', 'date': '1975-01-01'},
    {'name': 'AZT', 'description': 'First antiretroviral drug for HIV/AIDS', 'date': '1987-01-01'},
    {'name': 'Imatinib (Gleevec)', 'description': 'Drug for chronic myeloid leukemia', 'date': '2001-01-01'},
    {'name': 'CRISPR-Cas9', 'description': 'Genome editing tool', 'date': '2012-01-01'},
    {'name': 'Pembrolizumab (Keytruda)', 'description': 'Cancer immunotherapy drug', 'date': '2014-01-01'},
    {'name': 'Willow Bark Extract', 'description': 'Precursor to aspirin, used as a pain reliever', 'date': '1600-01-01'},
    {'name': 'Cell Theory', 'description': 'All living things are composed of cells', 'date': '1838-01-01'},
    {'name': 'Hemoglobin', 'description': 'Protein that carries oxygen in the blood', 'date': '1840-01-01'},
    {'name': 'First Protein Crystallization (Hemoglobin)', 'description': 'Crystallized by Otto Funke', 'date': '1849-01-01'},
    {'name': 'DNA Structure', 'description': 'Double helix structure discovered by Watson and Crick', 'date': '1953-01-01'},
    {'name': 'Messenger RNA (mRNA)', 'description': 'Discovered by Sydney Brenner, François Jacob, and Matthew Meselson', 'date': '1961-01-01'},
    {'name': 'Recombinant DNA Technology', 'description': 'Developed by Cohen and Boyer', 'date': '1973-01-01'},
    {'name': 'Human Genome Project', 'description': 'International research effort to map the human genome', 'date': '1990-01-01'},
    {'name': 'RNA Interference (RNAi)', 'description': 'Discovered by Andrew Fire and Craig Mello', 'date': '2001-01-01'}
]

for discovery in discoveries:
    MoleculeDisc.objects.create(
        name=discovery['name'],
        description=discovery['description'],
        date=datetime.strptime(discovery['date'], '%Y-%m-%d'),

    )

print("Database populated successfully.")