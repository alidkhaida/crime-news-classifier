# Final policy boundary

Load this reference only when the user asks which classified cases qualify for the client’s final pool. It is not used to suppress crime categories during recognition.

Apply the maintained `archive/rules.md` decision order. Keep factual categories even when the outcome is excluded.

Typical separate outcomes include: `out of US`, `popular/high-profile`, `political/federal`, `general news`, `aggregate story`, `accident / non-crime`, `victim follow-up`, `suspect not found`, `no arrest`, `unable to access`, `not enough info`, `suspect died / no arrest`, `court update`, `old case / court`, `minor / weak case`, and `citation only`.

Important boundaries:

- Serious sexual conduct is a policy exclusion even when the article also supports homicide, kidnapping, domestic, employee, or child categories.
- Federal involvement in a financial case routes to `federal/financial`.
- A court or sentencing article may inherit an underlying arrest only under the maintained policy’s narrow exception.
- A vehicle crash is not automatically noncrime; DUI, hit-and-run, pursuit, reckless criminal driving, vehicular homicide, or similar conduct proceeds through normal policy checks.
- `infrastructure_error` is a run state, not a classification.
