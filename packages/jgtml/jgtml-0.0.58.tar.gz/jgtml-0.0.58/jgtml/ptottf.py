
import pandas as pd
from jgtpy import JGTCDSSvc as svc
from jgtutils import jgtpov as jpov
from jgtutils.jgtconstants import (MFI_VAL, ZCOL, AO)

import os

def get_ttf_basedir(use_full,ns="ttf"):
    if use_full:
        bd=os.getenv("JGTPY_DATA_FULL")
        if bd is None:
            raise Exception("JGTPY_DATA_FULL environment variable is not set.")
    else:
        bd=os.getenv("JGTPY_DATA")
        if bd is None:
            raise Exception("JGTPY_DATA environment variable is not set.")
    fulldir=os.path.join(bd,ns)
    #mkdir -p fulldir
    os.makedirs(fulldir, exist_ok=True)
    return fulldir

def get_ttf_outfile_fullpath(i,t,use_full,suffix="",ns="ttf"):
    save_basedir=get_ttf_basedir(use_full,ns)
    ifn=i.replace("/","-")
    output_filename = f"{ifn}_{t}_ttf{suffix}.csv"
    return os.path.join(save_basedir,output_filename)
  
columns_to_get_from_higher_tf = [MFI_VAL, ZCOL, AO]

def make_htf_created_columns_array(workset,t):
    created_columns=[]
    for c in columns_to_get_from_higher_tf:
      for k in workset:
        if not c in created_columns: 
          created_columns.append(c)
        new_col_name = c+"_"+k
        if k != t:
          if not new_col_name in created_columns: 
            created_columns.append(new_col_name)
    return created_columns

def read_ttf_csv(i, t, use_full=False):
    output_filename=get_ttf_outfile_fullpath(i,t,use_full)
    print("Read TTF: ", output_filename)
    #if not os.path.exists(output_filename): create it
    if not os.path.exists(output_filename):
        create_ttf_csv(i, t, use_full,force_read=True)
    return pd.read_csv(output_filename, index_col=0)
  
def read_ttf_csv_selection(i, t, use_full=False):
    output_filename_sel=get_ttf_outfile_fullpath(i,t,use_full,suffix="_sel")
    return pd.read_csv(output_filename_sel, index_col=0)
 
def create_ttf_csv(i, t, use_full=False, use_fresh=True, quotescount=-1,force_read=False):
  if use_full:
    print("Using full dataset")

  povs = jpov.get_higher_tf_array(t)
  ttf = pd.DataFrame()

  workset = svc.get_higher_cdf_datasets(i, t, use_full=use_full, use_fresh=use_fresh, quotescount=quotescount, quiet=True, force_read=force_read)
  ttf=workset[t]
  created_columns = make_htf_created_columns_array(workset, t)
  

  for k in workset:  
    if k!=t:
      v=workset[k]
      for c in columns_to_get_from_higher_tf:
      
        new_col_name = c+"_"+k
        ttf[new_col_name]=None

        for ii, row in ttf.iterrows():
          #get the date of the current row (the index)
          date = ii
          #print(k)
          data = v[v.index <= date]
          if not data.empty:
            data = data.iloc[-1]
            ttf.at[ii,new_col_name]=data[c]
  
  columns_we_want_to_keep_to_view=created_columns
  ttf_sel=ttf[columns_we_want_to_keep_to_view].copy()
  
  #save basedir is $JGTPY_DATA/ttf is not use_full, if use_full save basedir is $JGTPY_DATA_FULL/ttf
  
  output_filename=get_ttf_outfile_fullpath(i,t,use_full)
  output_filename_sel=get_ttf_outfile_fullpath(i,t,use_full,suffix="_sel")
  
  ttf.to_csv(output_filename, index=True)
  ttf_sel.to_csv(output_filename_sel, index=True)
  print(f"Output CSV file '{output_filename}' created successfully.")
  print(f"Output CSV file '{output_filename_sel}' created successfully.")
  return ttf
