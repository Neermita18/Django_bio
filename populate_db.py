import os
import django
from datetime import datetime
import random

# Ensure the Django environment is set up correctly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BioLine.settings')
django.setup()

from timeline.models import MoleculeDisc


discoveries = [
    {'name': 'Quinine', 'description': 'Quinine synthesized; An antimalarial drug from cinchona bark', 'date': '1820-01-01'},
    {'name': 'Smallpox Vaccine', 'description': 'Small Pox Vaccine: the first successful vaccine, was developed by Edward Jenner', 'date': '1796-01-01'},
    {'name': 'Morphine', 'description': 'Morpohine: Pain medication isolated from opium', 'date': '1804-01-01'},
    {'name': 'Penicillin', 'description': 'Penicillin: First antibiotic discovered by Alexander Fleming', 'date': '1928-09-28'},
    {'name': 'Vitamin C', 'description': 'Vitamin C: Essential nutrient, ascorbic acid isolated by Albert Szent-Györgyi', 'date': '1932-01-01'},
    {'name': 'Aspirin', 'description': 'Aspirin: Pain reliever and anti-inflammatory drug, marketed by Bayer', 'date': '1899-01-01'},
    {'name': 'Insulin', 'description': 'Insulin: Hormone for diabetes treatment, discovered by Frederick Banting and Charles Best', 'date': '1921-01-01'},
    {'name': 'Cisplatin', 'description': 'Cisplatin discovered; a Chemotherapy drug', 'date': '1965-01-01'},
    {'name': 'Monoclonal Antibodies', 'description': 'Monoclonal Antibodies: Antibodies from a single clone of cells, developed by César Milstein and Georges Köhler', 'date': '1975-01-01'},
    {'name': 'AZT', 'description': 'AZT: First antiretroviral drug for HIV/AIDS synthesized by Jerome Horowitz', 'date': '1987-01-01'},
    {'name': 'Imatinib (Gleevec)', 'description': 'Imatinib: Drug for chronic myeloid leukemia was invented by a team led by Nicholas Lyndon', 'date': '2001-01-01'},
    {'name': 'CRISPR-Cas9', 'description': 'CRISPR-Cas9: A Genome editing tool developed by Jennifer Doudna and Emmanuelle Charpentier', 'date': '2012-01-01'},
    {'name': 'Pembrolizumab (Keytruda)', 'description': 'Pembrolizumab (Keytruda): A Cancer immunotherapy drug invented by scientists at Organon', 'date': '2014-01-01'},
    {'name': 'Willow Bark Extract', 'description': 'Precursor to aspirin, used as a pain reliever', 'date': '1600-01-01'},
    {'name': 'Nuclein', 'description': 'Friedrich Miescher discovers and isolates nuclein (now DNA)', 'date': '1869-01-01'},
    {'name': 'Cell Theory', 'description': 'Cell Theory: Developed by Schleiden and Schwann: All living things are composed of cells', 'date': '1838-01-01'},
    {'name': 'Haemoglobin', 'description': 'Haemoglobin: Protein that carries oxygen in the blood discovered by Hünefeld', 'date': '1840-01-01'},
    {'name': 'X-ray', 'description': 'Nobel Prize awarded to Max Perutz for determining structure of haemoglobin in Chemistry with John Kendrew, who sequenced the globular protein myoglobin.', 'date': '1962-01-01'},
    {'name': 'First Protein Crystallization (Hemoglobin)', 'description': 'First protein crystallization: Crystallization of haemoglobin by Otto Funke', 'date': '1849-01-01'},
    {'name': 'DNA Structure', 'description': 'Double helix structure of DNA discovered by Watson and Crick', 'date': '1953-01-01'},
    {'name': 'Messenger RNA (mRNA)', 'description': 'Messenger RNA: Discovered by Sydney Brenner, François Jacob, and Matthew Meselson', 'date': '1961-01-01'},
    {'name': 'Recombinant DNA Technology', 'description': 'Recombinant DNA Technology: Developed by Cohen and Boyer', 'date': '1973-01-01'},
    {'name': 'Human Genome Project', 'description': 'The Human Genome Project began: International research effort to map the human genome', 'date': '1990-01-01'},
    {'name': 'RNA Interference (RNAi)', 'description': 'RNA Interference: Discovered by Andrew Fire and Craig Mello', 'date': '2001-01-01'},
    {'name': 'Paracelsus', 'description': 'Paracelsus, a pioneer in toxicology and medicine, publishes "Great Surgery Book".', 'date': '1536-01-01'},
    {'name': 'Thermometer', 'description': 'Galileo Galilei invents an early version of the thermometer.', 'date': '1593-01-01'},
    {'name': 'Girolamo Fracastoro Germ Theory', 'description': 'Girolamo Fracastoro proposes that epidemic diseases are caused by transferable seedlike entities (germs).', 'date': '1546-01-01'},
    {'name': 'William Harvey', 'description': 'William Harvey describes the systemic circulation and properties of blood being pumped to the brain and body by the heart.', 'date': '1628-01-01'},
    {'name': 'Ambroise Paré', 'description': 'Ambroise Paré: Introduces the use of ligatures in amputation instead of cauterization', 'date': '1552-01-01'},
    {'name': 'Vesalius De humani corporis fabrica', 'description': 'Andreas Vesalius publishes "De humani corporis fabrica" (On the Fabric of the Human Body), revolutionizing the study of human anatomy.', 'date': '1543-01-01'},
    
]

for discovery in discoveries:
    MoleculeDisc.objects.create(
        name=discovery['name'],
        description=discovery['description'],
        date=datetime.strptime(discovery['date'], '%Y-%m-%d'),

    )

print("Database populated successfully.")