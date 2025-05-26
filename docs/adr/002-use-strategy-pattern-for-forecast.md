### docs/adr/0002-use-strategy-pattern-for-forecast.md

# ADR-0002: Use Strategy Pattern for Forecast Logic

## Context
Forecasting logic may vary based on user preference or data type (e.g., hourly vs daily forecasts).

## Decision
Use the Strategy Pattern to encapsulate forecast generation logic.

## Consequences
+ Easy to extend with new strategies
+ Promotes separation of concerns
- Slightly more code complexity
