import marimo

__generated_with = "0.6.16"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import plotnine as pn
    return mo, pd, pn


@app.cell
def __(pd):
    df = pd.read_csv("data/time_series.csv")
    df.head()
    return df,


@app.cell
def __(df):
    df.describe()
    return


@app.cell
def __(df):
    df.shape
    return


@app.cell
def __(df, pn):
    (
        pn.ggplot(
            df, pn.aes(x = "date", y = "value")
            ) 
        + pn.geom_point()
    )
    return


@app.cell
def __():
    from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
    from plotnine.data import mtcars

    (
        ggplot(mtcars, aes("wt", "mpg", color="factor(gear)"))
        + geom_point()
        + stat_smooth(method="lm")
        + facet_wrap("gear")
    )
    return aes, facet_wrap, geom_point, ggplot, mtcars, stat_smooth


if __name__ == "__main__":
    app.run()
