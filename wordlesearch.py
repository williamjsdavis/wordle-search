from collections import Counter
from itertools import compress
from operator import not_

"""
Dictionary comparison
"""
class DictComp:
    def __init__(self, l_dict):
        self.l_dict = l_dict
    def comparison(self, l_cand, comp_type):
        if comp_type == 'modal':
            return self.comparison_modal(l_cand)
        elif comp_type == 'sum':
            return self.comparison_sum(l_cand)
        elif comp_type == 'mean':
            return self.comparison_mean(l_cand)
        elif comp_type == 'max_green':
            return self.comparison_green(l_cand)
        elif comp_type == 'max_orange':
            return self.comparison_orange(l_cand)
        else:
            Raise ValueError('Comparison type not recognised.')
    def comparison_modal(self, l_cand):
        return self.comparison_over_list(l_cand, 
                                         most_common_match, 
                                         lexicographic_equality, 
                                         lexicographic_greaterthan)
    def comparison_sum(self, l_cand):
        return self.comparison_over_list(l_cand, 
                                         sum_match, 
                                         sum_equality, 
                                         sum_greaterthan)
    def comparison_mean(self, l_cand):
        return self.comparison_over_list(l_cand, 
                                         mean_match, 
                                         sum_equality, 
                                         sum_greaterthan)
    def comparison_green(self, l_cand):
        return self.comparison_over_list(l_cand, 
                                         meanmax_green, 
                                         sum_equality, 
                                         sum_greaterthan)
    def comparison_orange(self, l_cand):
        return self.comparison_over_list(l_cand, 
                                         meanmax_orange, 
                                         sum_equality, 
                                         sum_greaterthan)
    def comparison_over_list(self, l_cand, m_comp, m_eq, m_gr):
        scores_cand = map(lambda s: combined_score_map(self.l_dict, s), l_cand)
        metrics_cand = map(m_comp, scores_cand)
        metrics_cand = list(metrics_cand)
        
        running_best_val = metrics_cand[0]
        running_best_dict = {}
        for (i,v) in enumerate(metrics_cand):
            if m_gr(v, running_best_val):
                # Replace and add
                running_best_val = v
                running_best_dict = {l_cand[i] : v}
            elif m_eq(v, running_best_val):
                # Add to dict
                running_best_dict[l_cand[i]] = v
        return running_best_dict

# Modal method
def most_common_match(score_map):
    return Counter(score_map).most_common(1)[0]
def combined_score_most_common_match(l, s):
    score_map = combined_score_map(l, s)
    return most_common_match(score_map)
def lexicographic_equality(out1, out2):
    return (out1[0] == out2[0])
def lexicographic_greaterthan(out1, out2):
    return (out1[0] > out2[0])

# Sum method
def sum_match(score_map):
    return sum(map(lambda x: x[1]*sum(x[0]), dict(Counter(score_map)).items()))
def combined_score_sum_match(l, s):
    score_map = combined_score_map(l, s)
    return sum_match(score_map)
def sum_equality(out1, out2):
    return (out1 == out2)
def sum_greaterthan(out1, out2):
    return (out1 > out2)

# Mean method
def mean_match(score_map):
    score_list = list(score_map)
    return sum_match(score_list)/len(score_list)
def combined_score_mean_match(l, s):
    score_map = combined_score_map(l, s)
    return mean_match(score_map)

# Maximise green
def meanmax_green(score_map):
    score_list = list(score_map)
    score_dict = dict(Counter(score_list))
    green_sum = sum(map(lambda x: x[1]*x[0][0], score_dict.items()))
    return green_sum/len(score_list)
def combined_score_meanmax_green(l, s):
    score_map = combined_score_map(l, s)
    return meanmax_green(score_map)

# Maximise orange
def meanmax_orange(score_map):
    score_list = list(score_map)
    score_dict = dict(Counter(score_list))
    orange_sum = sum(map(lambda x: x[1]*x[0][1], score_dict.items()))
    return orange_sum/len(score_list)
def combined_score_meanmax_orange(l, s):
    score_map = combined_score_map(l, s)
    return meanmax_orange(score_map)

# Score calculator
def combined_score_map(l, s):
    greenorange_score_map = map(lambda ss: combined_score(s, ss), l)
    return greenorange_score_map
def step_1(s1, s2): # (l[i], s)
    perfect_match_mask = list(position_match(s1, s2))
    green_score = sum(perfect_match_mask)
    return green_score, perfect_match_mask
def step_2(s1, s2, mask): # (l[i], s)
    inverse_mask_string = lambda s: compress(s, map(not_, mask))
    s1_remaining = inverse_mask_string(s1)
    s2_remaining = inverse_mask_string(s2)
    orange_score = preset_match(set(s1_remaining), set(s2_remaining))
    return orange_score
def combined_score(s1, s2): # (l[i], s)
    green_score, perfect_match_mask = step_1(s1, s2)
    orange_score = step_2(s1, s2, perfect_match_mask)
    return green_score, orange_score
def position_match(s1, s2): 
    return map(lambda tup: tup[0] == tup[1], zip(s1, s2))
def preset_match(set1, set2): 
    return len(set1.intersection(set2))

    
