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
    {'name': 'Willow Bark Extract', 'description': 'Willow Bark Extract: Precursor to aspirin, used as a pain reliever', 'date': '1600-01-01'},
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
     {'name': 'William Harvey\'s Discovery of Blood Circulation', 'description': 'William Harvey published "De Motu Cordis," demonstrating that blood circulates continuously through the body, pumped by the heart.', 'date': '1628-01-01'},
    {'name': 'Anton van Leeuwenhoek\'s Microscopic Discoveries', 'description': 'Anton van Leeuwenhoek used a microscope to observe and describe microorganisms, including bacteria and protozoa.', 'date': '1676-01-01'},
    {'name': 'Marcello Malpighi\'s Discovery of Capillaries', 'description': 'Marcello Malpighi used a microscope to discover capillaries, thus completing the understanding of the circulatory system.', 'date': '1661-01-01'},
    {'name': 'John Ray\'s Classification of Plants', 'description': 'John Ray published "Historia Plantarum," a major step in the classification of plants, laying the foundation for modern botany.', 'date': '1686-01-01'},
    {'name': 'Robert Hooke\'s Micrographia', 'description': 'Robert Hooke published "Micrographia," where he described the cellular structure of cork and coined the term "cell."', 'date': '1665-01-01'},
    {'name': 'Stephen Hales\' Discovery of Blood Pressure', 'description': 'Stephen Hales conducted the first measurements of blood pressure in animals, establishing the concept of hemodynamics.', 'date': '1733-01-01'},
    {'name': 'Marcello Malpighi\'s Work on Plant Anatomy', 'description': 'Marcello Malpighi published "Anatome Plantarum," detailing the structure of plant tissues and advancing plant anatomy.', 'date': '1671-01-01'},
    {'name': 'Discovery of the Lymphatic System', 'description': 'Thomas Bartholin and Olaus Rudbeck independently discovered the lymphatic system, providing insights into the circulatory and immune systems.', 'date': '1652-01-01'},
    {'name': 'Stensen\'s Duct', 'description': 'Niels Stensen (Steno) discovered the parotid duct (Stensen\'s duct), contributing to the understanding of salivary glands and their function.', 'date': '1660-01-01'},
    {'name': 'Giovanni Alfonso Borelli\'s Muscular Mechanics', 'description': 'Giovanni Alfonso Borelli published "De Motu Animalium," explaining the mechanical principles of muscle movement and biomechanics.', 'date': '1680-01-01'},
    {'name': 'Linnaean Taxonomy', 'description': 'Carl Linnaeus publishes "Systema Naturae," laying the foundation for modern biological classification.', 'date': '1735-01-01'},
    {'name': 'Spallanzani\'s Experiment', 'description': 'Lazzaro Spallanzani conducts experiments disproving spontaneous generation and advancing the study of microbiology.', 'date': '1768-01-01'},
    {'name': 'Oxygen Discovery', 'description': 'Joseph Priestley and Antoine Lavoisier discover and describe oxygen, revolutionizing the understanding of respiration and combustion.', 'date': '1774-01-01'},
    {'name': 'William Withering and Digitalis', 'description': 'William Withering publishes on the use of digitalis (from foxglove) to treat heart conditions.', 'date': '1785-01-01'},
    {'name': 'Coagulation of Blood', 'description': 'William Hewson studies the coagulation of blood and describes the role of fibrinogen.', 'date': '1772-01-01'},
    {'name': 'Spontaneous Generation Disproved', 'description': 'Lazzaro Spallanzani demonstrates that boiling broth will sterilize it and prevent microbial growth, challenging the theory of spontaneous generation.', 'date': '1768-01-01'},
    {'name': 'Biogeography and Buffon\'s Law', 'description': 'Georges-Louis Leclerc, Comte de Buffon, proposes Buffon\'s Law, suggesting that different regions have distinct plants and animals.', 'date': '1761-01-01'},
    {'name': 'Electrophysiology', 'description': 'Luigi Galvani discovers bioelectricity by demonstrating that muscles of dead frogs\' legs twitch when struck by an electrical spark.', 'date': '1791-01-01'},
    {'name': 'Vaccination Against Cowpox', 'description': 'Benjamin Jesty performs an early form of vaccination using cowpox to protect against smallpox.', 'date': '1774-01-01'},
    {'name': 'Brownian Motion', 'description': 'Jan Ingenhousz describes the random movement of particles suspended in a fluid, later known as Brownian motion.', 'date': '1785-01-01'},
     {'name': 'Discovery of the Blood-Brain Barrier', 'description': 'Paul Ehrlich discovers that the brain is protected from certain dyes and chemicals by the blood-brain barrier.', 'date': '1885-01-01'},
    {'name': 'Discovery of Phagocytosis', 'description': 'Ilya Metchnikoff discovers phagocytosis, the process by which certain cells can engulf and destroy bacteria.', 'date': '1882-01-01'},
    {'name': 'First Human Blood Transfusion', 'description': 'James Blundell performs the first successful human-to-human blood transfusion.', 'date': '1818-01-01'},
    {'name': 'Germ Theory of Disease', 'description': 'Louis Pasteur and Robert Koch develop the germ theory of disease, proving that microorganisms cause diseases.', 'date': '1860-01-01'},
    {'name': 'Pasteurization', 'description': 'Louis Pasteur develops pasteurization, a process to kill harmful bacteria in beverages like milk and wine.', 'date': '1864-01-01'},
    {'name': 'Antiseptic Surgery', 'description': 'Joseph Lister introduces antiseptic surgical techniques, greatly reducing post-surgical infections.', 'date': '1867-01-01'},
    {'name': 'Discovery of the Golgi Apparatus', 'description': 'Camillo Golgi discovers the Golgi apparatus, a key structure in the cell responsible for packaging proteins.', 'date': '1898-01-01'},
    {'name': 'First Recorded Use of Ether as Anesthetic', 'description': 'William T.G. Morton demonstrates the use of ether as a surgical anesthetic.', 'date': '1846-01-01'},
    {'name': 'Discovery of Anesthesia', 'description': 'Crawford Long uses ether for the first time as an anesthetic during surgery.', 'date': '1842-01-01'},
    {'name': 'Discovery of Bacteria as a Cause of Disease', 'description': 'Robert Koch identifies the bacteria causing anthrax, establishing a direct link between specific bacteria and diseases.', 'date': '1876-01-01'},
    {'name': 'Mendelian Inheritance', 'description': 'Gregor Mendel publishes his work on the inheritance of traits in pea plants, laying the foundation for genetics.', 'date': '1865-01-01'},
    {'name': 'Louis Pasteur’s Rabies Vaccine', 'description': 'Louis Pasteur develops the first vaccine for rabies, saving the life of Joseph Meister.', 'date': '1885-01-01'},
    {'name': 'Discovery of Tuberculosis Bacillus', 'description': 'Robert Koch discovers Mycobacterium tuberculosis, the bacteria causing tuberculosis.', 'date': '1882-01-01'},
    {'name': 'Discovery of the Diphtheria Antitoxin', 'description': 'Emil von Behring and Kitasato Shibasaburō develop the diphtheria antitoxin, which can neutralize the effects of diphtheria toxin.', 'date': '1890-01-01'},
    {'name': 'Discovery of the Electrocardiogram (ECG)', 'description': 'Willem Einthoven invents the electrocardiogram, a device that measures the electrical activity of the heart.', 'date': '1903-01-01'},
     {'name': 'Discovery of Blood Groups', 'description': 'Karl Landsteiner identifies human blood groups (A, B, AB, and O), leading to safer blood transfusions.', 'date': '1901-01-01'},
    {'name': 'Discovery of Vitamins', 'description': 'Casimir Funk coins the term "vitamins" and identifies the first vitamin, thiamine (Vitamin B1).', 'date': '1912-01-01'},
    {'name': 'Discovery of Heparin', 'description': 'Jay McLean and William Henry Howell discover heparin, an anticoagulant used to prevent blood clots.', 'date': '1916-01-01'},
    {'name': 'Discovery of the Electroencephalogram (EEG)', 'description': 'Hans Berger records the first human electroencephalogram (EEG), a test that measures electrical activity in the brain.', 'date': '1924-01-01'},
    {'name': 'Discovery of Streptomycin', 'description': 'Selman Waksman discovers streptomycin, the first effective antibiotic against tuberculosis.', 'date': '1943-01-01'},
    {'name': 'Discovery of DNA as the Genetic Material', 'description': 'Oswald Avery, Colin MacLeod, and Maclyn McCarty identify DNA as the molecule responsible for heredity.', 'date': '1944-01-01'},
    {'name': 'Discovery of Cortisone', 'description': 'Edward Calvin Kendall, Tadeus Reichstein, and Philip Showalter Hench discover cortisone, a steroid hormone used to treat arthritis.', 'date': '1949-01-01'},
    {'name': 'Development of the Polio Vaccine', 'description': 'Jonas Salk develops the first effective polio vaccine, which significantly reduces the incidence of poliomyelitis.', 'date': '1955-01-01'},
    {'name': 'Discovery of the Structure of Insulin', 'description': 'Frederick Sanger determines the amino acid sequence of insulin, the first protein to be sequenced.', 'date': '1955-01-01'},
    {'name': 'Discovery of the Structure of Haemoglobin', 'description': 'Max Perutz and John Kendrew determine the three-dimensional structure of haemoglobin using X-ray crystallography.', 'date': '1959-01-01'},
    {'name': 'Discovery of Restriction Enzymes', 'description': 'Werner Arber, Hamilton Smith, and Daniel Nathans discover restriction enzymes, which cut DNA at specific sequences.', 'date': '1970-01-01'},
    {'name': 'Discovery of Reverse Transcriptase', 'description': 'Howard Temin and David Baltimore independently discover reverse transcriptase, an enzyme used by retroviruses to replicate.', 'date': '1970-01-01'},
    {'name': 'Development of the CT Scan', 'description': 'Godfrey Hounsfield and Allan Cormack develop the computed tomography (CT) scan, allowing detailed imaging of internal organs.', 'date': '1972-01-01'},
    {'name': 'Discovery of Oncogenes', 'description': 'Michael Bishop and Harold Varmus discover oncogenes, genes that have the potential to cause cancer.', 'date': '1976-01-01'},
    {'name': 'Development of PCR', 'description': 'Kary Mullis develops the polymerase chain reaction (PCR), a technique to amplify DNA sequences.', 'date': '1983-01-01'},
    {'name': 'Discovery of Prions', 'description': 'Stanley Prusiner discovers prions, infectious proteins that cause neurodegenerative diseases.', 'date': '1982-01-01'},
    {'name': 'Discovery of the Hepatitis B Virus', 'description': 'Baruch Blumberg discovers the Hepatitis B virus and develops a vaccine against it.', 'date': '1967-01-01'},
    {'name': 'Discovery of the Human Immunodeficiency Virus (HIV)', 'description': 'Luc Montagnier and Robert Gallo identify HIV as the virus responsible for AIDS.', 'date': '1983-01-01'},
    {'name': 'Identification of BRCA1', 'description': 'Mary-Claire King and colleagues identify the BRCA1 gene, mutations in which are linked to increased risk of breast and ovarian cancer.', 'date': '1990-01-01'},
    {'name': 'Cloning of Dolly the Sheep', 'description': 'Ian Wilmut and Keith Campbell successfully clone the first mammal, Dolly the sheep, from an adult somatic cell.', 'date': '1996-01-01'},
    {'name': 'Nitroplast', 'description': 'Scientists discover the first nitrogen-fixing algae.', 'date': '2024-01-01'},
    {
    "name": "COVID-19 Pandemic","description": "COVID-19, caused by the novel coronavirus SARS-CoV-2, was first identified in Wuhan, China, in December 2019. The virus rapidly spread worldwide, leading to a global pandemic declared by the World Health Organization in March 2020. The pandemic resulted in significant mortality and morbidity, overwhelming healthcare systems, and causing widespread socioeconomic disruption.","date": "2019-12-01"},
    {
    "name": "mRNA COVID-19 Vaccines",
    "description": "In response to the COVID-19 pandemic, mRNA vaccines such as Pfizer-BioNTech's BNT162b2 and Moderna's mRNA-1273 were developed. These vaccines use messenger RNA to instruct cells to produce a protein that triggers an immune response. The rapid development and approval of these vaccines marked a significant milestone in vaccine technology.",
    "date": "2020-12-11"
    }
]

for discovery in discoveries:
    MoleculeDisc.objects.create(
        name=discovery['name'],
        description=discovery['description'],
        date=datetime.strptime(discovery['date'], '%Y-%m-%d'),

    )

print("Database populated successfully.")