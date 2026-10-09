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
    # a: hora_total
    # r: hora_chegada
    # s: dias_depois
    r = a % 24
    s = a // 24

    return r, s


def tempo_viagem(a, b, c, d):
    # copy result
    # a: hora_partida
    # b: offset_origem
    # c: offset_destino
    # d: duracao_voo
    # e: horario_de_partida_em_greenwich
    # f: horario_de_partida_da_origem_no_fuso_do_destino
    # g: hora_total
    # r: hora_chegada
    # s: dias_depois

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
    A,  # hora_partida
    B,  # offset_origem
    C,  # offset_destino
    D,  # offset_hub
    E,  # horas_espera_hub
    F,  # duracao_voo_1
    G,  # duracao_voo_2
    H   # flag_tem_conexao
):
    # A: hora_partida
    # B: offset_origem
    # C: offset_destino
    # D: offset_hub
    # E: horas_espera_hub
    # F: duracao_voo_1
    # G: duracao_voo_2
    # H: flag_tem_conexao
    # I: hora_chegada_hub
    # J: dias_depois_hub
    # K: hora_partida_hub
    # L: hora_chegada
    # M: dias_depois
    # N: offset_origem convertido para horas
    # O: offset_destino convertido para horas
    # P: offset_hub convertido para horas
    # Q: retorno 1 (hora_chegada_hub)
    # R: retorno 2 (dias_depois_hub)
    # S: retorno 3 (hora_chegada)
    # T: retorno 4 (dias_depois)

    I = None
    J = None

    # Na máquina essas operações serão in place
    N = longitude_para_horas(B)
    O = longitude_para_horas(C)
    P = longitude_para_horas(D)

    if H == 1:
        I, J = tempo_viagem(
            A,
            N,
            P,
            F
        )

        K = somar(
            I,
            E
        )

        L, M = tempo_viagem(
            K,
            P,
            O,
            G
        )

    else:
        L, M = tempo_viagem(
            A,
            N,
            O,
            F
        )

    return (
        I,
        J,
        L,
        M
    )
