import numpy as np
import pandas as pd
def tree_to_decision_table(tree_classifier, feature_names, class_names):
   
    def update_bounds(current_bounds, threshold, is_left):
        
        lower_bound, upper_bound = current_bounds
        if is_left:
            return (lower_bound, min(upper_bound, threshold))
        else:
            return (max(lower_bound, threshold), upper_bound)

    
    def format_rule(lower_bound, upper_bound):

        if lower_bound == float('-inf') and upper_bound == float('inf'):
            return "-"
        elif lower_bound == float('-inf'):
            return f"<= {upper_bound:.2f}"
        elif upper_bound == float('inf'):
            return f"> {lower_bound:.2f}"
        else:
            return f"({lower_bound:.2f}; {upper_bound:.2f}]"


    tree_ = tree_classifier.tree_
    feature = tree_.feature
    threshold = tree_.threshold
    children_left = tree_.children_left
    children_right = tree_.children_right
    value = tree_.value

    decision_paths = []
    bounds = {fn: (float('-inf'), float('inf')) for fn in feature_names}

    def traverse(node, current_rule):
        if feature[node] == -2:  # Leaf node
            predictions = value[node][0]
            predicted_class = class_names[np.argmax(predictions)]
            formatted_rule = {k: format_rule(*v) for k, v in current_rule.items()}
            decision_paths.append({**formatted_rule, 'Class': predicted_class})
        else:
            name = feature_names[feature[node]]
            thres = threshold[node]
            left_bounds = update_bounds(current_rule.get(name, (float('-inf'), float('inf'))), thres, True)
            right_bounds = update_bounds(current_rule.get(name, (float('-inf'), float('inf'))), thres, False)

            left_rule = current_rule.copy()
            right_rule = current_rule.copy()
            left_rule[name] = left_bounds
            right_rule[name] = right_bounds

            traverse(children_left[node], left_rule)
            traverse(children_right[node], right_rule)

    traverse(0, bounds)
    decision_table = pd.DataFrame(decision_paths)
    decision_table.fillna('-', inplace=True)
    columns_sorted = [col for col in feature_names if col in decision_table] + ['Class']
    decision_table = decision_table.reindex(columns=columns_sorted)

    return decision_table.T
