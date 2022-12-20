import charts


def run(labels, values):
    charts.generate_pie_chart(labels, values)
    charts.generate_bar_chart(labels, values)


if __name__ == "__main__":
    labels = ["A", "B", "C"]
    values = [200, 34, 120]
    run(labels, values)
