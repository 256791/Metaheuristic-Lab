# Metaheuristic-Lab

LAB_1:

1. Wczytywanie instancji z biblioteki TSPLIB-a w formatach lower_diag_row, full_matrix, euc_2d
-- przykładowe instancje: gr120.tsp, berlin52.tsp, br17.atsp
-- obowiązkowo należy przetestować dla co najmniej jednej instancji danego formatu. Dobrze jest jednak przetestować na wszystkich instancjach danego formatu, by (1) sprawdzić czy zawsze działa, (2) zorientować się ile w ogóle jest takich instancji (pobrać je sobie od razu)
-- dla EUC_2D należy pamiętać o odpowiednim zaokrągleniu wyników
-- można użyć gotowych bibliotek (o ile działają)

2. Generowanie losowych instancji dla poszczególnych wariantów
(ogólny/asymetryczny, symetryczny, euklidesowy 2D).

3. Wyświetlanie wczytanej instancji (tj. wyświetlanie macierzy odległości).

4. Wyświetlanie rozwiązania (cyklu)
-- obowiązkowo: tekstowo (w konsoli)
-- opcjonalnie: graficzna wizualizacja rozwiązania na płaszczyźnie (tylko dla TSP euklidesowego 2D)

5. Liczenie funkcji celu (długości cyklu).
-- na TSPLIB dla niektórych instancji podane jest przykładowe rozwiązanie optymalne (np. gr24.opt.tour.gz dla instancji gr24), dzięki któremu można zweryfikować działanie

6. Obliczanie wartości PRD(x) = 100% * (f(x) - f(opt)) / f(opt), gdzie x to dane rozwiązanie, a opt to rozwiązanie optymalne.


