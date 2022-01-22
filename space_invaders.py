from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import randint

#Functions

def SpawnMonsters(janela):
    monstros = 20
    monstro = Sprite("bot.png", 1)
    MatrizMonsters = []
    longitudeMonster = 0
    latitudeMonster = 0
    fileiraMonstros = int(monstros/3)
    colunaMonstros = int(monstros)
    quantidadeMonstro = 0
    for i in range(0, fileiraMonstros, +1):
        longitudeMonster = 0
        MatrizMonsters.append([])
        for j in range(0, colunaMonstros, +1):
            monstro = Sprite("bot.png", 1)
            monstro.y = latitudeMonster
            monstro.x = longitudeMonster
            quantidadeMonstro += 1
            MatrizMonsters[i].append(monstro)
            longitudeMonster += 40*3/2
        latitudeMonster += 40*3/2
    return MatrizMonsters, quantidadeMonstro

def MoveMonsters(matrizMonsters, janela, direcao, nivel_dificuldade, etapa_menu, onda):
    fileiraMonstros = len(matrizMonsters)
    mudarDirecao = False
    velocidadeMonstros = 20*janela.delta_time()*direcao*(nivel_dificuldade**(1/2))*onda
    acabou = False
    for l in range(0, fileiraMonstros, +1):
            colunaMonstros = len(matrizMonsters[l])
            for c in range(0, colunaMonstros, +1):
                matrizMonsters[l][c].x += velocidadeMonstros
                if (matrizMonsters[l][c].x < 0) or (matrizMonsters[l][c].x + matrizMonsters[l][c].width > janela.width):
                    mudarDirecao = True
                if matrizMonsters[l][c].y > janela.height:
                    acabou = True
    if mudarDirecao == True:
        fileiraMonstros = len(matrizMonsters)
        for l in range(0, fileiraMonstros, +1):
            colunaMonstros = len(matrizMonsters[l])
            for c in range(0, colunaMonstros, +1):
                matrizMonsters[l][c].y += 20
                if velocidadeMonstros > 0:
                    matrizMonsters[l][c].x -= 2
                elif velocidadeMonstros < 0:
                    matrizMonsters[l][c].x += 2
        direcao *= -1
        mudarDirecao = False
    return matrizMonsters, direcao, etapa_menu, acabou

def DrawMonsters(MatrizMonsters):
    fileiraMonstros = len(MatrizMonsters)
    for l in range(0, fileiraMonstros, +1):
            colunaMonstros = len(MatrizMonsters[l])
            for c in range(0, colunaMonstros, +1):
                MatrizMonsters[l][c].draw()

#Main
janela = Window(1280, 640)
janela.set_title("Space Invaders")

fundo = GameImage("terra.jpg")
jogar = Sprite("botao_jogar.jpg", 1)
dificuldade = Sprite("botao_dificuldade.jpg", 1)
ranking = Sprite("botao_ranking.jpg", 1)
sair = Sprite("botao_sair.jpg", 1)

teclado = Window.get_keyboard()
mouse = Window.get_mouse()

mouse.set_position(janela.width/2, janela.height/2)
jogar.x = fundo.width/2 - jogar.width/2
dificuldade.x = fundo.width/2 - dificuldade.width/2
ranking.x = fundo.width/2 - ranking.width/2
sair.x = fundo.width/2 - sair.width/2
jogar.y = 100 - jogar.height/2
dificuldade.y = jogar.y + 100 + jogar.height/2 - dificuldade.height/2
ranking.y = dificuldade.y + 100 + dificuldade.height/2 - ranking.height/2
sair.y = ranking.y + 100 + ranking.height/2 - sair.height/2

etapa_menu = 1
nivel_dificuldade = 1
vel_player = 400
atirou_player = False
timerPontuacao = 0
pontuacaoMostrar = "0"
rank = []
sortedRank = []
acabou = False

while True:
    if teclado.key_pressed("ESC"):
        etapa_menu = 1

    #Menu Principal
    if etapa_menu == 1:
        jogar = Sprite("botao_jogar.jpg", 1)
        dificuldade = Sprite("botao_dificuldade.jpg", 1)
        ranking = Sprite("botao_ranking.jpg", 1)
        sair = Sprite("botao_sair.jpg", 1)
        jogar.x = fundo.width/2 - jogar.width/2
        dificuldade.x = fundo.width/2 - dificuldade.width/2
        ranking.x = fundo.width/2 - ranking.width/2
        sair.x = fundo.width/2 - sair.width/2
        jogar.y = 100 - jogar.height/2
        dificuldade.y = jogar.y + 100 + jogar.height/2 - dificuldade.height/2
        ranking.y = dificuldade.y + 100 + dificuldade.height/2 - ranking.height/2
        sair.y = ranking.y + 100 + ranking.height/2 - sair.height/2

        if mouse.is_over_area((jogar.x, jogar.y),(jogar.x + jogar.width, jogar.y + jogar.height)):
            jogar = Sprite("botao_jogar_HOVER.jpg", 1)
            jogar.x = fundo.width/2 - jogar.width/2
            jogar.y = 100 - jogar.height/2
            if mouse.is_button_pressed(1):
                etapa_menu = 2
        elif mouse.is_over_area((dificuldade.x, dificuldade.y),(dificuldade.x + dificuldade.width, dificuldade.y + dificuldade.height)):
            dificuldade = Sprite("botao_dificuldade_HOVER.jpg", 1)
            dificuldade.x = fundo.width/2 - dificuldade.width/2
            dificuldade.y = jogar.y + 100 + jogar.height/2 - dificuldade.height/2
            if mouse.is_button_pressed(1):
                etapa_menu = 4
        elif mouse.is_over_area((ranking.x, ranking.y),(ranking.x + ranking.width, ranking.y + ranking.height)):
            ranking = Sprite("botao_ranking_HOVER.jpg", 1)
            ranking.x = fundo.width/2 - ranking.width/2
            ranking.y = dificuldade.y + 100 + dificuldade.height/2 - ranking.height/2
            if mouse.is_button_pressed(1):
                etapa_menu = 5
        elif mouse.is_over_area((sair.x, sair.y),(sair.x + sair.width, sair.y + sair.height)):
            sair = Sprite("botao_sair_HOVER.jpg", 1)
            sair.x = fundo.width/2 - sair.width/2
            sair.y = ranking.y + 100 + ranking.height/2 - sair.height/2
            if mouse.is_button_pressed(1):
                janela.close()
    
    #Game
    if etapa_menu == 2:
        player = Sprite("player.png", 1)
        player.y = janela.height - 50
        player.x = janela.width/2 - player.width/2
        etapa_menu = 3
        projeteis_player = []
        projeteis_bot = []
        matrizMonsters, quantidadeMonstro = SpawnMonsters(janela)
        direcao = 1
        pontuacaoReal = 0
        pontosBot = 50*nivel_dificuldade
        timerFinish = 0
        pontuacaoMostrar = "0"
        timerBotTiro = 0
        vidas_player = 3
        acertado = False
        onda = 1
    
    if etapa_menu == 3:
        if teclado.key_pressed("LEFT"):
            player.x = player.x - vel_player*janela.delta_time()
        elif teclado.key_pressed("RIGHT"):
            player.x = player.x + vel_player*janela.delta_time()
        if player.x + player.width/2 < 0:
            player.x = janela.width - player.width
        elif player.x + player.width/2 > janela.width:
            player.x = 2
        if (teclado.key_pressed("SPACE")) and (atirou_player == False):
            tempo_tiro_player = 0
            tiro_player = Sprite("tiro_player.png", 1)
            tiro_player.y = player.y
            tiro_player.x = player.x + player.width/2
            tiro_auxiliar = tiro_player
            projeteis_player.append(tiro_auxiliar)
            atirou_player = True
        if atirou_player == True:
            tempo_tiro_player += janela.delta_time()
            if tempo_tiro_player > 0.4:
                atirou_player = False
        if (quantidadeMonstro <= 0) or (vidas_player == 0) or (acabou == True):
            timerFinish += janela.delta_time()
            if timerFinish >= 1.5:
                if vidas_player > 0:
                    projeteis_bot = []
                    projeteis_player = []
                    matrizMonsters, quantidadeMonstro = SpawnMonsters(janela)
                    pontosBot = 100*nivel_dificuldade
                    acabou = False
                    timerFinish = 0
                elif vidas_player <= 0:
                    etapa_menu = 1
                    rank.append(pontuacaoReal)
        timerPontuacao += janela.delta_time()
        if timerPontuacao >= 2.5:
            if pontosBot > 1:
                pontosBot -= 1
            timerPontuacao = 0
            pontuacaoMostrar = str(int(pontuacaoReal))
        timerBotTiro += janela.delta_time()
        if timerBotTiro >= 0.8/nivel_dificuldade:
            tiro_bot = Sprite("tiro_bot.png", 1)
            fileiraMonstros = len(matrizMonsters)
            fileiraRandom = randint(0, fileiraMonstros)
            for l in range(fileiraMonstros, -1, +1):
                colunaMonstros = len(matrizMonsters[l])
                if l == fileiraRandom:
                    colunaRandom = randint(0, colunaMonstros)
                    for c in range(colunaMonstros, -1, -1):
                        if c == colunaRandom:
                            tiro_bot.y = matrizMonsters[l][c].y + matrizMonsters[l][c].height
                            tiro_bot.x = matrizMonsters[l][c].x + matrizMonsters[l][c].width/2
                            tiro_auxiliar = tiro_bot
                            projeteis_bot.append(tiro_auxiliar)
            timerBotTiro = 0

    #Opções de Dificuldade
    if etapa_menu == 4:
        facil = Sprite("botao_facil.jpg", 1)
        medio = Sprite("botao_medio.jpg", 1)
        dificil = Sprite("botao_dificil.jpg", 1)
        facil.x = fundo.width/3 - facil.width/2
        medio.x = fundo.width/3 - medio.width/2
        dificil.x = fundo.width/3 - dificil.width/2
        facil.y = 100 - facil.height/2
        medio.y = facil.y + 100 + facil.height/2 - medio.height/2
        dificil.y = medio.y + 100 + medio.height/2 - dificil.height/2
    
        if mouse.is_over_area((facil.x, facil.y),(facil.x + facil.width, facil.y + facil.height)):
            facil = Sprite("botao_facil_HOVER.jpg", 1)
            facil.x = fundo.width/3 - facil.width/2
            facil.y = 100 - facil.height/2
            if mouse.is_button_pressed(1):
                etapa_menu = 1
                nivel_dificuldade = 0.5
        elif mouse.is_over_area((medio.x, medio.y),(medio.x + medio.width, medio.y + medio.height)):
            medio = Sprite("botao_medio_HOVER.jpg", 1)
            medio.x = fundo.width/3 - medio.width/2
            medio.y = facil.y + 100 + facil.height/2 - medio.height/2
            if mouse.is_button_pressed(1):
                etapa_menu = 1
                nivel_dificuldade = 1
        elif mouse.is_over_area((dificil.x, ranking.y),(dificil.x + dificil.width, dificil.y + dificil.height)):
            dificil = Sprite("botao_dificil_HOVER.jpg", 1)
            dificil.x = fundo.width/3 - dificil.width/2
            dificil.y = medio.y + 100 + medio.height/2 - dificil.height/2
            if mouse.is_button_pressed(1):
                etapa_menu = 1
                nivel_dificuldade = 1.5

    #Update da Janela
    fundo.draw()
    if etapa_menu == 1:
        jogar.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()
        janela.draw_text("Sua última pontuação: " + pontuacaoMostrar, 40, janela.height - 40, 20, (255, 0, 0), "Arial", True, False)
    if etapa_menu == 3:
        janela.draw_text("Vidas: " + str(vidas_player), 10, janela.height - 70, 30, (255, 0, 0), "Arial", True, False)
        janela.draw_text("Pontuação: " + pontuacaoMostrar, 10, janela.height - 40, 30, (255, 0, 0), "Arial", True, False)
        if acertado == False:
            player.draw()
        elif acertado == True:
            timerAcertado += janela.delta_time()
            timerInvisivel += janela.delta_time()
            if invisivel == False:
                player.draw()
                timerInvisivel += janela.delta_time()
                if timerInvisivel > 0.5:
                    invisivel = True
            elif invisivel == True:
                timerInvisivel += janela.delta_time()
                if timerInvisivel > 0.5:
                    invisivel = False
            if timerAcertado > 2:
                acertado = False
        for t in range(len(projeteis_player)-1, -1, -1):
            projeteis_player[t].draw()
            projeteis_player[t].y -= 300*janela.delta_time()
            fileiraMonstros = len(matrizMonsters)
            tirarTiro_player = False
            for l in range(fileiraMonstros-1, -1, -1):
                    colunaMonstros = len(matrizMonsters[l])
                    for c in range(colunaMonstros-1, -1, -1):
                        if projeteis_player[t].collided(matrizMonsters[l][c]):
                            tirarTiro_player = True
                            matrizMonsters[l].remove(matrizMonsters[l][c])
                            pontuacaoReal += pontosBot
                            quantidadeMonstro -= 1
                            break
                    if len(matrizMonsters[l]) == 0:
                        matrizMonsters.remove(matrizMonsters[l])
                        onda += 0.1
            if projeteis_player[t].y < 0:
                tirarTiro_player = True
            if tirarTiro_player == True:
                projeteis_player.remove(projeteis_player[t])
        for t in range(len(projeteis_bot)-1, -1, -1):
            projeteis_bot[t].draw()
            projeteis_bot[t].y += 150*janela.delta_time()*onda
            if projeteis_bot[t].y > janela.height:
                projeteis_bot.remove(projeteis_bot[t])
            elif (projeteis_bot[t].collided(player)) and (vidas_player > 0) and (acertado == False):
                projeteis_bot.remove(projeteis_bot[t])
                vidas_player -= 1
                player.x = janela.width/2 - player.width/2
                timerAcertado = 0
                timerInvisivel = 0
                acertado = True
                invisivel = True
        DrawMonsters(matrizMonsters)
        matrizMonsters, direcao, etapa_menu, acabou = MoveMonsters(matrizMonsters, janela, direcao, nivel_dificuldade, etapa_menu, onda)
    if etapa_menu == 4:
        facil.draw()
        medio.draw()
        dificil.draw()
    if etapa_menu == 5:
        rank.sort(reverse=True)
        y = 150
        janela.draw_text("OS TOPZERA", janela.width/2 - 200, 60, 60, (255, 0, 0), "Arial", True, False)
        for i in range(0, len(rank), +1):
            janela.draw_text(str(int(rank[i])), janela.width/2 - 60, y, 40, (255, 0, 0), "Arial", False, False)
            y += 80
    janela.update()