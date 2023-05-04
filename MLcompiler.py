import pandas as pd
import ast
from IPython.display import display

def checkLexemeType(t):
    if t.isalpha():
        return 'letter'
    elif t.isdigit():
        return 'digit'
    else:
        return t

def checkFinalState(f,token):
    type=tokenMap[f]
    val=None
    if type=='num':
        val=ast.literal_eval(token)
    li=[token,type,val]
    return li

states=['S','A','B','D','E','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24','F25','F26']
finalState=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24','F25','F26']
startState='S'
tFunct={('S','letter'):'A', ('A','letter'):'A', ('A','digit'):'A', ('S',';'):'F2', 
 ('S','|'):'B', ('B','|'):'F4', ('S','.'):'F5', ('S',','):'F6', ('S','/'):'F7', 
 ('S','@'):'F8', ('S','*'):'F9', ('S',':'):'F10',('S','{'):'F11',('S','}'):'F12',('S','('):'F13',
 ('S',')'):'F14',('S','['):'F15',('S',']'):'F16', ('S','>'):'F25',('S','<'):'F26',('F26','='):'D',('D','>'):'F17',
 ('S','='):'F18', ('S','^'):'F19', ('S','+'):'F20', ('S','-'):'F21', ('S','digit'):'F22', 
 ('F21','digit'):'F22', ('F21','>'):'F24', ('F22','digit'):'F22', ('F22','.'):'E', ('E','digit'):'F23', ('F23','digit'):'F23'}
lookAheadFunct={'A':'F1','B':'F3'}
tokenMap={'F1':'identifier', 'F2':';', 'F3':'|','F4':'||', 'F5':'.', 'F6':',', 'F7':'/','F8':'@', 'F9':'*','F10':':','F11':'{','F12':'}',
          'F13':'(','F14':')','F15':'[','F16':']','F17':'<=>', 'F18':'=', 'F19':'exponent', 'F20':'+', 'F21':'-', 'F22':'num', 'F23':'num', 'F24':'->','F25':'>','F26':'<'}
reservedWord=[['vect','reserved',None],['mat','reserved',None],['conr','reserved',None],['conc','reserved',None],['row','reserved',None],['col','reserved',None]
              ,['print','reserved',None],['R','reserved',None],['C','reserved',None],['T','reserved',None]]
symbolTable=pd.DataFrame(reservedWord,columns=['name','type','val'])

# print(symbolTable.loc[:,'name'].values)

pathfile=r'C:\Users\Nunan\Documents\GitHub\MLC\test1.mlc'
file=open(pathfile,'r')
stream=[]
for line in file:
    line=line.strip('\n')
    print('loop')
    currentState='S'
    t=0
    token=''
    while t<len(line):
        # if len(stream)==10:
        #     print(stream)
        #     stream=[]
        if token in [lis[0] for lis in reservedWord]:
            currentState='F1'
        if currentState in finalState:
            newEntry=checkFinalState(currentState,token)
            tupCheck=(currentState,checkLexemeType(line[t]))
            if tupCheck not in tFunct:
                if token not in symbolTable.loc[:,'name'].values:
                    print('not in')
                    symbolTable.loc[len(symbolTable.index)] = newEntry
                currentState='S'
                stream.append(token)
                print(token+'\n')
                token=''
        if line[t] == ' ':
            t+=1
            print('blank space')
            continue
        inp = checkLexemeType(line[t])
        tupInp = (currentState,inp)
        print('current state: '+currentState+', read: '+line[t]+', t: '+str(t)+', token: '+token)
        if tupInp in tFunct:
            currentState=tFunct[tupInp]
            token+=line[t]
            t+=1
            if t==len(line):
                print('last')
                if currentState in finalState:
                    newEntry=checkFinalState(currentState,token)
                    if token not in symbolTable.loc[:,'name'].values:
                        print('not in last')
                        symbolTable.loc[len(symbolTable.index)] = newEntry
                    currentState='S'
                    stream.append(token)
                    print(token+'\n')
                    token=''
        else:
            if currentState in lookAheadFunct:
                currentState=lookAheadFunct[currentState]
        #     t-=1
file.close()
print(stream)
display(symbolTable)

