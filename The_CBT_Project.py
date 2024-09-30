# THIS IS A CBT EXAMINATION
score = 0
subject_done = []
answer_done = ["A", "B", "C", "D"]
def chemistry_questions():
    chemistry = [
        {
            'question': "1.What is the chemical symbol for water?",
            'options': ['A) O2', 'B) CO2', 'C) H2O', 'D) H2SO4'],
            'answer': 'C'
        },
        {
            'question': "2.Which element is represented by the symbol 'Na'?",
            'options': ['A) Sodium', 'B) Nitrogen', 'C) Neon', 'D) Nickel'],
            'answer': 'A'
        },
        {
            'question': "3.What is the pH of pure water?",
            'options': ['A) 1', 'B) 7', 'C) 14', 'D) 10'],
            'answer': 'B'
        },
        {
            'question': "4.Which gas is commonly used in soda bottles?",
            'options': ['A) Nitrogen', 'B) Carbon Dioxide', 'C) Oxygen', 'D) Hydrogen'],
            'answer': 'B'
        },
        {
            'question': "5.What is the main component of natural gas?",
            'options': ['A) Ethylene', 'B) Methane', 'C) Propane', 'D) Butane'],
            'answer': 'B'
        },
        {
            'question': "6.Which acid is found in citrus fruits?",
            'options': ['A) Sulfuric Acid', 'B) Hydrochloric Acid', 'C) Citric Acid', 'D) Acetic Acid'],
            'answer': 'C'
        },

        {
            'question': "8.What is the atomic number of carbon?",
            'options': ['A) 6', 'B) 8', 'C) 12', 'D) 14'],
            'answer': 'A'
        },
        {
            'question': "9.What type of bond involves the sharing of electron pairs between atoms?",
            'options': ['A) Ionic Bond', 'B) Covalent Bond', 'C) Metallic Bond', 'D) Hydrogen Bond'],
            'answer': 'B'
        },
        {
            'question': "10.What is the common name for sodium chloride?",
            'options': ['A) Baking Soda', 'B) Table Salt', 'C) Epsom Salt', 'D) Sugar'],
            'answer': 'B'
        },
        {
            'question': "11.Which element is necessary for respiration in humans?",
            'options': ['A) Carbon', 'B) Hydrogen', 'C) Oxygen', 'D) Nitrogen'],
            'answer': 'C'
        },
        {
            'question': "12.What is the formula for sulfuric acid?",
            'options': ['A) H2SO4', 'B) HCl', 'C) HNO3', 'D) H2CO3'],
            'answer': 'A'
        },
        {
            'question': "13.Which element is most abundant in the Earth's crust?",
            'options': ['A) Iron', 'B) Silicon', 'C) Oxygen', 'D) Calcium'],
            'answer': 'C'
        },
        {
            'question': "14.What is the process of separating a solid from a liquid by filtering called?",
            'options': ['A) Distillation', 'B) Filtration', 'C) Evaporation', 'D) Chromatography'],
            'answer': 'B'
        },
        {
            'question': "15.Which type of reaction involves the combination of two or more substances to form a new compound?",
            'options': ['A) Decomposition Reaction', 'B) Single Replacement Reaction', 'C) Synthesis Reaction', 'D) Double Replacement Reaction'],
            'answer': 'C'
        },
        {
            'question': "16.What is the term for a solution that can no longer dissolve more solute at a given temperature?",
            'options': ['A) Unsaturated Solution', 'B) Saturated Solution', 'C) Supersaturated Solution', 'D) Diluted Solution'],
            'answer': 'B'
        },
        {
            'question': "17.Which gas is produced when an acid reacts with a metal?",
            'options': ['A) Hydrogen', 'B) Oxygen', 'C) Nitrogen', 'D) Carbon Dioxide'],
            'answer': 'A'
        },
        {
            'question': "18.What is the chemical formula for methane?",
            'options': ['A) CH4', 'B) C2H6', 'C) C3H8', 'D) C4H10'],
            'answer': 'A'
        },
        {
            'question': "19.Which type of reaction is characterized by the loss of electrons?",
            'options': ['A) Reduction', 'B) Oxidation', 'C) Neutralization', 'D) Precipitation'],
            'answer': 'B'
        },
        {
            'question': "20.What is the name of the process where a liquid changes to a gas at a temperature below its boiling point?",
            'options': ['A) Evaporation', 'B) Condensation', 'C) Sublimation', 'D) Freezing'],
            'answer': 'A'
        },
        {
            'question': "21.Which element has the highest atomic number in the periodic table?",
            'options': ['A) Uranium', 'B) Plutonium', 'C) Oganesson', 'D) Francium'],
            'answer': 'C'
        },
        {
            'question': "22.Which type of radiation has the highest energy?",
            'options': ['A) Alpha Radiation', 'B) Beta Radiation', 'C) Gamma Radiation', 'D) X-rays'],
            'answer': 'C'
        },
        {
            'question': "23.What is the chemical name for common table sugar?",
            'options': ['A) Glucose', 'B) Fructose', 'C) Sucrose', 'D) Lactose'],
            'answer': 'C'
        },
        {
            'question': "24.What is the most common form of carbon found in nature?",
            'options': ['A) Diamond', 'B) Graphite', 'C) Amorphous Carbon', 'D) Fullerene'],
            'answer': 'B'
        },
        {
            'question': "25.Which type of bond is formed by the transfer of electrons from one atom to another?",
            'options': ['A) Covalent Bond', 'B) Ionic Bond', 'C) Metallic Bond', 'D) Hydrogen Bond'],
            'answer': 'B'
        },
        {
            'question': "26.What is the chemical symbol for gold?",
            'options': ['A) Ag', 'B) Au', 'C) Pb', 'D) Fe'],
            'answer': 'B'
        },
        {
            'question': "27.Which compound is used as a disinfectant and is commonly found in bleach?",
            'options': ['A) Sodium Chloride', 'B) Sodium Hydroxide', 'C) Sodium Hypochlorite', 'D) Sodium Bicarbonate'],
            'answer': 'C'
        },
        {
            'question': "28.What is the name of the process where a solid changes directly to a gas?",
            'options': ['A) Condensation', 'B) Melting', 'C) Sublimation', 'D) Freezing'],
            'answer': 'C'
        },
        {
            'question': "29.Which element is found in all organic compounds?",
            'options': ['A) Carbon', 'B) Hydrogen', 'C) Oxygen', 'D) Nitrogen'],
            'answer': 'A'
        },
        {
            'question': "30.What is the chemical formula for hydrochloric acid?",
            'options': ['A) HCl', 'B) H2SO4', 'C) HNO3', 'D) CH3COOH'],
            'answer': 'A'
        },
        {
            'question': "31.What is the term for a substance that speeds up a chemical reaction without being consumed?",
            'options': ['A) Catalyst', 'B) Solvent', 'C) Reactant', 'D) Product'],
            'answer': 'A'
        },
        {
            'question': "32.What is the name of the acid used in car batteries?",
            'options': ['A) Sulfuric Acid', 'B) Nitric Acid', 'C) Hydrochloric Acid', 'D) Acetic Acid'],
            'answer': 'A'
        },
        {
            'question': "33.What is the name of the law that states that the volume of a gas is inversely proportional to its pressure at constant temperature?",
            'options': ['A) Charles’s Law', 'B) Boyle’s Law', 'C) Avogadro’s Law', 'D) Gay-Lussac’s Law'],
            'answer': 'B'
        },
        {
            'question': "34.Which substance is used as a reagent to test for the presence of starch?",
            'options': ['A) Benedict’s Solution', 'B) Iodine Solution', 'C) Silver Nitrate', 'D) Litmus Paper'],
            'answer': 'B'
        },
        {
            'question': "35.What is the chemical formula for baking soda?",
            'options': ['A) NaCl', 'B) NaHCO3', 'C) KCl', 'D) CaCO3'],
            'answer': 'B'
        },
        {
            'question': "36.Which element is represented by the symbol 'Hg'?",
            'options': ['A) Gold', 'B) Mercury', 'C) Helium', 'D) Hydrogen'],
            'answer': 'B'
        },
        {
            'question': "37.What is the name of the process where a solute dissolves in a solvent?",
            'options': ['A) Filtration', 'B) Distillation', 'C) Dissolution', 'D) Crystallization'],
            'answer': 'C'
        },
        {
            'question': "38.Which type of bond is found in a molecule of hydrogen gas (H2)?",
            'options': ['A) Ionic Bond', 'B) Covalent Bond', 'C) Metallic Bond', 'D) Hydrogen Bond'],
            'answer': 'B'
        },
        {
            'question': "39.What is the term for the number of protons in the nucleus of an atom?",
            'options': ['A) Atomic Mass', 'B) Atomic Number', 'C) Neutron Number', 'D) Mass Number'],
            'answer': 'B'
        },
        {
            'question': "40.What is the chemical formula for table salt?",
            'options': ['A) NaCl', 'B) KCl', 'C) NaBr', 'D) KBr'],
            'answer': 'A'
        },
        {
            'question': "41.Which of the following is an example of a non-metal?",
            'options': ['A) Iron', 'B) Copper', 'C) Carbon', 'D) Zinc'],
            'answer': 'C'
        },
        {
            'question': "42.What is the name of the process used to separate a liquid mixture into its individual components based on boiling points?",
            'options': ['A) Filtration', 'B) Distillation', 'C) Chromatography', 'D) Evaporation'],
            'answer': 'B'
        },
        {
            'question': "43.Which of the following acids is known as 'aqua regia'?",
            'options': ['A) Hydrochloric Acid', 'B) Nitric Acid', 'C) Sulfuric Acid', 'D) Hydrofluoric Acid'],
            'answer': 'B'
        },
        {
            'question': "44.What is the chemical formula for ethanol?",
            'options': ['A) C2H5OH', 'B) C2H6O', 'C) C3H7OH', 'D) CH3OH'],
            'answer': 'A'
        },
        {
            'question': "45.What is the common name for ethanoic acid?",
            'options': ['A) Citric Acid', 'B) Lactic Acid', 'C) Acetic Acid', 'D) Formic Acid'],
            'answer': 'C'
        },
        {
            'question': "46.Which type of chemical reaction absorbs heat from the surroundings?",
            'options': ['A) Exothermic Reaction', 'B) Endothermic Reaction', 'C) Combustion Reaction', 'D) Redox Reaction'],
            'answer': 'B'
        },
        {
            'question': "47.What is the name of the gas that causes the greenhouse effect?",
            'options': ['A) Oxygen', 'B) Carbon Dioxide', 'C) Nitrogen', 'D) Hydrogen'],
            'answer': 'B'
        },
        {
            'question': "48.Which type of bond involves the sharing of electrons in a metal lattice structure?",
            'options': ['A) Ionic Bond', 'B) Covalent Bond', 'C) Metallic Bond', 'D) Hydrogen Bond'],
            'answer': 'C'
        },
        {
            'question': "49.What is the name of the process where an ionic compound dissolves in water to form ions?",
            'options': ['A) Ionization', 'B) Dissolution', 'C) Hydrolysis', 'D) Precipitation'],
            'answer': 'A'
        },
        {
            'question': "50.What is the term for a solution that has a higher concentration of solute than a saturated solution?",
            'options': ['A) Saturated Solution', 'B) Supersaturated Solution', 'C) Unsaturated Solution', 'D) Diluted Solution'],
            'answer': 'B'
        },

    ]
    for trials in chemistry:
        print(trials["question"])
        for opt in trials["options"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        while answer not in answer_done:
            print("wrong input:Enter appropriate answer")
            answer = input("ENTER HERE:").upper()
            if answer in answer_done:
                break 
        
        if answer == trials["answer"]:
            global score
            score += 1
        else:
            score += 0
def Biology_question():
    biology = [
    {
        'question': "1.What is the powerhouse of the cell?",
        'options': ['A) Nucleus', 'B) Mitochondria', 'C) Ribosome', 'D) Endoplasmic Reticulum'],
        'answer': 'B'
    },
    {
        'question': "2.Which organelle is responsible for photosynthesis?",
        'options': ['A) Mitochondria', 'B) Chloroplast', 'C) Nucleus', 'D) Lysosome'],
        'answer': 'B'
    },
    {
        'question': "3.What is the basic unit of life?",
        'options': ['A) Atom', 'B) Tissue', 'C) Cell', 'D) Organ'],
        'answer': 'C'
    },
    {
        'question': "4.Which process converts glucose into energy in cells?",
        'options': ['A) Photosynthesis', 'B) Cellular Respiration', 'C) Fermentation', 'D) Diffusion'],
        'answer': 'B'
    },
    {
        'question': "5.What type of bond holds the two strands of DNA together?",
        'options': ['A) Ionic Bond', 'B) Hydrogen Bond', 'C) Covalent Bond', 'D) Metallic Bond'],
        'answer': 'B'
    },
    {
        'question': "6.Which part of the cell is selectively permeable?",
        'options': ['A) Cell Wall', 'B) Cell Membrane', 'C) Cytoplasm', 'D) Nucleus'],
        'answer': 'B'
    },
    {
        'question': "7.In which part of the cell does protein synthesis occur?",
        'options': ['A) Mitochondria', 'B) Ribosome', 'C) Golgi Apparatus', 'D) Lysosome'],
        'answer': 'B'
    },
    {
        'question': "8.Which organ is responsible for filtering blood in humans?",
        'options': ['A) Liver', 'B) Heart', 'C) Kidney', 'D) Stomach'],
        'answer': 'C'
    },
    {
        'question': "9.What is the role of ribosomes in the cell?",
        'options': ['A) Energy Production', 'B) Protein Synthesis', 'C) Storage of Nutrients', 'D) DNA Replication'],
        'answer': 'B'
    },
    {
        'question': "10.What structure in plant cells provides support and protection?",
        'options': ['A) Cell Membrane', 'B) Cell Wall', 'C) Chloroplast', 'D) Vacuole'],
        'answer': 'B'
    },
    {
        'question': "11.Which process involves the division of a cell’s nucleus?",
        'options': ['A) Cytokinesis', 'B) Mitosis', 'C) Meiosis', 'D) Interphase'],
        'answer': 'B'
    },
    {
        'question': "12.What is the main function of the xylem in plants?",
        'options': ['A) Transport of Water', 'B) Photosynthesis', 'C) Storage of Nutrients', 'D) Reproduction'],
        'answer': 'A'
    },
    {
        'question': "13.Which molecule carries genetic information?",
        'options': ['A) RNA', 'B) Protein', 'C) DNA', 'D) Lipid'],
        'answer': 'C'
    },
    {
        'question': "14.What is the primary function of chlorophyll?",
        'options': ['A) Energy Storage', 'B) Photosynthesis', 'C) Respiration', 'D) Protection'],
        'answer': 'B'
    },
    {
        'question': "15.Which blood cells are responsible for fighting infections?",
        'options': ['A) Red Blood Cells', 'B) Platelets', 'C) White Blood Cells', 'D) Plasma'],
        'answer': 'C'
    },
    {
        'question': "16.What is the basic structural unit of an organism?",
        'options': ['A) Atom', 'B) Molecule', 'C) Cell', 'D) Tissue'],
        'answer': 'C'
    },
    {
        'question': "17.Which organelle is known as the 'control center' of the cell?",
        'options': ['A) Ribosome', 'B) Nucleus', 'C) Mitochondria', 'D) Golgi Apparatus'],
        'answer': 'B'
    },
    {
        'question': "18.What is the function of the Golgi Apparatus?",
        'options': ['A) Protein Synthesis', 'B) DNA Replication', 'C) Packaging and Distribution of Proteins', 'D) Lipid Metabolism'],
        'answer': 'C'
    },
    {
        'question': "19.Which type of cell division produces four non-identical cells?",
        'options': ['A) Mitosis', 'B) Meiosis', 'C) Binary Fission', 'D) Cytokinesis'],
        'answer': 'B'
    },
    {
        'question': "20.What is the primary role of mitochondria?",
        'options': ['A) Photosynthesis', 'B) Energy Production', 'C) Protein Synthesis', 'D) Cell Division'],
        'answer': 'B'
    },
    {
        'question': "21.What process is used by plants to make food?",
        'options': ['A) Cellular Respiration', 'B) Photosynthesis', 'C) Digestion', 'D) Fermentation'],
        'answer': 'B'
    },
    {
        'question': "22.Which structure controls the movement of substances in and out of the cell?",
        'options': ['A) Cell Wall', 'B) Cell Membrane', 'C) Cytoplasm', 'D) Nucleus'],
        'answer': 'B'
    },
    {
        'question': "23.What type of macromolecule are enzymes?",
        'options': ['A) Lipids', 'B) Carbohydrates', 'C) Proteins', 'D) Nucleic Acids'],
        'answer': 'C'
    },
    {
        'question': "24.Which organelle is involved in the production of ATP?",
        'options': ['A) Ribosome', 'B) Mitochondria', 'C) Nucleus', 'D) Endoplasmic Reticulum'],
        'answer': 'B'
    },
    {
        'question': "25.What is the role of vacuoles in plant cells?",
        'options': ['A) Photosynthesis', 'B) Storage of Nutrients and Waste', 'C) Protein Synthesis', 'D) Cell Division'],
        'answer': 'B'
    },
    {
        'question': "26.What is the primary function of the cell membrane?",
        'options': ['A) Genetic Material Storage', 'B) Control of Cellular Activities', 'C) Protection and Regulation of Substance Movement', 'D) Energy Production'],
        'answer': 'C'
    },
    {
        'question': "27.Which phase of the cell cycle involves DNA replication?",
        'options': ['A) Prophase', 'B) Metaphase', 'C) Interphase', 'D) Telophase'],
        'answer': 'C'
    },
    {
        'question': "28.What type of bond is formed between amino acids in proteins?",
        'options': ['A) Hydrogen Bond', 'B) Ionic Bond', 'C) Peptide Bond', 'D) Covalent Bond'],
        'answer': 'C'
    },
    {
        'question': "29.What is the role of the endoplasmic reticulum?",
        'options': ['A) Energy Production', 'B) Storage of Genetic Material', 'C) Synthesis and Transport of Lipids and Proteins', 'D) Cell Wall Formation'],
        'answer': 'C'
    },
    {
        'question': "30.Which structure in plant cells contains chlorophyll?",
        'options': ['A) Mitochondria', 'B) Nucleus', 'C) Chloroplast', 'D) Ribosome'],
        'answer': 'C'
    },
    {
        'question': "31.What is the main component of the cell wall in plants?",
        'options': ['A) Cellulose', 'B) Lignin', 'C) Chitin', 'D) Peptidoglycan'],
        'answer': 'A'
    },
    {
        'question': "32.Which organ in the human body is responsible for digestion?",
        'options': ['A) Heart', 'B) Lungs', 'C) Stomach', 'D) Liver'],
        'answer': 'C'
    },
    {
        'question': "33.What is the term for the genetic material found in the nucleus?",
        'options': ['A) RNA', 'B) Chromatin', 'C) Protein', 'D) Lipid'],
        'answer': 'B'
    },
    {
        'question': "34.Which part of the cell is known as the 'suicide bag'?",
        'options': ['A) Lysosome', 'B) Mitochondria', 'C) Golgi Apparatus', 'D) Peroxisome'],
        'answer': 'A'
    },
    {
        'question': "35.What is the function of the nucleolus?",
        'options': ['A) DNA Replication', 'B) RNA Synthesis', 'C) Protein Synthesis', 'D) Lipid Metabolism'],
        'answer': 'B'
    },
    {
        'question': "36.What structure is responsible for the movement of substances within a cell?",
        'options': ['A) Cytoskeleton', 'B) Cell Membrane', 'C) Mitochondria', 'D) Nucleus'],
        'answer': 'A'
    },
    {
        'question': "37.Which type of RNA carries amino acids to the ribosome?",
        'options': ['A) mRNA', 'B) tRNA', 'C) rRNA', 'D) siRNA'],
        'answer': 'B'
    },
    {
        'question': "38.What is the term for the process of cell division in somatic cells?",
        'options': ['A) Meiosis', 'B) Mitosis', 'C) Binary Fission', 'D) Cytokinesis'],
        'answer': 'B'
    },
    {
        'question': "39.Which organelle is known as the 'suicide bag' of the cell?",
        'options': ['A) Lysosome', 'B) Mitochondria', 'C) Peroxisome', 'D) Ribosome'],
        'answer': 'A'
    },
    {
        'question': "40.What is the primary component of the cell wall in bacteria?",
        'options': ['A) Cellulose', 'B) Lignin', 'C) Chitin', 'D) Peptidoglycan'],
        'answer': 'D'
    },
    {
        'question': "41.Which organelle is involved in modifying and packaging proteins?",
        'options': ['A) Endoplasmic Reticulum', 'B) Golgi Apparatus', 'C) Lysosome', 'D) Mitochondria'],
        'answer': 'B'
    },
    {
        'question': "42.What type of bond holds the base pairs in DNA together?",
        'options': ['A) Covalent Bond', 'B) Hydrogen Bond', 'C) Ionic Bond', 'D) Metallic Bond'],
        'answer': 'B'
    },
    {
        'question': "43.What is the process by which cells convert glucose and oxygen into ATP?",
        'options': ['A) Photosynthesis', 'B) Cellular Respiration', 'C) Fermentation', 'D) Transcription'],
        'answer': 'B'
    },
    {
        'question': "44.Which organelle is known as the 'post office' of the cell?",
        'options': ['A) Ribosome', 'B) Nucleus', 'C) Golgi Apparatus', 'D) Endoplasmic Reticulum'],
        'answer': 'C'
    },
    {
        'question': "45.What is the function of the cytoskeleton?",
        'options': ['A) Genetic Material Storage', 'B) Cellular Movement and Structure', 'C) Energy Production', 'D) Protein Synthesis'],
        'answer': 'B'
    },
    {
        'question': "46.What structure in the cell is responsible for sorting and packaging proteins?",
        'options': ['A) Endoplasmic Reticulum', 'B) Golgi Apparatus', 'C) Lysosome', 'D) Mitochondria'],
        'answer': 'B'
    },
    {
        'question': "47.What is the role of lysosomes in the cell?",
        'options': ['A) Energy Production', 'B) Digestion of Waste Materials', 'C) Protein Synthesis', 'D) Photosynthesis'],
        'answer': 'B'
    },
    {
        'question': "48.Which process in the cell requires oxygen to produce ATP?",
        'options': ['A) Anaerobic Respiration', 'B) Photosynthesis', 'C) Cellular Respiration', 'D) Glycolysis'],
        'answer': 'C'
    },
    {
        'question': "49.What type of cell division results in two identical daughter cells?",
        'options': ['A) Mitosis', 'B) Meiosis', 'C) Binary Fission', 'D) Cytokinesis'],
        'answer': 'A'
    },
    {
        'question': "50.Which structure is responsible for the synthesis of lipids in a cell?",
        'options': ['A) Ribosome', 'B) Golgi Apparatus', 'C) Smooth Endoplasmic Reticulum', 'D) Mitochondria'],
        'answer': 'C'
    }
]
    for trials in biology:
        print(trials["question"])
        for opt in trials["options"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        while answer not in answer_done:
            print("wrong input:Enter appropriate answer")
            answer = input("ENTER HERE:").upper()
            if answer in answer_done:
                break
        
        if answer == trials["answer"]:
            global score
            score += 1
        else:
            score += 0
def physic_questions():
    physics = [
    
        {
            'question': "1.What is the SI unit of force?",
            'options': ['A) Newton', 'B) Joule', 'C) Watt', 'D) Pascal'],
            'answer': 'A'
        },
        {
            'question': "2.What is the speed of light in a vacuum?",
            'options': ['A) 3 x 10^8 m/s', 'B) 3 x 10^6 m/s', 'C) 3 x 10^4 m/s', 'D) 3 x 10^2 m/s'],
            'answer': 'A'
        },
        {
            'question': "3.Who is known as the father of classical mechanics?",
            'options': ['A) Isaac Newton', 'B) Albert Einstein', 'C) Galileo Galilei', 'D) James Clerk Maxwell'],
            'answer': 'A'
        },
        {
            'question': "4.What is the law that states that the total energy in a closed system remains constant?",
            'options': ['A) Newton’s First Law', 'B) Law of Conservation of Energy', 'C) Ohm’s Law', 'D) Hooke’s Law'],
            'answer': 'B'
        },
        {
            'question': "5.What is the formula for calculating kinetic energy?",
            'options': ['A) KE = 1/2 mv^2', 'B) KE = mgh', 'C) KE = 1/2 mv', 'D) KE = mv'],
            'answer': 'A'
        },
        {
            'question': "6.In which type of wave does the particle displacement occur parallel to the direction of wave propagation?",
            'options': ['A) Longitudinal Wave', 'B) Transverse Wave', 'C) Electromagnetic Wave', 'D) Mechanical Wave'],
            'answer': 'A'
        },
        {
            'question': "7.What is the SI unit of electric charge?",
            'options': ['A) Ampere', 'B) Volt', 'C) Coulomb', 'D) Ohm'],
            'answer': 'C'
        },
        {
            'question': "8.What does Ohm’s Law state?",
            'options': ['A) V = IR', 'B) P = IV', 'C) E = mc^2', 'D) F = ma'],
            'answer': 'A'
        },
        {
            'question': "9.What is the phenomenon where light bends as it passes from one medium to another?",
            'options': ['A) Reflection', 'B) Refraction', 'C) Diffraction', 'D) Dispersion'],
            'answer': 'B'
        },
        {
            'question': "10.Which law states that for every action there is an equal and opposite reaction?",
            'options': ['A) Newton’s First Law', 'B) Newton’s Second Law', 'C) Newton’s Third Law', 'D) Law of Universal Gravitation'],
            'answer': 'C'
        },
        {
            'question': "11.What is the unit of power in the International System of Units?",
            'options': ['A) Watt', 'B) Joule', 'C) Newton', 'D) Volt'],
            'answer': 'A'
        },
        {
            'question': "12.What is the force that opposes the motion of an object through a fluid?",
            'options': ['A) Gravity', 'B) Friction', 'C) Drag', 'D) Tension'],
            'answer': 'C'
        },
        {
            'question': "13.What is the formula to calculate the gravitational force between two masses?",
            'options': ['A) F = G(m1m2)/r^2', 'B) F = ma', 'C) F = mg', 'D) F = qE'],
            'answer': 'A'
        },
        {
            'question': "14.What type of energy is stored in a stretched or compressed spring?",
            'options': ['A) Kinetic Energy', 'B) Potential Energy', 'C) Thermal Energy', 'D) Chemical Energy'],
            'answer': 'B'
        },
        {
            'question': "15.What is the term for the rate of change of velocity?",
            'options': ['A) Speed', 'B) Acceleration', 'C) Force', 'D) Momentum'],
            'answer': 'B'
        },
        {
            'question': "16.What is the term for the total amount of energy an object has due to its motion and position?",
            'options': ['A) Kinetic Energy', 'B) Potential Energy', 'C) Mechanical Energy', 'D) Thermal Energy'],
            'answer': 'C'
        },
        {
            'question': "17.Which law of thermodynamics states that energy cannot be created or destroyed, only transformed?",
            'options': ['A) Zeroth Law', 'B) First Law', 'C) Second Law', 'D) Third Law'],
            'answer': 'B'
        },
        {
            'question': "18.What is the SI unit of frequency?",
            'options': ['A) Hertz', 'B) Watt', 'C) Joule', 'D) Newton'],
            'answer': 'A'
        },
        {
            'question': "19.What is the energy called that is associated with an object due to its motion?",
            'options': ['A) Potential Energy', 'B) Kinetic Energy', 'C) Thermal Energy', 'D) Electrical Energy'],
            'answer': 'B'
        },
        {
            'question': "20.What is the speed of sound in air at room temperature (20°C)?",
            'options': ['A) 343 m/s', 'B) 300 m/s', 'C) 1500 m/s', 'D) 600 m/s'],
            'answer': 'A'
        },
        {
            'question': "21.What is the principle behind a lever?",
            'options': ['A) Conservation of Momentum', 'B) Conservation of Energy', 'C) Mechanical Advantage', 'D) Work-Energy Principle'],
            'answer': 'C'
        },
        {
            'question': "22.What is the term for the amount of energy required to raise the temperature of 1 kilogram of a substance by 1 degree Celsius?",
            'options': ['A) Specific Heat Capacity', 'B) Latent Heat', 'C) Thermal Conductivity', 'D) Power'],
            'answer': 'A'
        },
        {
            'question': "23.What type of wave requires a medium to propagate?",
            'options': ['A) Electromagnetic Wave', 'B) Longitudinal Wave', 'C) Transverse Wave', 'D) Mechanical Wave'],
            'answer': 'D'
        },
        {
            'question': "24.Which quantity is conserved in an isolated system during a collision?",
            'options': ['A) Energy', 'B) Momentum', 'C) Mass', 'D) Force'],
            'answer': 'B'
        },
        {
            'question': "25.What is the effect of increasing the temperature on the resistance of a metal conductor?",
            'options': ['A) Resistance Increases', 'B) Resistance Decreases', 'C) Resistance Remains the Same', 'D) Resistance Fluctuates'],
            'answer': 'A'
        },
        {
            'question': "26.What is the formula for calculating work done?",
            'options': ['A) W = Fd', 'B) W = mgh', 'C) W = 1/2 mv^2', 'D) W = Pt'],
            'answer': 'A'
        },
        {
            'question': "27.Which principle explains the buoyant force on an object submerged in a fluid?",
            'options': ['A) Bernoulli’s Principle', 'B) Archimedes’ Principle', 'C) Pascal’s Principle', 'D) Newton’s Law'],
            'answer': 'B'
        },
        {
            'question': "28.What is the SI unit of pressure?",
            'options': ['A) Pascal', 'B) Newton', 'C) Joule', 'D) Watt'],
            'answer': 'A'
        },
        {
            'question': "29.What is the quantity of heat required to change the state of a substance without changing its temperature?",
            'options': ['A) Specific Heat Capacity', 'B) Latent Heat', 'C) Thermal Energy', 'D) Kinetic Energy'],
            'answer': 'B'
        },
        {
            'question': "30.What is the measure of the average kinetic energy of particles in a substance?",
            'options': ['A) Temperature', 'B) Heat', 'C) Energy', 'D) Pressure'],
            'answer': 'A'
        },
        {
            'question': "31.What is the term for the transfer of thermal energy through direct contact?",
            'options': ['A) Conduction', 'B) Convection', 'C) Radiation', 'D) Diffusion'],
            'answer': 'A'
        },
        {
            'question': "32.What is the SI unit of electric current?",
            'options': ['A) Ampere', 'B) Coulomb', 'C) Volt', 'D) Ohm'],
            'answer': 'A'
        },
        {
            'question': "33.Which fundamental force is responsible for holding atomic nuclei together?",
            'options': ['A) Gravitational Force', 'B) Electromagnetic Force', 'C) Weak Nuclear Force', 'D) Strong Nuclear Force'],
            'answer': 'D'
        },
        {
            'question': "34.What is the term for the phenomenon where a wave changes direction when it encounters an obstacle or opening?",
            'options': ['A) Reflection', 'B) Refraction', 'C) Diffraction', 'D) Interference'],
            'answer': 'C'
        },
        {
            'question': "35.What is the formula for calculating the period of a pendulum?",
            'options': ['A) T = 2π√(L/g)', 'B) T = 1/f', 'C) T = 2πf', 'D) T = L/g'],
            'answer': 'A'
        },
        {
            'question': "36.What is the term for the resistance of an object to changes in its state of motion?",
            'options': ['A) Mass', 'B) Weight', 'C) Inertia', 'D) Momentum'],
            'answer': 'C'
        },
        {
            'question': "37.What is the formula for calculating gravitational potential energy?",
            'options': ['A) PE = mgh', 'B) PE = 1/2 mv^2', 'C) PE = Fd', 'D) PE = qV'],
            'answer': 'A'
        },
        {
            'question': "38.What is the unit of work in the International System of Units?",
            'options': ['A) Joule', 'B) Watt', 'C) Newton', 'D) Coulomb'],
            'answer': 'A'
        },
        {
            'question': "39.What is the term for the change in velocity over time?",
            'options': ['A) Speed', 'B) Acceleration', 'C) Force', 'D) Momentum'],
            'answer': 'B'
        },
        {
            'question': "40.What is the name of the effect that describes the bending of light as it passes through different media?",
            'options': ['A) Reflection', 'B) Refraction', 'C) Diffraction', 'D) Dispersion'],
            'answer': 'B'
        },
        {
            'question': "41.Which law states that the current through a conductor between two points is directly proportional to the voltage across the two points?",
            'options': ['A) Ohm’s Law', 'B) Joule’s Law', 'C) Faraday’s Law', 'D) Kirchhoff’s Law'],
            'answer': 'A'
        },
        {
            'question': "42.What is the SI unit of energy?",
            'options': ['A) Joule', 'B) Watt', 'C) Newton', 'D) Volt'],
            'answer': 'A'
        },
        {
            'question': "43.What is the term for the work done per unit charge in moving a charge between two points in an electric field?",
            'options': ['A) Current', 'B) Voltage', 'C) Resistance', 'D) Power'],
            'answer': 'B'
        },
        {
            'question': "44.What is the force per unit length on a current-carrying conductor in a magnetic field called?",
            'options': ['A) Magnetic Force', 'B) Lorentz Force', 'C) Electrostatic Force', 'D) Gravitational Force'],
            'answer': 'B'
        },
        {
            'question': "45.What is the rate of doing work or transferring energy?",
            'options': ['A) Energy', 'B) Work', 'C) Power', 'D) Force'],
            'answer': 'C'
        },
        {
            'question': "46.What is the term for the time taken for one complete cycle of a periodic process?",
            'options': ['A) Frequency', 'B) Period', 'C) Amplitude', 'D) Wavelength'],
            'answer': 'B'
        },
        {
            'question': "47.What is the name of the point where the total upward force on a floating object equals the weight of the object?",
            'options': ['A) Buoyancy', 'B) Equilibrium', 'C) Center of Mass', 'D) Stable Point'],
            'answer': 'B'
        },
        {
            'question': "48.What is the unit of electrical resistance?",
            'options': ['A) Ampere', 'B) Volt', 'C) Ohm', 'D) Joule'],
            'answer': 'C'
        },
        {
            'question': "49.What is the SI unit of pressure?",
            'options': ['A) Newton', 'B) Pascal', 'C) Joule', 'D) Watt'],
            'answer': 'B'
        },
        {
            'question': "50.What is the term for the process by which a liquid changes into a gas?",
            'options': ['A) Evaporation', 'B) Condensation', 'C) Sublimation', 'D) Freezing'],
            'answer': 'A'
        }
]
    for trials in physics:
        print(trials["question"])
        for opt in trials["options"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        while answer not in answer_done:
            print("wrong input:Enter appropriate answer")
            answer = input("ENTER HERE:").upper()
            if answer in answer_done:
                break
        
        if answer == trials["answer"]:
            global score
            score += 1
        else:
            score += 0
def English_questions():

    questions =[
        {'question': "1.What is the synonym of 'happy'?",
            'options': ['A) Sad', 'B) Joyful', 'C) Angry', 'D) Tired'],
            'answer': 'B'},
        {'question': "2.Which of the following is a noun?",
            'options': ['A) Run', 'B) Quickly', 'C) Book', 'D) Beautiful'],
            'answer': 'C'},
        {'question': "3.What is the antonym of 'brave'?",
            'options': ['A) Cowardly', 'B) Bold', 'C) Courageous', 'D) Heroic'],
            'answer': 'A'},
        {'question': "4.Choose the correct past tense form: 'She ____ a book.'",
            'options': ['A) Readed', 'B) Reads', 'C) Read', 'D) Reading'],
            'answer': 'C'},
        {'question': "5.Which sentence is grammatically correct?",
            'options': ['A) He go to school.', 'B) He going to school.', 'C) He goes to school.', 'D) He gone to school.'],
            'answer': 'C'},
        {'question': "6.What is the synonym of 'benevolent'?",
            'options': ['A) Malevolent', 'B) Kind', 'C) Hostile', 'D) Harsh'],
            'answer': 'B'},
        {'question': "7.Which word means 'a place where books are kept'?",
            'options': ['A) Library', 'B) Laboratory', 'C) Museum', 'D) Gym'],
            'answer': 'A'},
        {'question': "8.Which of the following is an adjective?",
            'options': ['A) Quickly', 'B) Happiness', 'C) Tall', 'D) Run'],
            'answer': 'C'},
        {'question': "9.Choose the correct plural form: 'Child'...",
            'options': ['A) Childs', 'B) Children', 'C) Childes', 'D) Childrens'],
            'answer': 'B'},
        {'question': "10.What is the antonym of 'ascend'?",
            'options': ['A) Climb', 'B) Rise', 'C) Descend', 'D) Elevate'],
            'answer': 'C'},
        {'question': "11.Complete the sentence: 'He _____ to the store yesterday.'",
            'options': ['A) Go', 'B) Went', 'C) Going', 'D) Goes'],
            'answer': 'B'},
        {'question': "12.Which of the following sentences is a question?",
            'options': ['A) She went to the market.', 'B) Do you like apples?', 'C) He is a teacher.', 'D) It is raining.'],
            'answer': 'B'},
        {'question': "13.What is the synonym of 'difficult'?",
            'options': ['A) Easy', 'B) Hard', 'C) Simple', 'D) Smooth'],
            'answer': 'B'},
        {'question': "14.Which sentence is in the passive voice?",
            'options': ['A) The dog bit the man.', 'B) The man bites the dog.', 'C) The man is bitten by the dog.', 'D) The dog is biting the man.'],
            'answer': 'C'},
        {'question': "15.Choose the correct sentence:",
            'options': ['A) She don’t like oranges.', 'B) She doesn’t like oranges.', 'C) She not likes oranges.', 'D) She doesn’t likes oranges.'],
            'answer': 'B'},
        {'question': "16.What is the antonym of 'generous'?",
            'options': ['A) Selfish', 'B) Giving', 'C) Kind', 'D) Charitable'],
            'answer': 'A'},
        {'question': "17.Complete the idiom: 'Break the ____.'",
            'options': ['A) Glass', 'B) Ice', 'C) News', 'D) Silence'],
            'answer': 'D'},
        {'question': "18.Which word is a verb?",
            'options': ['A) Happiness', 'B) Sing', 'C) Book', 'D) Beautiful'],
            'answer': 'B'},
        {'question': "19.What is the synonym of 'arduous'?",
            'options': ['A) Easy', 'B) Difficult', 'C) Smooth', 'D) Simple'],
            'answer': 'B'},
        {'question': "20.Which sentence uses 'there' correctly?",
            'options': ['A) Their going to the park.', 'B) There going to the park.', 'C) They’re going to the park.', 'D) There are going to the park.'],
            'answer': 'D'},
        {'question': "21.What is the plural of 'mouse'?",
            'options': ['A) Mouses', 'B) Mice', 'C) Mouse', 'D) Mices'],
            'answer': 'B'},
        {'question': "22.Choose the correct form of the verb: 'She ____ to the gym every day.'",
            'options': ['A) Go', 'B) Goes', 'C) Going', 'D) Gone'],
            'answer': 'B'},
        {'question': "23.What is the antonym of 'happy'?",
            'options': ['A) Joyful', 'B) Elated', 'C) Sad', 'D) Ecstatic'],
            'answer': 'C'},
        {'question': "24.Which of the following is an adverb?",
            'options': ['A) Quickly', 'B) Cat', 'C) Loud', 'D) Happiness'],
            'answer': 'A'},
        {'question': "25.Complete the sentence: 'She ____ her homework.'",
            'options': ['A) Does', 'B) Do', 'C) Doing', 'D) Did'],
            'answer': 'A'},
        {'question': "26.What is the synonym of 'ancient'?",
            'options': ['A) Modern', 'B) Old', 'C) New', 'D) Young'],
            'answer': 'B'},
        {'question': "27.Which sentence is in the past continuous tense?",
            'options': ['A) She was reading a book.', 'B) She reads a book.', 'C) She is reading a book.', 'D) She will read a book.'],
            'answer': 'A'},
        {'question': "28.What is the antonym of 'hard'?",
            'options': ['A) Tough', 'B) Soft', 'C) Difficult', 'D) Solid'],
            'answer': 'B'},
        {'question': "29.Complete the idiom: 'Let the cat out of the ____.'",
            'options': ['A) Bag', 'B) House', 'C) Box', 'D) Room'],
            'answer': 'A'},
        {'question': "30.Which word is a preposition?",
            'options': ['A) Quickly', 'B) On', 'C) Happy', 'D) Sing'],
            'answer': 'B'},
        {'question': "31.What is the synonym of 'negligent'?",
            'options': ['A) Careful', 'B) Attentive', 'C) Lazy', 'D) Diligent'],
            'answer': 'C'},
        {'question': "32.Which of the following sentences is correct?",
            'options': ['A) She have a car.', 'B) She has a car.', 'C) She had a car.', 'D) She having a car.'],
            'answer': 'B'},
        {'question': "33.What is the antonym of 'dull'?",
            'options': ['A) Bright', 'B) Boring', 'C) Plain', 'D) Boring'],
            'answer': 'A'},
        {'question': "34.Complete the sentence: 'They ____ going to the concert.'",
            'options': ['A) Is', 'B) Are', 'C) Were', 'D) Was'],
            'answer': 'B'},
        {'question': "35.Which word is a conjunction?",
            'options': ['A) And', 'B) Quickly', 'C) Blue', 'D) Happiness'],
            'answer': 'A'},
        {'question': "36.What is the synonym of 'abundant'?",
            'options': ['A) Scarce', 'B) Plenty', 'C) Rare', 'D) Limited'],
            'answer': 'B'},
        {'question': "37.Which sentence is in the present perfect tense?",
            'options': ['A) She eats breakfast.', 'B) She ate breakfast.', 'C) She has eaten breakfast.', 'D) She will eat breakfast.'],
            'answer': 'C'},
        {'question': "38.What is the antonym of 'late'?",
            'options': ['A) Early', 'B) Tardy', 'C) Delayed', 'D) Behind'],
            'answer': 'A'},
        {'question': "39.Complete the idiom: 'Hit the nail on the ____.'",
            'options': ['A) Head', 'B) Finger', 'C) Hand', 'D) Toe'],
            'answer': 'A'},
        {'question': "40.Which word is a noun?",
            'options': ['A) Walk', 'B) Happiness', 'C) Run', 'D) Quietly'],
            'answer': 'B'},
        {'question': "41.What is the synonym of 'genuine'?",
            'options': ['A) Fake', 'B) Authentic', 'C) False', 'D) Bogus'],
            'answer': 'B'},
        {'question': "42.Which of the following sentences uses 'your' correctly?",
            'options': ['A) Your going to the store.', 'B) You’re going to the store.', 'C) Your going to store.', 'D) You’re going store.'],
            'answer': 'B'},
        {'question': "43.What is the antonym of 'strict'?",
            'options': ['A) Flexible', 'B) Severe', 'C) Rigid', 'D) Stern'],
            'answer': 'A'},
        {'question': "44.Complete the sentence: 'She ____ a book on the table.'",
            'options': ['A) Put', 'B) Puts', 'C) Putting', 'D) Putted'],
            'answer': 'B'},
        {'question': "45.Which of the following is a preposition?",
            'options': ['A) Run', 'B) Happy', 'C) Under', 'D) Quickly'],
            'answer': 'C'},
        {'question': "46.What is the synonym of 'elevate'?",
            'options': ['A) Lower', 'B) Raise', 'C) Drop', 'D) Decrease'],
            'answer': 'B'},
        {'question': "47.Which sentence is in the future tense?",
            'options': ['A) She will go to the party.', 'B) She went to the party.', 'C) She is going to the party.', 'D) She goes to the party.'],
            'answer': 'A'},
        {'question': "48.What is the antonym of 'joyful'?",
            'options': ['A) Cheerful', 'B) Sad', 'C) Elated', 'D) Happy'],
            'answer': 'B'},
        {'question': "49.Complete the idiom: 'Bite the ____.'",
            'options': ['A) Dust', 'B) Nail', 'C) Lip', 'D) Tongue'],
            'answer': 'A'},
        {'question': "50.Which word is an adverb?",
            'options': ['A) Table', 'B) Loudly', 'C) Smile', 'D) Chair'],
            'answer': 'B'}
    ]

    for trials in questions:
        print(trials["question"])
        for opt in trials["options"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        while answer not in answer_done:
            print("wrong input:Enter appropriate answer")
            answer = input("ENTER HERE:").upper()
            if answer in answer_done:
                break
        if answer == trials["answer"]:
            global score
            score += 1
        else:
            score += 0
def name_of_examinee():
    print(" ")
    print("HELLLO")
    print("WHAT IS YOUR NAME")
    name = input("FIRST NAME:").upper()
    dec = input("LAST NAME:").upper()
    print("OKAY " + name +" " + dec)
def intro_duc_tion():
    print("WELCOME TO ELEGANCE 2024 CBT EXAMINATION")
    print("""INSTRUCTION:1.DO NOT START UNTIL YOU TOLD TO DO SO
            2.DO NOT CHOOSE TWO OR MORE ANSWER IN ONE QUESTION
            3.DO NOT ENGAGED IN MALPRACTICE AS THIS AS SEVERE CONSEQUENCES 
            4.Answer should only be A,B,C or D""")
    print("THIS EXAMINATION CONTAINS  4 SUBJECTS AND 500 QUESTION ")
    print("THERE IS A TOTAL OF 4 SUBJECTS AND 200 QUESTIONS WITH EACH SUBJECT HAVING 50 QUESTIONS EACH")
    print("THE SUBJECTS BELOW ARE THE ONLY AVAILABLE SUBJECTS FOR THIS EXAMIXATION")
    print("""SUBJECTS:1.English
         2.Biology
         3.PHYSICS
         4.CHEMISTRY""")
    
name_of_examinee()
intro_duc_tion()

print("ENTER 'START' TO BEGIN OR 'EXIT' TO QUIT")
reply = input("ENTER HERE:").lower()
if reply == "start":
    print("what subject would you like to start with")
    first = input("ENTER HERE:").lower()
    if first == "physics":
        print("     ELEGANCE 2024 CBT EXAMINATION PHYSICS QUESTIONS")
        physic_questions()
        print("This is the end of your physics question")
    elif first == "biology":
        print("     ELEGANCE 2024 CBT EXAMINATION BIOLOGY QUESTIONS")
        Biology_question()
        print("This is the end of your biology question")
    elif first == "chemistry":
        print("     ELEGANCE 2024 CBT EXAMINATION CHEMISTRY QUESTIONS")
        chemistry_questions()
        print("This is the end of your chemistry question")
    elif first == "english":
        print("     ELEGANCE 2024 CBT EXAMINATION ENGLISH QUESTIONS")
        English_questions()
        print("This is the end of your english question")
    subject_done.append(first)
    
else:
    print("ARE YOU SURE YOU WANT TO EXIT")
    dummy = input("ENTER HERE:")
    if dummy == 'yes':
        exit()
    else:
        print("ill take that as a yes to start you examination")




print("what subject would you like to do next")
second = input("ENTER HERE:").lower()
while second in subject_done:
    print("you have done this subject")
    second = input("ENTER HERE:").lower()
    if second not in subject_done:
        break
if second == "physics":
    print("     ELEGANCE 2024 CBT EXAMINATION PHYSICS QUESTIONS")
    physic_questions()
    print("This is the end of your physics question")
elif second == "chemistry":
    print("     ELEGANCE 2024 CBT EXAMINATION CHEMISTRY QUESTIONS")
    chemistry_questions()
    print("This is the end of your chemistry question")
elif second == "biology":
    print("     ELEGANCE 2024 CBT EXAMINATION BIOLOGY QUESTIONS")
    Biology_question()
    print("This is the end of your biology question")
elif second == "english":
    print("     ELEGANCE 2024 CBT EXAMINATION ENGLISH QUESTIONS")
    English_questions()
    print("This is the end of your english question")
subject_done.append(second)


print("what is you third subject")
third = input("ENTER HERE:").lower()
while third in subject_done:
    print("you have done this subject")
    third = input("ENTER HERE:").lower()
    if third not in subject_done:
        break
if third == "physics":
    print("     ELEGANCE 2024 CBT EXAMINATION PHYSICS QUESTIONS")
    physic_questions()
    print("This is the end of your physics question")
elif third == "chemistry":
    print("     ELEGANCE 2024 CBT EXAMINATION CHEMISTRY QUESTIONS")
    chemistry_questions()
    print("This is the end of your chemistry question")
elif third == "biology":
    print("     ELEGANCE 2024 CBT EXAMINATION BIOLOGY QUESTIONS")
    Biology_question()
    print("This is the end of your biology question")
elif third == "english":
    print("     ELEGANCE 2024 CBT EXAMINATION ENGLISH QUESTIONS")
    English_questions()
    print("This is the end of your english question")
subject_done.append(third)

print("what is fourth and last subject")
fourth = input("ENTER HERE:").lower()
while fourth in subject_done:
    print("you have done this subject")
    fourth = input("ENTER HERE:").lower()
    if fourth not in subject_done:
        break
if fourth == "physics":
    print("     ELEGANCE 2024 CBT EXAMINATION PHYSICS QUESTIONS")
    physic_questions()
    print("This is the end of your physics question")
elif fourth == "chemistry":
    print("     ELEGANCE 2024 CBT EXAMINATION CHEMISTRY QUESTIONS")
    chemistry_questions()
    print("This is the end of your chemistry question")
elif fourth == "biology":
    print("     ELEGANCE 2024 CBT EXAMINATION BIOLOGY QUESTIONS")
    Biology_question()
    print("This is the end of your biology question")
elif fourth == "english":
    print("     ELEGANCE 2024 CBT EXAMINATION ENGLISH QUESTIONS")
    English_questions()
    print("This is the end of your english question")

print("THIS IS THE END OF THE EXAM, THANK YOU")
print("Your final score = " + str(score))