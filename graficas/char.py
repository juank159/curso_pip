import matplotlib.pyplot as plt

def pie_char():
    labels = ['A','B','C']
    values = [100,20,50]

    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()