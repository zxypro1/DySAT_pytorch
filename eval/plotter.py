import matplotlib.pyplot as plt


def plotter(epochs, all_loss, auc_val, auc_test):
    fig, axs = plt.subplots(3)
    axs[0].plot(epochs, all_loss, label='All loss')
    axs[0].set_title('All loss')
    axs[1].plot(epochs, auc_val, label='Val Auc')
    axs[1].set_title('Val Auc')
    axs[2].plot(epochs, auc_test, label='Test Auc')
    axs[2].set_title('Test Auc')

    plt.tight_layout()
    plt.show()


plotter([1, 2, 3], [1, 2, 3], [4, 6, 7], [3, 2, 5])
