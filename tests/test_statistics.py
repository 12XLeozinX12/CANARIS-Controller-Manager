from database.statistics import GamerStatistics


print("==============================")
print(" TESTE ESTATISTICAS CANARIS ")
print("==============================")


stats = GamerStatistics()



usuario_id = 2



print(
    "Criando estatística..."
)


resultado = stats.create_statistics(

    usuario_id

)


print(
    "Criado:",
    resultado
)



print(
    "\nBuscando dados..."
)



dados = stats.get_statistics(

    usuario_id

)



print(
    dados
)



print(
    "\nAdicionando horas..."
)



stats.add_hours(

    usuario_id,

    5

)



print(

    stats.get_statistics(

        usuario_id

    )

)



print(
    "\nFinalizado!"
)