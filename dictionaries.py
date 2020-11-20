rally_shots = [
    
    'f', 'r', 'v', 'u', 'l', 'h', 'j', 'o',  
    'b', 's', 'z', 'y', 'm', 'i', 'k', 'p',
    't', 'q', '@'
    
]

failure = [ 'n', 'w', 'd', 'x', 'g', 'e', '!', 'V' ]

shot_dir = [ '1', '2', '3' ]

sv_dir = ['4', '5', '6']

ret_dir = ['7', '8', '9']

match_attributes = [ 'hard', 'clay', 'grass', 'gender' ]

misc_attributes = [ 'svr', 'pt_wr', 'gm_wr' ]

misc_attributes_player = ['+', 'hnd', 'fr', 'fsr', 'swr', 'ssr'] 

labels = [ 'match_wr', 'match_win', 'set_wr', 'set_win' ]

player_attributes = rally_shots + shot_dir + sv_dir + ret_dir + misc_attributes_player

attr_keys = misc_attributes + [s + '0' for s in player_attributes] + [s + '1' for s in player_attributes] + match_attributes
labl_keys = labels

all_keys = attr_keys + labl_keys