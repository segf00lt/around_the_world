#!/usr/bin/env python3


#def somar(a, b):
#    # copiar parâmetros antes da chamada
#    r = a + b
#    return r
#
#
#def subtrair(a, b):
#    # copiar parâmetros antes da chamada
#    r = a - b
#    return r
#
#
#def inverter_sentido(offset):
#    # em linha
#    # in-place
#
#    return -offset
#
#
#def calcular_hora_chegada_e_dias_depois(hora_total):
#    # copiar parâmetros antes da chamada
#
#    hora_chegada = hora_total % 24
#    dias_depois = hora_total // 24
#
#    return hora_chegada, dias_depois
#
#def get_sentido(offset):
#    if offset < 0:
#        return '-'
#    else
#        return '+'
#
#
#def tempo_viagem(
#    hora_partida,
#    offset_origem,
#    offset_destino,
#    duracao_voo
#):
#    # copiar parâmetros antes da chamada
#
#    offset_origem = inverter_sentido(offset_origem) # executará em linha, não conta como sub-máquina
#
#    # Converter o horário de partida para o horário de Greenwich.
#    # copiar parâmetros antes da chamada
#    horario_de_partida_em_greenwich = \
#    somar(hora_partida, offset_origem) if get_sentido(offset_origem) == '+' else subtrair(hora_partida, offset_origem)
#    
#    # label depois_horario_de_partida_em_greenwich
#
#    # Converter o horário de Greenwich para o fuso horário do destino.
#    # copiar parâmetros antes da chamada
#    horario_de_partida_da_origem_no_fuso_do_destino = \
#    somar(horario_de_partida_em_greenwich, offset_destino) if get_sentido(offset_destino) == '+' else subtrair(horario_de_partida_em_greenwich, offset_destino)
#
#    # label depois_horario_de_partida_da_origem_no_fuso_do_destino
#
#    # copiar parâmetros antes da chamada
#    hora_total = somar(horario_de_partida_da_origem_no_fuso_do_destino, duracao_voo)
#
#    # label depois_hora_total
#
#    # copiar parâmetros antes da chamada
#    #hora_chegada, dias_depois = calcular_hora_chegada_e_dias_depois(hora_total)
#
#    # label depois_hora_chegada_e_dias_depois
#
#    #return hora_chegada, dias_depois
#    return hora_total
#
#
#def longitude_para_horas(offset):
#    # in-place
#
#    return offset // 15
#
#
#def tempo_viagem_com_possivel_conexao(
#    flag_conexao,
#    hora_partida,       
#    offset_origem,      
#    offset_hub,         
#    duracao_voo_1,      
#    horas_espera_hub,   
#    offset_destino,
#    duracao_voo_2,
#):
#    hora_chegada_hub = None
#    dias_depois_hub = None
#    hora_chegada = None
#    dias_depois = None
#
#    # Na máquina, essas operações serão feitas in-place e em linha
#    offset_origem = longitude_para_horas(offset_origem)
#
#    offset_destino = longitude_para_horas(offset_destino)
#
#    offset_hub = longitude_para_horas(offset_hub)
#
#    if flag_conexao == 1:
#        #hora_chegada_hub, dias_depois_hub = tempo_viagem(
#        hora_total_hub = tempo_viagem(
#            hora_partida=hora_partida,
#            offset_origem=offset_origem,
#            offset_destino=offset_hub,
#            duracao_voo=duracao_voo_1
#        )
#
#        # label depois_hora_chegada_hub_e_dias_depois_hub
#
#        hora_partida_hub = somar(
#                #hora_chegada_hub,
#            hora_total_hub,
#            horas_espera_hub
#        )
#
#        # label depois_hora_partida_hub
#
#        #hora_partida_hub, dias_espera_adicionais = calcular_hora_chegada_e_dias_depois(
#        #    hora_total=hora_partida_hub
#        #)
#
#        # label depois_hora_partida_hub_e_dias_espera_adicionais
#
#        #dias_antes_segundo_voo = somar(
#        #    dias_depois_hub,
#        #    dias_espera_adicionais
#        #)
#
#        # label depois_dias_antes_segundo_voo
#
#        #hora_chegada, dias_depois = tempo_viagem(
#        hora_total = tempo_viagem(
#            hora_partida=hora_partida_hub,
#            offset_origem=offset_hub,
#            offset_destino=offset_destino,
#            duracao_voo=duracao_voo_2
#        )
#
#        # label depois_hora_chegada_e_dias_depois_destino
#
#        dias_depois = somar(
#            dias_depois,
#            dias_antes_segundo_voo
#        )
#
#        # label depois_dias_depois_destino
#
#    else:
#        hora_chegada, dias_depois = tempo_viagem(
#            hora_partida=hora_partida,
#            offset_origem=offset_origem,
#            offset_destino=offset_destino,
#            duracao_voo=duracao_voo_1
#        )
#
#    return (
#        hora_chegada_hub,
#        dias_depois_hub,
#        hora_chegada,
#        dias_depois
#    )


departure_time = 2
origin_offset = 4
destination_offset = -4
flight_duration = 1

departure_utc = departure_time - origin_offset

total = departure_utc + flight_duration + destination_offset

arrival_time = total % 24

days_elapsed = total // 24

print(arrival_time)
print(days_elapsed)



















print("test 2")

total = departure_time + -origin_offset + destination_offset + flight_duration

arrival_time = total % 24

days_elapsed = total // 24

print(arrival_time)
print(days_elapsed)






