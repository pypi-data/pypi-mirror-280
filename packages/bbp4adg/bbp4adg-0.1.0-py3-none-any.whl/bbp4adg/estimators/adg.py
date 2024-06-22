from ..estimators import BaseADG, Logger, ArgumentationDecisionGraph
import copy
from ..utils import df_to_evaluate_list, read_data_to_pairs
from fractions import Fraction
from decimal import Decimal
import pandas as pd

class ADG(BaseADG):
    def __init__(
        self, 
        threshold=0,
        adg_best=ArgumentationDecisionGraph(set(), set()),
        perf=0, 
        early_stopping=False,
        n_iter_no_change=2,
        validation_fraction=None, 
        es_lower_limit=Fraction(Decimal('0.85')),
    ):
        self.adg_best = adg_best
        self.perf = perf
        self.threshold = threshold
        self.early_stopping = early_stopping
        self.validation_fraction = validation_fraction
        self.n_iter_no_change = n_iter_no_change
        self.es_lower_limit = es_lower_limit
        self.logger = Logger()

    # def df_to_pred_list(self, df, target_column):
    #     eval_list = []
    #     for index, row in df.iterrows():
    #         features = []
    #         y = str(row[target_column])
    #         for i in df.columns:
    #             if(i != target_column):
    #                 features.append((i, row[i]))
    #         eval_list.append((features, y))
    #     return eval_list
    
    # def predict(self, df, target_column):
    #     '''
    #     return a list of tuples: (feature_values, predicted_class) 
    #     '''
    #     evaluate_list =  self.df_to_pred_list(df, target_column)
    #     results = []
    #     for i in evaluate_list:
    #         results.append( ( i[0], predict(self.adg_best,i[0]) ) ) 
    #     return results

    def fit(self, X, y):
        '''
        df is the dataframe for training,
        target_column is the column name of the target values,
        ruleset is the dictionary of mapping target values to 0 and 1, default is to make no change when target values are already either 0 or 1
        '''
        
        df = pd.concat([X, y], axis=1)

        target_column = y.columns[0]

        # early stopping by evaluation 1 of 3
        if self.early_stopping == True:
            df_eval = df.sample(frac=0.2, random_state=200)
            df = df.drop(df_eval.index)
            X = df.drop(columns=[target_column])
            y = df[[target_column]]
            X_eval = df_eval.drop(columns=[target_column])
            y_eval = df_eval[[target_column]]
            dfeval_eval_list = df_to_evaluate_list(X_eval, y_eval)


        arg = set()
        eval_list = df_to_evaluate_list(X,y)
        fvps = read_data_to_pairs(copy.deepcopy(X))

        # print nums of args to be added
        self.logger.log(str(len(fvps)*3) + " arguments to be added", "INFO")
        # print(len(fvps)*3, "arguments to be added")

        #iterate thru fvp and add target values 0, 1, and und to fvp
        for fvp in fvps:
            arg.add((fvp, 1))
            arg.add((fvp, 0))
            arg.add((fvp, 'und'))

        # early stopping by evaluation 2 of 3
        eval_best = 0
        eval_drop_cnt = 0

        # adg_best.arguments.add((('age', 30), 0))
        while len(arg) > 0 :
            adg_old = copy.deepcopy(self.adg_best)

            del_list = set()

            cnt = 0
            for a in arg:

                # print num of a in args processed
                cnt += 1
                # print(cnt, "of", len(arg), "arguments processed")
                self.logger.log(str(cnt) + " of" + " " + str(len(arg)) + " arguments processed", "INFO")
                

                adg_new = self.add_argument(self.adg_best, a, eval_list)
                perf_new = self.evaluate_plain(adg_new, eval_list)
                # print("perf_new_bf: ", perf_new)
                self.logger.log("perf_new_bf: " + str(perf_new) , "DEBUG")
                # print("perf_th_bf: ", self.perf + self.threshold)
                self.logger.log("perf_th_bf: " + str(self.perf + self.threshold), "DEBUG")
                if perf_new > self.perf + self.threshold:
                    self.perf = perf_new
                    self.adg_best = adg_new
                    # print("perf_new: ", perf_new)
                    self.logger.log(str(cnt) + " of" + " " + str(len(arg)) + " arguments processed" + "     perf_new: " + str(perf_new), "INFO")
                    # print(self.adg_best)
                    self.logger.log(str(self.adg_best), "DEBUG")
                    # arg.remove(a)
                    del_list.add((a[0], 0))
                    del_list.add((a[0], 1))
                    del_list.add((a[0], 'und'))

                    # early stopping by evaluation 3 of 3
                    if self.early_stopping == True:
                        eval_current = self.evaluate_plain(self.adg_best, dfeval_eval_list)
                        if ( eval_best >= eval_current ) and ( eval_best >= self.es_lower_limit ):
                            eval_drop_cnt += 1
                            # print("eval_drop_cnt: ", eval_drop_cnt)
                            self.logger.log("eval_drop_cnt: " + str(eval_drop_cnt), "DEBUG")
                            if eval_drop_cnt >= self.n_iter_no_change:
                                # print("early stopping by evaluation")
                                self.logger.log("early stopping by evaluation", "DEBUG")
                                return self.adg_best, self.perf
                        elif eval_best < eval_current :
                            eval_drop_cnt = 0
                            eval_best = eval_current
                            # print("eval_best: ", eval_best)
                            self.logger.log("eval_best: " + str(eval_best), "DEBUG")

            for a in del_list:
                arg.remove(a)
            
            if (self.adg_best.arguments == adg_old.arguments) and (self.adg_best.relations == adg_old.relations):
                return self.adg_best, self.perf
            
        return self.adg_best, self.perf