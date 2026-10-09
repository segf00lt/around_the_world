#!/usr/bin/env python3


def somar(a, b):
    r = a + b
    return r


def subtrair(a, b):
    r = a - b
    return r


def inverter_sentido(offset):
    # Returns the offset with its direction reversed.
    return -offset


def calcular_hora_chegada_e_dias_depois(hora_total):
    hora_chegada = hora_total % 24
    dias_depois = hora_total // 24

    return hora_chegada, dias_depois


def tempo_viagem(hora_partida, offset_origem, offset_destino, duracao_voo):
    # Convert departure time to Greenwich time.
    horario_de_partida_em_greenwich = (
        somar(hora_partida, inverter_sentido(offset_origem))
    )

    # Convert Greenwich time to the destination's time zone.
    horario_de_partida_da_origem_no_fuso_do_destino = somar(
        horario_de_partida_em_greenwich,
        offset_destino
    )

    hora_total = somar(
        horario_de_partida_da_origem_no_fuso_do_destino,
        duracao_voo
    )

    hora_chegada, dias_depois = (
        calcular_hora_chegada_e_dias_depois(hora_total)
    )

    return hora_chegada, dias_depois

def longitude_para_horas(offset):
    return offset // 15

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
