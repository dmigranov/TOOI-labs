def func(text):
    n = len(text)
    best = [1.0]
    words = []
    for i in range(n):
        best_est = 0.0
        best_word = ''
        for j in range(i+1):
            word = text[j:i+1]
            if word in voc:
                notin = voc[word]
            else:
                notin = 0
            cur_est = notin * best[j]

            if cur_est > best_est:
                best_est = cur_est
                best_word = word
        best.append(best_est)
        words.append(best_word)
    result = []

    i = n-1
    while i >= 0:
        wordi = words[i]
        if wordi == '':
            return FuncResult(False)

        result.insert(0, wordi)
        i = i - len(wordi)
    return FuncResult(result)
        
                               
