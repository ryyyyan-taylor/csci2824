def filterFun(msg,spam,ham):
    prob_spam = float(len(spam))/(len(spam)+len(ham))
    prob_ham = 1-prob_spam
    spam_ele_dict = {}
    ham_ele_dict = {}

    for ele in list(set(msg)):
        spam_ele_dict[ele] = 0
        ham_ele_dict[ele] = 0
        for sp in spam:
            if (ele in sp):
                spam_ele_dict[ele] += 1.0
        for hp in ham:
            if (ele in hp):
                ham_ele_dict[ele] += 1.0

    for key,value in spam_ele_dict.items():
        spam_ele_dict[key] = value/len(spam)
    for key,value in ham_ele_dict.items():
        ham_ele_dict[key] = value/len(ham)

    prob_ele_spam = prob_spam
    prob_ele_ham = prob_ham

    for ele in list(set(msg)):
        prob_ele_spam *= spam_ele_dict[ele]
        prob_ele_ham *= ham_ele_dict[ele]

    prob_msg_spam = prob_ele_spam / (prob_ele_spam + prob_ele_ham)
    prob_msg_ham = prob_ele_ham / (prob_ele_spam + prob_ele_ham)

    return (prob_msg_spam>prob_msg_ham)

msg = [1,2]
spam = [[0,1],[0,2],[0,3]]
ham = [[1],[1,2],[0,2]]
print (filterFun(msg,spam,ham))

msg = [0,1]
spam = [[0,1,2],[0,1,3],[2,3,4]]
ham = [[2,3,5],[6,1,0]]
print (filterFun(msg,spam,ham))
