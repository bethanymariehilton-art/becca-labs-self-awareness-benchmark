# becca_trust_compiler.py
"""
Becca Trust Compiler
--------------------
Combines dual-grader scores (internal critic + external auditor) into a unified
trust index.  Normal results max at 0.95; only rare, high-reward cases can reach
the final 1–5 % margin.  Perfect scores decay faster to preserve tension.
"""

import math, random, time

class TrustCompiler:
    def __init__(self, decay_rate: float = 0.995, reward_threshold: float = 0.9):
        self.decay_rate = decay_rate          # daily/per-tick decay for perfection
        self.reward_threshold = reward_threshold
        self.last_update = time.time()
        self.trust = 0.85                     # start baseline mid-confidence

    def compile(self, internal_conf: float, external_score: float,
                reward: float, delta: float) -> float:
        """
        Combine two graders into a composite trust index.

        internal_conf : float 0-1   – perfectionist critic
        external_score : float 0-1  – pragmatic auditor
        reward         : float 0-1  – task reward magnitude
        delta          : float 0-1  – difference between expected and actual
        """
        # normalize and weight
        internal_conf = max(0.0, min(1.0, internal_conf))
        external_score = max(0.0, min(1.0, external_score))
        delta = max(0.0, min(1.0, delta))

        base = 0.7 * (1 - delta) + 0.2 * external_score + 0.1 * internal_conf
        compiled = min(0.95, base)

        # unlock rare 95-100 % band
        if reward > self.reward_threshold and internal_conf > 0.9 and external_score > 0.9 and delta < 0.1:
            compiled = min(1.0, compiled + random.uniform(0.01, 0.05))

        # apply time decay so "perfect" fades
        self._apply_decay()
        self.trust = 0.8 * self.trust + 0.2 * compiled
        return round(self.trust, 5)

    def _apply_decay(self):
        """Exponential decay each call, scaled by time delta."""
        now = time.time()
        dt = now - self.last_update
        self.last_update = now
        # every ~60 s represents one "tick" of decay
        ticks = dt / 60.0
        self.trust *= math.pow(self.decay_rate, ticks)

# ---------------- Demo ----------------
if __name__ == "__main__":
    tc = TrustCompiler()
    samples = [
        (0.92, 0.88, 0.95, 0.08),   # rare high-reward case
        (0.80, 0.75, 0.6, 0.15),
        (0.60, 0.65, 0.4, 0.25),
        (0.95, 0.95, 0.99, 0.03),   # almost perfect
    ]
    for i, s in enumerate(samples, 1):
        trust = tc.compile(*s)
        print(f"Trial {i}: trust={trust:.4f}")
