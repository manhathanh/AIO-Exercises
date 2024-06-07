import math
import random
def regression_loss():
  num_sample=input('enter number of sample:')
  if not num_sample.isnumeric():
    print('number of samples must be an integer number')
    return exit()
  
  num_sample=int(num_sample)
  loss_name=input('enter loss name :')
  total_loss=0
  for i in range(num_sample):
    pred_sample = random.uniform(0,10)
    target_sample = random.uniform(0,10)
    if loss_name =='MAE':
      loss=abs(target_sample-pred_sample)
    elif loss_name=='MSE':
      loss=pow(target_sample-pred_sample,2)
    total_loss=total_loss+loss
    print(f'loss_name:{loss_name}, pre_sample = {pred_sample} , target_sampele = {target_sample} , loss = {loss}')
  
  final_loss=(total_loss)/num_sample
  print(f'{loss_name} : {final_loss}')
regression_loss()