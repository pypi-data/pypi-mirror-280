import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None)  
import os
import re
from tqdm import tqdm

def load_claim_property(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
    # Regular expression to find a four-digit year in the file name
    year_pattern = re.compile(r'\b(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
    for file in sorted(os.listdir(directory)):
        if file.endswith('.xlsx') and not file.startswith('~$'):
            
            # Find the year in the file name
            match = year_pattern.search(file)
            if match:
                year = match.group(1)
                file_path = os.path.join(directory, file)
                try:
                    """ IMPORT DATA"""
                    if diagnostics:
                        print(f"\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
                    # Load and clean data specifying the engine
                    df = pd.read_excel(file_path, header=None, skiprows=skip_rows, engine='openpyxl')
                    df.drop(df.columns[-1], axis = 1, inplace = True)  # remove na col at the end

                    # Dynamically determine headers based on the first non-empty cell per column
                    headers = []
                    for col in df.columns:
                        if pd.notna(df.iloc[1, col]):
                            headers.append(df.iloc[1, col])
                        elif pd.notna(df.iloc[0, col]) and pd.isna(df.iloc[1, col]):
                            headers.append(df.iloc[0, col])
                        elif diagnostics:
                            print(f'No headers found for {col}')

                    # Set the determined headers as column names
                    df.columns = headers
                    df = df.drop([0, 1])
                    df.reset_index(drop = True, inplace=True)
                    if diagnostics:
                        print(f'   Rows = {df.shape[0]}')
                    # print(f'Columns = {df.shape[1]}')
            
            
                    """ RENAME COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRenaming Columns:")
                    df_clm_dict = {
                        'mã đơn vị quản lý': 'MA_DVI',
                        'Mã đơn vị xử lý': 'MA_DVI_XL',
                        'Số hồ sơ': 'SO_HSBT',
                        'Ngày mở HSBT': 'NGAY_MO_HSBT',
                        'Ngày thông báo': 'NGAY_THONG_BAO',
                        'Ngày xảy ra': 'NGAY_XAY_RA',
                        'Số ngày tồn': 'SO_NGAY_TON',
                        'Ngày giải quyết': 'NGAY_GIAI_QUYET',
                        'Phòng': 'PHONG_BT',
                        'Cán bộ bồi thường': 'CAN_BO_BT',
                        'Nghiệp vụ': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Số hợp đồng': 'SO_HD',
                        'Tên khách hàng': 'TEN_KH',
                        'Mã khai thác': 'MA_KT',
                        'Mã khách hàng': 'MA_KH',
                        'Địa chỉ': 'DIA_CHI',
                        'Nguồn KT': 'NGUON_KT',
                        'Đối tượng bảo hiểm': 'LOAI_TS',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày KT': 'NGAY_KT',
                        'Mã NT': 'MA_NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Phí bảo hiểm VNĐ': 'PHI_BH',
                        'Nhóm': 'NHOM_TS', 
                        'Nguyên nhân': 'NGUYEN_NHAN_BT',
                        'Số tiền tổn thất': 'STTT',
                        'Số tiền bồi thường': 'STBT', 
                        'Ngày thanh toán bồi thường': 'NGAY_TT_BT',
                        'Hạch toán': 'HACH_TOAN',
                        'Ghi chú': 'GHI_CHU'

                    }

                    df.rename(columns={col: df_clm_dict[col] for col in df.columns if col in df_clm_dict}, inplace=True)

                            
                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Gara',
                        'Loại xe',
                        'Biển xe',
                        'Tuổi xe',
                        'Số GCN',
                        'Số khung/Số máy',
                        'Lĩnh vực kinh doanh',
                        'Cán bộ cấp đơn',
                        'Tổng giảm trừ', 
                        'STT',
                        'Số CV KN',
                        'Ngày hồ sơ đầy đủ', 
                        'Khu vực', 
                        'Điện thoại', 
                        'Danh mục cơ sở', 
                        'Email', 
                        'Số tiền bảo hiểm đưa vào tái',  
                        'Ngày thanh toán phí',
                        'Kiểu ĐBH', 
                        'Tỷ lệ ĐBH', 
                        'Thu đòi đồng BH', 
                        'Tỷ lệ tái CĐ', 
                        'Thu đòi tái bảo hiểm CĐ', 
                        'Tỷ lệ tái TT', 
                        'Thu đòi tái bảo hiểm TT',
                        'Giảm trừ tỷ lệ bảo hiểm',
                        'Giảm trừ khấu hao',
                        'Giảm trừ chế tài',
                        'Giảm trừ khác',
                        'Miễn thường',
                        'Thu hồi bồi thường',
                        'Phí giám định'
                    ]

                    # Removing columns, check if the columns exist
                    for col in removed_cols:
                        if col in df.columns:
                            df.drop(columns=col, inplace=True)
                        elif diagnostics:
                            print(f"   Column {col} not found in DataFrame.")                       


                    """ ADD COLUMN FOR DATA YEAR"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nAdding Column NAM_DATA:")
                    if dup_year:
                        df['NAM_DATA'] = file
                    else:
                        df['NAM_DATA'] = year


                    """ FILTER FOR LHNV"""
                    if lhnv:
                        if diagnostics:
                            print("--------------------------------------------------------------------------\nFiltering for LHNV:")    
                        rows_b4 = df.shape[0]    
                        df = df[df['MA_LHNV'].str.startswith(lhnv)]
                        if diagnostics:
                            print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')

                    
                    
                    """ CONVERT DATE COLUMNS""" 
                    if diagnostics:          
                        print("--------------------------------------------------------------------------\nReformatting Date Cols:")
                    dates_columns = [
                        "NGAY_MO_HSBT",
                        "NGAY_THONG_BAO",
                        "NGAY_XAY_RA",
                        "NGAY_GIAI_QUYET",
                        "NGAY_CAP",
                        "NGAY_HL",
                        "NGAY_KT",
                        "NGAY_TT_BT"
                    ]

                    for dates_col in dates_columns:
                        if dates_col in df.columns:  # Ensure column exists before converting
                            original_na_count = df[dates_col].isna().sum()
                            df[dates_col] = pd.to_datetime(df[dates_col], errors='coerce', dayfirst=True)
                            new_na_count = df[dates_col].isna().sum()
                            detected_errors = new_na_count - original_na_count
                            if (detected_errors > 0) & diagnostics:
                                print(f"   Detected {detected_errors} Incorrect Dates in {dates_col}")
                        elif diagnostics:
                            print(f"   Column {dates_col} not found in DataFrame.")


                    """ CONVERT NUMERICAL COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nReformatting Num Cols:")
                    num_columns = [
                        'STBH',
                        'PHI_BH',
                        'STTT',
                        'STBT'
                    ]
                    
                    for num_col in num_columns:
                        if num_col in df.columns:  # Ensure column exists before converting
                            original_na_count = df[num_col].isna().sum()
                            df[num_col] = pd.to_numeric(df[num_col], errors='coerce')
                            new_na_count = df[num_col].isna().sum()
                            detected_errors = new_na_count - original_na_count
                            if (detected_errors > 0) & diagnostics:
                                print(f"   Detected {detected_errors} Incorrect Values in {num_col}")
                        elif diagnostics:
                            print(f"   Column {num_col} not found in DataFrame.")
                    
                    
                    
                    """ REMOVE ROWs WITH MISSING EFF DATE """
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Rows Missing NGAY_HL:")    
                    rows_b4 = df.shape[0]    
                    df = df[df['NGAY_HL'].notna()]
                    if diagnostics:
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                    
                    
                    
                    """ PRINT EFF_YEAR COUNTS IN EACH DF"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nEff Year Count:")
                    df['NAM_HL'] = df['NGAY_HL'].dt.year 
                    if dup_year & diagnostics:
                        print(f"Effective Year Count in {file}: {df['NAM_HL'].value_counts()}")
                    elif diagnostics:    
                        print(f"Effective Year Count in CY{year}: {df['NAM_HL'].value_counts()}")

                        
                    
                    """ SAVE DF TO GLOBAL VARIABLE"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nSaving DF:")
                    # Assign DataFrame to a global variable dynamically using the year
                    df_name = f'{file}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                    elif diagnostics:
                        print(f"Summary of CY{year}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                        print('--------------------------------------------------------------------------\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                    
                except Exception as e:
                    if diagnostics:
                        print(f"Failed to process {file}: {e}")
            else:
                if diagnostics:
                    print(f"No year found in the file name {file}")

    # Print all global DataFrame names created
    print("\n\n\n==========================================================================\n==========================================================================\nSuccessfully Imported:", ", ".join(global_df_names))
    
    """ CONCAT INTO ONE DF"""
    all_dataframes = [globals()[name] for name in global_df_names if name in globals()]
    df_clm = pd.concat(all_dataframes, ignore_index=True)
    print(f"   Total Rows = {df_clm.shape[0]:,.0f}\n   Total Claims = {df_clm['STBT'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_clm

