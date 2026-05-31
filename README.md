# SGC – Protokół Kontroli Kontekstu LLM (GlobalCoreSkeleton)

## Czym jest SGC?

SGC (GlobalCoreSkeleton) to lekki protokół inżynierski zaprojektowany, by **tłumić dryf kontekstu** w długich sesjach z modelami językowymi (LLM).

Każdy, kto pracował z ChatGPT, Claude czy Gemini nad złożonym projektem technicznym, zna problem: po kilkunastu wymianach model zaczyna „dryfować" – zapomina wcześniejsze ustalenia, zmienia styl odpowiedzi, a w końcu generuje odpowiedzi sprzeczne z tym, co było ustalone na początku sesji. To jest właśnie **Efekt Motyla w LLM** – mała zmiana we wczesnym kontekście powoduje narastający chaos w późniejszych odpowiedziach.

SGC rozwiązuje ten problem przez:
- **Kotwiczenie stanu projektu** w zewnętrznym pliku `.py` (Single Source of Truth)
- **Podział ról** na Strażnika (rygor, domena, geometria rozmowy) i Proroka (kreatywność wewnątrz zdefiniowanych ram)
- **Matematyczną granicę tolerancji dryfu** – zamiast intuicji, konkretny próg (domyślnie 0.5)

---

## Co robi ten plik?

`sgc_protocol_core.py` to **demonstracja matematyczna** działania protokołu.

Uruchom go i zobaczysz dwa scenariusze:

```
--- SCENARIUSZ A: Brak SGC (Zwykły czat, wysoka entropia) ---
Krok 1: Dryf = 0.140 | Status: STABLE
Krok 2: Dryf = 0.230 | Status: STABLE
Krok 3: Dryf = 0.365 | Status: STABLE
Krok 4: Dryf = 0.568 | Status: HURRICANE (HALUCYNACJA)
Krok 5: Dryf = 0.872 | Status: HURRICANE (HALUCYNACJA)

--- SCENARIUSZ B: Aktywny Protokół SGC (Niska entropia) ---
Krok 1: Dryf = 0.029 | Status: STABLE
Krok 2: Dryf = 0.014 | Status: STABLE
Krok 3: Dryf = 0.009 | Status: STABLE
Krok 4: Dryf = 0.008 | Status: STABLE
Krok 5: Dryf = 0.007 | Status: STABLE
```

Bez protokołu – wykładniczy wzrost błędu. Z protokołem – dryf szybko zbiega do stabilnego minimum.

---

## Jak uruchomić

Wymagany Python 3.7+, brak zewnętrznych zależności.

```bash
python sgc_protocol_core.py
```

---

## Dla kogo?

- Inżynierowie i programiści pracujący z LLM nad projektami trwającymi wiele sesji
- Osoby budujące własne workflow multi-AI (np. weryfikacja krzyżowa Claude / GPT / Gemini)
- Każdy, kto zmaga się z problemem „model zapomniał, co ustaliliśmy tydzień temu"

---

## Koncepcja w skrócie

```
Plik .py = jedyne źródło prawdy o stanie projektu
     │
     ├── STRAŻNIK → pilnuje domeny, rygoru, geometrii rozmowy
     └── PROROK   → kreatywność i innowacja w bezpiecznych granicach

Dryf < 0.5  →  STABLE   (model działa w domenie)
Dryf ≥ 0.5  →  HURRICANE (halucynacje, odejście od tematu)
```

---

## Status projektu

**To nie jest gotowa biblioteka – ten plik pokazuje wyłącznie zasadę działania SGC.**

Właściwy protokół żyje w plikach `.py` tworzonych ręcznie przez użytkownika dla konkretnego projektu. Taki plik jest wstrzykiwany do sesji LLM jako jedyne źródło prawdy o stanie projektu – zawiera parametry techniczne, historię decyzji, wykaz błędów modeli i asercje weryfikujące spójność danych.

W praktyce SGC stosowany jest w projektach inżynierskich (automatyka, geodezja, systemy wbudowane) z weryfikacją krzyżową między modelami (Claude / GPT / Gemini).

---

## Licencja

MIT – używaj, modyfikuj, dziel się.
