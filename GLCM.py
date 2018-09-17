imgn = length(imgt)

for i in mslice[1:imgn]:
    imag(mslice[(i * 16) - 15:i * 16], 1).lvalue = i
    frag = 0
    frag_template = mcat([1, OMPCSEMI, 2, OMPCSEMI, 3, OMPCSEMI, 4, OMPCSEMI, 5, OMPCSEMI, 6, OMPCSEMI, 7, OMPCSEMI, 8, OMPCSEMI, 9, OMPCSEMI, 10, OMPCSEMI, 11, OMPCSEMI, 12, OMPCSEMI, 13, OMPCSEMI, 14, OMPCSEMI, 15, OMPCSEMI, 16])
    for i in mslice[1:imgn]:
        frag = vertcat(frag, frag_template)
        frag(1, mslice[:]).lvalue = mcat([])
        template = horzcat(imag, frag)
        matriz_contrastes_0 = cat(2, matriz_contrastes_0, imag, frag)
        matriz_contrastes_135 = cat(2, matriz_contrastes_135, imag, frag)
        matriz_contrastes_45 = cat(2, matriz_contrastes_45, imag, frag)
        matriz_contrastes_90 = cat(2, matriz_contrastes_90, imag, frag)
        matriz_energias_0 = cat(2, matriz_energias_0, imag, frag)
        matriz_energias_135 = cat(2, matriz_energias_135, imag, frag)
        matriz_energias_45 = cat(2, matriz_energias_45, imag, frag)
        matriz_energias_90 = cat(2, matriz_energias_90, imag, frag)
        matriz_entropias_0 = cat(2, matriz_entropias_0, imag, frag)
        matriz_entropias_135 = cat(2, matriz_entropias_135, imag, frag)
        matriz_entropias_45 = cat(2, matriz_entropias_45, imag, frag)
        matriz_entropias_90 = cat(2, matriz_entropias_90, imag, frag)
        matriz_homog_0 = cat(2, matriz_homog_0, imag, frag)
        matriz_homog_135 = cat(2, matriz_homog_135, imag, frag)
        matriz_homog_45 = cat(2, matriz_homog_45, imag, frag)
        matriz_homog_90 = cat(2, matriz_homog_90, imag, frag)
        z = mcat([0, 0, 0])
        z = vertcat(z, matriz_contrastes_135, matriz_contrastes_45, matriz_contrastes_90, matriz_energias_0, matriz_energias_135, matriz_energias_45, matriz_energias_90, matriz_entropias_0, matriz_entropias_135, matriz_entropias_45, matriz_entropias_90, matriz_homog_0, matriz_homog_135, matriz_homog_45, matriz_homog_90, matriz_contrastes_0)
        z(1, mslice[:]).lvalue = mcat([])
        zmax = max(max(z))
        zmin = min(min(z))
		for i in mslice[1:size(matriz_contrastes_0, 1)]:
    matriz_contrastes_0(i, 1).lvalue = (matriz_contrastes_0(i, 1) - zmin) / (zmax - zmin)
    
    for i in mslice[1:size(matriz_contrastes_135, 1)]:
        matriz_contrastes_135(i, 1).lvalue = (matriz_contrastes_135(i, 1) - zmin) / (zmax - zmin)
        
        for i in mslice[1:size(matriz_contrastes_45, 1)]:
            matriz_contrastes_45(i, 1).lvalue = (matriz_contrastes_45(i, 1) - zmin) / (zmax - zmin)
            
            for i in mslice[1:size(matriz_contrastes_90, 1)]:
                matriz_contrastes_90(i, 1).lvalue = (matriz_contrastes_90(i, 1) - zmin) / (zmax - zmin)
                
                for i in mslice[1:size(matriz_energias_0, 1)]:
                    matriz_energias_0(i, 1).lvalue = (matriz_energias_0(i, 1) - zmin) / (zmax - zmin)
                    
                    for i in mslice[1:size(matriz_energias_135, 1)]:
                        matriz_energias_135(i, 1).lvalue = (matriz_energias_135(i, 1) - zmin) / (zmax - zmin)
                        
                        for i in mslice[1:size(matriz_energias_45, 1)]:
                            matriz_energias_45(i, 1).lvalue = (matriz_energias_45(i, 1) - zmin) / (zmax - zmin)
                            
                            for i in mslice[1:size(matriz_energias_90, 1)]:
                                matriz_energias_90(i, 1).lvalue = (matriz_energias_90(i, 1) - zmin) / (zmax - zmin)
                                
                                for i in mslice[1:size(matriz_entropias_0, 1)]:
                                    matriz_entropias_0(i, 1).lvalue = (matriz_entropias_0(i, 1) - zmin) / (zmax - zmin)
                                    
                                    for i in mslice[1:size(matriz_entropias_135, 1)]:
                                        matriz_entropias_135(i, 1).lvalue = (matriz_entropias_135(i, 1) - zmin) / (zmax - zmin)
                                        
                                        for i in mslice[1:size(matriz_entropias_45, 1)]:
                                            matriz_entropias_45(i, 1).lvalue = (matriz_entropias_45(i, 1) - zmin) / (zmax - zmin)
                                            
                                            for i in mslice[1:size(matriz_entropias_90, 1)]:
                                                matriz_entropias_90(i, 1).lvalue = (matriz_entropias_90(i, 1) - zmin) / (zmax - zmin)
                                                
for i in mslice[1:size(matriz_homog_0, 1)]:
    matriz_homog_0(i, 1).lvalue = (matriz_homog_0(i, 1) - zmin) / (zmax - zmin)
    
    for i in mslice[1:size(matriz_homog_135, 1)]:
        matriz_homog_135(i, 1).lvalue = (matriz_homog_135(i, 1) - zmin) / (zmax - zmin)
        
        for i in mslice[1:size(matriz_homog_45, 1)]:
            matriz_homog_45(i, 1).lvalue = (matriz_homog_45(i, 1) - zmin) / (zmax - zmin)
            
            for i in mslice[1:size(matriz_homog_90, 1)]:
                matriz_homog_90(i, 1).lvalue = (matriz_homog_90(i, 1) - zmin) / (zmax - zmin)
                
                matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                for amostra in mslice[1:imgn]:
                    matriz_precision_recall = buscaClasseDatabase(amostra, matriz_contrastes_0) + matriz_precision_recall
                    
                    media_matriz_contrastes_0 = matriz_precision_recall / imgn
                    matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                    for amostra in mslice[1:imgn]:
                        matriz_precision_recall = buscaClasseDatabase(amostra, matriz_contrastes_135) + matriz_precision_recall
                        
                        media_matriz_contrastes_135 = matriz_precision_recall / imgn
                        matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                        for amostra in mslice[1:imgn]:
                            matriz_precision_recall = buscaClasseDatabase(amostra, matriz_contrastes_45) + matriz_precision_recall
                            
                            media_matriz_contrastes_45 = matriz_precision_recall / imgn
                            matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                            for amostra in mslice[1:imgn]:
                                matriz_precision_recall = buscaClasseDatabase(amostra, matriz_contrastes_90) + matriz_precision_recall
                                
                                media_matriz_contrastes_90 = matriz_precision_recall / imgn
                                matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                for amostra in mslice[1:imgn]:
                                    matriz_precision_recall = buscaClasseDatabase(amostra, matriz_energias_0) + matriz_precision_recall
                                    
                                    media_matriz_energias_0 = matriz_precision_recall / imgn
                                    matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                    for amostra in mslice[1:imgn]:
                                        matriz_precision_recall = buscaClasseDatabase(amostra, matriz_energias_135) + matriz_precision_recall
                                        
                                        media_matriz_energias_135 = matriz_precision_recall / imgn
                                        matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                        for amostra in mslice[1:imgn]:
                                            matriz_precision_recall = buscaClasseDatabase(amostra, matriz_energias_45) + matriz_precision_recall
                                            
                                            media_matriz_energias_45 = matriz_precision_recall / imgn
                                            matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                            for amostra in mslice[1:imgn]:
                                                matriz_precision_recall = buscaClasseDatabase(amostra, matriz_energias_90) + matriz_precision_recall
                                                
                                                media_matriz_energias_90 = matriz_precision_recall / imgn
                                                matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                                for amostra in mslice[1:imgn]:
                                                    matriz_precision_recall = buscaClasseDatabase(amostra, matriz_entropias_0) + matriz_precision_recall
                                                    
                                                    media_matriz_entropias_0 = matriz_precision_recall / imgn
                                                    matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                                    for amostra in mslice[1:imgn]:
                                                        matriz_precision_recall = buscaClasseDatabase(amostra, matriz_entropias_135) + matriz_precision_recall
                                                        
                                                        media_matriz_entropias_135 = matriz_precision_recall / imgn
                                                        matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                                        for amostra in mslice[1:imgn]:
                                                            matriz_precision_recall = buscaClasseDatabase(amostra, matriz_entropias_45) + matriz_precision_recall
                                                            
                                                            media_matriz_entropias_45 = matriz_precision_recall / imgn
                                                            matriz_precision_recall = mcat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                                                            for amostra in mslice[1:imgn]:
                                                                matriz_precision_recall = buscaClasseDatabase(amostra, matriz_entropias_90) + matriz_precision_recall

if gerarDescritores:
    matriz_energias_0 = 0
    matriz_energias_45 = 0
    matriz_energias_90 = 0
    matriz_energias_135 = 0
    for i in mslice[1:imgn]:
        imgEncontrada = imgt(i).name
        img = imread(imgEncontrada)
		[parte1, parte2, parte3, parte4, parte5, parte6, parte7, parte8, parte9, parte10, parte11, parte12, parte13, parte14, parte15, parte16] = cortaImagem(img)
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte1, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte1, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte1, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte1, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte2, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte2, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte2, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte2, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte3, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte3, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte3, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte3, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte4, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte4, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte4, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte4, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte5, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte5, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte5, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte5, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte6, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte6, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte6, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte6, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte7, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte7, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte7, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte7, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte8, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte8, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte8, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte8, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte9, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte9, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte9, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte9, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte10, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte10, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte10, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte10, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte11, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte11, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte11, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte11, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte12, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte12, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte12, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte12, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte13, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte13, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte13, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte13, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte14, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte14, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte14, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte14, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte15, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte15, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte15, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte15, 135)))
    matriz_energias_0 = vertcat(matriz_energias_0, calcEnergia(buscaVizinhos(parte16, 0)))
    matriz_energias_45 = vertcat(matriz_energias_45, calcEnergia(buscaVizinhos(parte16, 45)))
    matriz_energias_90 = vertcat(matriz_energias_90, calcEnergia(buscaVizinhos(parte16, 90)))
    matriz_energias_135 = vertcat(matriz_energias_135, calcEnergia(buscaVizinhos(parte16, 135)))
matriz_energias_0(1, mslice[:]).lvalue = mcat([])
matriz_energias_45(1, mslice[:]).lvalue = mcat([])
matriz_energias_90(1, mslice[:]).lvalue = mcat([])
matriz_energias_135(1, mslice[:]).lvalue = mcat([])
matriz_contrastes_0 = 0
matriz_contrastes_45 = 0
matriz_contrastes_90 = 0
matriz_contrastes_135 = 0
for i in mslice[1:imgn]:
    imgEncontrada = imgt(i).name
    img = imread(imgEncontrada)
    [parte1, parte2, parte3, parte4, parte5, parte6, parte7, parte8, parte9, parte10, parte11, parte12, parte13, parte14, parte15, parte16] = cortaImagem(img)
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte1, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte1, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte1, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte1, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte2, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte2, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte2, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte2, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte3, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte3, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte3, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte3, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte4, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte4, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte4, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte4, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte5, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte5, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte5, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte5, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte6, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte6, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte6, 90)))
	matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte6, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte7, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte7, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte7, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte7, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte8, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte8, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte8, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte8, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte9, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte9, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte9, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte9, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte10, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte10, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte10, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte10, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte11, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte11, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte11, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte11, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte12, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte12, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte12, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte12, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte13, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte13, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte13, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte13, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte14, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte14, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte14, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte14, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte15, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte15, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte15, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte15, 135)))
    matriz_contrastes_0 = vertcat(matriz_contrastes_0, calcContraste(buscaVizinhos(parte16, 0)))
    matriz_contrastes_45 = vertcat(matriz_contrastes_45, calcContraste(buscaVizinhos(parte16, 45)))
    matriz_contrastes_90 = vertcat(matriz_contrastes_90, calcContraste(buscaVizinhos(parte16, 90)))
    matriz_contrastes_135 = vertcat(matriz_contrastes_135, calcContraste(buscaVizinhos(parte16, 135)))
matriz_contrastes_0(1, mslice[:]).lvalue = mcat([])
matriz_contrastes_45(1, mslice[:]).lvalue = mcat([])
matriz_contrastes_90(1, mslice[:]).lvalue = mcat([])
matriz_contrastes_135(1, mslice[:]).lvalue = mcat([])
matriz_entropias_0 = 0
matriz_entropias_45 = 0
matriz_entropias_90 = 0
matriz_entropias_135 = 0
for i in mslice[1:imgn]:
    imgEncontrada = imgt(i).name
    img = imread(imgEncontrada)
    [parte1, parte2, parte3, parte4, parte5, parte6, parte7, parte8, parte9, parte10, parte11, parte12, parte13, parte14, parte15, parte16] = cortaImagem(img)
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte1, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte1, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte1, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte1, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte2, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte2, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte2, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte2, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte3, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte3, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte3, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte3, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte4, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte4, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte4, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte4, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte5, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte5, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte5, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte5, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte6, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte6, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte6, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte6, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte7, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte7, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte7, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte7, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte8, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte8, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte8, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte8, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte9, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte9, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte9, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte9, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte10, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte10, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte10, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte10, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte11, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte11, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte11, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte11, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte12, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte12, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte12, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte12, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte13, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte13, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte13, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte13, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte14, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte14, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte14, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte14, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte15, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte15, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte15, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte15, 135)))
    matriz_entropias_0 = vertcat(matriz_entropias_0, calcEntropia(buscaVizinhos(parte16, 0)))
    matriz_entropias_45 = vertcat(matriz_entropias_45, calcEntropia(buscaVizinhos(parte16, 45)))
    matriz_entropias_90 = vertcat(matriz_entropias_90, calcEntropia(buscaVizinhos(parte16, 90)))
    matriz_entropias_135 = vertcat(matriz_entropias_135, calcEntropia(buscaVizinhos(parte16, 135)))
matriz_entropias_0(1, mslice[:]).lvalue = mcat([])
matriz_entropias_45(1, mslice[:]).lvalue = mcat([])
matriz_entropias_90(1, mslice[:]).lvalue = mcat([])
matriz_entropias_135(1, mslice[:]).lvalue = mcat([])
matriz_homog_0 = 0
matriz_homog_45 = 0
matriz_homog_90 = 0
matriz_homog_135 = 0
for i in mslice[1:imgn]:
    imgEncontrada = imgt(i).name
    img = imread(imgEncontrada)
    [parte1, parte2, parte3, parte4, parte5, parte6, parte7, parte8, parte9, parte10, parte11, parte12, parte13, parte14, parte15, parte16] = cortaImagem(img)
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte1, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte1, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte1, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte1, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte2, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte2, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte2, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte2, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte3, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte3, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte3, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte3, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte4, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte4, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte4, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte4, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte5, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte5, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte5, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte5, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte6, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte6, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte6, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte6, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte7, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte7, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte7, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte7, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte8, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte8, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte8, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte8, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte9, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte9, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte9, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte9, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte10, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte10, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte10, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte10, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte11, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte11, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte11, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte11, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte12, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte12, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte12, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte12, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte13, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte13, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte13, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte13, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte14, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte14, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte14, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte14, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte15, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte15, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte15, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte15, 135)))
    matriz_homog_0 = vertcat(matriz_homog_0, calcHomogeneidade(buscaVizinhos(parte16, 0)))
    matriz_homog_45 = vertcat(matriz_homog_45, calcHomogeneidade(buscaVizinhos(parte16, 45)))
    matriz_homog_90 = vertcat(matriz_homog_90, calcHomogeneidade(buscaVizinhos(parte16, 90)))
    matriz_homog_135 = vertcat(matriz_homog_135, calcHomogeneidade(buscaVizinhos(parte16, 135)))
matriz_homog_0(1, mslice[:]).lvalue = mcat([])
matriz_homog_45(1, mslice[:]).lvalue = mcat([])
matriz_homog_90(1, mslice[:]).lvalue = mcat([])
matriz_homog_135(1, mslice[:]).lvalue = mcat([])

                                                                
for i in mslice[1:size(matriz_vizinhos, 1)]:
    for j in mslice[1:size(matriz_vizinhos, 2)]:
        energia = matriz_vizinhos(i, j) ** 2 + energia
@mfunction("contraste")
def calcContraste(matriz_vizinhos=None):
    contraste = 0
    for i in mslice[1:size(matriz_vizinhos, 1)]:
        for j in mslice[1:size(matriz_vizinhos, 2)]:
            contraste = (((i - j) ** 2) * matriz_vizinhos(i, j)) + contraste
@mfunction("homog")
def calcHomogeneidade(matriz_vizinhos=None):
    homog = 0
    for i in mslice[1:size(matriz_vizinhos, 1)]:
        for j in mslice[1:size(matriz_vizinhos, 2)]:
            if matriz_vizinhos(i, j) != 0:
                homog = double((matriz_vizinhos(i, j) / (((i - j) ** 2) + 1)) + homog)
            else:
                homog = homog + 0