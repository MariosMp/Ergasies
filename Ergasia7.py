import randomtriliza={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}def print_triliza(triliza):    print(triliza['1']+'|'+triliza['2']+'|'+triliza['3'])    print('-+-+-')    print(triliza['4']+'|'+triliza['5']+'|'+triliza['6'])    print('-+-+-')    print(triliza['7']+'|'+triliza['8']+'|'+triliza['9'])done='false'i=0seira='X'theseis=[]for theseis[j] in range(9):    if triliza[j] == " ":        theseis.append(j)print_triliza(triliza)while (i<9 and done=='false') :    if seira=='X':        if i==0:            move=input('Παίζεις πρώτος')        else:            move=input('Σειρά σου')        while triliza[move]!=' ':            print ('Το τετραγωνάκι είναι πιασμένο, παίξε αλλού')            move=input()        triliza[move]=seira        theseis.remove(theseis[seira]);        if (triliza['1']==triliza['2'] and triliza['2']==triliza['3'] and triliza['3']==seira):            done='true'        elif (triliza['4']==triliza['5'] and triliza['5']==triliza['6'] and triliza['6']==seira):            done='true'        elif (triliza['7']==triliza['8'] and triliza['8']==triliza['9'] and triliza['9']==seira):            done='true'        elif (triliza['1']==triliza['4'] and triliza['4']==triliza['7'] and triliza['7']==seira):            done='true'        elif (triliza['2']==triliza['5'] and triliza['5']==triliza['8'] and triliza['8']==seira):            done='true'        elif (triliza['3']==triliza['6'] and triliza['6']==triliza['9'] and triliza['9']==seira):            done='true'        elif (triliza['1']==triliza['5'] and triliza['5']==triliza['9'] and triliza['9']==seira):            done='true'        elif (triliza['3']==triliza['5'] and triliza['5']==triliza['7'] and triliza['7']==seira):            done='true'        seira='O'        i=i+1        print_triliza(triliza)     else:         print('Σειρά του υπολογιστή')         move=random.choice(theseis)         triliza[move]=seira         if (triliza['1']==triliza['2'] and triliza['2']==triliza['3'] and triliza['3']==seira):             done='true'        elif (triliza['4']==triliza['5'] and triliza['5']==triliza['6'] and triliza['6']==seira):             done='true'        elif (triliza['7']==triliza['8'] and triliza['8']==triliza['9'] and triliza['9']==seira):             done='true'        elif (triliza['1']==triliza['4'] and triliza['4']==triliza['7'] and triliza['7']==seira):             done='true'        elif (triliza['2']==triliza['5'] and triliza['5']==triliza['8'] and triliza['8']==seira):             done='true'        elif (triliza['3']==triliza['6'] and triliza['6']==triliza['9'] and triliza['9']==seira):             done='true'        elif (triliza['1']==triliza['5'] and triliza['5']==triliza['9'] and triliza['9']==seira):             done='true'        elif (triliza['3']==triliza['5'] and triliza['5']==triliza['7'] and triliza['7']==seira):             done='true'        seira='X'        i=i+1        print_triliza(triliza)if done=='true':    if seira=='O':        print ('Κέρδισες!')    else:        print ('Έχασες!')else:    print ('Ισοπαλία')