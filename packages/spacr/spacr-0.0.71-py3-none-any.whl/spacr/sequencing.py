import os, re, time, math, subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Bio import pairwise2
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import gmean
from difflib import SequenceMatcher

def reverse_complement(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N':'N'}
    reverse_seq = dna_sequence[::-1]
    reverse_complement_seq = ''.join([complement_dict[base] for base in reverse_seq])
    return reverse_complement_seq

def complement(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N':'N'}
    complement_seq = ''.join([complement_dict[base] for base in dna_sequence])
    return complement_seq

def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])

def generate_plate_heatmap(df, plate_number, variable, grouping, min_max):
    if grouping == 'mean':
        temp = df.groupby(['plate','row','col']).mean()[variable]
    if grouping == 'sum':
        temp = df.groupby(['plate','row','col']).sum()[variable]
    if grouping == 'count':
        temp = df.groupby(['plate','row','col']).count()[variable]
    if grouping in ['mean', 'count', 'sum']:
        temp = pd.DataFrame(temp)
    if min_max == 'all':  
        min_max=[np.min(temp[variable]),np.max(temp[variable])]   
    if min_max == 'allq':
        min_max = np.quantile(temp[variable], [0.2, 0.98])
    plate = df[df['plate'] == plate_number]
    plate = pd.DataFrame(plate)
    if grouping == 'mean':
        plate = plate.groupby(['plate','row','col']).mean()[variable]
    if grouping == 'sum':
        plate = plate.groupby(['plate','row','col']).sum()[variable]
    if grouping == 'count':
        plate = plate.groupby(['plate','row','col']).count()[variable]
    if grouping not in ['mean', 'count', 'sum']:
        plate = plate.groupby(['plate','row','col']).mean()[variable]
    if min_max == 'plate':
        min_max=[np.min(plate[variable]),np.max(plate[variable])]
    plate = pd.DataFrame(plate)
    plate = plate.reset_index()
    if 'plate' in plate.columns:
        plate = plate.drop(['plate'], axis=1)
    pcol = [*range(1,28,1)]
    prow = [*range(1,17,1)]
    new_col = []
    for v in pcol:
        col = 'c'+str(v)
        new_col.append(col)
    new_col.remove('c15')
    new_row = []
    for v in prow:
        ro = 'r'+str(v)
        new_row.append(ro)
    plate_map = pd.DataFrame(columns=new_col, index = new_row)
    for index, row in plate.iterrows():
        r = row['row']
        c = row['col']
        v = row[variable]
        plate_map.loc[r,c]=v
    plate_map = plate_map.fillna(0)
    return pd.DataFrame(plate_map), min_max

def plot_plates(df, variable, grouping, min_max, cmap):
    try:
        plates = np.unique(df['plate'], return_counts=False)
    except:
        try:
            df[['plate', 'row', 'col']] = df['prc'].str.split('_', expand=True)
            df = pd.DataFrame(df)
            plates = np.unique(df['plate'], return_counts=False)
        except:
            next
    #plates = np.unique(df['plate'], return_counts=False)
    nr_of_plates = len(plates)
    print('nr_of_plates:',nr_of_plates)
    # Calculate the number of rows and columns for the subplot grid
    if nr_of_plates in [1, 2, 3, 4]:
        n_rows, n_cols = 1, 4
    elif nr_of_plates in [5, 6, 7, 8]:
        n_rows, n_cols = 2, 4
    elif nr_of_plates in [9, 10, 11, 12]:
        n_rows, n_cols = 3, 4
    elif nr_of_plates in [13, 14, 15, 16]:
        n_rows, n_cols = 4, 4

    # Create the subplot grid with the specified number of rows and columns
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(40, 5 * n_rows))

    # Flatten the axes array to a one-dimensional array
    ax = ax.flatten()

    # Loop over each plate and plot the heatmap
    for index, plate in enumerate(plates):
        plate_number = plate
        plate_map, min_max = generate_plate_heatmap(df=df, plate_number=plate_number, variable=variable, grouping=grouping, min_max=min_max)
        if index == 0:
            print('plate_number:',plate_number,'minimum:',min_max[0], 'maximum:',min_max[1])
        # Plot the heatmap on the appropriate subplot
        sns.heatmap(plate_map, cmap=cmap, vmin=min_max[0], vmax=min_max[1], ax=ax[index])
        ax[index].set_title(plate_number)

    # Remove any empty subplots
    for i in range(nr_of_plates, n_rows * n_cols):
        fig.delaxes(ax[i])

    # Adjust the spacing between the subplots
    plt.subplots_adjust(wspace=0.1, hspace=0.4)

    # Show the plot
    plt.show()
    print()
    return

def count_mismatches(seq1, seq2, align_length=10):
    alignments = pairwise2.align.globalxx(seq1, seq2)
    # choose the first alignment (there might be several with the same score)
    alignment = alignments[0]
    # alignment is a tuple (seq1_aligned, seq2_aligned, score, begin, end)
    seq1_aligned, seq2_aligned, score, begin, end = alignment
    # Determine the start of alignment (first position where at least align_length bases are the same)
    start_of_alignment = next(i for i in range(len(seq1_aligned) - align_length + 1) 
                              if seq1_aligned[i:i+align_length] == seq2_aligned[i:i+align_length])
    # Trim the sequences to the same length from the start of the alignment
    seq1_aligned = seq1_aligned[start_of_alignment:]
    seq2_aligned = seq2_aligned[start_of_alignment:]
    # Trim the sequences to be of the same length (from the end)
    min_length = min(len(seq1_aligned), len(seq2_aligned))
    seq1_aligned = seq1_aligned[:min_length]
    seq2_aligned = seq2_aligned[:min_length]
    mismatches = sum(c1 != c2 for c1, c2 in zip(seq1_aligned, seq2_aligned))
    return mismatches
    

def get_sequence_data(r1,r2):
    forward_regex = re.compile(r'^(...GGTGCCACTT)TTTCAAGTTG.*?TTCTAGCTCT(AAAAC[A-Z]{18,22}AACTT)GACATCCCCA.*?AAGGCAAACA(CCCCCTTCGG....).*') 
    r1fd = forward_regex.search(r1)
    reverce_regex = re.compile(r'^(...CCGAAGGGGG)TGTTTGCCTT.*?TGGGGATGTC(AAGTT[A-Z]{18,22}GTTTT)AGAGCTAGAA.*?CAACTTGAAA(AAGTGGCACC...).*') 
    r2fd = reverce_regex.search(r2)
    rc_r1 = reverse_complement(r1)
    rc_r2 = reverse_complement(r2) 
    if all(var is not None for var in [r1fd, r2fd]):
        try:
            r1_mis_matches, _ = count_mismatches(seq1=r1, seq2=rc_r2, align_length=5)
            r2_mis_matches, _ = count_mismatches(seq1=r2, seq2=rc_r1, align_length=5)
        except:
            r1_mis_matches = None
            r2_mis_matches = None
        column_r1 = reverse_complement(r1fd[1])
        sgrna_r1 = r1fd[2]
        platerow_r1 = r1fd[3]
        column_r2 = r2fd[3]
        sgrna_r2 = reverse_complement(r2fd[2])
        platerow_r2 = reverse_complement(r2fd[1])+'N'

        data_dict = {'r1_plate_row':platerow_r1,
                     'r1_col':column_r1,
                     'r1_gRNA':sgrna_r1,
                     'r1_read':r1,
                     'r2_plate_row':platerow_r2,
                     'r2_col':column_r2,
                     'r2_gRNA':sgrna_r2,
                     'r2_read':r2,
                     'r1_r2_rc_mismatch':r1_mis_matches,
                     'r2_r1_rc_mismatch':r2_mis_matches,
                     'r1_len':len(r1),
                     'r2_len':len(r2)}
    else:
        try:
            r1_mis_matches, _ = count_mismatches(r1, rc_r2, align_length=5)
            r2_mis_matches, _ = count_mismatches(r2, rc_r1, align_length=5)
        except:
            r1_mis_matches = None
            r2_mis_matches = None
        data_dict = {'r1_plate_row':None,
             'r1_col':None,
             'r1_gRNA':None,
             'r1_read':r1,
             'r2_plate_row':None,
             'r2_col':None,
             'r2_gRNA':None,
             'r2_read':r2,
             'r1_r2_rc_mismatch':r1_mis_matches,
             'r2_r1_rc_mismatch':r2_mis_matches,
             'r1_len':len(r1),
             'r2_len':len(r2)}

    return data_dict

def get_read_data(identifier, prefix):
    if identifier.startswith("@"):
        parts = identifier.split(" ")
        # The first part contains the instrument, run number, flowcell ID, lane, tile, and coordinates
        instrument, run_number, flowcell_id, lane, tile, x_pos, y_pos = parts[0][1:].split(":")
        # The second part contains the read number, filter status, control number, and sample number
        read, is_filtered, control_number, sample_number = parts[1].split(":")
        rund_data_dict = {'instrument':instrument, 
                          'run_number':run_number, 
                          'flowcell_id':flowcell_id, 
                          'lane':lane, 
                          'tile':tile, 
                          'x_pos':x_pos, 
                          'y_pos':y_pos, 
                          'read':read, 
                          'is_filtered':is_filtered, 
                          'control_number':control_number, 
                          'sample_number':sample_number}
        modified_dict = {prefix + key: value for key, value in rund_data_dict.items()}
    return modified_dict

def pos_dict(string):
    pos_dict = {}
    for i, char in enumerate(string):
        if char not in pos_dict:
            pos_dict[char] = [i]
        else:
            pos_dict[char].append(i)
    return pos_dict

def truncate_read(seq,qual,target):
    index = seq.find(target)
    end = len(seq)-(3+len(target))
    if index != -1: # If the sequence is found
        if index-3 >= 0:
            seq = seq[index-3:]
            qual = qual[index-3:]

    return seq, qual

def equalize_lengths(seq1, seq2, pad_char='N'):
    len_diff = len(seq1) - len(seq2)

    if len_diff > 0:  # seq1 is longer
        seq2 += pad_char * len_diff  # pad seq2 with 'N's
    elif len_diff < 0:  # seq2 is longer
        seq1 += pad_char * (-len_diff)  # pad seq1 with 'N's

    return seq1, seq2

def get_read_data(identifier, prefix):
    if identifier.startswith("@"):
        parts = identifier.split(" ")
        # The first part contains the instrument, run number, flowcell ID, lane, tile, and coordinates
        instrument, run_number, flowcell_id, lane, tile, x_pos, y_pos = parts[0][1:].split(":")
        # The second part contains the read number, filter status, control number, and sample number
        read, is_filtered, control_number, sample_number = parts[1].split(":")
        rund_data_dict = {'instrument':instrument, 
                          'x_pos':x_pos, 
                          'y_pos':y_pos}
        modified_dict = {prefix + key: value for key, value in rund_data_dict.items()}
    return modified_dict

def extract_barecodes(r1_fastq, r2_fastq, csv_loc, chunk_size=100000):
    data_chunk = []
    # Open both FASTQ files.
    with open(r1_fastq) as r1_file, open(r2_fastq) as r2_file:
        index = 0
        save_index = 0
        while True:
            index += 1
            start = time.time()
            # Read 4 lines at a time
            r1_identifier = r1_file.readline().strip()
            r1_sequence = r1_file.readline().strip()
            r1_plus = r1_file.readline().strip()
            r1_quality = r1_file.readline().strip()
            r2_identifier = r2_file.readline().strip()
            r2_sequence = r2_file.readline().strip()
            r2_sequence = reverse_complement(r2_sequence)
            r2_sequence = r2_sequence
            r2_plus = r2_file.readline().strip()
            r2_quality = r2_file.readline().strip()
            r2_quality = r2_quality
            if not r1_identifier or not r2_identifier:
                break
            #if index > 100:
            #    break
            target = 'GGTGCCACTT'
            r1_sequence, r1_quality = truncate_read(r1_sequence, r1_quality, target)
            r2_sequence, r2_quality = truncate_read(r2_sequence, r2_quality, target)
            r1_sequence, r2_sequence = equalize_lengths(r1_sequence, r2_sequence, pad_char='N')
            r1_quality, r2_quality = equalize_lengths(r1_quality, r2_quality, pad_char='-')
            alignments = pairwise2.align.globalxx(r1_sequence, r2_sequence)
            alignment = alignments[0]
            score = alignment[2]
            column = None
            platerow = None
            grna = None
            if score >= 125:
                aligned_r1 = alignment[0]
                aligned_r2 = alignment[1]
                position_dict = {i+1: (base1, base2) for i, (base1, base2) in enumerate(zip(aligned_r1, aligned_r2))}
                phred_quality1 = [ord(char) - 33 for char in r1_quality]
                phred_quality2 = [ord(char) - 33 for char in r2_quality]
                r1_q_dict = {i+1: quality for i, quality in enumerate(phred_quality1)}
                r2_q_dict = {i+1: quality for i, quality in enumerate(phred_quality2)}
                read = ''
                for key in sorted(position_dict.keys()):
                    if position_dict[key][0] != '-' and (position_dict[key][1] == '-' or r1_q_dict.get(key, 0) >= r2_q_dict.get(key, 0)):
                        read = read + position_dict[key][0]
                    elif position_dict[key][1] != '-' and (position_dict[key][0] == '-' or r2_q_dict.get(key, 0) > r1_q_dict.get(key, 0)):
                        read = read + position_dict[key][1]
                pattern = re.compile(r'^(...GGTGC)CACTT.*GCTCT(TAAAC[A-Z]{18,22}AACTT)GACAT.*CCCCC(TTCGG....).*')
                regex_patterns = pattern.search(read)
                if all(var is not None for var in [regex_patterns]):
                    column = regex_patterns[1]
                    grna = reverse_complement(regex_patterns[2])
                    platerow = reverse_complement(regex_patterns[3])
            elif score < 125:
                read = r1_sequence
                pattern = re.compile(r'^(...GGTGC)CACTT.*GCTCT(TAAAC[A-Z]{18,22}AACTT)GACAT.*CCCCC(TTCGG....).*')
                regex_patterns = pattern.search(read)
                if all(var is not None for var in [regex_patterns]):
                    column = regex_patterns[1]
                    grna = reverse_complement(regex_patterns[2])
                    platerow = reverse_complement(regex_patterns[3])
                    #print('2', platerow)
            data_dict = {'read':read,'column':column,'platerow':platerow,'grna':grna, 'score':score}
            end = time.time()
            if data_dict.get('grna') is not None:
                save_index += 1
                r1_rund_data_dict = get_read_data(r1_identifier, prefix='r1_')
                r2_rund_data_dict = get_read_data(r2_identifier, prefix='r2_')
                r1_rund_data_dict.update(r2_rund_data_dict)
                r1_rund_data_dict.update(data_dict)
                r1_rund_data_dict['r1_quality'] = r1_quality
                r1_rund_data_dict['r2_quality'] = r2_quality
                data_chunk.append(r1_rund_data_dict)
                print(f'Processed reads: {index} Found barecodes in {save_index} Time/read: {end - start}', end='\r', flush=True)
                if save_index % chunk_size == 0:  # Every `chunk_size` reads, write to the CSV
                    if not os.path.isfile(csv_loc):
                        df = pd.DataFrame(data_chunk)
                        df.to_csv(csv_loc, index=False)
                    else:
                        df = pd.DataFrame(data_chunk)
                        df.to_csv(csv_loc, mode='a', header=False, index=False)
                    data_chunk = []  # Clear the chunk
                    
def split_fastq(input_fastq, output_base, num_files):
    # Create file objects for each output file
    outputs = [open(f"{output_base}_{i}.fastq", "w") for i in range(num_files)]
    with open(input_fastq, "r") as f:
        # Initialize a counter for the lines
        line_counter = 0
        for line in f:
            # Determine the output file
            output_file = outputs[line_counter // 4 % num_files]
            # Write the line to the appropriate output file
            output_file.write(line)
            # Increment the line counter
            line_counter += 1
    # Close output files
    for output in outputs:
        output.close()

def process_barecodes(df):
    print('==== Preprocessing barecodes ====')
    plate_ls = []
    row_ls = [] 
    column_ls = []
    grna_ls = []
    read_ls = []
    score_ls = []
    match_score_ls = []
    index_ls = []
    index = 0
    print_every = 100
    for i,row in df.iterrows():
        index += 1
        r1_instrument=row['r1_instrument']
        r1_x_pos=row['r1_x_pos']
        r1_y_pos=row['r1_y_pos']
        r2_instrument=row['r2_instrument']
        r2_x_pos=row['r2_x_pos']
        r2_y_pos=row['r2_y_pos']
        read=row['read']
        column=row['column']
        platerow=row['platerow']
        grna=row['grna']
        score=row['score']
        r1_quality=row['r1_quality']
        r2_quality=row['r2_quality']
        if r1_x_pos == r2_x_pos:
            if r1_y_pos == r2_y_pos:
                match_score = 0
                
                if grna.startswith('AAGTT'):
                    match_score += 0.5
                if column.endswith('GGTGC'):
                    match_score += 0.5
                if platerow.endswith('CCGAA'):
                    match_score += 0.5
                index_ls.append(index)
                match_score_ls.append(match_score)
                score_ls.append(score)
                read_ls.append(read)
                plate_ls.append(platerow[:2])
                row_ls.append(platerow[2:4])
                column_ls.append(column[:3])
                grna_ls.append(grna)
                if index % print_every == 0:
                    print(f'Processed reads: {index}', end='\r', flush=True)
    df = pd.DataFrame()
    df['index'] = index_ls
    df['score'] = score_ls
    df['match_score'] = match_score_ls
    df['plate'] = plate_ls
    df['row'] = row_ls
    df['col'] = column_ls
    df['seq'] = grna_ls
    df_high_score = df[df['score']>=125]
    df_low_score = df[df['score']<125]
    print(f'', flush=True)
    print(f'Found {len(df_high_score)} high score reads;Found {len(df_low_score)} low score reads')
    return df, df_high_score, df_low_score

def find_grna(df, grna_df):
    print('==== Finding gRNAs ====')
    seqs = list(set(df.seq.tolist()))
    seq_ls = []
    grna_ls = []
    index = 0
    print_every = 1000
    for grna in grna_df.Seq.tolist():
        reverse_regex = re.compile(r'.*({}).*'.format(grna))
        for seq in seqs:
            index += 1
            if index % print_every == 0:
                print(f'Processed reads: {index}', end='\r', flush=True)
            found_grna = reverse_regex.search(seq)
            if found_grna is None:
                seq_ls.append('error')
                grna_ls.append('error')
            else:
                seq_ls.append(found_grna[0])
                grna_ls.append(found_grna[1])
    grna_dict = dict(zip(seq_ls, grna_ls))
    df = df.assign(grna_seq=df['seq'].map(grna_dict).fillna('error'))
    print(f'', flush=True)
    return df

def map_unmapped_grnas(df):
    print('==== Mapping lost gRNA barecodes ====')
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()
    index = 0
    print_every = 100
    sequence_list = df[df['grna_seq'] != 'error']['seq'].unique().tolist()
    grna_error = df[df['grna_seq']=='error']
    df = grna_error.copy()
    similarity_dict = {}
    #change this so that it itterates throug each well
    for idx, row in df.iterrows():
        matches = 0
        match_string = None
        for string in sequence_list:
            index += 1
            if index % print_every == 0:
                print(f'Processed reads: {index}', end='\r', flush=True)
            ratio = similar(row['seq'], string)
            # check if only one character is different
            if ratio > ((len(row['seq']) - 1) / len(row['seq'])):
                matches += 1
                if matches > 1: # if we find more than one match, we break and don't add anything to the dictionary
                    break
                match_string = string
        if matches == 1: # only add to the dictionary if there was exactly one match
            similarity_dict[row['seq']] = match_string
    return similarity_dict

def translate_barecodes(df, grna_df, map_unmapped=False):
    print('==== Translating barecodes ====')
    if map_unmapped:
        similarity_dict = map_unmapped_grnas(df)
        df = df.assign(seq=df['seq'].map(similarity_dict).fillna('error'))
    df = df.groupby(['plate','row', 'col'])['grna_seq'].value_counts().reset_index(name='count')
    grna_dict = grna_df.set_index('Seq')['gene'].to_dict()
    
    plate_barcodes = {'AA':'p1','TT':'p2','CC':'p3','GG':'p4','AT':'p5','TA':'p6','CG':'p7','GC':'p8'}
    
    row_barcodes = {'AA':'r1','AT':'r2','AC':'r3','AG':'r4','TT':'r5','TA':'r6','TC':'r7','TG':'r8',
                    'CC':'r9','CA':'r10','CT':'r11','CG':'r12','GG':'r13','GA':'r14','GT':'r15','GC':'r16'}
    
    col_barcodes = {'AAA':'c1','TTT':'c2','CCC':'c3','GGG':'c4','AAT':'c5','AAC':'c6','AAG':'c7',
                    'TTA':'c8','TTC':'c9','TTG':'c10','CCA':'c11','CCT':'c12','CCG':'c13','GGA':'c14',
                    'CCT':'c15','GGC':'c16','ATT':'c17','ACC':'c18','AGG':'c19','TAA':'c20','TCC':'c21',
                    'TGG':'c22','CAA':'c23','CGG':'c24'}

    
    df['plate'] = df['plate'].map(plate_barcodes)
    df['row'] = df['row'].map(row_barcodes)
    df['col'] = df['col'].map(col_barcodes)
    df['grna'] = df['grna_seq'].map(grna_dict)
    df['gene'] = df['grna'].str.split('_').str[1]
    df = df.fillna('error')
    df['prc'] = df['plate']+'_'+df['row']+'_'+df['col']
    df = df[df['count']>=2]
    error_count = df[df.apply(lambda row: row.astype(str).str.contains('error').any(), axis=1)].shape[0]
    plate_error = df['plate'].str.contains('error').sum()/len(df)
    row_error = df['row'].str.contains('error').sum()/len(df)
    col_error = df['col'].str.contains('error').sum()/len(df)
    grna_error = df['grna'].str.contains('error').sum()/len(df)
    print(f'Matched: {len(df)} rows; Errors: plate:{plate_error*100:.3f}% row:{row_error*100:.3f}% column:{col_error*100:.3f}% gRNA:{grna_error*100:.3f}%')
    return df

def vert_horiz(v, h, n_col):
    h = h+1
    if h not in [*range(0,n_col)]:
        v = v+1
        h = 0
    return v,h
                                            
def plot_data(df, v, h, color, n_col, ax, x_axis, y_axis, fontsize=12, lw=2, ls='-', log_x=False, log_y=False, title=None):
    ax[v, h].plot(df[x_axis], df[y_axis], ls=ls, lw=lw, color=color, label=y_axis)
    ax[v, h].set_title(None)
    ax[v, h].set_xlabel(None)
    ax[v, h].set_ylabel(None)
    ax[v, h].legend(fontsize=fontsize)
    
    if log_x:
        ax[v, h].set_xscale('log')
    if log_y:
        ax[v, h].set_yscale('log')
    v,h =vert_horiz(v, h, n_col)
    return v, h  

def test_error(df, min_=25,max_=3025, metric='count',log_x=False, log_y=False):
    max_ = max_+min_
    step = math.sqrt(min_)
    plate_error_ls = []
    col_error_ls = []
    row_error_ls = []
    grna_error_ls = []
    prc_error_ls = []
    total_error_ls = []
    temp_len_ls = []
    val_ls = []
    df['sum_count'] = df.groupby('prc')['count'].transform('sum')
    df['fraction'] = df['count'] / df['sum_count']
    if metric=='fraction':
        range_ = np.arange(min_, max_, step).tolist()
    if metric=='count':
        range_ = [*range(int(min_),int(max_),int(step))]
    for val in range_:
        temp = pd.DataFrame(df[df[metric]>val])
        temp_len = len(temp)
        if temp_len == 0:
            break
        temp_len_ls.append(temp_len)
        error_count = temp[temp.apply(lambda row: row.astype(str).str.contains('error').any(), axis=1)].shape[0]/len(temp)
        plate_error = temp['plate'].str.contains('error').sum()/temp_len
        row_error = temp['row'].str.contains('error').sum()/temp_len
        col_error = temp['col'].str.contains('error').sum()/temp_len
        prc_error = temp['prc'].str.contains('error').sum()/temp_len
        grna_error = temp['gene'].str.contains('error').sum()/temp_len
        #print(error_count, plate_error, row_error, col_error, prc_error, grna_error)
        val_ls.append(val)
        total_error_ls.append(error_count)
        plate_error_ls.append(plate_error)
        row_error_ls.append(row_error)
        col_error_ls.append(col_error)
        prc_error_ls.append(prc_error)
        grna_error_ls.append(grna_error)
    df2 = pd.DataFrame()
    df2['val'] = val_ls
    df2['plate'] = plate_error_ls
    df2['row'] = row_error_ls
    df2['col'] = col_error_ls
    df2['gRNA'] = grna_error_ls
    df2['prc'] = prc_error_ls
    df2['total'] = total_error_ls
    df2['len'] = temp_len_ls
                                 
    n_row, n_col = 2, 7
    v, h, lw, ls, color = 0, 0, 1, '-', 'teal'
    fig, ax = plt.subplots(n_row, n_col, figsize=(n_col*5, n_row*5))
    
    v, h = plot_data(df=df2, v=v, h=h, color=color, n_col=n_col, ax=ax, x_axis='val', y_axis='total',log_x=log_x, log_y=log_y)
    v, h = plot_data(df=df2, v=v, h=h, color=color, n_col=n_col, ax=ax, x_axis='val', y_axis='prc',log_x=log_x, log_y=log_y)
    v, h = plot_data(df=df2, v=v, h=h, color=color, n_col=n_col, ax=ax, x_axis='val', y_axis='plate',log_x=log_x, log_y=log_y)
    v, h = plot_data(df=df2, v=v, h=h, color=color, n_col=n_col, ax=ax, x_axis='val', y_axis='row',log_x=log_x, log_y=log_y)
    v, h = plot_data(df=df2, v=v, h=h, color=color, n_col=n_col, ax=ax, x_axis='val', y_axis='col',log_x=log_x, log_y=log_y)
    v, h = plot_data(df=df2, v=v, h=h, color=color, n_col=n_col, ax=ax, x_axis='val', y_axis='gRNA',log_x=log_x, log_y=log_y)
    v, h = plot_data(df=df2, v=v, h=h, color=color, n_col=n_col, ax=ax, x_axis='val', y_axis='len',log_x=log_x, log_y=log_y)
    
def generate_fraction_map(df, gene_column, min_=10, plates=['p1','p2','p3','p4'], metric = 'count', plot=False):
    df['prcs'] = df['prc']+''+df['grna_seq']
    df['gene'] = df['grna'].str.split('_').str[1]
    if metric == 'count':
        df = pd.DataFrame(df[df['count']>min_])
    df = df[~(df == 'error').any(axis=1)]
    df = df[df['plate'].isin(plates)]
    gRNA_well_count = df.groupby('prc')['prcs'].transform('nunique')
    df['gRNA_well_count'] = gRNA_well_count
    df = df[df['gRNA_well_count']>=2]
    df = df[df['gRNA_well_count']<=100]
    well_sum = df.groupby('prc')['count'].transform('sum')
    df['well_sum'] = well_sum
    df['gRNA_fraction'] = df['count']/df['well_sum']
    if metric == 'fraction':
        df = pd.DataFrame(df[df['gRNA_fraction']>=min_])
        df = df[df['plate'].isin(plates)]
        gRNA_well_count = df.groupby('prc')['prcs'].transform('nunique')
        df['gRNA_well_count'] = gRNA_well_count
        well_sum = df.groupby('prc')['count'].transform('sum')
        df['well_sum'] = well_sum
        df['gRNA_fraction'] = df['count']/df['well_sum']
    if plot:
        print('gRNAs/well')
        plot_plates(df=df, variable='gRNA_well_count', grouping='mean', min_max='allq', cmap='viridis')
        print('well read sum')
        plot_plates(df=df, variable='well_sum', grouping='mean', min_max='allq', cmap='viridis')
    genes = df[gene_column].unique().tolist()
    wells = df['prc'].unique().tolist()
    print('numer of genes:',len(genes),'numer of wells:', len(wells))
    independent_variables = pd.DataFrame(columns=genes, index = wells)
    for index, row in df.iterrows():
        prc = row['prc']
        gene = row[gene_column]
        fraction = row['gRNA_fraction']
        independent_variables.loc[prc,gene]=fraction
    independent_variables = independent_variables.fillna(0.0)
    independent_variables['sum'] = independent_variables.sum(axis=1)
    independent_variables = independent_variables[independent_variables['sum']==1.0]
    independent_variables = independent_variables.drop('sum', axis=1)
    independent_variables.index.name = 'prc'
    independent_variables = independent_variables.loc[:, (independent_variables.sum() != 0)]
    return independent_variables

# Check if filename or path
def split_filenames(df, filename_column):
    plate_ls = []
    well_ls = []
    col_ls = []
    row_ls = []
    field_ls = []
    obj_ls = []
    ls = df[filename_column].tolist()
    if '/' in ls[0]:
        file_list = [os.path.basename(path) for path in ls] 
    else:
        file_list = ls
    print('first file',file_list[0])
    for filename in file_list:
        plate = filename.split('_')[0]
        plate = plate.split('plate')[1]
        well = filename.split('_')[1]
        field = filename.split('_')[2]
        object_nr = filename.split('_')[3]
        object_nr = object_nr.split('.')[0]
        object_nr = 'o'+str(object_nr)
        if re.match('A..', well):
            row = 'r1'
        if re.match('B..', well):
            row = 'r2'
        if re.match('C..', well):
            row = 'r3'
        if re.match('D..', well):
            row = 'r4'
        if re.match('E..', well):
            row = 'r5'
        if re.match('F..', well):
            row = 'r6'
        if re.match('G..', well):
            row = 'r7'
        if re.match('H..', well):
            row = 'r8'
        if re.match('I..', well):
            row = 'r9'
        if re.match('J..', well):
            row = 'r10'
        if re.match('K..', well):
            row = 'r11'
        if re.match('L..', well):
            row = 'r12'
        if re.match('M..', well):
            row = 'r13'
        if re.match('N..', well):
            row = 'r14'
        if re.match('O..', well):
            row = 'r15'
        if re.match('P..', well):
            row = 'r16'
        if re.match('.01', well):
            col = 'c1'
        if re.match('.02', well):
            col = 'c2'
        if re.match('.03', well):
            col = 'c3'
        if re.match('.04', well):
            col = 'c4'
        if re.match('.05', well):
            col = 'c5'
        if re.match('.06', well):
            col = 'c6'
        if re.match('.07', well):
            col = 'c7'
        if re.match('.08', well):
            col = 'c8'
        if re.match('.09', well):
            col = 'c9'
        if re.match('.10', well):
            col = 'c10'
        if re.match('.11', well):
            col = 'c11'
        if re.match('.12', well):
            col = 'c12'
        if re.match('.13', well):
            col = 'c13'
        if re.match('.14', well):
            col = 'c14'
        if re.match('.15', well):
            col = 'c15'
        if re.match('.16', well):
            col = 'c16'
        if re.match('.17', well):
            col = 'c17'
        if re.match('.18', well):
            col = 'c18'
        if re.match('.19', well):
            col = 'c19'
        if re.match('.20', well):
            col = 'c20'
        if re.match('.21', well):
            col = 'c21'
        if re.match('.22', well):
            col = 'c22'
        if re.match('.23', well):
            col = 'c23'
        if re.match('.24', well):
            col = 'c24'
        plate_ls.append(plate)
        well_ls.append(well)
        field_ls.append(field)
        obj_ls.append(object_nr)
        row_ls.append(row)
        col_ls.append(col)
    df['file'] = ls
    df['plate'] = plate_ls
    df['well'] = well_ls
    df['row'] = row_ls
    df['col'] = col_ls
    df['field'] = field_ls
    df['obj'] = obj_ls
    df['plate_well'] = df['plate']+'_'+df['well']
    df = df.set_index(filename_column)
    return df

def rename_plate_metadata(df):
    try:
        df = df.drop(['plateID'], axis=1)
        df = df.drop(['rowID'], axis=1)
        df = df.drop(['columnID'], axis=1)
        df = df.drop(['plate_row_col'], axis=1)
        df = df.drop(['Unnamed: 0'], axis=1)
        df = df.drop(['Unnamed: 0.1'], axis=1)
    except:
        next
    
    df['plate'] = df['plate'].astype('string')
    df.plate.replace('1', 'A', inplace=True)
    df.plate.replace('2', 'B', inplace=True)
    df.plate.replace('3', 'C', inplace=True)
    df.plate.replace('4', 'D', inplace=True)
    df.plate.replace('5', 'E', inplace=True)
    df.plate.replace('6', 'F', inplace=True)
    df.plate.replace('7', 'G', inplace=True)
    df.plate.replace('8', 'H', inplace=True)
    df.plate.replace('9', 'I', inplace=True)
    df.plate.replace('10', 'J', inplace=True)

    df.plate.replace('A', 'p1', inplace=True)# 1 - 1
    df.plate.replace('B', 'p2', inplace=True)# 2 - 2
    df.plate.replace('C', 'p3', inplace=True)# 3 - 3
    df.plate.replace('E', 'p4', inplace=True)# 5 - 4
    
    df.plate.replace('F', 'p5', inplace=True)# 6 - 5
    df.plate.replace('G', 'p6', inplace=True)# 7 - 6
    df.plate.replace('H', 'p7', inplace=True)# 8 - 7
    df.plate.replace('I', 'p8', inplace=True)# 9 - 8
    
    df['plateID'] = df['plate']
    
    df.loc[(df['plateID'].isin(['D'])) & (df['col'].isin(['c1', 'c2', 'c3'])), 'plate'] = 'p1'
    df.loc[(df['plateID'].isin(['D'])) & (df['col'].isin(['c4', 'c5', 'c6'])), 'plate'] = 'p2'
    df.loc[(df['plateID'].isin(['D'])) & (df['col'].isin(['c7', 'c8', 'c9'])), 'plate'] = 'p3'
    df.loc[(df['plateID'].isin(['D'])) & (df['col'].isin(['c10', 'c11', 'c12'])), 'plate'] = 'p4'
    
    df.loc[(df['plateID'].isin(['J'])) & (df['col'].isin(['c1', 'c2', 'c3'])), 'plate'] = 'p5'
    df.loc[(df['plateID'].isin(['J'])) & (df['col'].isin(['c4', 'c5', 'c6'])), 'plate'] = 'p6'
    df.loc[(df['plateID'].isin(['J'])) & (df['col'].isin(['c7', 'c8', 'c9'])), 'plate'] = 'p7'
    df.loc[(df['plateID'].isin(['J'])) & (df['col'].isin(['c10', 'c11', 'c12'])), 'plate'] = 'p8'
    
    df.loc[(df['plateID'].isin(['D', 'J'])) & (df['col'].isin(['c1', 'c4', 'c7', 'c10'])), 'col'] = 'c1'
    df.loc[(df['plateID'].isin(['D', 'J'])) & (df['col'].isin(['c2', 'c5', 'c8', 'c11'])), 'col'] = 'c2'
    df.loc[(df['plateID'].isin(['D', 'J'])) & (df['col'].isin(['c3', 'c6', 'c9', 'c12'])), 'col'] = 'c3'
    
    df.loc[(~df['plateID'].isin(['D', 'J'])) & (df['col'].isin(['c1'])), 'col'] = 'c25'
    df.loc[(~df['plateID'].isin(['D', 'J'])) & (df['col'].isin(['c2'])), 'col'] = 'c26'
    df.loc[(~df['plateID'].isin(['D', 'J'])) & (df['col'].isin(['c3'])), 'col'] = 'c27'
    
    df.loc[(~df['plateID'].isin(['D', 'J'])) & (df['col'].isin(['c1'])), 'col'] = 'c25'

    df = df.drop(['plateID'], axis=1)
    
    df = df.loc[~df['plate'].isin(['D', 'J'])]

    screen_cols = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','c21','c22','c23','c24']
    screen_plates = ['p1','p2','p3','p4']
    positive_control_plates = ['p5','p6','p7','p8']
    positive_control_cols = screen_cols
    negative_control_cols = ['c25','c26','c27']
    #extra_plates = ['p9','p10']
    cond_ls = []

    cols = df.col.tolist()
    for index, plate in enumerate(df.plate.tolist()):
        co = cols[index]
        if plate in screen_plates:
            if co in screen_cols:
                cond = 'SCREEN'
            if co in negative_control_cols:
                cond = 'NC'
        if plate in positive_control_plates:
            if co in positive_control_cols:
                cond = 'PC'
            if co in negative_control_cols:
                cond = 'NC'
        cond_ls.append(cond)
        
    df['cond'] = cond_ls
    df['plate'] = df['plate'].astype('string')
    df['row'] = df['row'].astype('string')
    df['col'] = df['col'].astype('string')
    df['obj'] = df['obj'].astype('string')
    df['prco'] = df['plate']+'_'+df['row']+'_'+df['col']+'_'+df['field']+'_'+df['obj']
    df['prc'] = df['plate']+'_'+df['row']+'_'+df['col']
    df = df.set_index(['prco'], drop=True)
    df = df.sort_values(by = ['plate'], ascending = [True], na_position = 'first')
    values, counts = np.unique(df['plate'], return_counts=True)
    print('plates:', values)
    print('well count:', counts)
    return df

def plot_reg_res(df, coef_col='coef', col_p='P>|t|'):
    df['gene'] = df.index
    df[coef_col] = pd.to_numeric(df[coef_col], errors='coerce')
    df[col_p] = pd.to_numeric(df[col_p], errors='coerce')
    df = df.sort_values(by = [coef_col], ascending = [False], na_position = 'first')
    df['color'] = 'None'
    df.loc[df['gene'].str.contains('239740'), 'color'] = '239740'
    df.loc[df['gene'].str.contains('205250'), 'color'] = '205250'
    
    df.loc[df['gene'].str.contains('000000'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000001'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000002'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000003'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000004'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000005'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000006'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000007'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000008'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000009'), 'color'] = '000000'
    df.loc[df['gene'].str.contains('000010'), 'color'] = '000000'
    fig, ax = plt.subplots(figsize=(10,10))
    df.loc[df[col_p] == 0.000, col_p] = 0.001
    df['logp'] = -np.log10(df[col_p])
    sns.scatterplot(data = df, x = coef_col, y = 'logp', legend = False, ax = ax,
                    hue= 'color', hue_order = ['239740','205250','None', '000000'],
                    palette = ['purple', 'teal', 'lightgrey', 'black'],
                    size = 'color', sizes = (100, 10))
    g14 = df[df['gene'].str.contains('239740')]
    r18 = df[df['gene'].str.contains('205250')]
    res = pd.concat([g14, r18], axis=0)
    res = res[[coef_col, col_p]]
    print(res)
    return df, res

def reg_model(iv_loc,dv_loc):
    independent_variables = pd.read_csv(iv_loc)
    dependent_variable = pd.read_csv(dv_loc)
    independent_variables = independent_variables.set_index('prc')
    columns = independent_variables.columns
    new_columns = [col.replace('TGGT1_', '') for col in columns]
    independent_variables.columns = new_columns

    dependent_variable = dependent_variable.set_index('prc')

    reg_input = pd.DataFrame(pd.merge(independent_variables, dependent_variable, left_index=True, right_index=True))
    reg_input = reg_input.dropna(axis=0, how='any')
    reg_input = reg_input.dropna(axis=1, how='any')
    print('Number of wells',len(reg_input))
    x = reg_input.drop(['score'], axis=1)
    x = sm.add_constant(x)
    y = np.log10(reg_input['score']+1)
    model = sm.OLS(y, x).fit()
    predictions = model.predict(x)
    results_summary = model.summary()
    print(results_summary)
    results_as_html = results_summary.tables[1].as_html()
    results_df = pd.read_html(results_as_html, header=0, index_col=0)[0]
    df, res = plot_reg_res(df=results_df)
    return df, res

def mixed_model(iv_loc,dv_loc):
    independent_variables = pd.read_csv(iv_loc)
    dependent_variable = pd.read_csv(dv_loc)
    independent_variables = independent_variables.set_index('prc')
    columns = independent_variables.columns
    new_columns = [col.replace('TGGT1_', '') for col in columns]
    independent_variables.columns = new_columns
    dependent_variable = dependent_variable.set_index('prc')
    reg_input = pd.DataFrame(pd.merge(independent_variables, dependent_variable, left_index=True, right_index=True))
    reg_input = reg_input.dropna(axis=0, how='any')

    y = np.log10(reg_input['score']+1)
    X = reg_input.drop('score', axis=1)
    X.columns = pd.MultiIndex.from_tuples([tuple(col.split('_')) for col in X.columns],
                                          names=['main_variable', 'sub_variable'])
    # Melt the DataFrame
    X_long = X.melt(ignore_index=False, var_name=['main_variable', 'sub_variable'], value_name='value')
    X_long = X_long[X_long['value']>0]

    # Create a new column to represent the nested structure of gRNA within gene
    X_long['gene_gRNA'] = X_long['main_variable'].astype(str) + "_" + X_long['sub_variable'].astype(str)

    # Add 'score' to the DataFrame
    X_long['score'] = y

    # Create and convert the plate, row, and column variables to type category
    X_long.reset_index(inplace=True)  
    split_values = X_long['prc'].str.split('_', expand=True)
    X_long[['plate', 'row', 'col']] = split_values
    X_long['plate'] = X_long['plate'].str[1:]
    X_long['plate'] = X_long['plate'].astype(int)
    X_long['row'] = X_long['row'].str[1:]
    X_long['row'] = X_long['row'].astype(int)
    X_long['col'] = X_long['col'].str[1:]
    X_long['col'] = X_long['col'].astype(int)
    X_long = X_long.set_index('prc')
    # Create a new column to represent the nested structure of plate, row, and column
    X_long['plate_row_col'] = X_long['plate'].astype(str) + "_" + X_long['row'].astype(str) + "_" + X_long['col'].astype(str)
    n_group = pd.DataFrame(X_long.groupby(['gene_gRNA']).count()['main_variable'])
    n_group = n_group.rename({'main_variable': 'n_group'}, axis=1)
    n_group = n_group.reset_index(drop=False)
    X_long = pd.merge(X_long, n_group, on='gene_gRNA')
    X_long = X_long[X_long['n_group']>1]
    #print(X_long.isna().sum())
    
    X_long['main_variable'] = X_long['main_variable'].astype('category')
    X_long['sub_variable'] = X_long['sub_variable'].astype('category')
    X_long['plate'] = X_long['plate'].astype('category')
    X_long['row'] = X_long['row'].astype('category')
    X_long['col'] = X_long['col'].astype('category')
    X_long = pd.DataFrame(X_long)
    print(X_long)
    
    md = smf.mixedlm("score ~ C(main_variable)", X_long, 
                 groups=X_long["sub_variable"])
    
    # Define your nonlinear function here
    def nonlinear_function(x, *params):
        pass  # Implement non linear function here

    mdf = md.fit(method='bfgs', maxiter=1000)
    print(mdf.summary())
    summary = mdf.summary()
    df = pd.DataFrame(summary.tables[1])
    df, res = plot_reg_res(df, coef_col='Coef.', col_p='P>|z|')
    return df, res

def calculate_accuracy(df):
    df.loc[df['pc_score'] <= 0.5, 'pred'] = 0
    df.loc[df['pc_score'] >= 0.5, 'pred'] = 1
    df.loc[df['cond'] == 'NC', 'lab'] = 0
    df.loc[df['cond'] == 'PC', 'lab'] = 1
    df = df[df['cond'] != 'SCREEN']
    df_nc = df[df['cond'] != 'NC']
    df_pc = df[df['cond'] != 'PC']
    correct = []
    all_ls = []
    pred_list = df['pred'].tolist()
    lab_list = df['lab'].tolist()
    for i,v in enumerate(pred_list):
        all_ls.append(1)
        if v == lab_list[i]:
            correct.append(1)
    print('total accuracy',len(correct)/len(all_ls))
    correct = []
    all_ls = []
    pred_list = df_pc['pred'].tolist()
    lab_list = df_pc['lab'].tolist()
    for i,v in enumerate(pred_list):
        all_ls.append(1)
        if v == lab_list[i]:
            correct.append(1)
    print('positives accuracy', len(correct)/len(all_ls))
    correct = []
    all_ls = []
    pred_list = df_nc['pred'].tolist()
    lab_list = df_nc['lab'].tolist()
    for i,v in enumerate(pred_list):
        all_ls.append(1)
        if v == lab_list[i]:
            correct.append(1)
    print('negatives accuracy',len(correct)/len(all_ls))

def preprocess_image_data(df, resnet_loc, min_count=25, metric='mean', plot=True, score='pc_score'):
    print('number of cells', len(df))
    resnet_preds = pd.read_csv(resnet_loc)
    res_df = split_filenames(df=resnet_preds, filename_column='path')
    pred_df = rename_plate_metadata(df=res_df)
    pred_df['prcfo'] = pred_df['plate']+'_'+pred_df['row']+'_'+pred_df['col']+'_'+pred_df['field']+'_'+pred_df['obj']
    print('number of resnet scores', len(df))
    merged_df = pd.merge(df, pred_df, on='prcfo', how='inner', suffixes=('', '_right'))
    merged_df = merged_df.rename(columns={'pred': 'pc_score'})
    
    merged_df = merged_df[(merged_df['pc_score'] <= 0.25) | (merged_df['pc_score'] >= 0.75)]
    
    merged_df['recruitment'] = merged_df['Toxo_channel_1_quartiles75']/merged_df['Cytosol_channel_1_quartiles75']
    merged_df = pd.DataFrame(merged_df[merged_df['duplicates'] == 1.0])
    columns_to_drop = [col for col in merged_df.columns if col.endswith('_right')]
    merged_df = merged_df.drop(columns_to_drop, axis=1)
    well_group = pd.DataFrame(merged_df.groupby(['prc']).count()['cond'])
    well_group = well_group.rename({'cond': 'cell_count'}, axis=1)
    merged_df = pd.merge(merged_df, well_group, on='prc', how='inner', suffixes=('', '_right'))
    columns_to_drop = [col for col in merged_df.columns if col.endswith('_right')]
    merged_df = merged_df.drop(columns_to_drop, axis=1)
    #merged_df = merged_df.drop(['duplicates', 'outlier', 'prcfo.1'], axis=1)
    merged_df = merged_df.drop(['duplicates', 'prcfo.1'], axis=1)
    merged_df = pd.DataFrame(merged_df[merged_df['cell_count'] >= min_count])
    
    if metric == 'mean':
        well_scores_score = pd.DataFrame(merged_df.groupby(['prc']).mean()['pc_score'])
        well_scores_score = well_scores_score.rename({'pc_score': 'mean_pc_score'}, axis=1)
        well_scores_rec = pd.DataFrame(merged_df.groupby(['prc']).mean()['recruitment'])
        well_scores_rec = well_scores_rec.rename({'recruitment': 'mean_recruitment'}, axis=1)
    if metric == 'geomean':
        well_scores_score = pd.DataFrame(merged_df.groupby(['prc'])['pc_score'].apply(gmean))
        well_scores_score = well_scores_score.rename({'pc_score': 'mean_pc_score'}, axis=1)
        well_scores_rec = pd.DataFrame(merged_df.groupby(['prc'])['recruitment'].apply(gmean))
        well_scores_rec = well_scores_rec.rename({'recruitment': 'mean_recruitment'}, axis=1)
    if metric == 'median':
        well_scores_score = pd.DataFrame(merged_df.groupby(['prc']).median()['pc_score'])
        well_scores_score = well_scores_score.rename({'pc_score': 'mean_pc_score'}, axis=1)
        well_scores_rec = pd.DataFrame(merged_df.groupby(['prc']).median()['recruitment'])
        well_scores_rec = well_scores_rec.rename({'recruitment': 'mean_recruitment'}, axis=1)
    if metric == 'quntile':
        well_scores_score = pd.DataFrame(merged_df.groupby(['prc']).quantile(0.75)['pc_score'])
        well_scores_score = well_scores_score.rename({'pc_score': 'mean_pc_score'}, axis=1)
        well_scores_rec = pd.DataFrame(merged_df.groupby(['prc']).quantile(0.75)['recruitment'])
        well_scores_rec = well_scores_rec.rename({'recruitment': 'mean_recruitment'}, axis=1)
    well = pd.DataFrame(pd.DataFrame(merged_df.select_dtypes(include=['object'])).groupby(['prc']).first())
    well['mean_pc_score'] = well_scores_score['mean_pc_score']
    well['mean_recruitment'] = well_scores_rec['mean_recruitment']
    nc = well[well['cond'] == 'NC']
    max_nc = nc['mean_recruitment'].max()
    pc = well[well['cond'] == 'PC']
    screen = well[well['cond'] == 'SCREEN']
    screen = screen[screen['mean_recruitment'] <= max_nc]
    if plot:
        x_axis = 'mean_pc_score'
        fig, ax = plt.subplots(1,3,figsize=(30,10))
        sns.histplot(data=nc, x=x_axis, kde=False, stat='density', element="step", ax=ax[0], color='lightgray', log_scale=False)
        sns.histplot(data=pc, x=x_axis, kde=False, stat='density', element="step", ax=ax[0], color='teal', log_scale=False)
        sns.histplot(data=screen, x=x_axis, kde=False, stat='density', element="step", ax=ax[1], color='purple', log_scale=False)
        sns.histplot(data=nc, x=x_axis, kde=False, stat='density', element="step", ax=ax[2], color='lightgray', log_scale=False)
        sns.histplot(data=pc, x=x_axis, kde=False, stat='density', element="step", ax=ax[2], color='teal', log_scale=False)
        sns.histplot(data=screen, x=x_axis, kde=False, stat='density', element="step", ax=ax[2], color='purple', log_scale=False)
        ax[0].set_title('NC vs PC wells')
        ax[1].set_title('Screen wells')
        ax[2].set_title('NC vs PC vs Screen wells')
        ax[0].spines['top'].set_visible(False)
        ax[0].spines['right'].set_visible(False)
        ax[1].spines['top'].set_visible(False)
        ax[1].spines['right'].set_visible(False)
        ax[2].spines['top'].set_visible(False)
        ax[2].spines['right'].set_visible(False)
        ax[0].set_xlim([0, 1])
        ax[1].set_xlim([0, 1])
        ax[2].set_xlim([0, 1])
        loc = '/media/olafsson/umich/matt_graphs/resnet_score_well_av.pdf'
        fig.savefig(loc, dpi = 600, format='pdf', bbox_inches='tight')
        x_axis = 'mean_recruitment'
        fig, ax = plt.subplots(1,3,figsize=(30,10))
        sns.histplot(data=nc, x=x_axis, kde=False, stat='density', element="step", ax=ax[0], color='lightgray', log_scale=False)
        sns.histplot(data=pc, x=x_axis, kde=False, stat='density', element="step", ax=ax[0], color='teal', log_scale=False)
        sns.histplot(data=screen, x=x_axis, kde=False, stat='density', element="step", ax=ax[1], color='purple', log_scale=False)
        sns.histplot(data=nc, x=x_axis, kde=False, stat='density', element="step", ax=ax[2], color='lightgray', log_scale=False)
        sns.histplot(data=pc, x=x_axis, kde=False, stat='density', element="step", ax=ax[2], color='teal', log_scale=False)
        sns.histplot(data=screen, x=x_axis, kde=False, stat='density', element="step", ax=ax[2], color='purple', log_scale=False)
        ax[0].set_title('NC vs PC wells')
        ax[1].set_title('Screen wells')
        ax[2].set_title('NC vs PC vs Screen wells')
        ax[0].spines['top'].set_visible(False)
        ax[0].spines['right'].set_visible(False)
        ax[1].spines['top'].set_visible(False)
        ax[1].spines['right'].set_visible(False)
        ax[2].spines['top'].set_visible(False)
        ax[2].spines['right'].set_visible(False)
        loc = '/media/olafsson/umich/matt_graphs/mean_recruitment_well_av.pdf'
        fig.savefig(loc, dpi = 600, format='pdf', bbox_inches='tight')
    plates = ['p1','p2','p3','p4']
    screen = screen[screen['plate'].isin(plates)]
    if score == 'pc_score':
        dv = pd.DataFrame(screen['mean_pc_score'])
        dv = dv.rename({'mean_pc_score': 'score'}, axis=1)
    if score == 'recruitment':
        dv = pd.DataFrame(screen['mean_recruitment'])
        dv = dv.rename({'mean_recruitment': 'score'}, axis=1)
    print('dependant variable well count:', len(well))
    dv_loc = '/media/olafsson/Data2/methods_paper/data/dv.csv'
    dv.to_csv(dv_loc)
    calculate_accuracy(df=merged_df)
    return merged_df, well