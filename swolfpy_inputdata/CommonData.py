# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:05:32 2019

@author: msardar2
"""
from .InputData import InputData
from pathlib import Path
import pandas as pd


class CommonData(InputData):
    # Recycling products index
    Reprocessing_Index = ['Al', 'Fe',
                          'OCC', 'Mixed_Paper', 'ONP', 'OFF', 'Fiber_Other',
                          'Brown_glass', 'Clear_glass', 'Green_glass', 'Mixed_Glass',
                          'PET', 'HDPE_P', 'HDPE_T', 'LDPE_Film']

    # Collection products index
    Collection_Index = ['RWC', 'SSR', 'DSR', 'MSR', 'LV', 'SSYW', 'SSO', 'SSO_AnF',
                        'SSO_HC', 'ORG', 'DryRes', 'REC', 'WetRes',
                        'MRDO', 'SSYWDO', 'MSRDO']

    # Waste products index
    Waste_Pr_Index = ['Bottom_Ash', 'Fly_Ash', 'Unreacted_Ash', 'Separated_Organics',
                      'Other_Residual', 'Separated_Recyclables', 'RDF']

    # all waste_pr_index
    All_Waste_Pr_Index = (Waste_Pr_Index
                          + Collection_Index
                          + Reprocessing_Index)

    # Materials
    Index = ['Yard_Trimmings_Leaves', 'Yard_Trimmings_Grass', 'Yard_Trimmings_Branches', 'Food_Waste_Vegetable',
             'Food_Waste_Non_Vegetable', 'Wood', 'Wood_Other', 'Textiles', 'Rubber_Leather', 'Newsprint',
             'Corr_Cardboard', 'Office_Paper', 'Magazines', 'Third_Class_Mail', 'Folding_Containers', 'Paper_Bags',
             'Mixed_Paper', 'Paper_Non_recyclable', 'HDPE_Translucent_Containers', 'HDPE_Pigmented_Containers',
             'PET_Containers', 'Plastic_Other_1_Polypropylene', 'Plastic_Other_2', 'Mixed_Plastic', 'Plastic_Film',
             'Plastic_Non_Recyclable', 'Ferrous_Cans', 'Ferrous_Metal_Other', 'Aluminum_Cans', 'Aluminum_Foil',
             'Aluminum_Other', 'Ferrous_Non_recyclable', 'Al_Non_recyclable', 'Glass_Brown', 'Glass_Green',
             'Glass_Clear', 'Mixed_Glass', 'Glass_Non_recyclable', 'Misc_Organic', 'Misc_Inorganic', 'E_waste',
             'Bottom_Ash', 'Fly_Ash', 'Diapers_and_sanitary_products']

    def __init__(self, input_data_path=None, process_name='CommonData'):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / 'Data/CommonData.csv'

        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        ### Read Material properties
        self.Material_Properties = pd.read_csv(Path(__file__).parent / "Data/Material properties.csv",
                                               index_col=0,
                                               header=0,
                                               skiprows=[1, 2, 3]).loc[self.Index].astype(float)
        self.Material_Properties.fillna(0, inplace=True)
        self.Material_Properties_Info = pd.read_csv(Path(__file__).parent / "Data/Material properties.csv",
                                                    index_col=0,
                                                    header=0,
                                                    nrows=3)
