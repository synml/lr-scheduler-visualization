import torch
import matplotlib.pyplot as plt


class Model(torch.nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(5, 3)

    def forward(self, x):
        return self.linear1(x)


model = Model()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Various lr_scheduler objects can be assigned to the scheduler.
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=8, gamma=0.8)
scheduler_name = scheduler.__class__.__name__

lr_list = []
for epoch in range(100):
    lr = None
    for param_group in optimizer.param_groups:
        lr = param_group['lr']
    print('epoch: {:3d}, lr={:.8f}'.format(epoch, lr))
    lr_list.append(lr)
    scheduler.step()

plt.title(scheduler_name)
plt.xticks(range(0, 100, scheduler.step_size))
plt.ylim(0, 0.0011)
plt.plot(lr_list)
plt.show()
