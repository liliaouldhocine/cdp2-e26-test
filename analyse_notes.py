notes = [72, 85, 91, 68, 77]

moyenne = sum(notes) / len(notes)

print(f"Moyenne : {moyenne:.1f}")

# Un commentaire 
nombre_notes = len(notes)

print(f"Nombre de notes : {nombre_notes}")

notes_triees = sorted(notes)
indice_milieu = len(notes_triees) // 2
mediane = notes_triees[indice_milieu]

print(f"Médiane : {mediane}")