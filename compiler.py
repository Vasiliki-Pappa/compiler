
#Vasiliki Pappa
#AM :4149
#cse74149
import sys
import os

file= open(sys.argv[1],'r')

#Tokens


#identifier
id_token=50

#Arithmitikes statheres
number_token=51

#addOperator : +,-
prosthesi_token=52
afairesi_token=53

#mulOperator: *,/
pol_token=54
diairesi_token=55

isotita_token=56
mikrotero_token=57
megalutero_token=58
EOF_token=59
koma_token=60
erwtimatiko_token=61

aristeri_par_token=62
deksia_par_token=63

aristeri_agk_token=64 #einai [
deksia_agk_token=65 #einai ]

anoigma_b_token=66# einai {
kleisimo_b_token=67#einai 

mikrotero_iso_token=68
megalutero_iso_token=69

anwkatw_teleia_token=70
anathesi_token=71
diaforo_token=72
teleia_token=73


                                  
#keyword periexei tis desmeumenes lekseis tis glwssas
program_token=150
declare_token=151
if_token=152
else_token=153
while_token=154
switchcase_token=155
incase_token=156
forcase_token=157
case_token=158
default_token=159
procedure_token=160
function_token=161
call_token=162
return_token=163
in_token=164
inout_token=165
and_token=166
or_token=167
not_token=168
input_token=169
print_token=170



#otan blepei tous parakatw xaraktires allazei katastasi to automato leitourgias toy ektikou analuti

keno=0
grammata=1
number=2
prosthesi=3
afairesis=4
pol=5
diairesi=6
isotita=7
mikrotero=8
megalutero=9
oxi_apodekto=10
koma=11
erwtimatiko=12
aristeri_par=13
deksia_par=14
aristeri_agk=15
deksia_agk=16
anoigma_b=17
kleisimo_b=18
allagi_grammis= 19
anwkatw_teleia=20
teleia=21
hashtag=22
EOF=23

#Katastaseis me bash to automato leitourgias tou lektikou analuti

start=0
idk=1
dig=2
smaller=3
larger=4
asgn=5
sxolia=6


#parakate einai enas pinkas pou periexei tis desmeumenes lekseis tis glwssas


desmeumenes_lekseis=['program' ,'declare','if','else','while','switchcase','forcase','incase','default','case',
                                        'not','and','or','function','procedure','call','return','in','inout','input','print']






#Sfalmata

#den einai apodekto to sumbolo
sfalma_oxi_apodekto=-1
#meta apo ena psifio den prepei na uparxei gramma
sfalma_gramma_psifio=-2
#emfanizetai to = alla meta den blepw to : ,alla allo xaraktira
sfalma_anwkatw_teleia=-3
#mia akeraia stathera prepei na briskete sto epitrepto euros timwn
sfalma_oxi_egkuros_arithmos=-4
#to mikos prepei na einai to polu 30 xaraktires
sfalma_panw_apo_30=-5
#anoigw sxolia alla den ta kleinw pote
sfalma_sxolia=-6



#pinakas metabasewn me basi to automato stoibas tou lektikou analuti

metabaseis=[
        #start
        [start,idk,dig,prosthesi_token,afairesi_token,pol_token, diairesi_token,isotita_token,smaller,larger,sfalma_oxi_apodekto,
         koma_token,erwtimatiko_token,aristeri_par_token,deksia_par_token,aristeri_agk_token,deksia_agk_token,anoigma_b_token,kleisimo_b_token,
         start,asgn,teleia_token,sxolia,EOF_token],
        
    #idk
        [id_token,idk,idk,id_token,id_token,id_token,id_token,id_token,id_token,id_token,sfalma_oxi_apodekto,
         id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token],
        
    #dig
        [number_token,sfalma_gramma_psifio, dig,number_token,number_token,number_token,
         number_token,number_token,number_token,number_token,sfalma_oxi_apodekto,
         number_token,number_token,number_token,number_token,number_token,number_token,number_token,number_token,
         number_token,number_token,number_token,number_token,number_token],

        #smaller
        [mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,
         mikrotero_token,mikrotero_iso_token,mikrotero_token,diaforo_token,sfalma_oxi_apodekto,
         mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,
         mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token,mikrotero_token],

        #larger
        [megalutero_token,megalutero_token,megalutero_token,megalutero_token,megalutero_token,megalutero_token,
         megalutero_token,megalutero_iso_token,megalutero_token,megalutero_token,sfalma_oxi_apodekto,
         megalutero_token,megalutero_token,megalutero_token,megalutero_token,megalutero_token,megalutero_token,megalutero_token,megalutero_token,
         megalutero_token,megalutero_token,megalutero_token,megalutero_token,megalutero_token],

        #asgn
        [sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,
         sfalma_anwkatw_teleia,anathesi_token,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_oxi_apodekto,
         sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia
         ,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia,sfalma_anwkatw_teleia],

        #sxolia
        [sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,
         sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,sxolia,start,sfalma_sxolia]

        ]

                

grammi=1

alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        
arithmoi=['0','1','2','3','4','5','6','7','8','9']


#lektikos analutis 
def lex():


        global grammi

        #arxizw apo tin katastash start
        katastasi= start

        mikos_id=''

        #metritis grammis
        metritis_grammis= grammi


        apotelesmata=[]


        while(katastasi>=0 and katastasi<=6):

                char = file.read(1)

                if (char == ' ' or char == '\t'):
                        char_token = keno
                elif (char in alphabet):
                        char_token = grammata
                elif (char in arithmoi):
                        char_token = number
                elif (char == '+'):
                        char_token = prosthesi
                elif (char == '-'):
                        char_token = afairesis
                elif (char == '*'):
                        char_token = pol
                elif (char == '/'):
                        char_token = diairesi
                elif(char == '='):
                        char_token = isotita
                elif (char == '<'):
                        char_token = mikrotero
                elif (char == '>'):
                        char_token = megalutero
                elif (char == ':'):
                        char_token = anwkatw_teleia
                elif (char == ','):
                        char_token = koma
                elif (char == ';'):
                        char_token = erwtimatiko
                elif (char == '('):
                        char_token = aristeri_par
                elif (char == ')'):
                        char_token = deksia_par
                elif (char == '['):
                        char_token = aristeri_agk
                elif (char == ']'):
                        char_token = deksia_agk
                elif (char == '{'):
                        char_token = anoigma_b
                elif (char == '}'):
                        char_token = kleisimo_b
                elif (char == '\n'):
                        metritis_grammis=metritis_grammis+1
                        char_token = allagi_grammis
                elif (char == ''): 
                        char_token = EOF
                elif (char == '.'):
                        char_token = teleia
                elif (char == '#'):
                        char_token = hashtag
                else:
                        char_token = oxi_apodekto
                
               
                
                katastasi=metabaseis[katastasi][char_token]
                
                #print('katastasi :   ', katastasi)

                 #an to mikos einai mikrotero tou 30 prosthetw xaraktiras
                if(len(mikos_id)<30):
                        if(katastasi!=start and katastasi!=sxolia):
                                        mikos_id+=char

                #to mikos einai megalutero apo 30 xaraktires
                #epomenws exw sfalma
                else:


                        katastasi=sfalma_panw_apo_30


        #tha brw token 
        #apo edw kai katw token 

        if(katastasi==id_token or katastasi==number_token or katastasi==mikrotero_token or katastasi==megalutero_token ):
                if (char == '\n'):
                        metritis_grammis -= 1
                char=file.seek(file.tell()-1,0)  #epistrofj teleutaiou xaraktira

                mikos_id = mikos_id[:-1]        

        if(katastasi==id_token):
                if(mikos_id in desmeumenes_lekseis):

                        if(mikos_id=='program'):
                                katastasi=program_token

                        elif(mikos_id=='declare'):
                                katastasi=declare_token

                        elif (mikos_id == 'if'):
                                katastasi = if_token

                        elif (mikos_id == 'else'):
                                katastasi = else_token

                        elif (mikos_id == 'while'):
                                katastasi = while_token

                        elif (mikos_id == 'switchcase'):
                                katastasi = switchcase_token

                        elif (mikos_id == 'forcase'):
                                katastasi = forcase_token

                        elif (mikos_id == 'incase'):
                                katastasi = incase_token

                        elif (mikos_id == 'case'):
                                katastasi = case_token

                        elif (mikos_id == 'default'):
                                katastasi = default_token

                        elif (mikos_id == 'procedure'):
                                katastasi = procedure_token

                        elif (mikos_id == 'function'):
                                katastasi = function_token

                        elif (mikos_id == 'call'):
                                katastasi = call_token

                        elif (mikos_id == 'return'):
                                katastasi = return_token

                        elif (mikos_id == 'in'):
                                katastasi = in_token

                        elif (mikos_id == 'inout'):
                                katastasi = inout_token

                        elif (mikos_id == 'and'):
                                katastasi = and_token

                        elif (mikos_id == 'or'):
                                katastasi = or_token

                        elif (mikos_id == 'not'):
                                katastasi = not_token

                        elif (mikos_id == 'input'):
                                katastasi = input_token

                        elif (mikos_id == 'print'):
                                katastasi = print_token


        #prepei na eleksw an oi aritmoi einai entos tou euros timwn
        #prepei na einai apo to [-32767,32767]
        #an den einai ,einai sfalma
        if (katastasi == number_token):
                if (mikos_id.isdigit() >= pow(2,32)):
                    katastasi = sfalma_oxi_egkuros_arithmos

       #sfalmata
        if(katastasi==sfalma_oxi_apodekto):
                 print("SFALMA : MH APODEKTO SYMBOLO!!!")

        elif(katastasi==sfalma_gramma_psifio):
                print("SFALMA:META APO ENA PSIFIO EXOUME GRAMMA !!!")

        elif(katastasi==sfalma_anwkatw_teleia):
                print("SFALMA :YPARXEI ANW-KATW TELEIA KAI META DEN YPARXEI ISOTHTA")

        elif(katastasi==sfalma_oxi_egkuros_arithmos):
                print("SFALMA:O ARITHMOS EINAI EKTOS ORIWN!!!")

        elif(katastasi==sfalma_sxolia):
                print("SFALMA:TA SXOLIA ANOIKSAN ,ALLA DEN EKLEISAN!!!")

        elif(katastasi==sfalma_panw_apo_30):
                print("SFALMA : TO MIKOS THS LEKSHS EINAI PANW APO 30 XARAKTITES ")



        apotelesmata.append(katastasi)
        apotelesmata.append(mikos_id)
        apotelesmata.append(metritis_grammis) #oxi aparaithto
        grammi=metritis_grammis
        #print("grammi :",grammi)

        #print(apotelesmata)
        return apotelesmata


####################### Endiamesos kodikas ########################
#endiamesos kwdikas einai sunolo apo 4ades
# enas telestis kai 3 teloumena



global lista_tetradwn       #lista me Oles tis tetrades pou tha paraxthoun apo to programma.
lista_tetradwn = []
metritis_tetradwn = 1               #O arithmos pou xarakthrizei thn tetrada. Brisketai mprosta apo thn 4ada.

#epistrephei ton arithmo tis epomenis 4adas pou projupti na paraxthei
def nextQuad():


    global metritis_tetradwn
    
    return metritis_tetradwn


#dimiourgei epomeni 4ada (op,x,y,z)
def genQuad(first, second, third, fourth):
    #print("dimiourgei epomeni 4ada (op,x,y)")
    global metritis_tetradwn
    global lista_tetradwn

    listgQ = []
    
    genQ=nextQuad()
    #print("genQ:",genQ)

       
    listgQ += [genQ] + [first] + [second] + [third] + [fourth]     
    
    metritis_tetradwn +=1  
    #print("metritis_tetradwn einai :",metritis_tetradwn)

    lista_tetradwn += [listgQ]    
    #print("listgQ :",listgQ)

    return listgQ

T_i = 1
lista_met = []

#dimiourgei kai epistrefei mia proswrini metabliti
def newTemp():


    global T_i #proswrinh metabliti tis  morfis T_1,T_2,....... 
    global lista_met
    
    listnewT = ['T_']
    Ti=str(T_i)
    #print("Ti"+ Ti)

    listnewT.append(Ti)
    #print(listnewT)

    prMetabliti="".join(listnewT)
    #print("prMetabliti"+ prMetabliti)

    T_i +=1

        #print("T_i:"+Ti)
    lista_met += [prMetabliti]
    ent = Entity()                              #Create an Entity
    ent.type = 'TEMP'                           #
    ent.name = prMetabliti                   #
    ent.pmet.offset = compute_offset()       #
    new_entity(ent) 
    #print(lista_met)

    #print("proswrinh mwtabliti ="+ prMetabliti)
    return prMetabliti

#dimiourgei keni lista
def emptyList():

    keni_lista = []    
    
    return keni_lista

#dimiougia mia lista etiketwn 4adwn pou periexei mono to x
def makeList(x):
    
    
    mlist = [x]
    
    return mlist

#dimiougei mia lista etiketwn 4adwn apo tin sunenwsi 2 listwn list1 kai list2
def merge(list1, list2):

    mergelist=[]
    mergelist += list1 + list2

    return mergelist

#i lista apoteleitai apo deiktes se 4ades twn opoiwn to teleutaio teloumeno den einai sumplirwmeno
#backpatch episkeptetpia mia mia tis tetrades autes kai tis sumplirwnei me tin etiketa z
def backpatch(list, z):

    global lista_tetradwn
    
    for i in range(len(list)):
        for j in range(len(lista_tetradwn)):
            if(list[i]==lista_tetradwn[j][0] and lista_tetradwn[j][4]=='_'):
                lista_tetradwn[j][4] = z
                break; 
    return

print("##### PINAKAS SUMBOLWN#####")


#------------------- PINAKAS SUMBOLWN



class Entity():
	#orthogenio

    def __init__(self):
        self.name = ''          #Dinw to name gia na kserw poio Entity einai.
        self.type = ''          #  'VAR' or 'SUBPR' or 'PARAM' or 'TEMP'
        
        self.variable = self.Variable()
        self.sunartisi = self.Sunartisi()
        self.parameter = self.Parameter()
        self.pmet = self.ProsMetabliti()
        
    class Variable: # metavliti
        def __init__(self):

            self.offset = 0             # Apostash apo thn arxh ths stoibas.
    class Sunartisi: # ypoprogramma            
        def __init__(self):
            self.type = ''              # 'Procedure' h' 'Function' .
            self.startQuad = 0          # H proti tetrada tis (apo ton endiameso).
            self.frameLength = 0        # To mhkos eggrafhmatos drasthriopoihshs.
            self.argument = []          #h lista parametrwn (gia na apothikeuso ta TRIGONA)
            
    class Parameter: # parametros
        def __init__(self):
            self.parMode = ''              # 'CV', 'REF'
            self.offset = 0             # Apostash apo thn arxh ths stoibas.
    class ProsMetabliti: # prosorini metavliti
        def __init__(self):

            self.offset = 0             # Apostash apo thn arxh ths stoibas.


class Scope():

    def __init__(self):
        self.name = ''                      #Dinw to name gia na kserw poio Scope einai.
        self.entityList = []        #h lista apo entities
        self.nestingLevel = 0               # Bathos fwliasmatos.
        self.enclosingScope = None          #Perikleion scope.

class Argument():

    #rombos

    def __init__(self):

        self.parMode = '' #tropos perasmatos
        self.type = 'Int'   #tupos metablitis
        self.name = ''   #onoma argument


def new_argument(object): 


    global topScope
    
    a=topScope.entityList[-1]
    b=a.sunartisi
    c=b.argument
    d=c.append(object)


def new_entity(object):  
    global topScope
    
    a=topScope.entityList
    b=a.append(object)



global topScope
topScope = None

def new_scope(name):  

    global topScope

    nextScope = Scope()   
    nextScope.name = name
    nextScope.enclosingScope=topScope

    if(topScope == None): #arxika None(null)
        nextScope.nestingLevel = 0
    else:
        nextScope.nestingLevel = topScope.nestingLevel + 1

    topScope = nextScope

def delete_scope(): 
    global topScope
    
    freeScope = topScope
    topScope = topScope.enclosingScope 
    del freeScope

def compute_offset():

    global topScope
    
    metritis_offset=0
    j=topScope.entityList
    if(j is not []):  
        for ent in (j):  
            if(ent.type == 'VAR' or ent.type == 'TEMP' or ent.type=='PARAM'): 

                metritis_offset +=1  

    offset = 12+(metritis_offset*4)   #12 reserved
    
    return offset


            
def add_parameters():  
    global topScope
    
    a=topScope.enclosingScope
    b=a.entityList[-1]
    c=b.sunartisi
    d=c.argument

    for i in d: # gia kathe trigwno
        entity1 = Entity() # ftiakse orthogonio
        entity1.name = i.name
        entity1.type = 'PARAM'
        ep=entity1.parameter
        ep.parMode = i.parMode
        ep.offset = compute_offset()
        new_entity(entity1)






#Syntaktikos Analyths
        
def suntaktikos(cCodeF):

        global grammi
        global lex1


        lex1= lex()
        grammi = lex1[2]
         



        def print_Symbol_table():

            global topScope
            f = open("pinakas_sumbolwn.txt", "w")
            print("---------------------------------------------------------------------------------------------------------------")
            f.write("---------------------------------------------------------------------------------------------------------------")
            f.write("\n")
            print("\n")
            print("---------------------------------------------------------------------------------------------------------------")
            f.write("---------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("")
            
            
            sco=topScope
            while sco != None:
                print("SCOPE: "+"name:"+sco.name+" nestingLevel:"+str(sco.nestingLevel))
                f.write("SCOPE: ")
                f.write("\n")
                f.write("\tName is :"+sco.name+" nestingLevel:"+str(sco.nestingLevel))
                f.write("\n")
                print("---------------------------------------------------------------------------------------------------------------")
                f.write("---------------------------------------------------------------------------------------------------------------")
                print("\n")
                f.write("\n")
                print("---------------------------------------------------------------------------------------------------------------")
                f.write("---------------------------------------------------------------------------------------------------------------")
                print("\n")
                f.write("\n")
                print("\tENTITIES:")
                f.write("\tENTITIES")
                f.write("\n")
                for ent in sco.entityList:
                    if(ent.type == 'VAR'):
                        print("___________________________________________________________________________________________________")
                        f.write("___________________________________________________________________________________________________")
                        f.write("\n")
                       	print("\tENTITY: "+" name:"+ent.name+"\n\t\t offset:"+str(ent.variable.offset))
                        f.write("\tENTITY: "+" name:"+ent.name+"\n\t\t offset:"+str(ent.variable.offset))
                        f.write("\n")
                    elif(ent.type == 'TEMP'):
                        print("_________________________________________________________________________________________________")
                        f.write("___________________________________________________________________________________________________")
                        f.write("\n")
                        print("\tENTITY: "+" name:"+ent.name+"\n\t\t offset:"+str(ent.pmet.offset))
                        f.write("\tENTITY: "+" name:"+ent.name+"\n\t\t offset:"+str(ent.pmet.offset))
                        f.write("\n")
                    elif(ent.type == 'SUBPR'):
                        if(ent.sunartisi.type == 'Function'):
                            print("______________________________________________________________________")
                            f.write("___________________________________________________________________________________________________")
                            f.write("\n")
                            print("\tENTITY: "+" name:"+ent.name+"\n\t\t type:"+ent.type+"\n\t\t function-type:"+ent.sunartisi.type)
                            f.write("\tENTITY: "+" name:"+ent.name+"\n\t\t type:"+ent.type+"\n\t\t function-type:"+ent.sunartisi.type)
                            f.write("\n")
                            print("\tARGUMENTS:")
                            f.write("-----------------------------------------------------------------------------------------------------------------------------------------")
                            f.write("\n")
                            f.write("\tARGUMENTS")
                            f.write("\n")
                            print("\n")
                            print("---------------------------------------------------------------------------------------------------------------")
                            f.write("---------------------------------------------------------------------------------------------------------------")
                            f.write("\n")
                            for arg in ent.sunartisi.argument:
                                    print("_________________________________________________________________________________________________")
                                    #f.write("___________________________________________________________________________________________________")
                                    f.write("\n")
                                    print("\t\tARGUMENT: "+" name:"+str(arg.name)+"\t type:"+arg.type+"\t parMode:"+arg.parMode)
                                    f.write("\tARGUMENT: "+" name:"+str(arg.name)+"\n\t\t type:"+arg.type+"\n\t\t parMode:"+arg.parMode)
                                    f.write("\n")
                        elif(ent.sunartisi.type == 'Procedure'):
                            print("_________________________________________________________________________________________________")
                            f.write("___________________________________________________________________________________________________")
                            f.write("\n")
                            print("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t procedure-type:"+ent.sunartisi.type)
                            f.write("\tENTITY: "+" name:"+ent.name+"\n\t\t type:"+ent.type+"\n\t\t procedure-type:"+ent.sunartisi.type)
                            f.write("\n")
                            print("\tARGUMENTS:")
                            f.write("-----------------------------------------------------------------------------------------------------------------------------------------")
                            f.write("\n")
                            f.write("\tARGUMENTS")
                            f.write("\n")
                            print("\n")
                            print("---------------------------------------------------------------------------------------------------------------")
                            f.write("---------------------------------------------------------------------------------------------------------------")
                            f.write("\n")
                            for arg in ent.sunartisi.argument:
                                #print("_________________________________________________________________________________________________")
                                #f.write("___________________________________________________________________________________________________")
                                f.write("\n")
                                print("\t\tARGUMENT: "+" name:"+str(arg.name)+"\t type:"+arg.type+"\t parMode:"+arg.parMode)
                                f.write("\tARGUMENT: "+" name:"+str(arg.name)+"\n\t\t type:"+arg.type+"\n\t\t parMode:"+arg.parMode)
                                f.write("\n")
                        elif(ent.type == 'PARAM'):
                            print("_________________________________________________________________________________________________")
                            f.write("___________________________________________________________________________________________________")
                            f.write("\n")
                            print("\tENTITY: "+" name:"+str(ent.name)+"\t type:"+ent.type+"\t parMode:"+ent.parameter.parMode+"\t offset:"+str(ent.parameter.offset))
                            f.write("\tENTITY: "+" name:"+str(ent.name)+"\n\t\t type:"+ent.type+"\n\t\t parMode:"+ent.parameter.parMode+"\n\t\t offset:"+str(ent.parameter.offset))
                sco = sco.enclosingScope

                print("---------------------------------------------------------------------------------------------------------------")
 

        #program: program ID block

        #<program> ::= program name
             #       <program_block> (name)
        def program():

                global grammi 
                global lex1
                
                if(lex1[0] == program_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == id_token):

                                id = lex1[1]
                                lex1 = lex()
                                grammi = lex1[2]

                                block(id,1)
                                if(lex1[0] == teleia_token):
                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                        return
                                else:
                                        print("SFALMA :Sto program! Den yparxei  teleia  gia na kleisei to program", grammi)
                                        exit(-1)

                        else:
                                print("sfalma :Sto program !To programma den exei onoma",grammi)
                                exit(-1)
                else:
                         print("sfalma :Sto program !To programma den arxizei me tin leksi program",grammi)
                         exit(-1)


            #block : declarations subprograms statements 

            #<program_block> (name) ::= <declarations>
                                        #<subprograms>
                                        #genquad(“begin_block”,name,”_”,”_”)
                                        #< block>
                                        #genquad(“halt”,”_,”_”,”_”)
            
                                        #genquad(“end_block”,name,”_”,”_”)
        

        def block(name, flag):


            print("block")
            global lex1
        
            new_scope(name)

            #if (flag!=1):
                

                #declarations()
                
           

            
            if(flag!=1):
                add_parameters()
            declarations()
            subprograms()

            genQuad('begin_block',name,'_','_')
            statements()

            if(flag==1):
                genQuad('halt','_','_','_')

            #else:
                #compute_framelength()
                        
            genQuad('end_block',name,'_','_')
            print("o pinakas sumbolwn einai :")
            print_Symbol_table()
            #printSumbolo()
            delete_scope()

            

         # declarations : (declare varlist ;)*                
        def declarations():

                global lex1 
                global cCodeF
                
                while(lex1[0] == declare_token):
                        lex1 = lex()
                        grammi = lex1[2]

                        cCodeF.write("int ")
                        varlist()
                        cCodeF.write(" ;\n\t")
                        
                        if(lex1[0] == erwtimatiko_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                
                        else:
                                print("sfalma :Sto declarations !Meta to varlist den uperxei erwtimatiko", grammi)
                                exit(-1)
                return
                 

        #varlist : ID(, ID)*
        #        | e(keno)    

        def varlist():

                global lex1
                global cCodeF
                
                if(lex1[0] == id_token):

                        cCodeF.write(lex1[1])

                        entity1=Entity()
                        entity1.type='VAR'
                        entity1.name=lex1[1]
                        entity1.variable.offset = compute_offset()  #
                        new_entity(entity1)

                        lex1 = lex()
                        grammi = lex1[2]
                        
                        while(lex1[0] == koma_token):

                                cCodeF.write(lex1[1])#



                                lex1 = lex()
                                grammi = lex1[2]
                                
                                if(lex1[0] == id_token):

                                        cCodeF.write(lex1[1])

                                        entity1=Entity()
                                        entity1.type='VAR'
                                        entity1.name=lex1[1]
                                        entity1.variable.offset = compute_offset()  #
                                        new_entity(entity1)

                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                else:
                                        print("sfalma :Sto varlist! Prin to ID den uparxei koma", grammi)
                                        exit(-1)
                
                return



        # kanena or perisotera subgrams epitrepontai
        #subprograms :(subprogram)*
    #<subprograms> ::= function id <formalpars>
                    #{ genquad(“begin_block”,id,”_”,”_”)
                    #<block>
                    #genquad(“end_block”,id,”_”,”_”)
                    #}     
        def subprograms():

                global lex1
                
                while(lex1[0] == procedure_token or lex1[0] == function_token ):
                        
                        subprogram()
                return
                
          

        #a subprogram is a function or a procedure
        #followed by parameters and block 
         
        #subprogram:function ID (formalparlist) block
         #           | procedure ID (formalparlist) block       
        def subprogram():

                global lex1
                
                #procedure 
                if(lex1[0]==procedure_token):

                        lex1=lex()
                        grammi=lex1[2]
                        
                        if(lex1[0]==id_token):

                                id = lex1[1]

                                ent = Entity()                      #Create an Entity
                                ent.type = 'SUBPR'                  #
                                ent.name= lex1[1]                 #
                                ent.sunartisi.type = 'Procedure'   #
                                new_entity(ent)

                                lex1 = lex()
                                grammi = lex1[2]

                                if(lex1[0] == aristeri_par_token):

                                        lex1 = lex()
                                        grammi = lex1[2]

                                        formalparlist()
                        
                                        if(lex1[0] == deksia_par_token):
                                                

                                                
                                                lex1 = lex()
                                                grammi = lex1[2]
                                                block(id,0)
                                
                                                return
                                        else:
                                                print("sfalma :Sto subprogram!Den uparxei parenthesi meta to formalparlist ,sugkekrimena h deksi parenthesi",grammi)
                                                exit(-1)

                                else:
                                        print("sfalma :Sto subprogram!Den uparxei parenthesi prin to formalparlist ,sugkekrimena h aristeri parenthesi",grammi)
                                        exit(-1)
                        else:
                                print("sfalma :Sto subprogram!To procedure prohgeitai tou id ", grammi)
                                exit(-1)

                elif(lex1[0]== function_token):
                        lex1 = lex()
                        grammi = lex1[2]

                        if(lex1[0]==id_token):

                                id = lex1[1]

                                ent = Entity()                      #Create an Entity
                                ent.type = 'SUBPR'                  #
                                ent.name = lex1[1]                 #
                                ent.sunartisi.type = 'Function'    #
                                new_entity(ent)
                                lex1 = lex()
                                grammi = lex1[2]

                                if(lex1[0] == aristeri_par_token):

                                        lex1 = lex()
                                        grammi = lex1[2]

                                        formalparlist()
                        
                                        if(lex1[0] == deksia_par_token):
                                                


                                                lex1 = lex()
                                                grammi = lex1[2]
                                                block(id,0)
                                
                                                return
                                        else:
                                                print("sfalma :Sto subprogram!Den uparxei parenthesi meta to formalparlist ,sugkekrimena h deksi parenthesi",grammi)
                                                exit(-1)
                                else:
                                        print("sfalma :Sto subprogram!Den uparxei parenthesi prin to formalparlist ,sugkekrimena h aristeri parenthesi",grammi)
                                        exit(-1)

                        else:
                                print("sfalma : to  function prohgeitai tou id  ", grammi)
                                exit(-1)
         

        #formalparlist : formalparlist (, formalparlist)*
         #               |e        
        def formalparlist():
                global lex1
                
                formalparitem()
                
                while(lex1[0] == koma_token):

                        lex1  = lex()
                        grammi = lex1[2]
                        
                        formalparitem()
                                
                return


        #formalparitem : in ID
        #              | inout ID
                
        def formalparitem():
                global lex1
                global grammi
                
                if(lex1[0] == in_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0]== id_token):

                                arg = Argument()        #Creation of a new argument. (Pinakas Symbolwn)
                                arg.name = lex1[1]     #
                                arg.parMode = 'CV'      #
                                new_argument(arg)       #
                                lex1 = lex()
                                grammi = lex1[2]
                                
                        else:
                                print("sfalma :Sto formalparitem! Meta to in prepei na uparxei onoma ", grammi)
                                exit(-1)

                elif(lex1[0] == inout_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == id_token):
                                arg = Argument()        #Creation of a new argument. (Pinakas Symbolwn)
                                arg.name = lex1[1]     #
                                arg.parMode = 'REF'     #
                                new_argument(arg)       #
                                lex1 = lex()
                                grammi = lex1[2]
                                
                        else:
                                print("sfalma :Sto formalparitem! Meta to inout prepei na uparxei onoma ", grammi)
                                exit(-1)

                #else:
                     #   print("sfalma: Den uparxei in h inout ", grammi)
                      #  exit(-1)

                return
                       

        #statements:statement ;
        #          |{statement (;statement)*}                         
                        
        def statements():
                global lex1
                global grammi
                
                if(lex1[0] == anoigma_b_token):

                        lex1 = lex()
                        grammi  =  lex1[2]
                        
                        statement()
                        
                        while(lex1[0] == erwtimatiko_token):

                                lex1 = lex()
                                grammi = lex1[2]
                                
                                statement()
                                
                        if(lex1[0] == kleisimo_b_token):

                                lex1 = lex()
                                grammi = lex1[2]
                                return
                                
                        else:
                                print("sfalma:Sto statements! To block den kleinei", grammi)
                                exit(-1)
                else:

                        statement()

                        if(lex1[0] == erwtimatiko_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                return
                        else:
                                print("sfalma: Sto statements! Meta apo statement den uparxei erotimatiko 1", grammi)
                                exit(-1)
                
                 
        # statement : assignstat 
         #         | ifStat
          #        |whileStat
           #       |switchcaseStat 
           #       |forcaseStat
           #       |incaseStat 
            #      |callStat 
            #      |returnStat 
             #     |inputStat 
            #      |printStat 
              #    |e               
                
        def statement():

                global lex1
                
                if(lex1[0]==id_token):
                        assignmentStat()

                elif(lex1[0]==if_token):
                        ifStat()

                elif(lex1[0]==while_token):
                        whileStat()

                elif(lex1[0]==switchcase_token):
                        switchcaseStat()

                elif(lex1[0]==forcase_token):
                        forcaseStat()

                elif(lex1[0]==incase_token):
                        incaseStat()

                elif(lex1[0]==call_token):
                        callStat()

                elif(lex1[0]==return_token):
                        returnStat()

                elif(lex1[0]==input_token):
                        inputStat()

                elif(lex1[0]==print_token):
                        printStat()

                return
                        
        
         #assignment :ID := expression   
         #S -> id := E {P1};
           # {P1} : genQuad(“:=“,E.place,”_”,id)     
        def assignmentStat():

                global lex1
                
                if(lex1[0] == id_token):
                        id_a = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == anathesi_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                
                                ex = expression()
                                genQuad(':=', ex, '_', id_a)
                                return
                        else:
                                print("sfalma:Sto assignmentStat! Meta to onoma metavlitis prepei na exoume to sumbolo anathesis  ", grammi)
                                exit(-1) 
                else:
                        print("sfalma:Sto assignmentStat!",grammi)
                        exit(-1)


        #ifStat : if(condition) statement elsepart

        #S -> if B then {P1} S1 {P2} TAIL {P3}
           #     {P1}: backpatch(B.true,nextquad())
            #    {P2}: ifList=makelist(nextquad())
             #           genquad(“jump”,”_”,”_”,”_”)
             #           backpatch(B.false,nextquad())
             #   {P3}: backpatch(ifList,nextquad())
        #TAIL -> else S2 | TAIL -> ε

        def ifStat():

                global lex1
                global grammi
                
                if(lex1[0] == if_token):
                        lex1= lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == aristeri_par_token):

                                lex1 = lex()
                                grammi = lex1[2]
                                
                                con = condition()
                                backpatch(con[0], nextQuad())
                                
                                if(lex1[0]== deksia_par_token):

                                        lex1 = lex()
                                        grammi = lex1[2]

                                        statements()

                                        next1 = nextQuad() #alla3a edww
                                        ifList = makeList(next1)
                                        genQuad('jump', '_', '_', '_')
                                        backpatch(con[1], nextQuad())

                                        elsepart()

                                        backpatch(ifList, nextQuad())

                                        return
                                else:
                                        print("sfalma:Sto ifStat! H paranthesi den kleinei swsta", grammi)
                                        exit(-1)
                        else:
                                print("sfalma :Sto ifStat! H paranthesi den anoigei", grammi)
                                exit(-1)
                else:
                        print("sfalma:Sto ifStat! H if exei problima sto anoigma",grammi)
                        exit(-1)
          

        #elsepart : else statemant
        #          | e  

                
        def elsepart():

                global lex1
                global grammi
                
                if(lex1[0] == else_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        statements()
                        
                return
                

         #whileStat :while (condition) statemants 

         #S -> while {P1} B do {P2} S1 {P3}
                    #{P1}: Bquad:=nextquad()
                    #{P2}: backpatch(B.true,nextquad())
                    #{P3}: genquad(“jump”,”_”,”_”,Bquad)
                            #backpatch(B.false,nextquad())  

        def whileStat():
        	
                global lex1
                global grammi
                
                if(lex1[0]== while_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == aristeri_par_token):
                                lex1 = lex()
                                grammi = lex1[2]

                                Bquad=nextQuad()
                                con = condition()
                                backpatch(con[0], nextQuad())
                                
                                if(lex1[0] == deksia_par_token):
                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                        statements()

                                        genQuad('jump', '_', '_', Bquad)
                                        backpatch(con[1], nextQuad())
                                        
                                        return
                                else:
                                        print("sfalma:Sto whileStat! H paranthesi den kleinei swsta", grammi)
                                        exit(-1)
                        else:
                                print("sfalma:Sto whileStat! H paranthesi den anoigei swsta",grammi)
                                exit(-1)
                else:
                        print("sfalma:Sto whileStat! ", grammi)
                        exit(-1)

        #swotcjcaseStat : switchcase 
                        #  (case(condition)statements)*
                        # 



        #S -> switch {P1}
          #     ( (cond): {P2} S1 break {P3} )*
          #  default: S2 {P4}
         #   {P1} : exitlist = emptylist()
          #  {P2} : backpatch(cond.true,nextquad())
          #  {P3} : e = makelist(nextquad())
            #        genquad('jump', '_', '_', '_')
           #         mergelist(exitlist,e)
            #        backpatch(cond.false,nextquad())
           # {P4} : backpatch(exitlist,nextquad)
        def switchcaseStat():

                global lex1
                global grammi
                
                if(lex1[0] == switchcase_token):
                        lex1 = lex()
                        grammi = lex1[2]

                        exitlist=emptyList()
                        
                        while(lex1[0] == case_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                
                                if(lex1[0] == aristeri_par_token):
                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                        con = condition()
                                        backpatch(con[0], nextQuad())
                                        
                                        if(lex1[0] == deksia_par_token):
                                                lex1 = lex()
                                                grammi = lex1[2]

                                                statements()
                                                e = makeList(nextQuad())
                                                genQuad('jump', '_', '_', '_')
                                                exitlist = merge(exitlist, e)
                                                backpatch(con[1], nextQuad())

                                        else:
                                                print("sfalma :Sto switchcase ! Den uparxei  deksia parenthesi", grammi)
                                                exit(-1)
                                else:
                                        print("sfalma :Sto switchcase ! Den uparxei  aristeri parenthesi", grammi)
                                        exit(-1)
                        if(lex1[0] == default_token):
                                lex1 = lex()
                                grammi = lex1[2]

                                statements()
                                backpatch(exitlist, nextQuad())
                        else:
                                print("sfalma :Sto switchcase!Thema me tin default", grammi)
                                exit(-1)
                else:
                        print("sfalma : sto switchcase!", grammi)
                        exit(-1)
        

        #forcasestat :forcase 
                    # (case (condition)statemants)*
                    # default statements


#S -> forcase  {P1}
  #  ( when (condition) do {P2}
   #     sequence {P3}
    #    end do ) *
    #endforcase
    #{P1}:   p1Quad=nextquad()
    #{P2}:   backpatch(cond.true,nextquad())
    #{P3}:   genquad(“jump”, ”_”, ”_”,p1quad)
    #backpatch(cond.false,nextquad())
        
        def forcaseStat():

                global lex1
                global grammi
                
                if(lex1[0] == forcase_token):
                        lex1 = lex()
                        grammi = lex1[2]

                        p1quad=nextQuad()
                        
                        while(lex1[0] == case_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                
                                if(lex1[0] == aristeri_par_token):
                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                        con= condition()
                                        backpatch(con[0], nextQuad())
                                        
                                        if(lex1[0] == deksia_par_token):
                                                lex1 = lex()
                                                grammi = lex1[2]

                                                statements()
                                                genQuad('jump','_','_',p1quad)
                                                backpatch(con[1], nextQuad())

                                        else:
                                                print("sfalma :Sto forcase ! Den uparxei  deksia parenthesi", grammi)
                                                exit(-1)

                                else:
                                        print("sfalma :Sto forcase ! Den uparxei  aristeri parenthesi", grammi)
                                        exit(-1)

                        if(lex1[0] == default_token):
                                lex1 = lex()
                                grammi = lex1[2]

                                statements()
                        else:
                                print("sfalma :Sto forcase!Thema me tin default", grammi)
                                exit(-1)
                else:
                        print("sfalma :Sto forcase!", grammi)
                        exit(-1)
        

         #incaseStat : incase
                    #   (case (condition)statements)*   

        #S -> incase {P1}
            #( when (condition) do {P2}
                #sequence {P3}
                #end do ) *
            #endincase {P4}
        #{P1}:  w=newTemp()
                #p1Quad=nextquad()
                #genquad(“:=“,1,”_”,w)
        #{P2}: backpatch(cond.true,nextquad())
                #genquad(“:=“,0,”_”,w)
        #{P3}: backpatch(cond.false,nextquad())
        #{P4}: genquad(“=”, w,0,p1quad)            

        def incaseStat():

                global lex1
                global grammi
                ena=str(1)
                miden=str(0)
                
                if(lex1[0] == incase_token):
                        lex1 = lex()
                        grammi = lex1[2]


                        w = newTemp()
                        p1Quad=nextQuad()
                        genQuad(':=',ena,'_',w)#    p1
                        
                        while(lex1[0] == case_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                
                                if(lex1[0] == aristeri_par_token):
                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                        con = condition()
                                        backpatch(con[0], nextQuad())

                                        
                                        if(lex1[0] == deksia_par_token):
                                                lex1 = lex()
                                                grammi = lex1[2]

                                                statements()
                                                genQuad(':=',miden,'_',w)#p2
                                                backpatch(con[1], nextQuad() )#p3


                                        else:
                                                print("sfalma :Sto incase ! Den uparxei  deksia parenthesi", grammi)
                                                exit(-1)
                                else:
                                        print("sfalma :Sto forcase ! Den uparxei  aristeri parenthesi", grammi)
                                        exit(-1)


                        genQuad('=',w,miden,p1Quad)#p4
                else:
                        print("sfalma :Sto forcase !", grammi)
                        exit(-1)
                
         #returnstat : return (expression)
            #S -> return (E) {P1}
                #{P1}: genquad(“retv”,E.place,”_”,”_”)
                
        def returnStat():

                global lex1
                global grammi

                
                if(lex1[0] == return_token):

                        lex1 = lex()
                        grammi = lex1[2]

                        if(lex1[0] == aristeri_par_token):

                                lex1 = lex()
                                grammi = lex1[2]
                                
                                ex = expression()
                                genQuad('retv', ex, '_', '_')
                                
                                if(lex1[0] == deksia_par_token):

                                        lex1 = lex()
                                        grammi = lex1[2]
                                        return
                                else:
                                        print("sfalma :Sto returnstat!Den uparxei  deksia parenthesi",grammi)
                                        exit(-1)
                        else:
                                print("sfalma :Sto returnstat!Den uparxei  aristeri parenthesi", grammi)
                                exit(-1)



        #callStat : call ID (actualparlist)                  
                
        def callStat():

                global lex1
                global grammi
                
                if(lex1[0] == call_token):

                        lex1 = lex()
                        grammi = lex1[2]
                                
                        if(lex1[0] == id_token):

                                idc = lex1[1]
                                lex1 = lex()
                                grammi = lex1[2]

                                if(lex1[0] == aristeri_par_token):
                                        lex1 = lex()
                                        grammi = lex1[2]
                                
                                        actualparlist()
                                        genQuad('call', idc, '_', '_')
                                
                                        if(lex1[0] == deksia_par_token):
                                                lex1 = lex()
                                                grammi = lex1[2]
                                                return
                                        else:
                                                print("sfalma :Sto call ! Den kleinei h paranthesi",grammi)
                                                exit(-1)
                                else:
                                        print("sfalma :Sto call ! Den anoigei h paranthesi", grammi)
                                        exit(-1)
                                
                        else:
                                print("sfalma:Sto call! Meta tin call den uparxei id ", grammi)
                                exit(-1)
                else:
                        print("sfalma:Sto call!Problima me thn call",grammi)
                        exit(-1)
                
                return
        

        #printStat : print (expression)  

       # S -> print (E) {P2}
          #      {P2}: genquad(“out”,E.place,”_”,”_”)        
        def printStat():

                global lex1
                global grammi
                
                if(lex1[0] == print_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == aristeri_par_token):

                                lex1 = lex()
                                grammi = lex1[2]
                                
                                ex = expression()
                                genQuad('out', ex, '_', '_')
                                
                                if(lex1[0] == deksia_par_token):
                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                else:
                                        print("sfalma :Sto print ! Den kleinei h paranthesi",grammi)
                                        exit(-1)
                        else:
                                print("sfalma :Sto print ! Den anoigei h paranthesi", grammi)
                                exit(-1)
                else:
                        print("sfalma : Sto print!", grammi)
                        exit(-1)
                return
              
                
         #inputStat : input (ID) 

         #S -> input (id) {P1}
                    #{P1}: genquad(“inp”,id.place,”_”,”_”)
        def inputStat():

                global lex1
                global grammi
                
                if(lex1[0] == input_token):

                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == aristeri_par_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                
                                if(lex1[0] == id_token):
                                        idi = lex1[1]
                                        genQuad('inp',idi,'_','_')
                                        lex1 = lex()
                                        grammi = lex1[2]
                                        
                                        if(lex1[0] == deksia_par_token):
                                                lex1 = lex()
                                                grammi = lex1[2]
                                                return
                                                
                                        else:
                                                print("sfalma :Sto input ! Den kleinei h paranthesi",grammi)
                                                exit(-1)
                                else:
                                        print("sfalma :Sto input !Meta tin paranthesi den uparxei ID",grammi)
                                        exit(-1)
                        else:
                                print("sfalma :Sto input ! Den anoigei h paranthesi", grammi)
                                exit(-1)
                else:
                        print("sfalma :Sto input ! ", grammi)
                        exit(-1)



        #actualparlist : actualparitem ( , actualparitem)*
                    #   | e

        def actualparlist():
                global lex1
                global grammi 
                
                actualparitem()
                
                while(lex1[0] == koma_token):

                        lex1  = lex()
                        grammi = lex1[2]
                        
                        actualparitem()
                        
                return
                

        #actualparitem : in expression
        #              | inout ID                
        def actualparitem():

                global lex1
                global grammi
                

                if(lex1[0] == in_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        ex = expression()
                        genQuad('par', ex, 'CV', '_')
                        
                elif(lex1[0] == inout_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        if(lex1[0] == id_token):
                                name = lex1[1]

                                lex1 = lex()
                                grammi = lex1[2]

                                genQuad('par', name, 'REF', '_')
                                
                        else:
                                print("sfalma:Sto  actualparitem! Meta to inout prepei na uparxei ID ", grammi)
                                exit(-1)
                #else:
                     #   print("sfalma:Sto  actualparitem!", grammi)
                     #   exit(-1)
                
                return
             

          # condition : booltem (or boolterm )*                 
        def condition():

                global lex1
                global grammi

                true1 = []
                false1 = []
                boolterm1 = boolterm()

                true1 = boolterm1[0]
                false1 = boolterm1[1]
                
                while(lex1[0]==or_token):
                        lex1=lex()
                        grammi = lex1[2]

                        backpatch(false1, nextQuad())
                        
                        boolterm2 = boolterm()

                        true1 = merge(true1, boolterm2[0])

                        false1 = boolterm2[1]

                return true1, false1
                

         #boolterm  : boolfactor (and boolfactor )*                
        def boolterm():

                global lex1
                global grammi

                true2 = []
                false2 = []
                
                boolfactor1 = boolfactor()
                true2 = boolfactor1[0]
                false2 = boolfactor1[1]
        
                while(lex1[0]==and_token):
                        lex1=lex()
                        grammi = lex1[2]

                        backpatch(true2, nextQuad())
                        
                        boolfactor2 = boolfactor()

                        false2 = merge(false2, boolfactor2[1])
                        true2 = boolfactor2[0]

                return true2, false2


             

        #boolfactor  : not [condition]
        #             | [condition]
        #             | expression REL_OP expression                  
        def boolfactor():

                global lex1
                global grammi

                true3 = []
                false3 = []
                
                if(lex1[0]==not_token):

                        lex1=lex()
                        grammi = lex1[2]
                        
                        if(lex1[0]==aristeri_agk_token):

                                lex1 = lex()
                                grammi = lex1[2]
                                
                                con = condition()
                                
                                if(lex1[0]==deksia_agk_token):

                                        lex1 = lex()
                                        grammi = lex1[2]

                                        true3 = con[1]
                                        false3 = con[0]
                                        
                                else:
                                        print("sfalma : Sto boolfactor! Den kleinei ] ",grammi)
                                        exit(-1)
                        else:
                                print("sfalma : Sto boolfactor! Den anoigei [", grammi)
                                exit(-1)

                elif(lex1[0]==aristeri_agk_token):
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        con = condition()
                        
                        if(lex1[0]==deksia_agk_token):

                                lex1 = lex()
                                grammi = lex1[2]

                                true3 = con[0]
                                false3 = con[1]
                                
                        else:
                                print("sfalma: Sto boolfactor", grammi)
                                exit(-1)
                else:
                        
                        ex1 = expression()
                        
                        relational = relational_oper()
                        
                        ex2 = expression()

                        true3=makeList(nextQuad())
                        genQuad(relational, ex1, ex2, '_')
                        false3=makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')

                return true3, false3
                
                
         #expression :optinalSign term (ADD_OP  term )*                    
        def expression():

                global lex1
                global grammi
                
                optional_sign()
                
                term1 = term()
                

                while(lex1[0]==prosthesi_token or lex1[0]==afairesi_token):

                        prosthesiOrafairesis = add_oper()
                        
                        term2 = term()

                        w = newTemp()
                        genQuad(prosthesiOrafairesis, term1, term2, w)
                        term1 = w

                ex = term1
                return ex
                
                
                 
        #term : factor (MUL_OP factor)*                 
        def term():

                global lex1
                global grammi
                
                factor1 = factor()
                
                while(lex1[0]==pol_token or lex1[0]==diairesi_token):

                        mulOper = mul_oper()
                        
                        factor2 = factor()

                        w=newTemp()
                        genQuad(mulOper, factor1, factor2, w)
                        factor1 = w
                factor3 =factor1
                return factor3
                

        #factor : INTEGER 
        #       | (expression)
        #       | ID idtail                
                                
        def factor():

                global lex1
                global grammi
                
                if(lex1[0]==number_token):

                        factor1 = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                elif(lex1[0]==aristeri_par_token):

                        lex1 = lex()
                        grammi = lex1[2]

                        ex = expression()
                        factor1 = ex
                        if(lex1[0]==deksia_par_token):

                                lex1 = lex()
                                grammi = lex1[2]
                                
                        else:
                                print("sfalma sto factos ! Meta to expression den uparxei paranthsei ",grammi)
                                exit(-1)

                elif(lex1[0]==id_token):

                        factor2 = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                        factor1 = idtail(factor2)
                        
                else:
                        print("sfalma :sto factor!",grammi)
                        exit(-1)
                
                return factor1
                
                

        #idtail   : (actualparlist)
        #         | e         
        def idtail(name):
                global lex1
                global grammi
                
                if(lex1[0] == aristeri_par_token ):
                        lex1 = lex()
                        grammi = lex1[2]

                        actualparlist()
                        w=newTemp()
                        genQuad('par', w, 'RET', '_')
                        genQuad('call', name, '_', '_')
                        
                        if(lex1[0]==deksia_par_token):
                                lex1 = lex()
                                grammi = lex1[2]
                                return w
                        else:
                                print("sfalma :sto idtail!",grammi)
                                exit(-1)
                        
                else:
                        return name


        #optionalSign : ADD_OP
        #             | e
        def optional_sign():

                global lex1
                global grammi
                
                if(lex1[0] == prosthesi_token or lex1[0] == afairesi_token):
                        
                        add_oper()
                        
                return
             

        #rel_op : =|<=|>=|>|<|<>
        #       ;                 
        def relational_oper():

                global lex1 
                global grammi
                
                if(lex1[0]==isotita_token):
                        relational = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                elif(lex1[0]==mikrotero_token):

                        relational = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                elif(lex1[0]==mikrotero_iso_token):

                        relational = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                elif(lex1[0]==diaforo_token):

                        relational = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                elif(lex1[0]== megalutero_token):

                        relational = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        

                elif(lex1[0]==megalutero_iso_token):

                        relational = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                else:
                        print("sfalma:sto relational_oper!",grammi)
                        exit(-1)

                return relational



        #add_op : +|-                  
        def add_oper():

                global lex1 
                global grammi
                
                if(lex1[0]==prosthesi_token):

                        addOp = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        

                elif(lex1[0]==afairesi_token):

                        addOp = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                return addOp


        #mul_op : *|/
        def mul_oper():

                global lex1 
                global grammi
                
                if (lex1[0] == pol_token):

                        oper = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]
                        
                elif (lex1[0] == diairesi_token):

                        oper = lex1[1]
                        lex1 = lex()
                        grammi = lex1[2]

                return oper





        program()


        return




#Isodunamos se C kwdikas
def conversionCodeC(cCodeF):

    global lista_met
    L=str("L_")
    akteleia=str(" : ")
    iso=str(" = ")
    er1=" ;\n\t"
    if1=" if ("
    goto1=" )  goto L_"


    if(len(lista_met)!=0):
        cCodeF.write("int ")



    for i in range(len(lista_met)):

        cCodeF.write(lista_met[i])
        if(len(lista_met) == i+1):
            cCodeF.write(" ;\n\t")

        else:
            cCodeF.write(",")

    
    for j in range(len(lista_tetradwn)):

        if(lista_tetradwn[j][1] == 'begin_block'):
            cCodeF.write(L+str(j+1)+":\n\n\t")

            #:=
        elif(lista_tetradwn[j][1] == ":= "):
            cCodeF.write(L+str(j+1)+akteleia+ lista_tetradwn[j][4]+ iso +lista_tetradwn[j][2]+er1)

        elif(lista_tetradwn[j][1] == "+"):
            cCodeF.write(L+str(j+1)+akteleia+ lista_tetradwn[j][4]+iso+lista_tetradwn[j][2]+" + "+lista_tetradwn[j][3]+er1)

        elif(lista_tetradwn[j][1] == "-"):
            cCodeF.write(L+str(j+1)+akteleia+ lista_tetradwn[j][4]+ iso +lista_tetradwn[j][2]+" - "+lista_tetradwn[j][3]+er1)

        elif(lista_tetradwn[j][1] == "*"):
            cCodeF.write(L+str(j+1)+akteleia+ lista_tetradwn[j][4]+ iso +lista_tetradwn[j][2]+" * "+lista_tetradwn[j][3]+er1)
            
        elif(lista_tetradwn[j][1] == "<"):
            cCodeF.write(L+str(j+1)+akteleia+if1+lista_tetradwn[j][2]+" < "+lista_tetradwn[j][3]+ goto1+str(lista_tetradwn[j][4])+er1)

        elif(lista_tetradwn[j][1] == ">"):
            cCodeF.write(L+str(j+1)+akteleia+if1+lista_tetradwn[j][2]+" > "+lista_tetradwn[j][3]+goto1+str(lista_tetradwn[j][4])+er1)

        elif(lista_tetradwn[j][1] == ">="):
            cCodeF.write(L+str(j+1)+akteleia+if1+lista_tetradwn[j][2]+" >= "+lista_tetradwn[j][3]+goto1+str(lista_tetradwn[j][4])+er1)

        elif(lista_tetradwn[j][1] == "<="):
            cCodeF.write(L+str(j+1)+akteleia+if1+lista_tetradwn[j][2]+" <= "+lista_tetradwn[j][3]+goto1+str(lista_tetradwn[j][4])+er1)

        elif(lista_tetradwn[j][1] == "<>"):
            cCodeF.write(L+str(j+1)+akteleia+if1+str(lista_tetradwn[j][2])+" != "+str(lista_tetradwn[j][3])+goto1+str(lista_tetradwn[j][4])+er1)

        elif(lista_tetradwn[j][1] == "="):
            cCodeF.write(L+str(j+1)+akteleia+if1+lista_tetradwn[j][2]+ iso + iso +lista_tetradwn[j][3]+goto1+str(lista_tetradwn[j][4])+er1)


        elif(lista_tetradwn[j][1] == "/"):
            cCodeF.write(L+str(j+1)+akteleia+ lista_tetradwn[j][4]+ iso +lista_tetradwn[j][2]+"/"+lista_tetradwn[j][3]+er1)

        elif(lista_tetradwn[j][1] == "jump"):
            cCodeF.write(L+str(j+1)+akteleia+"goto L_"+str(lista_tetradwn[j][4])+ er1)


        elif(lista_tetradwn[j][1] == "out"):
            cCodeF.write(L+str(j+1)+akteleia+"printf(\""+lista_tetradwn[j][2]+iso+"%d\", "+lista_tetradwn[j][2]+")"+er1)

        elif(lista_tetradwn[j][1] == 'halt'):
            cCodeF.write(L+str(j+1)+akteleia+" {}\n\t")



# se int kwdikas
def conversionIntCode(intF):
    keno1= "  "

    intF.write("\n")
    for i in range(len(lista_tetradwn)):
        

        quad = lista_tetradwn[i]

        intF.write(str(quad[0]))
        intF.write(":  ")

        intF.write(str(quad[1]))
        intF.write(keno1)
        intF.write(str(quad[2]))
        intF.write(keno1)
        intF.write(str(quad[3]))
        intF.write(keno1)
        intF.write(str(quad[4]))
        intF.write("\n")






def fileIntC():

        global cCodeF

  
        intCodeF = open('intCodeF.int', 'w')
        cCodeF = open('cCodeF.c', 'w')
        #f=open()

        cCodeF.write("int main(){\n\t")



        #print("prin ton suntaktiko!")
        suntaktikos(intCodeF)
        print("Teleiwse o suntaktikos!")

        conversionIntCode(intCodeF)
        conversionCodeC(cCodeF)

        cCodeF.write("\n}")


        cCodeF.close()
        intCodeF.close()





fileIntC()


#suntaktikos()
#telos syntaktikou analyti
print("GINETAI SWSTA !")


#ektupwsei tetradwn 
def print_lista_tetradwn():

    keno1="  "
    koma1=" , "

    for i in range(len(lista_tetradwn)):
        print (keno1 + str(lista_tetradwn[i][0])+koma1+str(lista_tetradwn[i][1])+koma1+str(lista_tetradwn[i][2])
                    + koma1 +str(lista_tetradwn[i][3])+ koma1 +str(lista_tetradwn[i][4]))
#print_lista_tetradwn()

print(" OK tiponwntai oi tetrades!")



