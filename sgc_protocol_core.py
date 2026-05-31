#!/usr/bin/env python3
# coding: utf-8
# =============================================================================
# PROJEKT: GlobalCoreSkeleton (SGC) – Protokół Kontroli Kontekstu LLM
# Plik: sgc_protocol_core.py
#
# CEL: Zademonstrowanie inzynierom mechanizmu tlumienia Efektu Motyla (dryfu)
#      w dlugich sesjach z modelami jezykowymi (LLM) za pomoca struktur stanowych.
# =============================================================================

import json
import math

class SGCProtocolEngine:
    def __init__(self):
        # Definicja rol i rygoru zaimplementowana bezposrednio w logice modelu
        self.roles = {
            "STRAZNIK": "Odpowiada za geometrie konwersacji, rygor i bezwzgledne trzymanie sie domeny.",
            "PROROK": "Odpowiada za kreatywnosc, predykcje awarii i innowacje wewnatrz zdefiniowanych ram."
        }

        # Matematyczna granica tolerancji dryfu (0.0 = idealna zbieznosc, 1.0 = calkowity chaos)
        self.CRITICAL_DRIFT_THRESHOLD = 0.500

    def load_manifest(self):
        """
        Zarys struktury strukturalnej (Single Source of Truth),
        ktora uzytkownik wstrzykuje na start projektu.
        """
        manifest_template = {
            "project": "GlobalCoreSkeleton",
            "mode": "collaboration",
            "principle": "Models are partners, not slaves",
            "project_core": {
                "domain": "Concrete engineering and system simulation",
                "error_model": "Small drift allowed, large jumps forbidden"
            },
            "tolerance_model": {
                "allowed": ["Architectural changes", "Risk analysis", "Direct code optimization"],
                "forbidden": ["Abstract philosophy", "Sci-fi", "Unrelated topics", "Emotional digressions"]
            }
        }
        return manifest_template

    def simulate_butterfly_effect(self, steps=10, initial_drift=0.05, sgc_active=False):
        """
        Symulacja matematyczna narastania bledu w modelach autoregresyjnych.
        Pokazuje, jak mala zmiana na poczatku (initial_drift) wywoluje huragan na koncu.
        """
        drift_history = []
        current_drift = initial_drift

        for step in range(1, steps + 1):
            if sgc_active:
                # SGC dziala jak sprzezenie zwrotne (ujemne) – Straznik tlumi dryf
                # Kreatywnosc Proroka dziala w bezpiecznych granicach
                damping_factor = 0.3  # Sila tlumienia przez strukture kodu
                innovation = 0.05     # Kontrolowana ekspresja tworcza (dusza artysty)
                current_drift = max(0.0, (current_drift * damping_factor) + (innovation * 0.1))
            else:
                # Brak SGC – klasyczny czat. Kazdy kolejny krok buduje na bledzie poprzedniego
                # Wykladniczy wzrost chaosu (Efekt Motyla)
                current_drift = current_drift * 1.5 + 0.02

            # Zaokraglenie dla stabilnosci numerycznej
            current_drift = round(min(current_drift, 1.0), 3)

            status = "STABLE" if current_drift < self.CRITICAL_DRIFT_THRESHOLD else "HURRICANE (HALUCYNACJA)"
            drift_history.append({"step": step, "drift": current_drift, "status": status})

        return drift_history


def zaprezentuj_inzynierom():
    engine = SGCProtocolEngine()

    print("=== PROJEKT GlobalCoreSkeleton (SGC) ===")
    print(f"Rola 1: Straznik -> {engine.roles['STRAZNIK']}")
    print(f"Rola 2: Prorok   -> {engine.roles['PROROK']}\n")

    # 1. Symulacja BEZ PROTOKOLU SGC (Klasyczny czat proza)
    print("--- SCENARIUSZ A: Brak SGC (Zwykly czat, wysoka entropia) ---")
    chaos_run = engine.simulate_butterfly_effect(steps=5, initial_drift=0.08, sgc_active=False)
    for r in chaos_run:
        print(f"Krok {r['step']}: Dryf = {r['drift']:.3f} | Status: {r['status']}")

    # 2. Symulacja Z PROTOKOLEM SGC (Kotwiczenie plikami .py)
    print("\n--- SCENARIUSZ B: Aktywny Protokol SGC (Niska entropia) ---")
    stable_run = engine.simulate_butterfly_effect(steps=5, initial_drift=0.08, sgc_active=True)
    for r in stable_run:
        print(f"Krok {r['step']}: Dryf = {r['drift']:.3f} | Status: {r['status']}")


if __name__ == "__main__":
    zaprezentuj_inzynierom()
