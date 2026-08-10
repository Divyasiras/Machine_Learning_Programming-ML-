import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","Python"]
    Students = [30,40,35,55]

    plt.bar(
        language,
        Students,
        width=0.6,            #Width of Bars
        edgecolor="black",    #Border color of bars
        linewidth=1,          #width of bar border
        alpha=0.8,            #transperance 0.0
        label="Students"      # legend text
    )

    plt.title("Marvellous bar plot")
    plt.xlabel(language)
    plt.ylabel("Number of Student")
    plt.legend()
    plt.show()


if __name__=="__main__":
    main()
