from ..estimators import BaseADG, Logger, ArgumentationDecisionGraph
import numpy as np
import copy
from ..utils import df_to_evaluate_list, read_data_to_pairs


def update_weights(adg, evaluate_list, acc, model):
    aos = 0.5 * np.log(float(acc/(1-acc)))
    cw = np.exp([-1*aos])[0]
    ww = np.exp([aos])[0]

    correct = 0
    total = 0

    evaluate_list_rw = []

    for i in evaluate_list:
        if model.predict(adg, i[0]) == i[1]:
            nw = i[2] * cw
            evaluate_list_rw.append((i[0], i[1], nw))
            correct += nw
            total += nw
        else:
            nw = i[2] * ww
            evaluate_list_rw.append((i[0], i[1], nw))
            total += nw

    evaluate_list = []
    #normalize weights
    for i in evaluate_list_rw:
        evaluate_list.append( (i[0], i[1], i[2] * len(evaluate_list_rw)/total) )
    model.logger.log("evaluate_list[0]:" + str(evaluate_list[0]), 'DEBUG')
    model.logger.log("correct:" + str(correct), 'DEBUG')
    model.logger.log("total: " + str(total), 'DEBUG')
    model.logger.log("len:" + str(len(evaluate_list_rw)), 'DEBUG')
    return evaluate_list

class BBP(BaseADG):
    def __init__(
        self, 
        threshold=0,
        adg_best=ArgumentationDecisionGraph(set(), set()),
        perf=0, 
        early_stopping=False,
        validation_fraction=None, 
        n_iter_no_change=None,
        above_threshold_acc=None
    ):
        self.adg_best = adg_best
        self.perf = perf
        self.threshold = threshold
        self.early_stopping = early_stopping
        self.validation_fraction = validation_fraction
        self.n_iter_no_change = n_iter_no_change
        self.above_threshold_acc = above_threshold_acc
        self.logger = Logger()

    def fit_stage(self, adg, args, perf, eval_list, perf_plain):
        adg_base = copy.deepcopy(adg)

        adg_best = copy.deepcopy(adg)

        perf = perf

        perf_plain_best = perf_plain

        added_arg = None

        iter = 0
        for arg in args:

            adg_new = self.add_argument(adg_base, arg, eval_list)
            perf_new = self.evaluate(adg_new, eval_list)
            perf_plain_new = self.evaluate_plain(adg_new, eval_list) 
            if ( round(perf_new, 5) > round(perf, 5) ) and ( round(perf_plain_new, 5) > round(perf_plain, 5) ):
                perf = perf_new
                adg_best = adg_new
                added_arg = arg
                perf_plain_best = perf_plain_new
            iter += 1
            self.logger.log("stage: " + str(iter) + "/" + str(len(args)) + " " + str(perf_plain_best), 'INFO')

        return adg_best, perf, added_arg, perf_plain_best

    def fit_stages(self, adg, args, perf, eval_list, threshold, perf_plain):  
        
        next_adg, next_perf, added_arg, next_perf_plain= self.fit_stage(adg, args, perf, eval_list, perf_plain)

        self.logger.log("perf_new: " + str(next_perf), 'DEBUG')
        self.logger.log("added_arg: " + str(added_arg), 'DEBUG')
        self.logger.log("current adg: " + str(next_adg), 'DEBUG')
        self.logger.log("perf_plain_new: " + str(next_perf_plain), 'INFO')

        # remove added_arg
        next_args = [arg for arg in args if arg[0] != added_arg[0]]

        # stop criteria
        if len(next_args) == 0:
            return next_adg, next_perf
        if round(perf_plain,5) + threshold >= round(next_perf_plain,5):
            return next_adg, next_perf

        # update weights
        if next_perf > 0.5:
            eval_list = update_weights(next_adg, eval_list, next_perf, self)
            next_perf = float(self.evaluate(next_adg, eval_list))
            self.logger.log("perf_after_reweight: " + str(next_perf), 'DEBUG')
            self.logger.log("eval_list[0]:" + str(eval_list[0]), 'DEBUG')
        
        return self.fit_stages(next_adg, next_args, next_perf, eval_list, threshold, next_perf_plain)

    def fit(self, X, y):

        eval_list = df_to_evaluate_list(X,y)
        fvps = read_data_to_pairs(copy.deepcopy(X))
        #iterate thru fvp and add target values 0, 1, and und to args
        args = set()
        for fvp in fvps:
            args.add((fvp, 1))
            args.add((fvp, 0))
            args.add((fvp, 'und'))
        self.logger.log(self.adg_best, 'DEBUG')
        self.adg_best, self.perf = self.fit_stages(adg=self.adg_best, args=args, perf=self.perf, eval_list=eval_list, threshold=self.threshold, perf_plain=self.perf)
        return self.adg_best, self.perf