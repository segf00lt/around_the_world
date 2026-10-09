#!/usr/bin/env python3


def somar(a, b):
    # copiar parâmetros antes da chamada
    # alocar espaço no final da fita para o r
    r = a + b
    return r


def subtrair(a, b):
    # copiar parâmetros antes da chamada
    # alocar espaço no final da fita para o r
    r = a - b
    return r


def inverter_sentido(offset):
    # em linha
    # in-place

    # mapa de nomes para símbolos
    # a: offset

    return -offset


def calcular_hora_chegada_e_dias_depois(hora_total):
    # copiar parâmetros antes da chamada
    # alocar espaço no final da fita para o r

    # mapa de nomes para símbolos
    # a: hora_total
    # r: hora_chegada
    # s: dias_depois

    hora_chegada = hora_total % 24
    dias_depois = hora_total // 24

    return hora_chegada, dias_depois


def tempo_viagem(
    hora_partida,
    offset_origem,
    offset_destino,
    duracao_voo
):
    # copiar parâmetros antes da chamada
    # alocar espaço no final da fita para o r

    # mapa de nomes para símbolos
    # a: hora_partida
    # b: offset_origem
    # c: offset_destino
    # d: duracao_voo
    # e: horario_de_partida_em_greenwich
    # f: horario_de_partida_da_origem_no_fuso_do_destino
    # g: hora_total
    # r: hora_chegada
    # s: dias_depois

    offset_origem = inverter_sentido(offset_origem) # a máquina executará em linha

    # Converter o horário de partida para o horário de Greenwich.
    # copiar parâmetros antes da chamada
    r = somar(a=hora_partida, b=offset_origem)
    horario_de_partida_em_greenwich = r # renomear r

    # Converter o horário de Greenwich para o fuso horário do destino.
    # copiar parâmetros antes da chamada
    r = somar(a=horario_de_partida_em_greenwich, b=offset_destino)
    horario_de_partida_da_origem_no_fuso_do_destino = r # renomear r

    # copiar parâmetros antes da chamada
    r = somar(a=horario_de_partida_da_origem_no_fuso_do_destino, b=duracao_voo)
    hora_total = r # renomear r

    # copiar parâmetros antes da chamada
    hora_chegada, dias_depois = calcular_hora_chegada_e_dias_depois(hora_total=hora_total)

    return hora_chegada, dias_depois


def longitude_para_horas(offset):
    # in-place

    # a: offset

    return offset // 15


def tempo_viagem_com_possivel_conexao(
    hora_partida,       
    offset_origem,      
    offset_destino,     
    offset_hub,         
    horas_espera_hub,   
    duracao_voo_1,      
    duracao_voo_2,      
    flag_conexao   
):
    # mapa de nomes para símbolos
    # A: hora_partida
    # B: offset_origem
    # C: offset_destino
    # D: offset_hub
    # E: horas_espera_hub
    # F: duracao_voo_1
    # G: duracao_voo_2
    # H: flag_conexao
    # I: hora_chegada_hub
    # J: dias_depois_hub
    # K: hora_chegada
    # L: dias_depois
    # M: hora_partida_hub
    # N: dias_espera_adicionais
    # O: dias_antes_segundo_voo

    # Q: retorno 1 (hora_chegada_hub)
    # R: retorno 2 (dias depois_hub)
    # S: retorno 3 (hora_chegada)
    # T: retorno 4 (dias_depois)

    hora_chegada_hub = None
    dias_depois_hub = None
    hora_chegada = None
    dias_depois = None

    # Na máquina, essas operações serão feitas in-place e em linha, ou seja, modificarão os valores de B, C e D
    a = longitude_para_horas(offset_origem)
    offset_origem = a # renomear parâmetro modificado in-place

    a = longitude_para_horas(offset_destino)
    offset_destino = a # renomear parâmetro modificado in-place

    a = longitude_para_horas(offset_hub)
    offset_hub = a # renomear parâmetro modificado in-place

    if flag_conexao == 1:
        r, s = tempo_viagem(
            hora_partida=hora_partida,
            offset_origem=offset_origem,
            offset_destino=offset_hub,
            duracao_voo=duracao_voo_1
        )
        hora_chegada_hub, dias_depois_hub = r, s # renomear r, s

        r = somar(
            a=hora_chegada_hub,
            b=horas_espera_hub
        )
        hora_partida_hub = r # renomear r

        hora_partida_hub, dias_espera_adicionais = calcular_hora_chegada_e_dias_depois(
            hora_total=hora_partida_hub
        )

        dias_antes_segundo_voo = somar(
            a=dias_depois_hub,
            b=dias_espera_adicionais
        )

        r, s = tempo_viagem(
            hora_partida=hora_partida_hub,
            offset_origem=offset_hub,
            offset_destino=offset_destino,
            duracao_voo=duracao_voo_2
        )
        hora_chegada, dias_depois = r, s # renomear r, s

        dias_depois = somar(
            a=dias_depois,
            b=dias_antes_segundo_voo
        )

    else:
        r, s = tempo_viagem(
            hora_partida=hora_partida,
            offset_origem=offset_origem,
            offset_destino=offset_destino,
            duracao_voo=duracao_voo_1
        )
        hora_chegada, dias_depois = r, s # renomear r, s

    return (
        hora_chegada_hub,
        dias_depois_hub,
        hora_chegada,
        dias_depois
    )
