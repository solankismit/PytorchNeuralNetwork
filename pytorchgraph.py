import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

model_name = 'MODEL - 1686747730'

def create_acc_log_graph(model_name):
    contents = open('D:\Projects\DL\helloWorld\model.log', 'r').read().split('\n')


    time = []
    acc = []
    loss = []
    val_acc = []
    val_loss = []

    for c in contents:
        if model_name in c:
            name, timestamp, acc_, loss_, val_acc_, val_loss_ = c.split(',')

            time.append(float(timestamp))
            acc.append(float(acc_))
            loss.append(float(loss_))
            val_acc.append(float(val_acc_))
            val_loss.append(float(val_loss_))
    
    fig = plt.figure()
    # plt.plot(time, acc, label='acc')
    # plt.plot(time, val_acc, label='val_acc')
    # plt.plot(time, loss, label='loss')
    # plt.plot(time, val_loss, label='val_loss')

    ax1 = plt.subplot2grid((2,1), (0,0))
    ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)

    ax1.plot(time, acc, label='acc')
    ax1.plot(time, val_acc, label='val_acc')
    ax1.legend(loc = 2)

    ax2.plot(time, loss, label='loss')
    ax2.plot(time, val_loss, label='val_loss')
    ax2.legend(loc = 2)

    plt.legend()
    plt.show()

create_acc_log_graph(model_name)
