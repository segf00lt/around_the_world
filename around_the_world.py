#!/usr/bin/env python3


def somar(a, b):
    # copy result
    r = a + b
    return r


def subtrair(a, b):
    # copy result
    r = a - b
    return r


def inverter_sentido(a):
    # in place
    # a = offset
    return -a


def calcular_hora_chegada_e_dias_depois(a):
    # copy result
    # a = hora_total, r = hora_chegada, s = dias_depois
    r = a % 24
    s = a // 24

    return r, s


def tempo_viagem(a, b, c, d):
    # copy result
    # a = hora_partida
    # b = offset_origem
    # c = offset_destino
    # d = duracao_voo
    # e = horario_de_partida_em_greenwich
    # f = horario_de_partida_da_origem_no_fuso_do_destino
    # g = hora_total
    # r = hora_chegada
    # s = dias_depois

    # Convert departure time to Greenwich time.
    e = somar(a, inverter_sentido(b))

    # Convert Greenwich time to the destination's time zone.
    f = somar(e, c)

    g = somar(f, d)

    r, s = calcular_hora_chegada_e_dias_depois(g)

    return r, s


def longitude_para_horas(a):
    # in place
    # a = offset
    return a // 15


def tempo_viagem_com_possivel_conexao(
    hora_partida,     # horas
    offset_origem,    # longitude multiplo de 15
    offset_destino,   # longitude multiplo de 15
    offset_hub,       # longitude multiplo de 15
    horas_espera_hub, # horas
    duracao_voo_1,    # horas
    duracao_voo_2,    # horas
    flag_tem_conexao  # 0 ou 1
):
    hora_chegada_hub = None
    dias_depois_hub = None

    # Na máquina essas operações serão in place
    offset_origem = longitude_para_horas(offset_origem)
    offset_destino = longitude_para_horas(offset_destino)
    offset_hub = longitude_para_horas(offset_hub)

    if flag_tem_conexao == 1:
        hora_chegada_hub, dias_depois_hub = tempo_viagem(
            hora_partida,
            offset_origem,
            offset_hub,
            duracao_voo_1
        )

        hora_partida_hub = somar(
            hora_chegada_hub,
            horas_espera_hub
        )

        hora_chegada, dias_depois = tempo_viagem(
            hora_partida_hub,
            offset_hub,
            offset_destino,
            duracao_voo_2
        )

    else:
        hora_chegada, dias_depois = tempo_viagem(
            hora_partida,
            offset_origem,
            offset_destino,
            duracao_voo_1
        )

    return (
        hora_chegada_hub,
        dias_depois_hub,
        hora_chegada,
        dias_depois
    )
