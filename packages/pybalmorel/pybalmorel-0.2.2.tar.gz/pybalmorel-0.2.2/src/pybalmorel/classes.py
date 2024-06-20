"""
Created on 08.06.2024

@author: Mathias Berg Rosendal, PhD Student at DTU Management (Energy Economics & Modelling)
"""
#%% ------------------------------- ###
###        0. Script Settings       ###
### ------------------------------- ###

import pandas as pd
from typing import Union, Tuple
from functools import partial
import os
import gams
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from .functions import symbol_to_df
from .plotting.interactive_barchart import interactive_bar_chart
from .plotting.production_profile import plot_profile
from .plotting.maps_balmorel import plot_map

#%% ------------------------------- ###
###           1. Outputs            ###
### ------------------------------- ###

class MainResults:
    def __init__(self, files: Union[str, list, tuple], 
                 paths: Union[str, list, tuple] = '.', 
                 scenario_names: Union[str, list, tuple] = None,
                 system_directory: str = None):
        """
        Initialises the MainResults class and loads gdx result file(s)

        Args:
            files (str, list, tuple): Name(s) of the gdx result file(s)
            paths (str, list, tuple): Path(s) to the gdx result file(s), assumed in same path if only one path given, defaults to working directory
            scenario_names (str, list, tuple): Name of scenarios corresponding to each gdx file, defaults to ['SC1', 'SC2', ..., 'SCN'] if None given
            system_directory (str, optional): GAMS system directory. Is not used if not specified.
        """

        ## Loading scenarios
        if type(files) == str:
            # Change filenames to list if just one string
            files = [files]
            
        ## File paths
        if type(paths) == str:
            # Create identical paths if only one given
            paths = [paths]*len(files)
            
        elif ((type(paths) == list) or (type(paths) == tuple)) and (len(paths) == 1):
            paths = paths*len(files)
            
        elif len(files) != len(paths):
            # Raise error if not given same amount of paths and files     
            raise Exception("%d files, but %d paths given!\nProvide only one path or the same amount of paths as files"%(len(files), len(paths)))
        
        ## Scenario Names
        if scenario_names == None:
            # Try to make scenario names from filenames, if None given
            scenario_names = pd.Series(files).str.replace('MainResults_', '').str.replace('MainResults','').str.replace('.gdx', '')
            
            # Check if names are identical
            if (len(scenario_names.unique()) != len(scenario_names)) or (np.all(scenario_names == '')):
                scenario_names = ['SC%d'%(i+1) for i in range(len(files))] # if so, just make generic names
            else:
                scenario_names = list(scenario_names) 
                
        elif type(scenario_names) == str:
            scenario_names = [scenario_names]
            
        if len(files) != len(scenario_names):    
            # Raise error if not given same amount of scenario_names and files
            raise Exception("%d files, but %d scenario names given!\nProvide none or the same amount of scenario names as files"%(len(files), len(scenario_names)))
            
        ## Store MainResult databases
        self.files = files
        self.paths = paths
        self.sc = scenario_names
        self.db = {}
        if system_directory != None:
            ws = gams.GamsWorkspace(system_directory=system_directory)
        else:
            ws = gams.GamsWorkspace()
            
        for i in range(len(files)):
            self.db[scenario_names[i]] = ws.add_database_from_gdx(os.path.join(os.path.abspath(paths[i]), files[i]))
     
    # Getting a certain result
    def get_result(self, symbol: str, cols: str = 'None') -> pd.DataFrame:
        """Get a certain result from the loaded gdx file(s) into a pandas DataFrame

        Args:
            symbol (str): The desired result, e.g. PRO_YCRAGF
            cols (str, optional): Specify custom columns. Defaults to pre-defined formats.

        Returns:
            pd.DataFrame: The output DataFrame
        """
        # Placeholder
        df = pd.DataFrame()
        
        for SC in self.sc:
            # Get results from each scenario
            temp = symbol_to_df(self.db[SC], symbol, cols)
            temp['Scenario'] = SC 
            
            # Put scenario in first column
            temp = temp.loc[:, ['Scenario'] + list(temp.columns[:-1])]
            
            # Save
            df = pd.concat((df, temp), ignore_index=True)
            
        return df  
    
    ## Plotting tools
    # Interactive bar chart plotting
    def interactive_bar_chart(self):
        """
        GUI for bar chart plotting
        """
        return  interactive_bar_chart(self)        
    
    # Plotting a production profile
    def plot_profile(self,
                     commodity: str,  
                     year: int, 
                     scenario: str = 0,
                     columns: str = 'Technology',
                     region: str = 'ALL',
                     style: str = 'light') -> Tuple[Figure, Axes]:
        """Plots the production profile of a commodity, in a year, for a certain scenario

        Args:
            commodity (str): The commodity (Electricity, Heat or Hydrogen)
            year (int): The model year to plot
            scenario (str, optional): Defaults to the first scenario in MainResults.
            columns (str, optional): Technology or Fuel as . Defaults to 'Technology'.
            region (str, optional): Which country, region or area to plot. Defaults to 'ALL'.
            style (str, optional): Plot style, light or dark. Defaults to 'light'.

        Returns:
            Figure, Axes: The figure and axes objects for further manipulations 
        """
        return plot_profile(self, commodity, year, scenario, columns, region, style)
        
    
    def plot_map(self, 
                scenario: str, 
                commodity: str, 
                year: int,
                path_to_geofile: str = None,  
                bypass_path: str = None, 
                geo_file_region_column: str = 'id', 
                style: str = 'light') -> Tuple[Figure, Axes]:
        """Plots the transmission capacities in a scenario, of a certain commodity

        Args:
            path_to_result (str): Path to the .gdx file
            scenario (str): The scenario name
            commodity (str): Electricity or hydrogen
            year (int): Model year 
            path_to_geofile (str, optional): The path to the fitting geofile. Defaults to '../geofiles/2024 BalmorelMap.geojson' in package directory.
            bypass_path (str, optional): Extra coordinates for transmission lines for beauty. Defaults to '../geofiles/bypass_lines' in package directory.
            geo_file_region_column (str, optional): The columns containing the region names of MainResults. Defaults to 'id'.
            style (str, optional): Plot style. Defaults to 'light'.

        Returns:
            Tuple[Figure, Axes]: The figure and axes objects of the plot
        """
        # Find path of scenario
        idx = np.array(self.sc) == scenario
        path = np.array(self.paths)[idx][0]
        files = np.array(self.files)[idx][0]
        path = os.path.join(path, files)
        
        return plot_map(path, scenario, commodity, 
                        year, path_to_geofile, bypass_path,
                        geo_file_region_column, style)
        
    # For wrapping functions, makes it possible to add imported functions in __init__ easily
    def _existing_func_wrapper(self, function, *args, **kwargs):
        return function(self, *args, **kwargs)     


#%% ------------------------------- ###
###            2. Inputs            ###
### ------------------------------- ###

class IncFile:
    """A useful class for creating .inc-files for GAMS models
    Args:
    prefix (str): The first part of the .inc file.
    body (str): The main part of the .inc file.
    suffix (str): The last part of the .inc file.
    name (str): The name of the .inc file.
    path (str): The path to save the file, defaults to 'Balmorel/base/data'.
    """
    def __init__(self, prefix: str = '', body: str = '', 
                 suffix: str = '', name: str = 'name', 
                 path: str = 'Balmorel/base/data/'):
        self.prefix = prefix
        self.body = body
        self.suffix = suffix
        self.name = name
        self.path = path

    def body_concat(self, df: pd.DataFrame):
        """Concatenate a body temporarily being a dataframe to another dataframe
        """
        self.body = pd.concat((self.body, df)) # perhaps make a IncFile.body.concat function.. 

    def body_prepare(self, index: list, columns: list,
                    values: str = 'Value',
                    aggfunc: str ='sum',
                    fill_value: Union[str, int] = ''):
    
        # Pivot
        self.body = self.body.pivot_table(index=index, columns=columns, 
                            values=values, aggfunc=aggfunc,
                            fill_value=fill_value)
        
        # Check if there are multiple levels in index and 
        # concatenate with " . "
        if hasattr(self.body.index, 'levels'):
            new_ind = pd.Series(self.body.index.get_level_values(0))
            for level in range(1, len(self.body.index.levels)):
                new_ind += ' . ' + self.body.index.get_level_values(level) 

            self.body.index = new_ind
        
        # Check if there are multiple levels in columns and 
        # concatenate with " . "
        if hasattr(self.body.columns, 'levels'):
            new_ind = pd.Series(self.body.columns.get_level_values(0))
            for level in range(1, len(self.body.columns.levels)):
                new_ind += ' . ' + self.body.columns.get_level_values(level) 

            self.body.columns = new_ind
            
        # Delete names
        self.body.columns.name = ''
        self.body.index.name = ''


    def save(self):
        if self.name[-4:] != '.inc':
            self.name += '.inc'  
       
        with open(os.path.join(self.path, self.name), 'w') as f:
            f.write(self.prefix)
            if type(self.body) == str:
                f.write(self.body)
            elif type(self.body) == pd.DataFrame:
                f.write(self.body.to_string())
            else:
                print('Wrong format of %s.body!'%self.name)
                print('No body written')
            f.write(self.suffix)
 
