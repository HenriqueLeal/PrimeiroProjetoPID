'''
**************************************************
* Digital Image Processing Activity              *
* Prof. Dr. Aparecido Nilceu Marana              *
* PPGCC - UNESP Bauru                            *
* Henrique Leal Tavares                          *
* 09/2018                                        *
* WLD of Brodatz Album and Under the Curve Calc. *
**************************************************
'''

descriptorgen = 1
allimg = dir(mstring('*.gif'))
imgn = length(allimg)
if descriptorgen:
    histogenerate = zeros(16, 96)
    histo = zeros(1, 96)
	
	
    for i in mslice[1:imgn]:
        found = allimg(i).name
        img = imread(found)
        [subimage1, subimage2, subimage3, subimage4, subimage5, subimage6, subimage7, subimage8, subimage9, subimage10, subimage11, subimage12, subimage13, subimage14, subimage15, subimage16] = cortaImagem(img)
        histogenerate(1, mslice[:]).lvalue = calc(subimage1)
        histogenerate(2, mslice[:]).lvalue = calc(subimage2)
        histogenerate(3, mslice[:]).lvalue = calc(subimage3)
        histogenerate(4, mslice[:]).lvalue = calc(subimage4)
        histogenerate(5, mslice[:]).lvalue = calc(subimage5)
        histogenerate(6, mslice[:]).lvalue = calc(subimage6)
        histogenerate(7, mslice[:]).lvalue = calc(subimage7)
        histogenerate(8, mslice[:]).lvalue = calc(subimage8)
        histogenerate(9, mslice[:]).lvalue = calc(subimage9)
        histogenerate(10, mslice[:]).lvalue = calc(subimage10)
        histogenerate(11, mslice[:]).lvalue = calc(subimage11)
        histogenerate(12, mslice[:]).lvalue = calc(subimage12)
        histogenerate(13, mslice[:]).lvalue = calc(subimage13)
        histogenerate(14, mslice[:]).lvalue = calc(subimage14)
        histogenerate(15, mslice[:]).lvalue = calc(subimage15)
        histogenerate(16, mslice[:]).lvalue = calc(subimage16)
        histo = vertcat(histo, histogenerate)
     
    histo(1, mslice[:]).lvalue = mcat([])
    for i in mslice[1:imgn]:
        imag(mslice[(i * 16) - 15:i * 16], 1).lvalue = i
     
    frag = 0
    frag_template = mcat([1, OMPCSEMI, 2, OMPCSEMI, 3, OMPCSEMI, 4, OMPCSEMI, 5, OMPCSEMI, 6, OMPCSEMI, 7, OMPCSEMI, 8, OMPCSEMI, 9, OMPCSEMI, 10, OMPCSEMI, 11, OMPCSEMI, 12, OMPCSEMI, 13, OMPCSEMI, 14, OMPCSEMI, 15, OMPCSEMI, 16])
	for i in mslice[1:imgn]:
    frag = vertcat(frag, frag_template)
 
frag(1, mslice[:]).lvalue = mcat([])
template = horzcat(imag, frag)
maxv = max(max(histo))
minv = min(min(histo))
for i in mslice[1:size(histo, 1)]:
    for j in mslice[1:size(histo, 2)]:
        histo(i, j).lvalue = (histo(i, j) - minv) / maxv - minv
     
 
histo_identificavel = horzcat(template, histo)
matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in mslice[1:imgn]:
    query = buscaClasseDatabase(i, histo_identificavel)
    matriz_precision_recall = vertcat(matriz_precision_recall, query)
matriz_precision_recall(1, mslice[:]).lvalue = mcat([])
pr_media = mcat([mean(matriz_precision_recall(mslice[:], 1)), mean(matriz_precision_recall(mslice[:], 2)), mean(matriz_precision_recall(mslice[:], 3)), mean(matriz_precision_recall(mslice[:], 4)), mean(matriz_precision_recall(mslice[:], 5)), mean(matriz_precision_recall(mslice[:], 6)), mean(matriz_precision_recall(mslice[:], 7)), mean(matriz_precision_recall(mslice[:], 8)), mean(matriz_precision_recall(mslice[:], 9)), mean(matriz_precision_recall(mslice[:], 10)), mean(matriz_precision_recall(mslice[:], 11)), mean(matriz_precision_recall(mslice[:], 12)), mean(matriz_precision_recall(mslice[:], 13)), mean(matriz_precision_recall(mslice[:], 14)), mean(matriz_precision_recall(mslice[:], 15))])
recall = mcat([1 / 15, 2 / 15, 3 / 15, 4 / 15, 5 / 15, 6 / 15, 7 / 15, 8 / 15, 9 / 15, 10 / 15, 11 / 15, 12 / 15, 13 / 15, 14 / 15, 15 / 15])
WLD = vertcat(recall, pr_media)
hold(mstring('on'))
plot(WLD(1, mslice[:]), WLD(2, mslice[:]), mstring('-gx'))
leg (mstring('LBP'), mstring('GLCM'), mstring('WLD'))
@mfunction("value")
def calc(img=None):
    filtro1 = mcat([1, 1, 1, OMPCSEMI, 1, -8, 1, OMPCSEMI, 1, 1, 1])
    filtro2 = mcat([0, 0, 0, OMPCSEMI, 0, 1, 0, OMPCSEMI, 0, 0, 0])
    filtro3 = mcat([1, 2, 1, OMPCSEMI, 0, 0, 0, OMPCSEMI, -1, -2, -1])
    filtro4 = mcat([1, 0, -1, 2, 0, -2, 1, 0, -1])
    vetor1 = filter2(filtro1, img)
    vetor2 = filter2(filtro2, img)
    [linhas, colunas] = size(vetor1)
    ext = zeros(1, 8)
    for i in mslice[1:linhas]:
        for j in mslice[1:colunas]:
            a(i, j).lvalue = atan(vetor1(i, j) / vetor2(i, j))
            k = secondclassificator(a(i, j))
            ext(k).lvalue = ext(k) + 1
         
     
	v3 = filter2(filtro3, img)
    v4 = filter2(filtro4, img)
    ori = zeros(1, 12)
for i in mslice[1:linhas]:
    for j in mslice[1:colunas]:
        Theta(i, j).lvalue = atan(v3(i, j) / v4(i, j))    #??a
        if v3(i, j) > 0 and v4(i, j) > 0:
@mfunction("result")
def firstclass(x=None):
    if x >= logical_and(0, x < 0.15 * pi):
        result = 1
    elif x >= logical_and(0.15 * pi, x < 0.35 * pi):
        result = 2
    elif x >= logical_and(0.35 * pi, x < 0.5 * pi):
        result = 3
    elif x >= logical_and(0.5 * pi, x < 0.65 * pi):
        result = 4
    elif x >= logical_and(0.65 * pi, x < 0.85 * pi):
        result = 5
    elif x >= logical_and(0.85 * pi, x < pi):
        result = 6
    elif x >= logical_and(pi, x < 1.15 * pi):
        result = 7
    elif x >= logical_and(1.15 * pi, x < 1.35 * pi):
        result = 8
    elif x >= logical_and(1.35 * pi, x < 1.5 * pi):
        result = 9
    elif x >= logical_and(1.5 * pi, x < 1.65 * pi):
        result = 10
    elif x >= logical_and(1.65 * pi, x < 1.85 * pi):
        result = 11
    else:
        result = 12
     
 
@mfunction("result")
def secondclassificator(x=None):
    if logical_and((x >= (-0.5 * pi)), (x < (-0.3 * pi))):
        result = 1
    elif x >= logical_and(-0.3 * pi, x < -0.15 * pi):
        result = 2
    elif x >= logical_and(-0.15 * pi, x < -0.05 * pi):
        result = 3
    elif x >= logical_and(-0.05 * pi, x < 0):
        result = 4
    elif x >= logical_and(0, x < 0.05 * pi):
        result = 5
    elif x >= logical_and(0.05 * pi, x < 0.15 * pi):
        result = 6
    elif x >= logical_and(0.15 * pi, x < 0.25 * pi):
        result = 7
    else:
        result = 8
     
 
@mfunction("precisionRecallCurve")
def buscaClasseDatabase(classe=None, database=None):
    database_ord = ordenaPelaDistancia(classe, database)
    database_ord()
    precisionRecallCurve = zeros(1, 15)
    count = 0
    for i in mslice[1:size(database_ord, 1)]:
        if database_ord(i, 1) == classe:
            count = count + 1
            divisor = i
            if (count == 1) and (divisor == 1):
            else:
                precisionRecallCurve(1, count - 1).lvalue = count / divisor
             
         
     
 
@mfunction("database")
def ordenaPelaDistancia(classe=None, database=None):
    for i in mslice[1:size(database, 1)]:
        if database(i, 2) == 1:
            if database(i, 1) == classe:
                valor = database(i, mslice[3:98])
             
         
     
    for i in mslice[1:size(database, 1)]:
        database(i, 99).lvalue = norm(valor - database(i, mslice[3:98]))
     
    database = sortrows(database, 99)
 