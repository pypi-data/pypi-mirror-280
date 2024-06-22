# def evaluate(adg, evaluate_list):
#     correct = 0

#     for i in evaluate_list:
#         if predict(adg, i[0]) == i[1]:
#             correct += i[2]

#     return correct/len(evaluate_list)

# def evaluate_plain(adg, evaluate_list):
#     correct = 0

#     for i in evaluate_list:
#         if predict(adg, i[0]) == i[1]:
#             correct += 1

#     return correct/len(evaluate_list)

import copy
from .semantics import verified, grounded
from ..utils import df_to_evaluate_list

class ClassifierMixin:

    def evaluate(self, adg, evaluate_list):
        correct = 0

        for i in evaluate_list:
            if self.predict(adg, i[0]) == i[1]:
                correct += i[2]

        return correct/len(evaluate_list)

    def evaluate_plain(self, adg, evaluate_list):
        correct = 0

        for i in evaluate_list:
            if self.predict(adg, i[0]) == i[1]:
                correct += 1

        return correct/len(evaluate_list)
    
    def score(self,X,y):
        return self.evaluate(self.adg_best,df_to_evaluate_list(X,y))
    
class BaseADG(ClassifierMixin):
    def add_argument(self, adg, a, eval_list):

        for b in adg.arguments:
            if hasattr(self, "logger"):
                self.logger.log('eval relations between: ' + str(a) + ' ' + str(b), 'DEBUG')
            if ((a[0][0] != b[0][0]) and (a[1] != b[1]) and (a[1] != 'und') and (b[1] != 'und')):
                adg_non = copy.deepcopy(adg)
                adg_non.arguments.add(a)
                adg_in = copy.deepcopy(adg_non)
                adg_out = copy.deepcopy(adg_non)
                adg_bi = copy.deepcopy(adg_non)
                adg_in.relations.add((a, b))
                adg_out.relations.add((b, a))
                adg_bi.relations.add((a,b))
                adg_bi.relations.add((b,a))
                # print("in relations:", adg_in.relations)
                # evaluate adg_in, adg_out, and adg_bi, return the best one of these 3
                perf_in = self.evaluate(adg_in, eval_list)
                perf_out = self.evaluate(adg_out, eval_list)
                perf_bi = self.evaluate(adg_bi, eval_list)
                if perf_in > perf_out:
                    if perf_in > perf_bi:
                        adg = adg_in
                    else:    
                        adg = adg_bi
                else:
                    if perf_out > perf_bi:
                        adg = adg_out
                    else:
                        adg = adg_bi
            elif (a[0][0] != b[0][0]):
                adg_non = copy.deepcopy(adg)
                adg_non.arguments.add(a)
                adg_in = copy.deepcopy(adg_non)
                adg_out = copy.deepcopy(adg_non)
                adg_bi = copy.deepcopy(adg_non)
                adg_in.relations.add((a, b))
                adg_out.relations.add((b, a))
                adg_bi.relations.add((a,b))
                adg_bi.relations.add((b,a))
                # evaluate adg_in, adg_out, adg_bi and adg, return the best one of these 4
                perf_in = self.evaluate(adg_in, eval_list)
                perf_out = self.evaluate(adg_out, eval_list)
                perf_bi = self.evaluate(adg_bi, eval_list)
                perf_non = self.evaluate(adg_non, eval_list)
                if perf_in > perf_out and perf_in > perf_bi and perf_in > perf_non:
                    adg = adg_in
                elif perf_out > perf_in and perf_out > perf_bi and perf_out > perf_non:
                    adg = adg_out
                elif perf_bi > perf_in and perf_bi > perf_out and perf_bi > perf_non:
                    adg = adg_bi
                else:
                    adg = adg_non
        if len(adg.arguments) == 0 and a[1] != 'und':
            adg.arguments.add(a)
        return adg

    def predict(self, adg, t):
        v = verified(adg, t)
        l = grounded(v)
        if len(l['in']) > 0:
            for i in l['in']:
                if i[1] != 'und':
                    return i[1]
        else:
            if (len(l['und']) > 0):
                return 'und'
        return 'unk'
