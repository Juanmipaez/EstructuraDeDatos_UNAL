CandidatosyVotos = {}
Votantes = set()

while True:
    idVot, idCand = input().split()
    if (idVot, idCand) == ("0", "0"):
        break
    else:
        if idCand not in CandidatosyVotos and idVot not in Votantes:
            CandidatosyVotos[idCand] = {idVot}
            Votantes.add(idVot)
        elif  idCand in CandidatosyVotos and idVot not in Votantes:
            CandidatosyVotos[idCand].add(idVot)
            Votantes.add(idVot)
        
        elif idVot in Votantes:
            for votantes_candidato in CandidatosyVotos:
                if idVot in CandidatosyVotos[votantes_candidato]:
                    CandidatosyVotos[votantes_candidato].remove(idVot)
                    break

ResultadosOrdenados = dict(sorted(CandidatosyVotos.items(), key=lambda x: (len(x[1]), int(x[0])), reverse=True))
for candidato in ResultadosOrdenados:
    if ResultadosOrdenados[candidato]:
        print(candidato, len(ResultadosOrdenados[candidato]))