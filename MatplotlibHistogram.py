import matplotlib.pyplot as plt

def main():
    marks = [45,55,60,62,65,67,70,72,75,78,80,82,85,90,95]

    plt.hist(
        marks,             #Cuntinuos Data
        bins=5,             #number of groups
        edgecolor="black",  #Border color
        alpha=0.8,          #Transperancy
        rwidth=0.9,         #Relative width of bar

    )

    plt.title("marvellous histogram")
    plt.xlabel("marks")
    plt.ylabel("Frequency")
    plt.show()
    

if __name__=="__main__":
    main()
