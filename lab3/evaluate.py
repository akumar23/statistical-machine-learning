def evaluate(net, images, labels):
    acc = 0
    loss = 0
    batch_size = 1
    n= images.shape[0]
    for b in range(0, images.shape[0], batch_size):
        x = images[b]
        y = labels[b]
        
        for l in range(net.lay_num):
            output = net.layers[l].forward(x)
            x = output
        loss += cross_entropy(output, y)
        if np.argmax(output) == np.argmax(y):
            acc += 1
    accuracy = acc/n
    losses= loss/n
    return accuracy, losses