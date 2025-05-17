from data.timescale_loader import load_bars_from_timescaledb

df=load_bars_from_timescaledb(
    symbol="RB9999",
    timeframe="1h",
    start="2025-05-01T00:00:00Z",
    end="2025-05-01T00:00:00Z"
)

print(df)
