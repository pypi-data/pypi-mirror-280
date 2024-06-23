import datetime

from pandas import DataFrame, Series
from numpy import nan

from ..models import Board, Side


class BoardFactory:
    def from_series(self, low_series: Series, high_series: Series):
        assert low_series.index.max() == high_series.index.max()
        assert low_series.index.min() == high_series.index.min()

        low_series = low_series.copy()
        high_series = high_series.copy()

        x_is_datetime = isinstance(low_series.index[0], datetime.datetime)

        dtype_str = str(low_series.index.dtype)
        divider = 1
        if "ns" in dtype_str:
            divider = 1_000_000_000
        elif "us" in dtype_str:
            divider = 1_000_000
        elif "ms" in dtype_str:
            divider = 1_000

        if x_is_datetime:
            low_series.index = low_series.index.astype(int) // divider
            high_series.index = high_series.index.astype(int) // divider

        x_step = int(low_series.index.to_series().diff().min())
        x_start = low_series.index.min()
        x_stop = low_series.index.max()

        df = (
            DataFrame(
                (
                    [i, nan, nan]
                    for i in range(
                        x_start,
                        x_stop + x_step,
                        x_step,
                    )
                ),
                columns=["x", Side.LOW, Side.HIGH],
            )
            .astype({"x": "int"})
            .set_index("x")
        )

        df = df.merge(
            low_series.to_frame(Side.LOW), how="left", left_index=True, right_index=True
        )
        df = df.merge(
            high_series.to_frame(Side.HIGH),
            how="left",
            left_index=True,
            right_index=True,
        )

        df.rename(
            columns={f"{Side.LOW}_y": Side.LOW, f"{Side.HIGH}_y": Side.HIGH},
            inplace=True,
        )
        df.drop(columns=[f"{Side.LOW}_x", f"{Side.HIGH}_x"], inplace=True)

        df[Side.LOW.value] = df[Side.LOW.value].interpolate()
        df[Side.HIGH.value] = df[Side.HIGH.value].interpolate()

        y_min = low_series.min()
        y_max = high_series.max()
        x_min = df.index[0]
        samples = len(df.index)
        dv = (y_max - y_min) / samples

        df.index = range(samples)
        df[Side.LOW.value] = (df[Side.LOW.value] - y_min) / dv
        df[Side.HIGH.value] = (df[Side.HIGH.value] - y_min) / dv

        return Board(
            df=df,
            x_is_datetime=x_is_datetime,
            x_start=x_min,
            x_step=x_step,
            y_start=y_min,
            y_step=(y_max - y_min) / samples,
        )
