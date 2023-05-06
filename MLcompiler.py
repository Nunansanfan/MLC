import pandas as pd
import ast
from IPython.display import display
import itertools

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

def parse(stream):
    global stack,tree,productionRules,parsingTable,symbolTable
    print('stream : '+str(stream))
    current = stack[-1][1]
    print("stack before : "+str(stack))
    i=0
    while(i<len(stream)):
        realtype=symbolTable.loc[symbolTable['name']==stream[i],'type'].iloc[0]
        print('token : '+stream[i]+', type : '+realtype)
        if realtype=='reserved':
            realtype=stream[i]
        inpPair=(current,realtype)
        outPair=parsingTable[inpPair]
        action=outPair[0]
        stateOrRule=outPair[1]
        if action=='S':
            current=stateOrRule
            nodeType=symbolTable.loc[symbolTable['name']==stream[i],'type'].iloc[0]
            nodeVal=symbolTable.loc[symbolTable['name']==stream[i],'val'].iloc[0]
            shiftNode=node(stream[i],nodeType,nodeVal)
            tree.append(shiftNode)
            stack.append((stream[i],current))
            print("shift stack : "+str(stack))
            print("shift tree : "+str([str(i) for i in tree]))

            i+=1
        elif action=='R':
            print('reduce : '+stateOrRule)
            # 1. stateOrRule : เลข Rule ที่ต้องใช้ reduce
            # 2. productionRules[stateOrRule] -> (Nonterminal หน้าลูกศร,จำนวนหลังลูกศร)
            nonterminal=productionRules[stateOrRule][0]
            count = productionRules[stateOrRule][1]
            # 3. สร้าง node ใหม่ของ Nonterminal หน้าลูกศร
            nonterNode=node(nonterminal,'nonterminal',None)
            nonterNode.reduceAssign(stateOrRule)
            # 4. pop "จำนวนหลังลูกศร" ตัวออกจาก stack, ดึง node จาก tree "จำนวนหลังลูกศร" ตัวจากด้านหลังเอาไปใส่ list child ของ node จากข้อ 3.
            for j in range(count):
                stack.pop()
                temp=tree.pop()
                # temp=(tree.pop()).deepCopy()
                print("pop from tree : "+temp.tokenName)
                nonterNode.addChild(temp)
            # 4.1. current = stack[-1][1] เปลี่ยนสถานะเป็นตัวสุดท้ายหลัง pop สิ่งที่ reduce ออกๆไปแล้ว
            current = stack[-1][1]
            # 5. หา current ใหม่ -> current = parsingTable[(current,Nonterminal หน้าลูกศร)][1]
            current = parsingTable[(current,nonterminal)][1]
            # 6. push ("Nonterminal หน้าลูกศร",current) ลง stack
            stack.append((nonterminal,current))
            # 7. tree.append(node ใหม่)
            tree.append(nonterNode)
            print('stack reduce : '+str(stack))
            print('tree reduce : '+str([str(i) for i in tree]))

            # print('tree : '+str(tree))
        elif action=='A':
            nonterminal="Start'"
            nonterNode=node(nonterminal,'nonterminal',None)
            nonterNode.reduceAssign("P1")
            stack.pop()
            temp=tree.pop()
            print("pop from tree : "+temp.tokenName)
            # stack.append(("Start'",'G1'))
            nonterNode.addChild(temp)
            tree.append(nonterNode)
            print('finished')
            print('stack accept : '+str(stack))
            print('tree accept : '+str([str(i) for i in tree]))

            current = stack[-1][1]
            i+=1

def showTree(node,level):
    treeStr=""
    if node:
        for i in range(level):
            treeStr+="\t"
        treeStr+="|- "+str(node)+"\n"
        if(len(node.childs)>0):
            for nodei in node.childs:
                treeStr+=showTree(nodei,level+1)
    return treeStr

class node:
    id_iter = itertools.count()
    id=0
    tokenName=''
    type=''
    val=None
    childs=[]
    reduceFrom=''
    def __init__(self,tokenName,type,val=None):
        self.tokenName=tokenName
        self.type = type
        self.val = val
        self.id=next(self.id_iter)
        self.childs=[]

    def __str__(self):
        return str(self.id)+'_'+self.tokenName
    
    def addChild(self,obj):
        self.childs.append(obj)
    
    def reduceAssign(self,reduce):
        self.reduceFrom=reduce
    
    def deepCopy(self):
        ret=node(self.tokenName,self.type,self.val)
        ret.childs=self.childs[:]
        ret.reduceFrom=self.reduceFrom
        return ret


states=['S','A','B','D','E','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24','F25','F26','F27','F28','F29']
finalState=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24','F25','F26','F27','F28','F29']
startState='S'
tFunct={('S','letter'):'A', ('A','letter'):'A', ('A','digit'):'A', ('S',';'):'F2', 
 ('S','|'):'B', ('B','|'):'F4', ('S','.'):'F5', ('S',','):'F6', ('S','/'):'F7', 
 ('S','@'):'F8', ('S','*'):'F9', ('S',':'):'F10',('S','{'):'F11',('S','}'):'F12',('S','('):'F13',
 ('S',')'):'F14',('S','['):'F15',('S',']'):'F16', ('S','>'):'F25',('S','<'):'F26',('F26','='):'D',('D','>'):'F17',
 ('S','='):'F18', ('S','^'):'F19', ('S','+'):'F20', ('S','-'):'F21', ('S','digit'):'F22', 
 ('F21','digit'):'F22', ('F21','>'):'F24', ('F22','digit'):'F22', ('F22','.'):'E', ('E','digit'):'F23', ('F23','digit'):'F23',('F7','/'):'F28',
 ('F28','letter'):'F28', ('F28','digit'):'F28', ('F28',';'):'F28', ('F28','|'):'F28', ('F28','.'):'F28', ('F28',','):'F28',('F28','/'):'F28',  
 ('F28','@'):'F28', ('F28','*'):'F28', ('F28',':'):'F28', ('F28','{'):'F28', ('F28','}'):'F28',('F28','('):'F28', ('F28',')'):'F28', ('F28','['):'F28', 
 ('F28',']'):'F28', ('F28','>'):'F28', ('F28','<'):'F28', ('F28','='):'F28', ('F28','^'):'F28', ('F28','+'):'F28', ('F28','-'):'F28', ('F28',' '):'F28',
 ('F7','*'):'H', ('H','letter'):'H', ('H','digit'):'H', ('H',';'):'H', ('H','|'):'H', ('H','.'):'H', ('H',','):'H',('H','/'):'H',  
 ('H','@'):'H',  ('H',':'):'H', ('H','{'):'H', ('H','}'):'H',('H','('):'H', ('H',')'):'H', ('H','['):'H', 
 ('H',']'):'H', ('H','>'):'H', ('H','<'):'H', ('H','='):'H', ('H','^'):'H', ('H','+'):'H', ('H','-'):'H', ('H',' '):'H',
 ('H','*'):'I', ('I','/'):'F29', ('I','letter'):'H', ('I','digit'):'H', ('I',';'):'H', ('I','|'):'H', ('I','.'):'H', ('I',','):'H',('I','*'):'H',  
 ('I','@'):'H',  ('I',':'):'H', ('I','{'):'H', ('I','}'):'H',('I','('):'H', ('I',')'):'H', ('I','['):'H', 
 ('I',']'):'H', ('I','>'):'H', ('I','<'):'H', ('I','='):'H', ('I','^'):'H', ('I','+'):'H', ('I','-'):'H', ('I',' '):'H' }
lookAheadFunct={'A':'F1','B':'F3'}
tokenMap={'F1':'identifier', 'F2':';', 'F3':'|','F4':'||', 'F5':'.', 'F6':',', 'F7':'/','F8':'@', 'F9':'*','F10':':','F11':'{','F12':'}',
          'F13':'(','F14':')','F15':'[','F16':']','F17':'<=>', 'F18':'=', 'F19':'^', 'F20':'+', 'F21':'-', 'F22':'num', 'F23':'num', 'F24':'->','F25':'>','F26':'<','F28':'comment','F29':'comment'}
reservedWord=[['$','reserved',None],['vect','reserved',None],['mat','reserved',None],['conr','reserved',None],['conc','reserved',None],['row','reserved',None],['col','reserved',None]
              ,['print','reserved',None],['R','reserved',None],['C','reserved',None],['T','reserved',None]]
symbolTable=pd.DataFrame(reservedWord,columns=['name','type','val'])

# เลข production rule, ตัวหน้าลูกศร, จำนวนตัวหลังลูกศร (แลมด้าใส่ 0)
productionRules={'P1':("Start'",1),'P2':("Start",1),'P3':("Start",1),'P4':("Start",1),'P5':("Start",1),'P6':("Start",1)
                 ,'P9':("DecStmt",1),'P10':("DecStmt",1),'P44':("DecVectStmt",1),'P45':("DecVectStmt",1),'P46':("DecVect",4)
                 ,'P47':("AssignVectSet",1),'P48':("AssignVectSet",0),'P49':("AssignVect",3),'P50':("VectAssign",2)
                 ,'P51':("VectAssign'",3),'P52':("VectAssign'",1),'P53':("VectMember",2),'P54':("VectMember'",2)
                 ,'P55':("VectMember'",0),'P56':("DecMatrixStmt",1),'P57':("DecMatrixStmt",1),'P58':("DecMatrix",4)
                 ,'P59':("AssignMatrixSet",1),'P60':("AssignMatrixSet",0),'P61':("AssignMatrix",3),'P62':("MatrixAssign",2)
                 ,'P62':("MatrixAssign",2),'P63':("MatrixAssign'",1),'P64':("MatrixAssign'",1),'P65':("MatrixAssign'",1)
                 ,'P66':("MatrixAssign'",1),'P67':("MatrixAssign'",1)
                 ,'P68':('AssignMatrix2',4),'P69':('VectSet',3),'P70':('VectSet',0),'P77':('AssignMatrix3',3),'P78':('RowTermSet',2)
                 ,'P79':("RowTermSet'",2),'P80':("RowTermSet'",0),'P81':('RowTerm',2),'P82':("RowTerm'",1),'P83':("RowTerm'",0)
                 ,'P84':('RowOpBlock',4),'P85':('RowOpList',2),'P86':("RowOpList'",2),'P87':("RowOpList'",0),'P88':('RowOp',3)
                 ,'P89':('Action',3),'P90':('Action',2),'P91':('RowItOrAdd',5),'P92':('RowItOrAdd',3),'P93':("RowItOrAdd'",5)
                 ,'P138':("RowItOrAdd'",1),'P94':('Operation',1),'P95':('Operation',1),'P96':('Mult',2),'P97':('Mult',0)
                 ,'P98':('Divide',2),'P99':('Divide',0),'P100':('MatCPxp',2),'P101':("MatCPxp'",3),'P102':("MatCPxp'",0),'P103':('OpCP',1),'P104':('OpCP',1)
                 ,'P105':("OpCP",1),'P106':("OpCP",1),'P107':("MatMxp",2),'P108':("MatMxp'",3),'P109':("MatMxp'",0),'P110':("OpM",1),'P111':("OpM",1),'P112':("MatPPxp",4),'P113':("MatPPxp",2)
                 ,'P114':("MatPPxp'",2),'P115':("MatPPxp'",0),'P116':("SupScript",1),'P117':("SupScript",3),'P118':("MatExp",1),'P119':("Submat",2),'P120':("Submat'",1),'P121':("Submat'",1)
                 ,'P122':("SubOut",3),'P123':("RowColList",2),'P124':("RowColList'",2),'P125':("RowColList'",0),'P126':("RowCol",2),'P127':("RowCol",2),'P128':("SubIn",5),'P129':("RSlice",8),'P130':("CSlice",8)
                 ,'P131':("SubTerm",1),'P132':("SubTerm",0),'P133':("DimRow",3),'P134':("DimCol",3),'P137':("PrintStmt",5)}

                 
                 

# S = Shift
# G = Go to
# R = Reduce
parsingTable={('S0','vect'):('S','G13'), ('S0','mat'):('S','N7'), ('S0','print'):('S','G38') , ('S0','/'):('S','G31'), ('S0','identifier'):('S','G28')  
            , ('S0','identifier'):('S','N1')  , ('S0',"Start"):('G','G1'), ('S0','DecStmt'):('G','G2'), ('S0',"DecVectStmt"):('G','G7')
            , ('S0','DecVect'):('G','G9'), ('S0','AssignVect'):('G','G10'), ('S0','DecMatrixStmt'):('G','G8'), ('S0','DecMatrix'):('G','G11')
            , ('S0','AssignMatrix'):('G','G12'), ('S0','DimRow'):('G','G3'), ('S0','DimCol'):('G','G4'), ('S0','PrintStmt'):('G','G6')
            , ('N1','='):('S','C0'), ('N1','.'):('S','N4'), ('N1','MatrixAssign'):('G','N2'), ('N2',';'):('S','N3'), ('N3','$'):('R','P61')
            , ('N4','row'):('S','N5'), ('N4','col'):('S','N6'), ('N5',';'):('R','P133'), ('N6',';'):('R','P134'), ('N7','identifier'):('S','N8')
            , ('N8',';'):('R','P60'), ('N8','='):('S','C0'), ('N8','AssignMatrixSet'):('G','N10'), ('N8','MatrixAssign'):('G','N9'), ('N9',';'):('R','P59')
            , ('N10',';'):('S','N11'), ('N11','$'):('R','P58'), ('N12',';'):('R','P62'), ('N14',';'):('R','P63'), ('N15',';'):('R','P64')
            , ('N16',';'):('R','P65'), ('N17',';'):('R','P66'), ('N18',';'):('R','P67'), ('N19','conr'):('R','P118'), ('N19','conc'):('R','P118')
            , ('N19',';'):('R','P118'), ('N19','+'):('R','P118'), ('N19','-'):('R','P118'), ('N19','@'):('R','P118'), ('N19','*'):('R','P118')
            , ('N19','{'):('S','N53'), ('N19',')'):('R','P118'), ('N19','|'):('S','N25'), ('N19','||'):('S','N20'), ('N19','^'):('R','P118')
            , ('N19',"Submat'"):('G','N90'), ('N19','SubOut'):('G','N89'), ('N19','SubIn'):('G','N88'), ('N20','R'):('S','N23'), ('N20','C'):('S','N21'), ('N20','RowColList'):('G','N51')
            , ('N20','RowCol'):('G','N47'), ('N21','num'):('S','N22'), ('N22','||'):('R','P127'), ('N22',','):('R','P127'), ('N23','num'):('S','N24')
            , ('N24','||'):('R','P126'), ('N24',','):('R','P126'), ('N25','R'):('S','N39'), ('N25','RSlice'):('G','N26'), ('N26',','):('S','N27')
            , ('N27','C'):('S','N30'), ('N27','CSlice'):('G','N28'), ('N28','|'):('S','N29'), ('N29',';'):('R','P128'), ('N30','('):('S','N31')
            , ('N31',')'):('R','P132'), ('N31',':'):('R','P132'), ('N31','num'):('S','N38'), ('N31','SubTerm'):('G','N32'), ('N32',':'):('S','N33')
            , ('N33',')'):('R','P132'), ('N33',':'):('R','P132'), ('N33','num'):('S','N38'), ('N33','SubTerm'):('G','N34'), ('N34',':'):('S','N35')
            , ('N35',')'):('R','P132'), ('N35',':'):('R','P132'), ('N35','num'):('S','N38'), ('N35','SubTerm'):('G','N36'), ('N36',')'):('S','N37')
            , ('N37','|'):('R','P130'), ('N38',')'):('R','P131'), ('N38',':'):('R','P131'), ('N39','('):('S','N40'), ('N40',')'):('R','P132')
            , ('N40',':'):('R','P132'), ('N40','num'):('S','N38'), ('N40','SubTerm'):('G','N41'), ('N41',':'):('S','N42'), ('N42',')'):('R','P132')
            , ('N42',':'):('R','P132'), ('N42','num'):('S','N38'), ('N42','SubTerm'):('G','N43'), ('N43',':'):('S','N44'), ('N44',')'):('R','P132')
            , ('N44',':'):('R','P132'), ('N44','num'):('S','N38'), ('N44','SubTerm'):('G','N45'), ('N45',')'):('S','N46'), ('N46',','):('R','P129')
            , ('N47','||'):('R','P125'), ('N47',','):('S','N48'), ('N47',"RowColList'"):('G','N50'), ('N48','R'):('S','N23'), ('N48','C'):('S','N21')
            , ('N48','RowColList'):('G','N49'), ('N48','RowCol'):('G','N47'), ('N49','||'):('R','P124'), ('N50','||'):('R','P123'), ('N51','||'):('S','N52')
            , ('N52',';'):('R','P122'), ('N53','R'):('S','N54'), ('N53','RowOpList'):('G','N86'), ('N53','RowOp'):('G','N82'), ('N54','num'):('S','N55')
            , ('N55','->'):('S','N60'), ('N55','<=>'):('S','N57'), ('N55','Action'):('G','N56'), ('N56','}'):('R','P88'), ('N56',','):('R','P88')
            , ('N57','R'):('S','N58'), ('N58','num'):('S','N59'), ('N59','}'):('R','P89'), ('N59',','):('R','P89'), ('N60','R'):('S','N62')
            , ('N60','num'):('S','N77'), ('N60','RowItOrAdd'):('G','N61'), ('N61','}'):('R','P90'),('N61',','):('R','P90'),('N62','num'):('S','N63'),
            ('N63','+'):('S','N66'),('N63','-'):('S','N67'),('N63','/'):('S','N68'),('N63','Divide'):('G','N64'),('N63',"RowItOrAdd'"):('G','N65'),
            ('N63','Operation'):('G','N70'),('N63','}'):('R','P99'),('N63',','):('R','P99'),('N64','}'):('R','P138'),('N64',','):('R','P138'), 
            ('N65','}'):('R','P92'),('N65',','):('R','P92'),('N66','R'):('R','P94'),('N66','num'):('R','P94'),('N67','R'):('R','P95'),('N67','num'):('R','P95'),
            ('N68','num'):('S','N69'),('N69','}'):('R','P98'),('N69',','):('R','P98'),('N70','num'):('S','N71'),('N70','Mult'):('G','N73'),('N70','R'):('R','P97'),
            ('N71','*'):('S','N72'),('N72','R'):('R','P96'),('N73','R'):('S','N74'),('N74','num'):('S','N75'),
            ('N75','/'):('S','N68'),('N75','}'):('R','P99'),('N75',','):('R','P99'),('N75','Divide'):('G','N76'),
            ('N76',','):('R','P93'),('N76','}'):('R','P93'),('N77','*'):('S','N78'),('N77','Comment'):('G','G5'),('N77','PrintStmt'):('G','G6'),
            ('N78','R'):('S','N79'),('N79','num'):('S','N80'),('N80','/'):('S','N68'),('N80','}'):('R','P99'),('N80',','):('R','P99'),('N80','Divide'):('G','N81'),
            ('N81','}'):('R','P91'),('N81',','):('R','P91'),('N82',','):('S','N83'),('N82','}'):('R','P87'),('N82',"RowOpList'"):('G','N85'),
            ('N83','R'):('S','N54'),('N83','RowOp'):('G','N82'),('N83','RowOpList'):('G','N84'),('N84','}'):('R','P86'),('N85','}'):('R','P85'),
            ('N86','}'):('S','N87'),('N87',';'):('R','P84'),('N88',';'):('R','P121'),('N89',';'):('R','P120'),('N90',';'):('R','P119'),('G1','$'):('A','Accept'),
            ('G2','$'):('R','P2'),('G3','$'):('R','P3'),('G4','$'):('R','P4'),('G5','$'):('R','P5'),('G6','$'):('R','P6'),('G7','$'):('R','P9'), ('G8','$'):('R','P10'),
            ('G9','$'):('R','P44'),('G10','$'):('R','P45'),('G11','$'):('R','P56'),('G12','$'):('R','P57'),('G13','identifier'):('S','G14'),
            ('G14','='):('S','G18'),('G14','AssignVectSet'):('G','G15'),('G14','VectAssign'):('G','G17'),('G15',';'):('S','G16'),('G16','$'):('R','P46'),
            ('G17',';'):('R','P47'),('G18','<'):('S','G20'),('G18','identifier'):('S','G27'),('G18',"VectAssign'"):('G','G19'),('G19',';'):('R','P50'),
            ('G20','num'):('S','G23'),('G20','VectMember'):('G','G21'),('G21','>'):('S','G22'),('G22',';'):('R','P51'),
            ('G23',','):('S','G25'),('G23','>'):('R','P55'),('G23',"VectMember'"):('G','G24'),('G24','>'):('R','P53'),
            ('G25','num'):('S','G23'),('G25','VectMember'):('G','G26'),('G26','>'):('R','P54'),('G27',';'):('R','P52'),
            ('G28','='):('S','G18'),('G28','VectAssign'):('G','G29'),('G29',';'):('S','G30'),('G30','$'):('R','P49'),('G38','('):('S','G39'), 
            ('G39','obj'):('S','G40'), ('G40',')'):('S','G41'), ('G41',';'):('S','G42'), ('G42','$'):('R','P137'),
            ('C0','{'):('S','Y8'), ('C0','['):('S','Y1'), ('C0','('):('S','C17'), ('C0','identifier'):('S','N19'), ('C0',"MatrixAssign'"):('G','N12'), 
            ('C0','AssignMatrix2'):('G','N14'), ('C0','AssignMatrix3'):('G','N15'), ('C0','RowOpBlock'):('G','N16'), ('C0','MatCPxp'):('G','N17'), 
            ('C0','MatMxp'):('G','C1'), ('C0','MatPPxp'):('G','C10'), ('C0','MatExp'):('G','C27'), ('C0','Submat'):('G','N18'), 
            ('C1','conr'):('S','C7'), ('C1','conc'):('S','C6'), ('C1',';'):('R','P102'), ('C1','+'):('S','C8'), ('C1','-'):('S','C9'), ('C1',"MatCPxp'"):('G','C2'), ('C1','OpCP'):('G','C3'), 
            ('C2','conr'):('R','P100'), ('C2','conc'):('R','P100'), ('C2',';'):('R','P100'), ('C2','+'):('R','P100'), ('C2','-'):('R','P100'), ('C2',')'):('R','P100'), 
            ('C3','('):('S','C17'), ('C3','identifier'):('S','C29'), ('C3','MatCPxp'):('G','C4'), ('C3','MatMxp'):('G','C1'), ('C3','MatPPxp'):('G','C10'), ('C3','MatExp'):('G','C27'), 
            ('C4','conr'):('R','P102'), ('C4','conc'):('R','P102'), ('C4',';'):('R','P102'), ('C4','+'):('R','P102'), ('C4','-'):('R','P102'), ('C4',"MatCPxp'"):('G','C5'), ('C4','OpCP'):('G','C3'), 
            ('C5','conr'):('R','P101'), ('C5','conc'):('R','P101'), ('C5',';'):('R','P101'), ('C5','+'):('R','P101'), ('C5','-'):('R','P101'), 
            ('C6','('):('R','P103'), ('C6','identifier'):('R','P103'), ('C7','('):('R','P104'), ('C7','identifier'):('R','P104'), 
            ('C8','('):('R','P105'), ('C8','identifier'):('R','P105'), ('C9','('):('R','P106'), ('C9','identifier'):('R','P106'), 
            ('C10','conr'):('R','P109'), ('C10','conc'):('R','P109'), ('C10',';'):('R','P109'), ('C10','+'):('R','P109'), ('C10','-'):('R','P109'), 
            ('C10','@'):('S','C15'), ('C10','*'):('S','C16'), ('C10',')'):('R','P109'), ('C10',"MatMxp'"):('G','C11'), ('C10','OpM'):('G','C12'), 
            ('C11','conr'):('R','P107'), ('C11','conc'):('R','P107'), ('C11',';'):('R','P107'), ('C11','+'):('R','P107'), ('C11','-'):('R','P107'), 
            ('C11','@'):('R','P107'), ('C11','*'):('R','P107'), ('C11',')'):('R','P107'), ('C12','('):('S','C17'), ('C12','identifier'):('S','C29'), 
            ('C12','MatMxp'):('G','C13'), ('C12','MatPPxp'):('G','C10'), ('C12','MatExp'):('G','C27'), 
            ('C13','@'):('R','P109'), ('C13','*'):('R','P109'), ('C13','conc'):('R','P109'),('C13','conr'):('R','P109'),('C13','+'):('R','P109'),('C13','-'):('R','P109'),('C13',')'):('R','P109'),('C13',';'):('R','P109'),
            ('C13',"MatMxp'"):('G','C14'), ('C13','OpM'):('G','C12'), ('C14','conr'):('R','P108'), ('C14','conc'):('R','P108'), ('C14',';'):('R','P108'), 
            ('C14','+'):('R','P108'), ('C14','-'):('R','P108'), ('C14','@'):('R','P108'), ('C14','*'):('R','P108'), ('C14',')'):('R','P108'), 
            ('C15','('):('R','P110'), ('C15','identifier'):('R','P110'), ('C16','('):('R','P111'), ('C16','identifier'):('R','P111'), 
            ('C17','('):('S','C17'), ('C17','identifier'):('S','C29'), ('C17','MatCPxp'):('G','C18'), ('C17','MatMxp'):('G','C1'), ('C17','MatPPxp'):('G','C10'), ('C17','MatExp'):('G','C27'), 
            ('C18',')'):('S','C19'), ('C19','^'):('S','C21'), ('C19',"MatPPxp'"):('G','C20'), ('C20','conr'):('R','P112'), ('C20','conc'):('R','P112'), ('C20',';'):('R','P112'), 
            ('C20','+'):('R','P112'), ('C20','-'):('R','P112'), ('C20','@'):('R','P112'), ('C20','*'):('R','P112'), ('C20',')'):('R','P112'), 
            ('C21','('):('S','C24'), ('C21','T'):('S','C23'), ('C21','SupScript'):('G','C22'), ('C22','conr'):('R','P114'), ('C22','conc'):('R','P114'), ('C22',';'):('R','P114'), 
            ('C22','+'):('R','P114'), ('C22','-'):('R','P114'), ('C22','@'):('R','P114'), ('C22','*'):('R','P114'), ('C22',')'):('R','P114'), 
            ('C23','conr'):('R','P116'), ('C23','conc'):('R','P116'), ('C23',';'):('R','P116'), ('C23','+'):('R','P116'), ('C23','-'):('R','P116'), 
            ('C23','@'):('R','P116'), ('C23','*'):('R','P116'), ('C23',')'):('R','P116'), 
            ('C24','num'):('S','C25'), ('C25',')'):('S','C26'), ('C26','conr'):('R','P117'), ('C26','conc'):('R','P117'), ('C26',';'):('R','P117'), 
            ('C26','+'):('R','P117'), ('C26','-'):('R','P117'), ('C26','@'):('R','P117'), ('C26','*'):('R','P117'), ('C26',')'):('R','P117'), 
            ('C27','@'):('R','P115'), ('C27','*'):('R','P115'), ('C27','conc'):('R','P115'),('C27','conr'):('R','P115'),('C27','+'):('R','P115'),('C27','-'):('R','P115'),('C27',')'):('R','P115'),('C27',';'):('R','P115'),
            ('C27','^'):('S','C21'), ('C27',"MatPPxp'"):('G','C28'), ('C28','conr'):('R','P113'), ('C28','conc'):('R','P113'), ('C28',';'):('R','P113'), 
            ('C28','+'):('R','P113'), ('C28','-'):('R','P113'), ('C28','@'):('R','P113'), ('C28','*'):('R','P113'), ('C28',')'):('R','P113'), 
            ('C29','conr'):('R','P118'), ('C29','conc'):('R','P118'), ('C29',';'):('R','P118'), ('C29','+'):('R','P118'), ('C29','-'):('R','P118'), 
            ('C29','@'):('R','P118'), ('C29','*'):('R','P118'), ('C29',')'):('R','P118'), ('C29','^'):('R','P118'),
            ('Y1','identifier'):('S','Y2'), ('Y2',']'):('R','P70'), ('Y2',','):('S','Y5'), ('Y2','VectSet'):('G','Y3'), ('Y3',']'):('S','Y4'), 
            ('Y4',';'):('R','P68'), ('Y5','identifier'):('S','Y6'), ('Y6',']'):('R','P70'), ('Y6',','):('S','Y5'), ('Y6','VectSet'):('G','Y7'), 
            ('Y7',']'):('R','P69'), ('Y8','num'):('S','Y15'), ('Y8','RowTermSet'):('G','Y9'), ('Y8','RowTerm'):('G','Y11'), ('Y9','}'):('S','Y10'), 
            ('Y10',';'):('R','P77'), ('Y11','}'):('R','P80'), ('Y11',','):('S','Y13'), ('Y11',"RowTermSet'"):('G','Y12'), ('Y12','}'):('R','P78'), 
            ('Y13','num'):('S','Y15'), ('Y13','RowTermSet'):('G','Y14'), ('Y13','RowTerm'):('G','Y11'), 
            ('Y14','}'):('R','P79'), ('Y15','}'):('R','P83'), ('Y15',','):('R','P83'), ('Y15','num'):('S','Y15'), ('Y15','RowTerm'):('G','Y17'), ('Y15',"RowTerm'"):('G','Y16'), 
            ('Y16','}'):('R','P81'), ('Y16',','):('R','P81'), ('Y17','}'):('R','P82'), ('Y17',','):('R','P82')}

stack=[('$','S0')]
tree=[]

pathfile=r'./test1.mlc'
file=open(pathfile,'r')
stream=[]
currentState='S'
t=0
token=''
isComment=False
for line in file:
    line=line.strip('\n')
    if not isComment:
        currentState='S'
        token=''
        isComment=False
    t=0
    while t<len(line):
        if len(stream)>=10:
            parse(stream)
            stream=[]
        if token in [lis[0] for lis in reservedWord]:
            currentState='F1'
        if currentState in finalState:
            newEntry=checkFinalState(currentState,token)
            tupCheck=(currentState,checkLexemeType(line[t]))
            if tupCheck not in tFunct:
                if(newEntry[1]!='comment'):
                    if token not in symbolTable.loc[:,'name'].values:
                        print('not in')
                        symbolTable.loc[len(symbolTable.index)] = newEntry
                    currentState='S'
                    stream.append(token)
                    if(token==';'):
                        stream.append('$')
                    print(token+'\n')
                    token=''
                else:
                    currentState='S'
                    token=''
                    isComment=False
            
        if line[t] == ' ':
            if currentState=='A':
                currentState='F1'
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
                if currentState =='H' or currentState == 'I':
                    isComment=True
                    break
                if currentState in finalState:
                    newEntry=checkFinalState(currentState,token)
                    if(newEntry[1]!='comment'):
                        if token not in symbolTable.loc[:,'name'].values:
                            print('not in last')
                            symbolTable.loc[len(symbolTable.index)] = newEntry
                        currentState='S'
                        stream.append(token)
                        if(token==';'):
                            stream.append('$')
                        print(token+'\n')
                        token=''
                    else:
                        currentState='S'
                        token=''
                        isComment=False
        else:
            if currentState in lookAheadFunct:
                currentState=lookAheadFunct[currentState]
parse(stream)
file.close()
print(stream)
display(symbolTable)
root=tree[0]
# while len(root.childs)!=0:
#     print(str(root))
#     root=root.childs[0]
# print(root.tokenName)
print('final tree : ')
print(showTree(root,0))
# print('final tree'+str(tree))