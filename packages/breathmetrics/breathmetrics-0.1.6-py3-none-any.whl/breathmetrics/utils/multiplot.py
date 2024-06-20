import matplotlib.pyplot as plt


def multiplot(title, x, temp_1, temp_2, pressure_1, pressure_2, humidity_1, humidity_2):

    figure, axis = plt.subplots(3, 2)
    figure.suptitle(title)

    axis[0, 0].plot(x, temp_1)
    axis[0, 0].set_title("Temperature 1")
    axis[0, 0].set_xlabel('Time in sec')
    axis[0, 0].set_ylabel('mm in Hg')
    axis[0, 1].plot(x, temp_2)
    axis[0, 1].set_title("Temperature 2")
    axis[0, 1].set_xlabel('Time in sec')
    axis[0, 1].set_ylabel('mm in Hg')

    axis[1, 0].plot(x, pressure_1)
    axis[1, 0].set_title("Pressure 1")
    axis[1, 1].plot(x, pressure_2)
    axis[1, 1].set_title("Pressure 2")

    axis[2, 0].plot(x, humidity_1)
    axis[2, 0].set_title("Humidity 1")
    axis[2, 1].plot(x, humidity_2)
    axis[2, 1].set_title("Humidity 2")

    plt.subplots_adjust(hspace=0.7)

    plt.show()