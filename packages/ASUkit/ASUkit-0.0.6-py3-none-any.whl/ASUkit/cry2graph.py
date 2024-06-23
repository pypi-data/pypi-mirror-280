from ase.io import read
import numpy as np
from ase.db import connect
from ase.spacegroup import get_spacegroup, Spacegroup
from ase import Atoms
from ._utility._funs import *
import os
import random
import pkg_resources
import pandas as pd
import json
import copy
import warnings


class parser():
    def __init__(self,database,entry_id):
        """
        This function processes a given database file and data ID to extract and return various graph-related data structures.

        Parameters:
            db_file (str): Path to the database file (e.g., 'cif.db').
            data_id (int): The ID of the data entry to be processed.
            !!! the structures saved in the database file are by default in the conventional lattice cell format. 

        Returns:
            tuple: A tuple containing the following elements:
                - node_embedding (np.ndarray): The node embeddings, 106-d.
                - masked_adj_matrix (np.ndarray): The masked adjacency matrix.
                - distance_matrix (np.ndarray): The distance matrix in Cartesian coordinates.
                - global_graph_info (np.ndarray): Global information about the graph, 140-d.
                (when model = 'Simulation', the global information is the powder diffraction pattern)

        Example:
            from ASUkit import cry2graph
            from ase.db import connect

            database = connect('cif.db')
            entry_id = 1

            node_embedding, adj_matrix, dis_matrix, global_info = cry2graph.parser(database, entry_id).get()
        """


        self.entry_id = entry_id
        self.database = database
        warnings.filterwarnings("ignore")
        _loc = pkg_resources.resource_filename('ASUkit', '')
        with open(os.path.join(_loc,'CGCNN_atom_emb.json') , 'r') as file:
            self.cgcnn_emb = json.load(file)

    def get(self,model='ASUnet',):
        """
        Parameters:
        model (str): The model type for generating the diffraction pattern. Either 'ASUnet' or 'Simulation'.

        if model='ASUnet' (default), return the ideal diffraction pattern
        if model='Simulation', return the simulated diffraction pattern with practical factors   
        """
        try:
            atoms = self.database.get_atoms(id=self.entry_id)
            
            # for general db files contains conventional lattice cells
            # G_latt_consts = atoms.cell.cellpar()
            # in case the input is primitive unit cell 
            G_latt_consts,_, c_atom = prim2conv(atoms)  

            N_symbols = c_atom.get_chemical_symbols() 
            G_spacegroup = get_spacegroup(c_atom).no 
            G_latt_vol = c_atom.get_volume() 
            G_ASUnum = c_atom.get_global_number_of_atoms() 
            asu_atom_mass = c_atom.get_masses() 
            G_mass = sum(asu_atom_mass)

            spacegroup_obj = get_spacegroup(c_atom)
            spacegroup_symbol = spacegroup_obj.symbol[0] 
            # sg = Spacegroup(G_spacegroup)
            
            positions = c_atom.get_positions() 
            asu_positions, asu_symbols,sites,kinds = conlattcell2asu(c_atom,positions,N_symbols)
            # sites,kinds = sg.equivalent_sites(asu_positions,symprec=1e-4, onduplicates='warn') 
            # !!! In case the reoperator cannot merge the atoms due to numerical errors, we only operate it once.
            
            element_encode = symbol_to_atomic_number(asu_symbols)
            # 11-d : lattice cell constants (6) ; spacegroup ; total number ;asu number; c lattice volume ;  c lattice total mass
            global_info = [G_latt_consts[0],G_latt_consts[1],G_latt_consts[2],G_latt_consts[3],
                        G_latt_consts[4],G_latt_consts[5],G_spacegroup,G_ASUnum,len(asu_positions),G_latt_vol,G_mass]
            # 95-d, CGCNN embedding + fractional coordinates
            node_emd = []
            for index, code in enumerate(kinds):
                _code = element_encode[code] # covert the node index of asu list to periodic table number
                value = self.cgcnn_emb[str(_code)] # 92-d
                node_emd.append(np.array(value + sites[index].tolist()+ global_info)) # 92+3+11 : 106-d
            crystal_system = space_group_to_crystal_system(G_spacegroup) 
            AtomCoordinates = covert2WPEMformat(sites,kinds,asu_symbols)

            if model == 'ASUnet':
                _,global_graph = xrdsim(G_latt_vol,spacegroup_symbol,AtomCoordinates,G_latt_consts,crystal_system) # 140-d
            elif model == 'Simulation':
                GrainSize = random.uniform(2, 20)
                ori_1 = random.uniform(0, 0.1)
                ori_2 = random.uniform(0, 0.1)
                orientation = [ori_1, ori_2]
                thermo_vib = random.uniform(0, 0.2)
                zero_shift = random.uniform(-0.7, 0.7)
                _,global_graph = pxrdsim(G_latt_vol, spacegroup_symbol, AtomCoordinates, G_latt_consts, crystal_system,
                                 GrainSize, orientation, thermo_vib, zero_shift)
            else: print("error: unknown model " + model)
            
            # self connections, infilled 1 on edge between same asu  and infilled 1/dis on edge between diff ASU
            distance_matrix = c_atom.get_all_distances()
            asu_dis_matrix = copy.deepcopy(distance_matrix)
            np.fill_diagonal(asu_dis_matrix, asu_dis_matrix.diagonal() + 1)
            asu_dis_matrix = 1 / asu_dis_matrix

            adj_matrix =  copy.deepcopy(asu_dis_matrix)
            for i in range(len(kinds)):
                for j in range(len(kinds)):
                    # cal the asu distance matrix 
                    if kinds[i]==kinds[j]:
                        adj_matrix[i,j] = 1
            # cut to 1.1
            adj_matrix = np.array(adj_matrix)
            adj_matrix[adj_matrix > 1.1] = 1.1
            
            #_atoms = Atoms('X' * len(sites), positions=sites)
            #distance_matrix = _atoms.get_all_distances()

        except Exception as e:
            print("An error occurred : crystal id = {}".format(self.entry_id), e)
            return None
        
        return np.array(node_emd),adj_matrix, distance_matrix, global_graph
    

# ----------------------------------------------------------------
def covert2WPEMformat(sites, kinds, N_symbols):
    sites_list = sites.tolist()  
    for i in range(len(sites_list)):
        sites_list[i].insert(0, N_symbols[kinds[i]])
    return sites_list 

def space_group_to_crystal_system(space_group):
    if space_group < 1 or space_group > 230:
        return "Invalid space group number"
    elif space_group <= 2:
        return 7  
    elif space_group <= 15:
        return 6  
    elif space_group <= 74:
        return 4  
    elif space_group <= 142:
        return 3 
    elif space_group <= 167:
        return 5  
    elif space_group <= 194:
        return 2 
    else:
        return 1 
    

def xrdsim(Volume,Point_group,AtomCoordinates,latt,crystal_system,):
    # idear diffraction pattern with finite broadening 
    wavelength = 1.54184
    two_theta_range = (10, 80.0,0.5) 
    grid, d_list = Diffraction_index(crystal_system,latt,wavelength,two_theta_range)
    res_HKL, _, d_res_HKL, _ = cal_extinction(Point_group, grid,d_list,crystal_system,AtomCoordinates,wavelength,)
    mu_array = 2 * np.arcsin(wavelength /2/np.array(d_res_HKL)) * 180 / np.pi

    FHKL_square = []
    Mult = []
    for angle in range(len(res_HKL)):
        FHKL_square_left = 0
        FHKL_square_right = 0
        # _Atom_coordinate all atoms in lattice cell
        for atom in range(len(AtomCoordinates)):
            fi = cal_atoms(AtomCoordinates[atom][0],mu_array[angle], wavelength)
            FHKL_square_left += fi * np.cos(2 * np.pi * (AtomCoordinates[atom][1] * res_HKL[angle][0] +
                                                AtomCoordinates[atom][2] * res_HKL[angle][1] + AtomCoordinates[atom][3] * res_HKL[angle][2]))
            FHKL_square_right += fi * np.sin(2 * np.pi * (AtomCoordinates[atom][1] * res_HKL[angle][0] +
                                                AtomCoordinates[atom][2] * res_HKL[angle][1] + AtomCoordinates[atom][3] * res_HKL[angle][2]))
        Mult.append(mult_rule(res_HKL[angle][0],res_HKL[angle][1],res_HKL[angle][2],crystal_system))
        FHKL_square.append(FHKL_square_left ** 2 + FHKL_square_right ** 2)
        
    
  
    Ints = [] # cal peak intensity
    for angle in range(len(FHKL_square)):
        Ints.append(float(FHKL_square[angle] * Mult[angle] / Volume ** 2
                    * (1 + np.cos(mu_array[angle] * np.pi/180) ** 2) / (np.sin(mu_array[angle] / 2 * np.pi/180) **2 * np.cos(Mult[angle] / 2 * np.pi/180))))
    

    Γ = 0.888*wavelength/(20 * np.cos(np.radians(np.array(mu_array)/2))) # GrainSize = 20nm 
    gamma_list = Γ / 2 + 1e-10
    sigma2_list = Γ**2 / (8*np.sqrt(2)) + 1e-10


    x_sim = np.arange(two_theta_range[0],two_theta_range[1],two_theta_range[2])
    y_sim = 0
    for num in range(len(Ints)):
        _ = draw_peak_density(x_sim, Ints[num], mu_array[num], gamma_list[num], sigma2_list[num])
        y_sim += _
    # normalize the profile
    nor_y = y_sim / theta_intensity_area(x_sim,y_sim)
    
    # x_dis is 1.2 to 8.8
    return None, nor_y


def pxrdsim(Volume,Point_group,AtomCoordinates,latt,crystal_system,GrainSize,orientation,thermo_vib,zero_shift):
    wavelength = 1.54184
    two_theta_range = (8, 82.02,0.02) # 10-80, 0.02
    grid, d_list = Diffraction_index(crystal_system,latt,wavelength,two_theta_range)
    res_HKL, _, d_res_HKL, _ = cal_extinction(Point_group, grid,d_list,crystal_system,AtomCoordinates,wavelength,)
    mu_array = 2 * np.arcsin(wavelength /2/np.array(d_res_HKL)) * 180 / np.pi

    FHKL_square = []
    Mult = []
    for angle in range(len(res_HKL)):
        FHKL_square_left = 0
        FHKL_square_right = 0
        # _Atom_coordinate all atoms in lattice cell
        for atom in range(len(AtomCoordinates)):
            fi = cal_atoms(AtomCoordinates[atom][0],mu_array[angle], wavelength)
            FHKL_square_left += fi * np.cos(2 * np.pi * (AtomCoordinates[atom][1] * res_HKL[angle][0] +
                                                AtomCoordinates[atom][2] * res_HKL[angle][1] + AtomCoordinates[atom][3] * res_HKL[angle][2]))
            FHKL_square_right += fi * np.sin(2 * np.pi * (AtomCoordinates[atom][1] * res_HKL[angle][0] +
                                                AtomCoordinates[atom][2] * res_HKL[angle][1] + AtomCoordinates[atom][3] * res_HKL[angle][2]))
        Mult.append(mult_rule(res_HKL[angle][0],res_HKL[angle][1],res_HKL[angle][2],crystal_system))
        FHKL_square.append(FHKL_square_left ** 2 + FHKL_square_right ** 2)
        
    
  
    _Ints = [] # cal peak intensity
    for angle in range(len(FHKL_square)):
        _Ints.append(float(FHKL_square[angle] * Mult[angle] / Volume ** 2
                    * (1 + np.cos(mu_array[angle] * np.pi/180) ** 2) / (np.sin(mu_array[angle] / 2 * np.pi/180) **2 * np.cos(Mult[angle] / 2 * np.pi/180))))
    

    Γ = 0.888*wavelength/(GrainSize*np.cos(np.radians(np.array(mu_array)/2)))
    gamma_list = Γ / 2 + 1e-10
    sigma2_list = Γ**2 / (8*np.sqrt(2)) + 1e-10

    Ints = []
    for k in range(len(_Ints)):
        
        Ori_coe = np.clip(np.random.normal(loc=1, scale=0.2), 1-orientation[0], 1+orientation[0])
        M = 8/3 * np.pi**2*thermo_vib**2 * (np.sin(np.radians(mu_array[k]/2)) / wavelength)**2
        Deb_coe = np.exp(-2*M)
        Ints.append(_Ints[k] * Ori_coe * Deb_coe)

    x_sim = np.arange(two_theta_range[0],two_theta_range[1],two_theta_range[2])
    y_sim = 0
    for num in range(len(Ints)):
        _ = draw_peak_density(x_sim, Ints[num], mu_array[num], gamma_list[num], sigma2_list[num])
        y_sim += _
    # normalize the profile
    nor_y = y_sim / theta_intensity_area(x_sim,y_sim)
    
    x_sim += zero_shift
    random_polynomial = generate_random_polynomial(degree=6)
    _bac = random_polynomial(x_sim)
    _bac -= _bac.min()
    _bacI = _bac / _bac.max() * nor_y.max() * 0.05
    mixture = np.random.uniform(0, nor_y.max() * 0.02, size=len(x_sim))
    nor_y +=  np.flip(_bacI) + mixture
    nor_y = scale_list(nor_y)

    
    index_10 = np.abs(x_sim - 10).argmin()
    index_80 = np.abs(x_sim - 80).argmin() + 1
    x_sim = x_sim[index_10:index_80]
    nor_y = nor_y[index_10:index_80]

    return None, nor_y










