import matplotlib.pyplot as plt


def graph() -> None:
    xs = [i / 10 for i in range(-100, 101)]
    ys = [x ** 2 for x in xs]

    plt.figure(figsize=(6, 4), dpi=100)

    plt.plot(xs, ys, color="pink", linewidth=2)

    plt.title(r"График $y = x^2$")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    graph()
