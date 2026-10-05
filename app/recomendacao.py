def gerar_recomendacao(imc : float, objetivo : str) -> str : 
    if objetivo.lower() == "hipertrofia":
        if imc < 18.5 :
            return "Seu IMC está abaixo do ideal. Para ganhar massa, priorize treino de força progressivo, boa ingestão de proteínas e calorias suficientes. Vale o acompanhamento de um nutricionista."
        elif imc < 25 : 
            return "Seu IMC está na faixa saudável. Foque em progressão de carga, sono em dia e proteína suficiente para sustentar o ganho de massa."
        else : 
            return "Seu IMC passa de 25, mas ele não diferencia massa muscular de gordura. Mantenha o treino de força e acompanhe a evolução também por outras medidas, como circunferências."

        
    elif objetivo.lower() == "emagrecimento":
        if imc < 18.5 :
            return "Seu IMC já está abaixo do ideal, então emagrecer não é recomendado agora. Converse com um profissional de saúde antes de seguir com esse objetivo."
        elif imc < 25:
            return "Seu IMC está na faixa saudável. Foque em recomposição corporal: treino de força e alimentação equilibrada, sem cortes drásticos."
        else :
            return "Seu IMC está acima de 25. Combine déficit calórico moderado, treino de força e atividade aeróbica regular, com metas graduais e acompanhamento profissional." 


    else : 
        return "Mantenha treinos regulares e alimentação equilibrada e acompanhe sua evolução ao longo do tempo. Em caso de dúvidas, procure um profissional de saúde."
    