def registro():
    notas = []
    print("Digite as notas dos alunos e digite 'fim' para encerrar:")
    while True:
        nota = input("Nota: ")
        if nota.lower() == "fim":
            break
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10:
                notas.append(nota_float)
            else:
                print("Digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print("A média da turma é:", round(media, 2))
    else:
        print("Nenhuma nota foi registrada.")

print("Bem-vindo ao Registro de Notas! Calcule a médiada sua turma com praticidade")
registro()
