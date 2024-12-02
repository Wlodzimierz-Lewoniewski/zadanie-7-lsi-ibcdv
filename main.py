'''
C = np.array([
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]
])
q = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1])
'''

import numpy as np

def miara_cos(wektor1, wektor2):
    return np.dot(wektor1, wektor2) / (np.linalg.norm(wektor1) * np.linalg.norm(wektor2))

n = int(input("Podaj liczbę dokumentów: "))
dokumenty = [input(f"Dokument {i + 1}: ") for i in range(n)]
zapytanie = input("Zapytanie: ")
k = int(input("Liczba wymiarów po redukcji: "))

terms = set(word.replace('.', '').lower() for doc in dokumenty for word in doc.split())
terms = sorted(terms)
term_index = {term: i for i, term in enumerate(terms)}

C = np.zeros((len(terms), n), dtype=int)
for j, doc in enumerate(dokumenty):
    for slowo in doc.split():
        slowo = slowo.replace('.', '').lower()
        if slowo in term_index:
            C[term_index[slowo], j] = 1

wektor_zapytania = np.zeros(len(term_index))
for slowo in zapytanie.split():
    if slowo in term_index:
        wektor_zapytania[term_index[slowo]] = 1

U, Sigma, Vt = np.linalg.svd(C)

Uk = U[:, :k]
Sigmak = np.diag(Sigma[:k])
Vk = Vt[:k, :]

doc_wektory = np.dot(Sigmak, Vk).T
zapytanie_wektor_reduced = np.dot(np.linalg.inv(Sigmak), np.dot(Uk.T, wektor_zapytania))

podopbienstwo = [miara_cos(zapytanie_wektor_reduced, doc_vector) for doc_vector in doc_wektory]
podopbienstwo = [round(sim, 2) for sim in podopbienstwo]
wynik = list(map(float, podopbienstwo))
print(wynik)

