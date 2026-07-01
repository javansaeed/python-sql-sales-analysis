import matplotlib.pyplot as plt


def save_bar_chart(series, title, xlabel, ylabel, path):
    plt.figure(figsize=(10, 5))

    series.plot(kind="bar")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")

    plt.close()   # 🔥 مهم


def save_line_chart(x, y, title, xlabel, ylabel, path):
    plt.figure(figsize=(12, 5))

    plt.plot(x, y, marker="o")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")

    plt.close()   # 🔥 مهم
